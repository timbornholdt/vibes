---
id: "19"
slug: point-north
question: "From where you're reading this, point north."
category: sky
short_answer: "True north and magnetic north are almost the same in Rosemount right now: magnetic declination is only about 0.25 degrees west (WMM2025 model), so a compass needle points a quarter of a degree west of true north. Use the sun at solar noon (shadow points north), Polaris at night (altitude about 44.7 degrees), or the section-line street grid to check."
location_specific: true
time_sensitive: true
confidence: medium
last_researched: 2026-11-06
sources:
  - title: "NOAA NCEI - Magnetic Declination Calculator"
    url: "https://www.ngdc.noaa.gov/geomag/calculators/declinationForm.shtml"
  - title: "MDN - deviceorientationabsolute event"
    url: "https://developer.mozilla.org/docs/Web/API/Window/ondeviceorientationabsolute"
  - title: "Township America - Section line"
    url: "https://townshipamerica.com/glossary/section-line"
---

# From where you're reading this, point north.

## Short answer
Face the sun at solar noon and then turn around: your back is to **north** (Rosemount is far enough north of the tropics that the noon sun is always due south). Or find Polaris. A magnetic compass is also fine here, because declination is nearly zero.

## The details

### True vs. magnetic north
- **True north** is the direction toward the geographic North Pole (the rotation axis). Maps, the sun's noon shadow, and Polaris use this.
- **Magnetic north** is where the compass needle points, toward the wandering magnetic pole in the Arctic.
- **Declination** is the angle between them. I computed it for about 44.74 N, 93.12 W (central Rosemount; declination varies by well under 0.1 degree across the city) with the **WMM2025** coefficients, using the open-source `pygeomag` Python package:

| Date | Declination at Rosemount |
|---|---|
| Nov 2026 | about 0.25 degrees west (-0.25) |
| mid-2027 | about 0.28 degrees west |
| 2030 | about 0.38 degrees west |

A west declination means the needle points slightly west of true north. The line of zero declination (agonic line) has recently moved through the Upper Midwest, which is why the value is so small. The change is roughly 0.03 degree per year and westward. For hand-held use this is negligible (a quarter degree is about 0.4 ft of sideways error over 100 ft). Phone and car compasses are typically less accurate than that, and are usually thrown off by metal and electronics.

### Polaris
- Polaris sits within about 1 degree of the north celestial pole (roughly 0.7 degree at present from my background knowledge; I could not fetch a source to confirm the exact number). Its altitude above the horizon is approximately equal to your latitude, so it appears about **44.7 degrees up** in Rosemount, which is a bit under halfway between the horizon and straight up.
- To find it: extend the line through the two "pointer" stars at the end of the Big Dipper's bowl (Dubhe and Merak) about five times their separation. In autumn evenings, the Big Dipper is low in the north, so Cassiopeia (the W) is the better guide: Polaris is on the opposite side of the pole from the Big Dipper.
- Polaris is a good true-north reference to within about 1 degree. Drop a line to the horizon to get north.

### Shadow stick
At local solar noon the shadow of a vertical stick points due north in Rosemount. Solar noon is about 11:56 a.m. CST around Nov 6 and about 12:11 p.m. CST on Dec 21; see question 11 for the full table. Marking the shortest shadow works on any clear day without knowing the time exactly.

### Street grid
The Twin Cities area, including Dakota County, was surveyed under the Public Land Survey System (PLSS). Section lines are one mile apart and run nominally true north-south and east-west, and rural roads very often follow them (Township America's definition notes this pattern in agricultural states generally). That makes many Rosemount county roads and section-line avenues a convenient north-south reference. However, I did not confirm the orientation of any specific Rosemount street. Dodd Boulevard (a Dakota County road) is an older route, and older diagonal routes often do not follow the grid. Check your own street (below). Survey errors in the original 1850s lines mean "section-line roads" can be off true north by a degree or more.

## How to find and verify this yourself
1. **Declination:** go to the NOAA NCEI Magnetic Field Calculator (ngdc.noaa.gov/geomag/calculators/declinationForm.shtml). Enter latitude 44.74 N and longitude 93.12 W, or type your ZIP code (55068) into the location lookup. Pick model **WMM**, today's date, and result format HTML. The page states results are typically accurate to about 30 arcminutes (0.5 degree), so a 0.25 degree figure is within its own error. An API exists but needs registration.
2. **Street orientation:** open Google Maps or Dakota County's online map (maps.co.dakota.mn.us), which show north up by default. Zoom to your street. Measure the angle of your street and the nearest main road against the vertical edge of the screen; the measure tool in Google Earth Pro or QGIS gives bearings. If one is within about 1 degree of vertical, it runs close to north-south.
3. **PLSS section lines:** the Minnesota Geospatial Commons has the Township, Range, Section (TRS) layer (gisdata.mn.gov, search "TRS Boundaries"). Overlay it on an aerial and see whether your nearby roads run along section lines.
4. **Do it in person:** stand on your street at solar noon (see table in question 11), put a stick in the ground, and compare the shadow line to a compass app and to the road direction. Note that your phone compass may need calibration (move it in a figure-eight).
5. **At night:** locate Polaris and compare.


## Uncertainties and caveats
- Declination of 0.25 degrees W comes from my own WMM2025 calculation, not from NOAA's page directly (I could not run the web calculator). Verify with the steps above. The model's stated accuracy is about 0.5 degree.
- Polaris offset figure is from memory.
- I did not confirm the orientation of any specific Rosemount street.
- I could not verify details of the browser compass API beyond MDN's short reference, which flags limited browser support; check current MDN compatibility tables.
- Phone sensor accuracy and nearby steel will dominate any declination effect.

## Sources
1. [NOAA NCEI - Magnetic Declination Calculator](https://www.ngdc.noaa.gov/geomag/calculators/declinationForm.shtml)
2. [MDN - deviceorientationabsolute event](https://developer.mozilla.org/docs/Web/API/Window/ondeviceorientationabsolute)
3. [Township America - Section line](https://townshipamerica.com/glossary/section-line)
