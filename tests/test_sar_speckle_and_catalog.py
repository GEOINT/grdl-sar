# -*- coding: utf-8 -*-
"""Unit tests for SAR speckle filters and catalog export in grdl-sar."""

import numpy as np
import pytest

import grdl_sar
from grdl_sar.filters import (
    BoxcarFilter,
    ComplexLeeFilter,
    EnhancedLeeFilter,
    FrostFilter,
    KuanFilter,
    LeeFilter,
    LeeSigmaFilter,
    PhaseGradientFilter,
)


class TestSARSpeckleFilters:
    def test_frost_filter(self):
        arr = np.ones((25, 25), dtype=np.float32) * 10.0
        out = FrostFilter(window_size=5, damping_factor=2.0).apply(arr)
        assert out.shape == arr.shape
        assert np.allclose(out, 10.0, atol=1e-3)

    def test_kuan_filter(self):
        arr = np.ones((25, 25), dtype=np.float32) * 10.0
        out = KuanFilter(window_size=5, num_looks=2).apply(arr)
        assert out.shape == arr.shape
        assert np.allclose(out, 10.0, atol=1e-3)

    def test_boxcar_filter(self):
        arr = np.ones((15, 15), dtype=np.float32) * 5.0
        out = BoxcarFilter(window_size=3).apply(arr)
        assert out.shape == arr.shape
        assert np.allclose(out, 5.0, atol=1e-3)

    def test_lee_reduces_speckle_variance(self):
        rng = np.random.default_rng(42)
        source = np.abs(rng.standard_normal((64, 64)) + 1j * rng.standard_normal((64, 64)))
        out = LeeFilter(kernel_size=7).apply(source)
        assert np.var(out) < np.var(source)

    def test_complex_lee_preserves_shape(self):
        rng = np.random.default_rng(42)
        slc = (rng.standard_normal((32, 32)) + 1j * rng.standard_normal((32, 32))).astype(np.complex64)
        out = ComplexLeeFilter(kernel_size=5).apply(slc)
        assert out.shape == slc.shape
        assert np.iscomplexobj(out)

    def test_enhanced_lee_and_lee_sigma(self):
        rng = np.random.default_rng(42)
        img = np.abs(rng.standard_normal((32, 32))) + 1.0
        out_enh = EnhancedLeeFilter(kernel_size=5).apply(img)
        out_sig = LeeSigmaFilter(kernel_size=5).apply(img)
        assert out_enh.shape == img.shape
        assert out_sig.shape == img.shape

    def test_phase_gradient_filter(self):
        rng = np.random.default_rng(42)
        slc = (rng.standard_normal((32, 32)) + 1j * rng.standard_normal((32, 32))).astype(np.complex64)
        out = PhaseGradientFilter(kernel_size=5).apply(slc)
        assert out.shape == slc.shape


def test_catalog_export_and_image_formation_tags(tmp_path):
    from grdl.discovery.catalog_builder import build_catalog_data, export_catalog_yaml

    data = build_catalog_data("grdl_sar")
    names = {a["name"] for a in data["artifacts"]}
    assert "LeeFilter" in names
    assert "PauliDecomposition" in names
    assert "CACFARDetector" in names
    assert "PolarFormatAlgorithm" in names
    assert "RangeDopplerAlgorithm" in names

    out = export_catalog_yaml("grdl_sar", tmp_path / "catalog.yaml")
    assert out.exists()
    assert grdl_sar.get_catalog_path().exists()

