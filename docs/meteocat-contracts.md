# Meteocat Contracts

This document describes the internal data contracts for the Meteocat weather dataset within the Open Data Lakehouse Lab.

## Purpose of Contracts

Contracts in this lab are internal agreements that describe the minimal expectations for a resource. They help ensure that the data pipelines can rely on a certain structure while allowing the source to evolve.

## Schema vs Contract

- **Schema**: A flexible JSON Schema describing the expected shape of a resource payload or record. It is used for technical validation.
- **Contract**: A lab-level internal agreement describing minimal expectations, supported resource, current validation level, allowed evolution, and known limitations.

## Supported Resources

The following Meteocat resources have draft landing contracts and permissive schemas.

| Resource | Layer | Contract status | Validation level | Schema |
|----------|-------|-----------------|------------------|--------|
| `stations-metadata` | landing | draft | minimal | [Schema](../datasets/weather/meteocat/schemas/stations-metadata.schema.json) |
| `variables-metadata` | landing | draft | minimal | [Schema](../datasets/weather/meteocat/schemas/variables-metadata.schema.json) |
| `measured-variable` | landing | draft | minimal | [Schema](../datasets/weather/meteocat/schemas/measured-variable.schema.json) |

## Contract Status and Validation

All current contracts are in **draft** status and provide a **minimal** validation level. This means they verify the basic structure and presence of some key fields but are intentionally permissive to accommodate the experimental nature of the MVP.

## Known Limitations

- Schemas are intentionally permissive and do not set `additionalProperties` to `false`.
- These are not official upstream contracts from Meteocat.
- Real API payloads still require broader verification.
- This is a lab-level foundation for future, more strict contracts.

## Future Work

- Transition contracts to `stable` as the MVP matures.
- Add stricter Silver and Gold layer contracts.
- Implement automated real API payload verification.
