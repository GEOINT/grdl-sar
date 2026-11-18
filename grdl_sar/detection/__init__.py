# -*- coding: utf-8 -*-
"""
SAR Target Detection (CFAR Family).
"""

from grdl.image_processing.detection.base import ImageDetector
from grdl.image_processing.detection.fields import DATA_DICTIONARY, FieldDefinition, Fields
from grdl.image_processing.detection.models import Detection, DetectionSet
from grdl_sar.detection.cfar import (
    CACFARDetector,
    CFARDetector,
    GOCFARDetector,
    OSCFARDetector,
    SOCFARDetector,
)

__all__ = [
    "ImageDetector",
    "Detection",
    "DetectionSet",
    "FieldDefinition",
    "Fields",
    "DATA_DICTIONARY",
    "CFARDetector",
    "CACFARDetector",
    "GOCFARDetector",
    "SOCFARDetector",
    "OSCFARDetector",
]

