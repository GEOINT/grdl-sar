"""Performance benchmarks for grdl-sar polarimetric matrix formation kernels."""

import tracemalloc

import numpy as np
import pytest
from scipy.ndimage import uniform_filter

from grdl_sar.decomposition.pol_matrix import (
    build_target_vector_c,
    build_target_vector_t,
    compute_dual_elements,
    compute_matrix,
)

pytestmark = pytest.mark.benchmark


def _previous_dual_elements(components, window):
    first, second = components
    diagonal_first = uniform_filter(np.abs(first) ** 2, size=window)
    diagonal_second = uniform_filter(np.abs(second) ** 2, size=window)
    real = uniform_filter((first * second.conj()).real, size=window)
    imag = uniform_filter((first * second.conj()).imag, size=window)
    return diagonal_first, real + 1j * imag, diagonal_second


def _previous_full_matrix(components, window):
    result = np.zeros(
        (len(components), len(components), *components[0].shape), dtype=components[0].dtype
    )
    for row, first in enumerate(components):
        for col in range(row, len(components)):
            product = first * components[col].conj()
            element = uniform_filter(product.real, size=window).astype(
                product.real.dtype
            ) + 1j * uniform_filter(product.imag, size=window).astype(product.imag.dtype)
            result[row, col] = element
            if row != col:
                result[col, row] = element.conj()
    return result


def _shared_full_matrix(components, window):
    return compute_matrix(components, window, False)


@pytest.mark.parametrize(
    "basis,dimension,elements_only",
    [
        ("C", 2, True),
        ("T", 2, True),
        ("C", 2, False),
        ("T", 2, False),
        ("C", 3, False),
        ("T", 3, False),
    ],
)
@pytest.mark.parametrize("dtype", [np.complex64, np.complex128])
@pytest.mark.parametrize("window", [1, 7])
@pytest.mark.parametrize("implementation", ["previous", "shared"])
def test_polarimetric_formation(
    benchmark, basis, dimension, elements_only, dtype, window, implementation
):
    """Compare formation kernels; input/target allocation is outside measurement."""
    rng = np.random.default_rng(107)
    channels = (
        rng.normal(size=(dimension, 256, 256)) + 1j * rng.normal(size=(dimension, 256, 256))
    ).astype(dtype)
    builder = build_target_vector_c if basis == "C" else build_target_vector_t
    components = builder(channels)
    previous = _previous_dual_elements if elements_only else _previous_full_matrix
    shared = compute_dual_elements if elements_only else _shared_full_matrix
    operation = previous if implementation == "previous" else shared
    result = benchmark.pedantic(
        operation, args=(components, window), rounds=9, iterations=1, warmup_rounds=2
    )
    tolerance = 2e-6 if dtype == np.complex64 else 5e-14
    np.testing.assert_allclose(result, previous(components, window), rtol=tolerance, atol=tolerance)
    tracemalloc.start()
    try:
        measured = operation(components, window)
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    del measured
    benchmark.extra_info["peak_traced_bytes"] = peak
    benchmark.extra_info["input_shape"] = list(channels.shape)
    benchmark.extra_info["baseline"] = "historical kernel; precision matched; targets precomputed"

