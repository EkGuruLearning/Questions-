#!/usr/bin/env python3
"""
04_make_qgis_project.py
=======================
Writes an editable QGIS project (``.qgz`` = zipped ``.qgs`` XML) that points at
the master GeoPackage, so the atlas stays maintainable after future district
changes.

HONEST STATUS: QGIS Desktop is not installed in this environment, so this file
is generated programmatically against the QGIS 3.x project XML schema and has
NOT been opened in QGIS.  It is delivered as the editable master project the
task asks for, with that caveat recorded in reports/QA_REPORT.md.  If QGIS
rejects it, the same layers can be loaded by drag-and-drop from
``data/processed/rajasthan_border_atlas.gpkg``.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

import geopandas as gpd
from pyproj import CRS

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atlas_lib import PROCESSED, ROOT  # noqa: E402

GIS = ROOT / "gis_project"
GPKG_NAME = "rajasthan_border_atlas.gpkg"

LAYERS = [
    # (gpkg layer, tree name, geometry, draw order, style note)
    ("indian_state_outlines", "राज्य सीमारेखा (State outlines)",
     "MultiPolygon", 0),
    ("pakistan_province_outlines", "पाकिस्तान प्रांत (Pakistan provinces)",
     "MultiPolygon", 1),
    ("districts_all", "सभी ज़िले (All districts)", "MultiPolygon", 2),
    ("pakistan_districts", "पाकिस्तान ज़िले (Pakistan districts)",
     "MultiPolygon", 3),
    ("india_locator_states", "भारत — locator (India states)",
     "MultiPolygon", 4),
    ("rajasthan_districts", "राजस्थान ज़िले (Rajasthan districts)",
     "MultiPolygon", 5),
]

# simple, flat fills so the project opens with something legible
FILL = {
    "rajasthan_districts": "#fce8d5",
    "districts_all": "#f4f1ea",
    "pakistan_districts": "#ede6d8",
    "indian_state_outlines": "#00000000",
    "pakistan_province_outlines": "#00000000",
    "india_locator_states": "#efebe2",
}


def main():
    GIS.mkdir(parents=True, exist_ok=True)
    gpkg = PROCESSED / GPKG_NAME
    crs = CRS.from_epsg(4326)

    existing = gpd.list_layers(gpkg)["name"].tolist()
    used = [(n, t, g, o) for (n, t, g, o) in LAYERS if n in existing]

    maplayers, tree_items, order = [], [], []
    for i, (lname, tname, geom, order_idx) in enumerate(used):
        lid = f"{lname}_{i:04d}_{abs(hash(lname)) % 100000:05d}"
        src = f"{GPKG_NAME}|layername={lname}"
        fill = FILL.get(lname, "#f4f1ea")
        outline = "#8a8478" if lname != "indian_state_outlines" else "#6e6a63"
        maplayers.append(f"""
  <maplayer autoRefreshEnabled="0" geometry="{geom}" hasScaleBasedVisibilityFlag="0" \
maxScale="0" minScale="0" refreshOnNotifyEnabled="0" \
refreshOnNotifyMessage="" showFeatureCount="0" \
styleCategories="AllStyleCategories" type="vector" \
wkbType="{geom}" \
id="{lid}" name="{escape(tname)}" \
readOnly="0" labelsEnabled="0">
    <datasource>{escape(src)}</datasource>
    <keywordList><value></value></keywordList>
    <layername>{escape(tname)}</layername>
    <srs><spatialrefsys nativeFormat="WKT"><wkt>{escape(crs.to_wkt())}</wkt>\
<proj4>{escape(crs.to_proj4())}</proj4><srsid>3452</srsid><srid>4326</srid>\
<authid>EPSG:4326</authid><description>WGS 84</description>\
<projectionacronym>longlat</projectionacronym><ellipsoidacronym>EPSG:7030</ellipsoidacronym>\
<geographicflag>true</geographicflag></spatialrefsys></srs>
    <provider encoding="UTF-8">ogr</provider>
    <vectorjoins/>
    <layerDependencies/>
    <dataDependencies/>
    <expressionfields/>
    <map-layer-style-manager current="default"/>
    <renderer-v2 enableorderby="0" forceraster="0" \
symbollevels="0" type="singleSymbol">
      <symbols>
        <symbol alpha="1" clip_to_extent="1" force_rhr="0" name="0" \
type="fill">
          <data_defined_properties>
            <Option type="Map"><Option name="name" type="QString" value=""/>\
<Option name="properties"/><Option name="type" type="QString" value="collection"/></Option>
          </data_defined_properties>
          <layer class="SimpleFill" enabled="1" locked="0" pass="0">
            <Option type="Map"><Option name="color" type="QString" value="{fill}"/>\
<Option name="joinstyle" type="QString" value="bevel"/>\
<Option name="offset" type="QString" value="0,0"/>\
<Option name="offset_unit" type="QString" value="MM"/>\
<Option name="outline_color" type="QString" value="{outline}"/>\
<Option name="outline_style" type="QString" value="solid"/>\
<Option name="outline_width" type="QString" value="0.26"/>\
<Option name="outline_width_unit" type="QString" value="MM"/>\
<Option name="style" type="QString" value="solid"/></Option>
            <prop k="color" v="{fill}"/>
            <prop k="joinstyle" v="bevel"/>
            <prop k="outline_color" v="{outline}"/>
            <prop k="outline_style" v="solid"/>
            <prop k="outline_width" v="0.26"/>
            <prop k="outline_width_unit" v="MM"/>
            <prop k="style" v="solid"/>
          </layer>
        </symbol>
      </symbols>
      <source-symbol><symbol alpha="1" clip_to_extent="1" force_rhr="0" \
name="0" type="fill"/></source-symbol>
      <rotation/>
      <sizescale/>
    </renderer-v2>
    <labeling type="simple"/>
    <customproperties/>
    <geometryOptions geometryPrecision="0">
      <activeChecks/>
      <checkConfiguration/>
      <featureBlendMode>0</featureBlendMode>
      <featureBlendModeString>Normal</featureBlendModeString>
    </geometryOptions>
    <blendMode>0</blendMode>
    <featureBlendMode>0</featureBlendMode>
    <layerOpacity>1</layerOpacity>
    <legend showLabelLegend="0" type="default-vector"/>
    <referencedLayers/>
    <auxiliaryLayer/>
  </maplayer>""")
        tree_items.append(f'    <layer-tree-layer checked="Qt::Checked" \
expanded="1" id="{lid}" legend_exp="" legend_split_behavior="0" \
name="{escape(tname)}" patch_size="-1,-1" providerKey="ogr" \
source="{escape(src)}"/>')
        order.append(f'    <item>{lid}</item>')

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<qgis projectname="Rajasthan Border District Atlas" saveDateTime="2026-10-14T00:00:00" \
saveUser="arena" version="3.34.0-Prizren">
  <homePath path=""></homePath>
  <title>Rajasthan Border District Atlas — 41 districts, 7 divisions</title>
  <autotransaction active="0" value="0"/>
  <evaluateDefaultValues>0</evaluateDefaultValues>
  <transaction retried="0" value="0"/>
  <projectCrs>
    <spatialrefsys nativeFormat="WKT">
      <wkt>{escape(crs.to_wkt())}</wkt>
      <proj4>{escape(crs.to_proj4())}</proj4>
      <srsid>3452</srsid>
      <srid>4326</srid>
      <authid>EPSG:4326</authid>
      <description>WGS 84</description>
      <projectionacronym>longlat</projectionacronym>
      <ellipsoidacronym>EPSG:7030</ellipsoidacronym>
      <geographicflag>true</geographicflag>
    </spatialrefsys>
  </projectCrs>
  <layer-tree-canvas>
    <layer-tree-group checked="Qt::Checked" expanded="1" name="" \
short-name="">
      <customproperties/>
{chr(10).join(tree_items)}
    </layer-tree-group>
  </layer-tree-canvas>
  <mapcanvas annotationsVisible="1" name="theMapCanvas">
    <units>degrees</units>
    <extent>
      <xmin>67.2</xmin><ymin>23.1</ymin><xmax>79.6</xmax><ymax>31.1</ymax>
    </extent>
    <rotation>0</rotation>
    <destinationsrs>
      <spatialrefsys nativeFormat="WKT">
        <wkt>{escape(crs.to_wkt())}</wkt>
        <proj4>{escape(crs.to_proj4())}</proj4>
        <srsid>3452</srsid><srid>4326</srid>
        <authid>EPSG:4326</authid><description>WGS 84</description>
        <projectionacronym>longlat</projectionacronym>
        <ellipsoidacronym>EPSG:7030</ellipsoidacronym>
        <geographicflag>true</geographicflag>
      </spatialrefsys>
    </destinationsrs>
    <rendermaptile>0</rendermaptile>
    <expressionContextScope/>
  </mapcanvas>
  <projectlayers>
{chr(10).join(maplayers)}
  </projectlayers>
  <layerorder>
{chr(10).join(order)}
  </layerorder>
  <Legend showLegend="1" updateDrawingOrder="1"/>
  <properties>
    <Gui><SelectionColor><alpha>255</alpha><blue>0</blue>\
<green>255</green><red>255</red></SelectionColor>\
<CanvasColorBluepart>255</CanvasColorBluepart>\
<CanvasColorGreenpart>255</CanvasColorGreenpart>\
<CanvasColorRedpart>255</CanvasColorRedpart></Gui>
    <Measure><Ellipsoid>EPSG:7030</Ellipsoid></Measure>
    <PositionPrecision><Automatic>1</Automatic>\
<DecimalPlaces>2</DecimalPlaces></PositionPrecision>
  </properties>
  <dataDefinedServerProperties>
    <Option type="Map"><Option name="type" type="QString" value="collection"/></Option>
  </dataDefinedServerProperties>
</qgis>
"""
    qgs = "rajasthan_border_atlas.qgs"
    out = GIS / "rajasthan_border_atlas.qgz"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(qgs, xml)
    print("wrote", out, f"({out.stat().st_size} bytes)")
    print("layers:", [u[0] for u in used])


if __name__ == "__main__":
    main()
