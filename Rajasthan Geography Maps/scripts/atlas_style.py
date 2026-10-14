"""Cartographic style constants and the Rajasthan division lookup."""

# ---- page geometry (mm) ---------------------------------------------------
PAGES = {
    "A1": (841.0, 594.0),
    "A2": (594.0, 420.0),
    "A3": (420.0, 297.0),
}

# Geographic frame of the sheet (lon/lat).  Chosen so that (a) all 41 Rajasthan
# districts fit, (b) every district that shares a boundary with Rajasthan fits
# completely, and (c) the sheet aspect is close to ISO A-landscape (1.414).
FRAME = (67.2, 23.1, 79.6, 31.1)   # minx, miny, maxx, maxy

# ---- palette --------------------------------------------------------------
BG          = "#FBF7EE"   # light cream
PAGE_BG     = "#FFFFFF"
RAJ_INK     = "#4A4A4A"
INTL_RED    = "#C62828"   # India-Pakistan international boundary
INTER_YELLOW= "#F9A825"   # Rajasthan interstate boundary
DIST_EDGE   = "#B9B2A6"   # internal district boundaries
NEIGH_EDGE  = "#CFC8BA"
TEXT_HI     = "#2E2A25"
LEADER      = "#8A8478"

# Rajasthan divisions - current 7-division framework (28 Dec 2024 order).
RAJASTHAN_DIVISIONS = {
    "AJMER": "Ajmer", "BEAWAR": "Ajmer", "BHILWARA": "Ajmer",
    "DIDWANA-KUCHAMAN": "Ajmer", "NAGAUR": "Ajmer", "TONK": "Ajmer",
    "BHARATPUR": "Bharatpur", "DEEG": "Bharatpur", "DHAULPUR": "Bharatpur",
    "KARAULI": "Bharatpur", "SAWAI MADHOPUR": "Bharatpur",
    "BIKANER": "Bikaner", "CHURU": "Bikaner", "HANUMANGARH": "Bikaner",
    "GANGANAGAR": "Bikaner",
    "ALWAR": "Jaipur", "DAUSA": "Jaipur", "JAIPUR": "Jaipur",
    "JHUNJHUNUN": "Jaipur", "KHAIRTHAL-TIJARA": "Jaipur",
    "KOTPUTLI-BEHROR": "Jaipur", "SIKAR": "Jaipur",
    "BALOTRA": "Jodhpur", "BARMER": "Jodhpur", "JAISALMER": "Jodhpur",
    "JALOR": "Jodhpur", "JODHPUR": "Jodhpur", "PALI": "Jodhpur",
    "PHALODI": "Jodhpur", "SIROHI": "Jodhpur",
    "BARAN": "Kota", "BUNDI": "Kota", "JHALAWAR": "Kota", "KOTA": "Kota",
    "BANSWARA": "Udaipur", "CHITTAURGARH": "Udaipur", "DUNGARPUR": "Udaipur",
    "PRATAPGARH": "Udaipur", "RAJSAMAND": "Udaipur", "SALUMBAR": "Udaipur",
    "UDAIPUR": "Udaipur",
}

DIVISION_ORDER = ["Ajmer", "Bharatpur", "Bikaner", "Jaipur", "Jodhpur",
                  "Kota", "Udaipur"]

DIVISION_HI = {
    "Ajmer": "अजमेर", "Bharatpur": "भरतपुर", "Bikaner": "बीकानेर",
    "Jaipur": "जयपुर", "Jodhpur": "जोधपुर", "Kota": "कोटा", "Udaipur": "उदयपुर",
}

DIVISION_FILL = {
    "Ajmer":     "#F6D7C4",
    "Bharatpur": "#F7E6B0",
    "Bikaner":   "#E4EFC6",
    "Jaipur":    "#DCE9F2",
    "Jodhpur":   "#EADFF0",
    "Kota":      "#D6EFEA",
    "Udaipur":   "#F8DCE0",
}

# Neighbouring regions: fill, and the large region label.
NEIGHBOUR_STYLE = {
    "Pakistan":       dict(fill="#EDE6D8", label="पाकिस्तान", label_en="PAKISTAN"),
    "Punjab":         dict(fill="#EAF0D8", label="पंजाब",     label_en="PUNJAB (INDIA)"),
    "Haryana":        dict(fill="#FBE7D2", label="हरियाणा",   label_en="HARYANA"),
    "Uttar Pradesh":  dict(fill="#E6E3F2", label="उत्तर प्रदेश", label_en="UTTAR PRADESH"),
    "Madhya Pradesh": dict(fill="#DDEBF5", label="मध्य प्रदेश", label_en="MADHYA PRADESH"),
    "Gujarat":        dict(fill="#DFF0E4", label="गुजरात",    label_en="GUJARAT"),
}

# Pakistani provinces present on the sheet
PROVINCE_HI = {
    "Punjab": "पंजाब (पाकिस्तान)",
    "Sindh": "सिंध",
    "Balochistan": "बलूचिस्तान",
    "Khyber Pakhtunkhwa": "ख़ैबर पख़्तूनख़्वा",
}

# Districts named in the user's checklist that the GIS shows do NOT touch
# Rajasthan.  They are still drawn and labelled, but hatched and footnoted.
CHECKLIST_NOT_TOUCHING = [
    ("Pakistan", "Punjab (Pakistan)", "Dera Ghazi Khan"),
    ("Pakistan", "Punjab (Pakistan)", "Muzaffargarh"),
    ("Pakistan", "Punjab (Pakistan)", "Rajanpur"),
]

# Pakistani provinces are stored with a " (Pakistan)" suffix so that they never
# collide with Indian state names.  PROVINCE_HI is keyed by the bare name.
PK_SUFFIX = " (Pakistan)"


# ---------------------------------------------------------------------------
# Study-sheet upgrades
# ---------------------------------------------------------------------------
# District label sizes (pt at A1).  Kept legible: at A1 these are ~3.4 mm cap
# height for Rajasthan districts, ~2.7 mm for border-sharing neighbours.
FS_RAJASTHAN = 9.5
FS_TOUCHING  = 7.6
FS_OTHER     = 6.0
FS_REGION    = 32.0
FS_PROVINCE  = 14.0

# graticule
GRATICULE_STEP = 1.0          # degrees
GRATICULE_COLOR = "#B4AC9C"
GRATICULE_LW = 0.45

# crisp district edges (study use: lines must read clearly at arm's length)
DIST_EDGE_STUDY = "#8E8778"
DIST_EDGE_LW = 0.45

# panel column boundaries (figure fractions) for the bottom study strip
PANEL_COLS = ((0.010, 0.335), (0.350, 0.645), (0.660, 0.990))
