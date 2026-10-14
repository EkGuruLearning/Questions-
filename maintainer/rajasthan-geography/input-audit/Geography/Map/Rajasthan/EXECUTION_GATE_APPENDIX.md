# Preflight Gate to Append to the Master Prompt

Paste this block immediately after **ROLE AND MISSION**. It prevents an AI agent from drawing a convincing-looking but geographically false map when it lacks vector data or GIS execution access.

```text
## CAPABILITY PREFLIGHT — MUST PASS BEFORE CARTOGRAPHY

Before drawing or exporting any map, do a short preflight and show evidence:

1. List the actual GIS tools and versions available in this run (QGIS, GDAL/OGR, GeoPandas, Shapely, PyProj, or equivalents). Do not claim a tool is available merely because it is named in this prompt.
2. Download or load actual polygon vector datasets for Rajasthan, Gujarat, Madhya Pradesh, Uttar Pradesh, Haryana, Punjab, and Pakistan's Rajasthan-facing region into the local workspace. For each file, report its exact local path, source URL, retrieval date, byte size, SHA-256, CRS, feature count, name fields, and source version.
3. Confirm the Rajasthan layer matches the current government-confirmed district count, names, and effective date. Confirm all relevant Gujarat district changes, including Vav-Tharad if in force as of the execution date.
4. Confirm the data contain actual polygon coordinates, not screenshots, generated illustrations, SVG sketches, or manually transcribed labels.
5. Run an initial geometry-validity test and print the names of invalid, missing, duplicate, and unnamed features.
6. If any jurisdiction's needed polygon data cannot be obtained, STOP before cartography. Do not create an AI illustration as a substitute. Report the exact blocked jurisdiction, failed URL/action, and missing file; ask for the missing vector data or a network-enabled GIS environment.
7. Do not count a district as bordering Rajasthan unless polygon geometry confirms a shared boundary. Treat the nine Pakistani district names as candidates to investigate, not a required result.
8. Do not claim independent review rounds unless separate reviewers or separate agent sessions actually performed them. If unavailable, mark NOT RUN.
9. Before delivery, independently re-open the exact final PDF and PNG; report real page dimensions, pixel dimensions, and the checks actually completed.

The task may be called complete only after the local data files, reproducible GIS project, adjacency CSV, QA results, and final exports all exist and have been inspected. Source claims, geometry tests, and review rounds must be evidence-backed. If this gate fails, deliver the audit and blocker report only.
```
