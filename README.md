# datasets-catalog

The `datasets-catalog` repository is responsible for dataset governance within the Open Data Lakehouse Lab project. It contains dataset definitions, metadata, source documentation, license notes, data dictionaries, expected schemas, data contracts, refresh frequency information, and dataset status.

## Purpose

The purpose of this catalog is to provide a single source of truth for the datasets used in the Open Data Lakehouse Lab, ensuring proper governance, transparency, and reproducibility.

## Current MVP Focus: Weather Open Data

The first MVP of the project focuses on weather open data from Spanish and/or European public sources. We are currently in the evaluation phase, identifying candidate datasets that meet our selection criteria.

## Candidate Dataset Sources

We are currently evaluating candidates from the following providers:
* **AEMET**: Spanish State Meteorological Agency.
* **Meteocat**: Meteorological Service of Catalonia.
* **datos.gob.es**: Spain's national open data portal.
* **Dades Obertes Generalitat**: Catalonia's open data portal.
* **data.europa.eu**: The official portal for European data.

## Dataset Lifecycle Statuses

Datasets in the catalog can have the following statuses:
* `candidate`: Under evaluation for inclusion in the project.
* `selected`: Chosen for implementation.
* `implemented`: Fully integrated into the lakehouse.
* `deprecated`: No longer recommended for use.
* `rejected`: Evaluated and decided against inclusion.

## Repository Structure

For a detailed explanation of the repository structure, see [CATALOG_STRUCTURE.md](CATALOG_STRUCTURE.md).

## Licensing Note

Original upstream datasets, when referenced, remain governed by their original source licenses and terms. This project does not change the original upstream dataset license.

## Dataset Validation

To ensure all dataset metadata files are valid against the schema, you can run the validation script:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate-datasets.py
```

## License

Unless otherwise noted:

- Documentation, articles, diagrams, dataset metadata, data dictionaries, schemas, data contracts and written content are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
- Software, scripts, Infrastructure as Code, SQL models, configuration files and executable assets are licensed under the [Apache License 2.0](LICENSE-CODE).

Original upstream datasets, when referenced, remain governed by their original source licenses and terms.
