#!/usr/bin/env bash
# 00_fetch_sources.sh -- re-download every raw source used by this project.
#
# Requires network access to github.com (git protocol / codeload).
# NOTE: raw.githubusercontent.com, release-assets.githubusercontent.com and
# objects.githubusercontent.com are NOT reachable from the environment this
# project was built in, so release assets and Git-LFS payloads cannot be used.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAW="$HERE/../data/raw"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$RAW/india_soi" "$RAW/pakistan_opencarto" "$RAW/reference_uploads"
touch "$RAW/reference_uploads/.gitkeep"

echo "== Indian districts (Survey-of-India-derived GeoJSON) =="
git clone --depth 1 https://github.com/drguptavivek/soi-geojson.git "$TMP/soi"
for f in 08_RAJASTHAN 24_GUJARAT 23_MADHYA_PRADESH 09_UTTAR_PRADESH \
         06_HARYANA 03_PUNJAB; do
  cp "$TMP/soi/geojson/districts/$f.geojson" "$RAW/india_soi/"
done
cp "$TMP/soi/geojson/states.geojson"          "$RAW/india_soi/"
cp "$TMP/soi/geojson/districts/_disputed.geojson" "$RAW/india_soi/"

echo "== Pakistani districts (WFP/OCHA COD-AB v01 via OpenCarto) =="
git clone --filter=blob:none --sparse \
  https://github.com/PRABHMANNAT/OpenCarto.git "$TMP/opencarto"
( cd "$TMP/opencarto" && git sparse-checkout set --skip-checks public/data )
for f in pk-country-district pk-country-province pk-country-region; do
  cp "$TMP/opencarto/public/data/$f.geojson" "$RAW/pakistan_opencarto/"
done

echo "== Noto Sans Devanagari (SIL OFL 1.1) =="
FONT="$HERE/../fonts"; mkdir -p "$FONT"
git clone --filter=blob:none --sparse \
  https://github.com/notofonts/noto-fonts.git "$TMP/noto"
( cd "$TMP/noto" && \
  git sparse-checkout set --skip-checks hinted/ttf/NotoSansDevanagari )
cp "$TMP/noto/hinted/ttf/NotoSansDevanagari/NotoSansDevanagari-Regular.ttf" "$FONT/"
cp "$TMP/noto/hinted/ttf/NotoSansDevanagari/NotoSansDevanagari-Bold.ttf"    "$FONT/"
cp "$TMP/noto/hinted/ttf/NotoSansDevanagari/NotoSansDevanagari-SemiBold.ttf" "$FONT/"
cp "$TMP/noto/hinted/ttf/NotoSansDevanagari/NotoSansDevanagari-Medium.ttf"  "$FONT/"

echo "== done =="
find "$RAW" -type f | sort
