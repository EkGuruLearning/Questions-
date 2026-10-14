# PROMPT_FEASIBILITY_AUDIT.md

**Verdict: The prompt is a strong technical specification, but not a guarantee that an arbitrary AI agent can produce the requested map.** It will only work end-to-end in an environment with GIS processing, accessible/downloadable boundary datasets, adequate disk/runtime, Hindi font support, PDF/PNG export, and a mechanism for independently reviewing outputs.

## Strong parts
- Correctly forbids screenshot collage and text-to-image as the source of geometry.
- Requires source metadata, reproducibility, topology checks, true adjacency computations, and transparent PASS/FAIL/NOT TESTED results.
- Properly treats the nine Pakistani district names as a research checklist rather than a guaranteed correct adjacency list.
- Includes real print dimensions and PDF/PNG/vector deliverables.
- Requires disclosure rather than invented verification.

## Changes recommended before sending to an agent
1. **Make delivery conditional on source access:** require the agent to first list real dataset URLs, download files, hashes, CRS, feature counts, and source dates; stop if it cannot materialize current polygons locally.
2. **Do not require “1,000+ source checks” as a target.** It is not a meaningful proxy for boundary quality. The prompt already has an appropriate caveat; make unique authoritative sources and spatial tests the acceptance metric.
3. **Define independence of reviewers:** specify separate agent sessions or people, each receiving the same GIS export and source data but not the primary conclusion. If multi-agent execution is unavailable, mark this NOT TESTED rather than pretending.
4. **Separate legal boundary authority from cartographic availability:** an OSM-derived layer may be current and detailed yet still not be authoritative. Flag unresolved international-border or source-version disputes.
5. **Include source licensing/attribution** for every downloaded dataset and ensure fonts can be embedded legally.
6. **Require an explicit district-count reconciliation table** by country/state and effective date before rendering.
7. **Avoid a fixed 41 count if an official notice changes it:** your prompt already says this, and that rule should override every static reference image.

## Results of testing the current uploads
- User KML opens successfully but contains **33 polygons**, not 41.
- The KML uses EPSG:4326.
- Two geometries are invalid: AJMER (ring self-intersection) and B|KANER (ring self-intersection).
- Three stored labels appear corrupted: `BH|LWARA`, `B|KANER`, `S|KAR`.
- The remaining state maps are raster images without GIS CRS/coordinates; they cannot be geometrically merged as polygons.
- Existing A2/A3 PDFs have landscape page dimensions, but their map content derives from unverified illustrative images. Page size alone does not make them geographically correct.

## Exact capability conclusion for this session
- Prompt review: **PASS**.
- Input audit: **PASS for the files available**.
- Current official district count source check: **PASS** (government portal says 41).
- Current polygon data acquisition for all needed jurisdictions: **FAIL / BLOCKED**.
- Shared-boundary adjacency computation: **NOT TESTED** (required inputs absent).
- Three independent review rounds: **NOT RUN** (not available as separate independent reviewers in this session).
- Final GIS master, true adjacency CSV, authoritative A1/A2/A3 map: **NOT PRODUCED** because source polygon inputs are not available. Generating one from the screenshots or AI illustrations would violate the prompt's own requirements.
