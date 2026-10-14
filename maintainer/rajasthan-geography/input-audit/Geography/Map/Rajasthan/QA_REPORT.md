# QA_REPORT.md

**Status date:** 2026-10-14  
**Scope:** Uploaded-input audit and source-access feasibility only. This is not final-map QA.

| Acceptance test | Status | Evidence / reason |
|---|---|---|
| Current Rajasthan district count checked against a current government source | PASS | Rajasthan State Portal reports 41; official 2026 district-plan page lists 41 districts. |
| User KML is readable | PASS | Fiona/GeoPandas loads the KML. |
| User KML contains every current Rajasthan district | FAIL | 33 features only. |
| KML geometries valid | FAIL | Two invalid polygons; see INPUT_AUDIT.md. |
| KML district-name fields fully clean | FAIL | Three stored names appear text-corrupted. |
| Neighboring state/country district polygon data present among current inputs | FAIL | Supplied adjacent-region references are raster images; no adjacent-country/state vector layer is present. |
| Source CRS/date/authority for KML fully documented | FAIL | CRS exists (EPSG:4326), but source vintage and legal provenance do not. |
| Current official GIS polygons acquired for all relevant jurisdictions | NOT TESTED / BLOCKED | Terminal network DNS failed; available connector did not materialize source geometries locally. |
| Geometry merging / overlap / gap tests for combined region | NOT TESTED | No coherent set of current adjacent-jurisdiction polygons. |
| Actual shared-boundary adjacency and border-length CSV | NOT TESTED | Must be derived from current polygons; no relationship claims invented. |
| Hindi district labels correct at print scale | NOT TESTED | No final GIS layer/layout produced. |
| A1/A2/A3 final map from a GIS master | NOT PRODUCED | Deliberately stopped to avoid presenting a false/inaccurate map. |
| Independent review rounds 1–3 | NOT RUN | No independent reviewers actually executed; no report is claimed. |

## Disposition
Do not label any previous AI-rendered map/PDF as final or authoritative. The project is blocked at data acquisition and current-boundary validation.
