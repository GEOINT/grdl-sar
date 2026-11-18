# -*- coding: utf-8 -*-
"""
SAR Spatial & Polarimetric Filters.
"""

from importlib import import_module
from typing import TYPE_CHECKING

from grdl_sar.filters.enhanced_lee import EnhancedLeeFilter
from grdl_sar.filters.lee_sigma import LeeSigmaFilter
from grdl_sar.filters.phase import PhaseGradientFilter
from grdl_sar.filters.sar_base import SARFilter
from grdl_sar.filters.sar_speckle import BoxcarFilter, FrostFilter, KuanFilter
from grdl_sar.filters.standard_lee import ComplexLeeFilter, LeeFilter

if TYPE_CHECKING:
    from grdl_sar.filters.idan import IDANFilter
    from grdl_sar.filters.refined_lee import RefinedLeeFilter
    from grdl_sar.filters.wishart import WishartFilter


def __getattr__(name: str):
    """Load joint polarimetric filters on demand."""
    modules = {
        "RefinedLeeFilter": "refined_lee",
        "IDANFilter": "idan",
        "WishartFilter": "wishart",
    }
    if name not in modules:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(import_module(f"{__name__}.{modules[name]}"), name)


__all__ = [
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
]

