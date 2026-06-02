# Catalog Structure

This document describes the structure of the `datasets-catalog` repository and the role of each directory and file.

## Root Directory

* `README.md`: Main entry point and overview of the dataset catalog.
* `DATASET_STATUS.md`: High-level status tracking of all datasets in the catalog.
* `CATALOG_STRUCTURE.md`: This file, documenting the repository layout.
* `.gitignore`: Standard git ignore file.
* `LICENSE`, `LICENSE-CODE`, `NOTICE`: Project licensing information.

## Directories

### `datasets/`

Contains the definitions and documentation for all datasets. Organized by domain (e.g., `weather/`) and then by provider.

Each dataset directory contains:
* `dataset.yml`: Metadata following the standard schema.
* `source.md`: Detailed information about the data source.
* `license.md`: Information about the upstream license.
* `dictionary.md`: Data dictionary defining fields and types.
* `schema.json`: Expected JSON schema for the dataset.

### `schemas/`

Contains global schemas used for validation and standardization.
* `dataset.schema.json`: JSON schema for validating `dataset.yml` files.

### `contracts/`

Contains data contracts defining agreements between providers and consumers.

### `docs/`

General documentation about the catalog, selection process, and specific MVP initiatives.
* `dataset-selection-process.md`: Guidelines for evaluating and selecting datasets.
* `weather-mvp-candidates.md`: Details and comparison of weather dataset candidates.
