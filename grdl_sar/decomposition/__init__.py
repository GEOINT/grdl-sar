# -*- coding: utf-8 -*-
"""
Polarimetric Decomposition Sub-module - Scattering matrix decompositions.

Provides polarimetric decomposition methods for SAR imagery. Quad-pol
decompositions operate on the full scattering matrix [S]; dual-pol
decompositions operate on a 2-channel coherency matrix.

Key Classes
-----------
- PolarimetricDecomposition: ABC for all polarimetric decompositions
- PauliDecomposition: Quad-pol Pauli basis (surface / double-bounce / volume)
- DualPolHAlpha: Dual-pol entropy, alpha angle, anisotropy, and span

When to Use What
----------------
- **Quad-pol data (HH, HV, VH, VV):** ``PauliDecomposition`` decomposes
  the scattering matrix into three orthogonal Pauli basis components.
  RGB composite: R=double-bounce, G=volume, B=surface.

- **Dual-pol data (co-pol + cross-pol):** ``DualPolHAlpha`` computes
  the 2x2 coherency matrix eigendecomposition yielding entropy (H),
  mean scattering angle (alpha), anisotropy (A), and total span.
  Entropy near 0 means single dominant mechanism; near 1 means random.

Author
------
Duane Smalley, PhD
170194430+DDSmalls@users.noreply.github.com

License
-------
MIT License
Copyright (c) 2024 geoint.org
See LICENSE file for full text.

Created
-------
2026-01-30

Modified
--------
2026-02-17
"""

from grdl.image_processing.decomposition.base import PolarimetricDecomposition
from grdl_sar.decomposition.dual_pol_base import DualPolDecompositionBase
from grdl_sar.decomposition.pauli import PauliDecomposition
from grdl_sar.decomposition.h_a_alpha_base import HAalphaBase
from grdl_sar.decomposition.h_alpha_dp import DualPolHAlpha
from grdl_sar.decomposition.h_a_alpha_fp import FullPolHAalpha
from grdl_sar.decomposition.freeman_durden import FreemanDurden3C
from grdl_sar.decomposition.model_free import ModelFree3C, ModelFree4C
from grdl_sar.decomposition.dop import DegreeOfPolarization
from grdl_sar.decomposition.shannon_entropy import ShannonEntropy
from grdl_sar.decomposition.dop_dp import DegreeOfPolarizationDP
from grdl_sar.decomposition.shannon_entropy_dp import ShannonEntropyDP
from grdl_sar.decomposition.model_free_dp import ModelFree3CD
from grdl_sar.decomposition.dprbi import DualPolRadarBuiltUpIndex
from grdl_sar.decomposition.dprsi import DualPolRadarSurfaceIndex
from grdl_sar.decomposition.compact_pol_base import CompactPolDecompositionBase
from grdl_sar.decomposition.dop_cp import CompactPolDegreeOfPolarization
from grdl_sar.decomposition.model_free_cp import CompactPolModelFree3C
from grdl_sar.decomposition.s_omega_cp import CompactPolSOmega
from grdl_sar.decomposition.m_chi_cp import CompactPolMChi
from grdl_sar.decomposition.m_delta_cp import CompactPolMDelta
from grdl_sar.decomposition.scattering_power_dp import ScatteringPowerDP
from grdl_sar.decomposition.neumann import NeumannDecomposition
from grdl_sar.decomposition.praks import PraksParameters
from grdl_sar.decomposition.touzi import TouziDecomposition
from grdl_sar.decomposition.yamaguchi import Yamaguchi4C
from grdl_sar.decomposition.pol_matrix import (
    CovarianceMatrix,
    CoherencyMatrix,
    StokesVector,
    KennaughMatrix,
)

__all__ = [
    'PolarimetricDecomposition',
  'DualPolDecompositionBase',
    'CompactPolDecompositionBase',
    'HAalphaBase',
    'PauliDecomposition',
    'DualPolHAlpha',
    'FullPolHAalpha',
    'FreemanDurden3C',
    'ModelFree3C',
    'ModelFree4C',
    'DegreeOfPolarization',
    'ShannonEntropy',
    'DegreeOfPolarizationDP',
    'ShannonEntropyDP',
    'ModelFree3CD',
    'DualPolRadarBuiltUpIndex',
    'DualPolRadarSurfaceIndex',
    'CompactPolDegreeOfPolarization',
    'CompactPolModelFree3C',
    'CompactPolSOmega',
    'CompactPolMChi',
    'CompactPolMDelta',
    'ScatteringPowerDP',
    'NeumannDecomposition',
    'PraksParameters',
    'TouziDecomposition',
    'Yamaguchi4C',
    'CovarianceMatrix',
    'CoherencyMatrix',
    'StokesVector',
    'KennaughMatrix',
]
