# SOURCE_AUDIT.md

**Audit date:** 2026-10-14

## Verified from accessible sources

1. The Rajasthan government portal currently reports **41 districts**. This confirms the administrative count displayed by the portal, but does not provide polygon geometry on that page.
2. The Rajasthan Disaster Management, Relief & Civil Defence Department page lists **41 District Disaster Management Plans for 2026**. This independently supports the 41-district count and provides a government name cross-check, but not GIS polygon files.
3. Gujarat's official Vav-Tharad district site states that Vav-Tharad was carved from Banaskantha on **2 October 2025** and that it borders the southern side of Rajasthan. Therefore older Gujarat maps that show only Banaskantha across this segment are obsolete.
4. Vardhan Systems' open-source map repository identifies its districts as OSM-derived and explicitly says the map is **not official or survey-grade**. Its metadata records a 2026-09-08 generation date and 787 India district features. It is a potential comparison layer, not enough alone for an authoritative map.
5. DataMeet's district boundary project explicitly warns about geographic shifts and older/pre-delimitation areas in some states. It is not suitable as the sole current source.
6. The Chief Electoral Officer Rajasthan district-assembly-map page still lists 33 districts, so it is a useful legacy reference but unsuitable as the current 41-district boundary source without newer replacements.

## Acquisition blocker

The runtime's command-line internet access fails at DNS resolution (`curl: Could not resolve host`). The available GitHub connector can inspect repository metadata and text, but does not expose a usable local binary/GeoJSON download path in this session. Thus a candidate current OSM-derived source was inspected at repository/metadata level but its district polygon files were **not** acquired into the GIS runtime. Official current GIS polygons for all six adjacent jurisdictions (Rajasthan, Gujarat, Madhya Pradesh, Uttar Pradesh, Haryana, Punjab, and the Pakistani boundary region) were not obtained as a coherent set.

## Decision

**The source audit is incomplete for final cartography.** Current district count can be corroborated, but current legal/shared boundary geometry cannot. Do not calculate or assert border lengths, district adjacency, nine Pakistani neighbors, or final current border relationships until source polygons are acquired and checked. Full source metadata is in `SOURCES_REGISTER.csv`.
