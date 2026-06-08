# Weather MVP Candidates

This document tracks the candidate datasets being evaluated for the first MVP of the Open Data Lakehouse Lab, which focuses on weather data.

## MVP Selection

**Selected Dataset:** `meteocat-weather`

**Rationale:**
- Focused Catalonia weather API suitable for the first MVP.
- REST API with JSON output.
- Provides access to real-time and historical weather data.
- Provides station and variable metadata through XEMA documentation.
- Geographically bounded scope reduces MVP complexity.
- Initial schemas and landing data contracts have been defined.

## Candidate List

| Dataset ID | Provider | Region | Status | MVP Candidate |
|---|---|---|---|---|
| aemet-weather | AEMET | Spain | candidate | true |
| meteocat-weather | Meteocat | Catalonia, Spain | selected | true |
| datos-gob-es-weather | datos.gob.es | Spain | candidate | true |
| dades-obertes-generalitat-weather | Dades Obertes Generalitat de Catalunya | Catalonia, Spain | candidate | true |
| data-europa-eu-weather | data.europa.eu | European Union | candidate | true |

## Comparison Matrix

| Feature | AEMET | Meteocat | datos.gob.es | Dades Obertes | data.europa.eu |
|---|---|---|---|---|---|
| API Access | REST API | REST API | API | API | Discovery |
| Format | JSON | JSON | TODO | TODO | TODO |
| License | Authorized with citation | TODO | TODO | TODO | TODO |
| Historical Data | Yes | Yes | TODO | TODO | TODO |
| Refresh Frequency | TODO | High | TODO | TODO | TODO |

*Note: Final source-specific license verification is still required before production-like reuse.*
