# INPUT_AUDIT.md

**Audit date:** 2026-10-14

## Summary

- KML loaded with GeoPandas/Fiona: **33 district polygons**.
- CRS: **{g.crs}** (geographic WGS 84 coordinates).
- Geometry extent (xmin, ymin, xmax, ymax): **{[round(float(x),6) for x in g.total_bounds]}**.
- Valid geometries: **{int(g.geometry.is_valid.sum())}/{len(g)}**; invalid: **{len(invalid)}**.
- The district set corresponds to an older **33-district** Rajasthan layer, not the currently displayed 41-district administrative count confirmed by the Rajasthan state portal.
- No source date / revision metadata sufficient to identify the legal boundary vintage was found in the KML.
- The KML layer alone has no neighboring-state district polygons and no Pakistan district polygons.

## KML field audit

Fields: id, Name, description, timestamp, begin, end, altitudeMode, tessellate, extrude, visibility, drawOrder, icon, District, STATE, REMARKS, State_LGD, DISTRICT_L, Shape_Leng, Shape_Area, geometry

District names as stored in the KML `District` field:

- `AJMER`
- `ALWAR`
- `BANSWARA`
- `BARAN`
- `BARMER`
- `BHARATPUR`
- `BH|LWARA`
- `BUNDI`
- `B|KANER`
- `CHITTAURGARH`
- `CHURU`
- `DAUSA`
- `DHAULPUR`
- `DUNGARPUR`
- `GANGANAGAR`
- `HANUMANGARH`
- `JAIPUR`
- `JAISALMER`
- `JALOR`
- `JHALAWAR`
- `JHUNJHUNUN`
- `JODHPUR`
- `KARAULI`
- `KOTA`
- `NAGAUR`
- `PALI`
- `PRATAPGARH`
- `RAJ SAMAND`
- `SAWAI MADHOPUR`
- `SIROHI`
- `S|KAR`
- `TONK`
- `UDAIPUR`

### Invalid geometry findings

- **AJMER** — `Ring Self-intersection[74.8277799356186 25.8751670731408]`
- **B|KANER** — `Ring Self-intersection[74.1151940171417 28.9075198428122]`

### Likely text-field corruption

- `BH|LWARA` appears to be a corrupted rendering of **BHILWARA**.
- `B|KANER` appears to be a corrupted rendering of **BIKANER**.
- `S|KAR` appears to be a corrupted rendering of **SIKAR**.
- These are interpreted cautiously from the place-name context; source attribute values have not been overwritten.

## Uploaded input inventory

| Input | Format / coverage | Assessment and permitted use |
|---|---|---|
| `d5c393d6-d90d-49bf-8451-4d005a3bf34d.kml` | KML vector dataset: Rajasthan district polygons; 33 features; EPSG:4326; metadata says Rajasthan; no boundary vintage supplied | Useful as historical/reference geometry only; two invalid polygons and corrupted district names; not current 41-district source. |
| `New_district_map_of_Rajasthan.png` | Raster reference: 960×960 PNG labelled as newer Rajasthan district map; no embedded GIS coordinates/CRS detected by normal image inspection | Visual cross-check only; cannot serve as polygon data. |
| `Rajasthan-map-in-hindi-1 ffffffffffff.webp` | Raster reference: 1200×1086 WEBP, Hindi political district map; no CRS/coordinates | Visual reference only; cannot geospatially merge. |
| `rajasthan-district-map-with-neighbour-state-country_667085-626.jpg` | Raster reference: 626×626 JPG with Rajasthan/neighbouring regions; no CRS | Visual reference only; boundary-vintage uncertain. |
| `stock-vector-rajasthan-state-map-india-editable-vector-map-silhouette-illustration-isolated-at-india-2601323883.jpg` | Stock-map image: 1200×1600 JPG; India map with Rajasthan highlight; watermark visible in uploaded reference | Locator/reference only; not district geometry; do not use as deliverable artwork. |
| `stock-vector-detailed-vector-illustration-of-gujarat-map-state-and-district-map-with-neighbour-geographical-map-2485677497.jpg` | Stock-map image: 1500×1597 JPG; Gujarat districts shown; watermark visible | Visual reference only; district-vintage uncertain and no georeferencing. |
| `Punjab_district_map.png` | Raster reference: 960×1067 PNG; Punjab districts; no geospatial metadata | Visual reference only; not mergeable as vector geometry. |
| `Madhya_Pradesh_district_map.svg.webp` | Raster reference: 960×623 WEBP; MP district map; no geospatial metadata | Visual reference only; district-vintage uncertain. |
| `images.jpeg / images (1).jpeg / images (2).jpeg` | Raster references: Small JPG map images for India/Rajasthan/Pakistan/UP context; no geospatial metadata | Reference only; some have old boundaries, watermarks, or legibility limitations. |
| `71Pm3v2VdrL._AC_UF350,350_QL80_.jpg` | Raster reference: 350×277 JPG; low resolution | Reference only. |
| `a_detailed_cartographic_map_illustration_a_high_r.png, a_detailed_illustrated_political_map_infographic.png, a_detailed_infographic_map_image._overall_scene_a.png, a_detailed_infographic_map_scene_a_large_colorful.png, a_detailed_political_administrative_map_infographi.png, a_large_detailed_colorful_political_map_illustrati.png, wide_detailed_cartographic_map_illustration_a_col.png, wide_detailed_political_administrative_map_infogra.png, wide_infographic_map_of_rajasthan_and_neighbors_i.png` | AI-generated illustrations: Raster infographics made earlier in this conversation; visible label/boundary duplication and wrong names in some versions | Do not use for geographic geometry or as verified final map; aesthetic reference only. |
| `Rajasthan_Border_District_Map_A2.pdf / Rajasthan_Border_District_Map_A3.pdf and corresponding PNGs` | Earlier export drafts: A2 PDF page is 1683.78×1190.55 pt; A3 is 1190.55×841.89 pt. These are landscape A2/A3 pages with unverified AI-image content. | Correct page dimensions, but content is not a validated GIS map; must not label as final. |

## Decision

**STOP: do not generate a final “current 41-district” GIS map from these inputs alone.** The KML is old 33-district geometry, includes invalid polygons, and lacks all adjacent country/state district polygons. Raster screenshots cannot be merged as geographic datasets without georeferencing and digitization, and the prompt explicitly prohibits substituting hand-drawn screenshot geometry for verified coordinates.

The previous A2/A3 PDFs may be used only for layout inspiration; their current content is not accepted as a geographically verified deliverable.