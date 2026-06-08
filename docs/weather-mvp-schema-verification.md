# Weather MVP Schema Verification

This document outlines the approach to schema and contract verification for the Meteocat Weather MVP.

## Context

After validating the multi-resource local E2E for the Weather MVP, there is a need to document and validate minimal internal expectations for the resources. This ensures that the ingestion and transformation pipelines operate on predictable data structures.

## Approach

The current approach is **local and lightweight**, focusing on:

- **JSON Schemas**: Defining the shape of the data.
- **Data Contracts**: Defining the agreement and metadata around the resource.

### Permissive Schemas

Schemas are designed to be permissive. They allow additional fields (`additionalProperties: true`) to ensure that upstream changes in the API do not immediately break the lab environment unless a required field is missing or a type is incompatible.

### Lightweight Validation

Validation is performed using a custom Python script (`scripts/validate-contracts.py`) that checks the consistency of the contracts and their referenced schemas. This does not require network access or real API keys.

## Current State

Verification is currently implemented for the following Meteocat resources at the landing layer:

- `stations-metadata`
- `variables-metadata`
- `measured-variable`

## Future Work

- **Real API Verification**: Validating real payloads from the Meteocat API against these schemas.
- **Stronger Contracts**: Moving from `minimal` to `complete` validation levels as the project evolves.
- **Downstream Contracts**: Implementing contracts for Silver and Gold layers to ensure quality throughout the lakehouse.
