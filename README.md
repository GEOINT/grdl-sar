# GRDL-SAR

`geoint.org` managed component catalog for Synthetic Aperture Radar (SAR), Polarimetric SAR (PolSAR), CFAR Detection, Sub-aperture Analysis, and Phase-History Image Formation built on the [`grdl`](../grdl/) framework.

## Included Components
- **Filters (`grdl_sar.filters`)**: `LeeFilter`, `ComplexLeeFilter`, `EnhancedLeeFilter`, `LeeSigmaFilter`, `RefinedLeeFilter`, `IDANFilter`, `WishartFilter`, `FrostFilter`, `KuanFilter`, `BoxcarFilter`, `PhaseGradientFilter`
- **Polarimetric Decompositions (`grdl_sar.decomposition`)**: `PauliDecomposition`, `DualPolHAlpha`, `FullPolHAalpha`, `FreemanDurden3C`, `Yamaguchi4C`, `TouziDecomposition`, `NeumannDecomposition`, `CompactPol*`, and scattering/coherency matrix transforms
- **Detectors (`grdl_sar.detection`)**: `CACFARDetector`, `GOCFARDetector`, `SOCFARDetector`, `OSCFARDetector`
- **Sub-aperture (`grdl_sar.subaperture`)**: `SublookDecomposition`, `MultilookDecomposition`, `DominanceFeatures`, `CSIProcessor`
- **Image Formation (`grdl_sar.image_formation`)**: `PolarFormatAlgorithm`, `StripmapPFA`, `RangeDopplerAlgorithm`, `FastBackProjection`

## Catalog Auto-Discovery
`grdl-sar` exports a `catalog.yaml` generated from `@processor_version` and `@processor_tags` decorators and registers `[project.entry-points."grdl.catalogs"]` for automatic federation into `grdl-runtime`.

