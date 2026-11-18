# -*- coding: utf-8 -*-
"""
GRDL-SAR — geoint.org SAR, PolSAR & Image Formation Component Catalog.

Provides synthetic aperture radar (SAR) image processing components built
on the ``grdl`` framework, along with an auto-discovered ``catalog.yaml``
for ``grdl-runtime``.

License
-------
MIT License
Copyright (c) 2024 geoint.org
See LICENSE file for full text.
"""

from pathlib import Path

from grdl_sar.decomposition import (
    CoherencyMatrix,
    CompactPolDecompositionBase,
    CompactPolDegreeOfPolarization,
    CompactPolMChi,
    CompactPolMDelta,
    CompactPolModelFree3C,
    CompactPolSOmega,
    CovarianceMatrix,
    DegreeOfPolarization,
    DegreeOfPolarizationDP,
    DualPolDecompositionBase,
    DualPolHAlpha,
    DualPolRadarBuiltUpIndex,
    DualPolRadarSurfaceIndex,
    FreemanDurden3C,
    FullPolHAalpha,
    HAalphaBase,
    KennaughMatrix,
    ModelFree3C,
    ModelFree3CD,
    ModelFree4C,
    NeumannDecomposition,
    PauliDecomposition,
    PolarimetricDecomposition,
    PraksParameters,
    ScatteringPowerDP,
    ShannonEntropy,
    ShannonEntropyDP,
    StokesVector,
    TouziDecomposition,
    Yamaguchi4C,
)
from grdl_sar.detection import (
    CACFARDetector,
    CFARDetector,
    GOCFARDetector,
    OSCFARDetector,
    SOCFARDetector,
)
from grdl_sar.filters import (
    BoxcarFilter,
    ComplexLeeFilter,
    EnhancedLeeFilter,
    FrostFilter,
    IDANFilter,
    KuanFilter,
    LeeFilter,
    LeeSigmaFilter,
    PhaseGradientFilter,
    RefinedLeeFilter,
    SARFilter,
    WishartFilter,
)
from grdl_sar.image_formation import (
    CollectionGeometry,
    FastBackProjection,
    ImageFormationAlgorithm,
    PolarFormatAlgorithm,
    PolarGrid,
    RangeDopplerAlgorithm,
    StripmapPFA,
    SubaperturePartitioner,
)
from grdl_sar.subaperture import (
    CSIProcessor,
    DominanceFeatures,
    MultilookDecomposition,
    SublookDecomposition,
)

__version__ = "0.1.0"


def get_catalog_path() -> Path:
    """Return the path to the bundled ``grdl-sar`` ``catalog.yaml`` artifact."""
    return Path(__file__).resolve().parent / "catalog.yaml"


__all__ = [
    "__version__",
    "get_catalog_path",
    # Filters
    "SARFilter",
    "LeeFilter",
    "ComplexLeeFilter",
    "EnhancedLeeFilter",
    "LeeSigmaFilter",
    "RefinedLeeFilter",
    "IDANFilter",
    "PhaseGradientFilter",
    "WishartFilter",
    "FrostFilter",
    "KuanFilter",
    "BoxcarFilter",
    # Decomposition
    "PolarimetricDecomposition",
    "DualPolDecompositionBase",
    "CompactPolDecompositionBase",
    "HAalphaBase",
    "PauliDecomposition",
    "DualPolHAlpha",
    "FullPolHAalpha",
    "FreemanDurden3C",
    "ModelFree3C",
    "ModelFree4C",
    "DegreeOfPolarization",
    "ShannonEntropy",
    "DegreeOfPolarizationDP",
    "ShannonEntropyDP",
    "ModelFree3CD",
    "DualPolRadarBuiltUpIndex",
    "DualPolRadarSurfaceIndex",
    "CompactPolDegreeOfPolarization",
    "CompactPolModelFree3C",
    "CompactPolSOmega",
    "CompactPolMChi",
    "CompactPolMDelta",
    "ScatteringPowerDP",
    "NeumannDecomposition",
    "PraksParameters",
    "TouziDecomposition",
    "Yamaguchi4C",
    "CovarianceMatrix",
    "CoherencyMatrix",
    "StokesVector",
    "KennaughMatrix",
    # Detection
    "CFARDetector",
    "CACFARDetector",
    "GOCFARDetector",
    "SOCFARDetector",
    "OSCFARDetector",
    # Subaperture
    "SublookDecomposition",
    "MultilookDecomposition",
    "DominanceFeatures",
    "CSIProcessor",
    # Image Formation
    "ImageFormationAlgorithm",
    "CollectionGeometry",
    "PolarGrid",
    "PolarFormatAlgorithm",
    "SubaperturePartitioner",
    "StripmapPFA",
    "RangeDopplerAlgorithm",
    "FastBackProjection",
]

