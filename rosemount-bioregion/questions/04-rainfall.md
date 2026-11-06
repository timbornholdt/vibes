---
id: "04"
slug: rainfall
question: "What was the total rainfall in your area last year (July–June)? (Slack: 1″ for every 20″.)"
category: water
short_answer: "About 28 inches of liquid-equivalent precipitation fell at the Minneapolis–St. Paul airport station between July 1, 2025 and June 30, 2026 (27.80 in). That is roughly 3.8 in (12%) below the 1991–2020 normal of about 31.6 in. A Rosemount gauge could differ by a few inches."
location_specific: true
time_sensitive: true
confidence: medium
last_researched: 2026-11-06
sources:
  - title: "DNR State Climatology Office – monthly summaries, July 2025"
    url: "https://files.dnr.state.mn.us/natural_resources/climate/historical/monthly_summaries/monthly_202507.pdf"
  - title: "NWS Twin Cities MSP monthly report – April 2026"
    url: "https://www.weather.gov/media/mpx/Climate/MSP/apr2026.pdf"
  - title: "NWS Twin Cities MSP monthly report – May 2026"
    url: "https://www.weather.gov/media/mpx/Climate/MSP/may2026.pdf"
  - title: "NWS Twin Cities MSP monthly report – March 2026"
    url: "https://www.weather.gov/media/mpx/Climate/MSP/mar2026.pdf"
  - title: "NWS Twin Cities MSP monthly report – February 2026"
    url: "https://www.weather.gov/media/mpx/Climate/MSP/feb2026.pdf"
  - title: "CoCoRaHS Data Explorer"
    url: "https://dex.cocorahs.org/"
---

# What was the total rainfall in your area last year (July–June)? (Slack: 1″ for every 20″.)

## Short answer
Call it **about 28 inches** (27.8 in at the MSP airport station, the best long-record official gauge near Rosemount). "Rainfall" here means total precipitation: rain plus the melted water content of snow. The 1991–2020 normal for the same July–June window is about **31.6 in**, so the year ran roughly **3.8 in dry (about 88% of normal)**. With the "1 inch per 20 inches" slack, an answer of roughly 26.5–29 in would count as right for a number near 28.

## The details

### Why July–June?
A July 1 – June 30 year puts a whole winter's snow in a single "precipitation year" rather than splitting it across two calendar years, and it ends right as the growing season peaks. It is close to how hydrologists think about water supply.

### Monthly totals, MSP airport (inches)
Source for all rows: DNR State Climatology Office monthly summaries, cross-checked against NWS Twin Cities monthly reports for Feb–May 2026. "Normal" is derived as observed minus the published departure, and matches the 1991–2020 normals.

| Month | Observed | Normal (1991–2020) | Departure |
|---|---|---|---|
| Jul 2025 | 5.24 | 4.06 | +1.18 |
| Aug 2025 | 3.57 | 4.34 | −0.77 |
| Sep 2025 | 2.85 | 3.02 | −0.17 |
| Oct 2025 | 1.04 | 2.58 | −1.54 |
| Nov 2025 | 0.91 | 1.61 | −0.70 |
| Dec 2025 | 1.66 | 1.17 | +0.49 |
| Jan 2026 | 1.00 | 0.89 | +0.11 |
| Feb 2026 | 1.15 | 0.87 | +0.28 |
| Mar 2026 | 1.29 | 1.68 | −0.39 |
| Apr 2026 | 3.25 | 2.91 | +0.34 |
| May 2026 | 2.24 | 3.91 | −1.67 |
| Jun 2026 | 3.60 | 4.58 | −0.98 |
| **Total** | **27.80** | **31.62** | **−3.82** |

Notes on the pattern: a wet July, then a persistently dry autumn (October was less than half of normal), a near-normal winter, and a dry May and June. Winter months are snow water equivalent (for example March 2026 had 11.3 in of snow and February 9.3 in of snow, melted down to the 1.29 and 1.15 in shown).

### Nearer to Rosemount
- The UMN Rosemount Research & Outreach Center (just southeast of town) is the closest official-style station, but the DNR summaries show **no precipitation value for it in any month checked** (shown as "-"), so it cannot be used for a clean annual total.
- **Hastings Dam 2** (about 12 mi east) is in the same DNR tables: Jul 5.72, Aug 4.87, Sep 5.25, Oct 1.46, Nov 0.97, Dec 0.69, Feb 0.51, May 1.11, Jun 3.04. January and April were not listed, and the March value (9.33 in, +7.55 departure) looks like a data error. Its winter numbers also look low (likely rain-gauge undercatch of snow), so it is only a rough cross-check. It does confirm the same story: wet July–September, dry fall, dry May.
- Summer thunderstorm rain is patchy; neighbouring gauges can differ by 20–50% in a single month. Over a full year, a local gauge usually lands within roughly ±10% of the airport (about ±3 in), which is wider than the slack allowance. That is why this file carries medium confidence for "your yard".

## How to find and verify this yourself
1. **DNR monthly summaries (easiest, official).** Go to the Minnesota DNR State Climatology Office, "Historical" > "Monthly summaries" (the PDFs live at `files.dnr.state.mn.us/natural_resources/climate/historical/monthly_summaries/monthly_YYYYMM.pdf`; replace YYYYMM with 202507 … 202606). Find the row "Minneapolis-St. Paul International Airport" and read the "Total Precipitation" column. Add the 12 months. Also look at the "Hastings Dam 2" row.
2. **NWS Twin Cities monthly report.** At weather.gov/mpx, open Climate > "Local Climate Data" and choose the MSP monthly PDF (`.../Climate/MSP/mmmYYYY.pdf`). The "PRECIPITATION" block gives the month total, the normal, and the departure.
3. **NOWData (interactive).** At weather.gov/mpx, click "NOWData" under Climate. Choose Product: "Monthly summarized data", Variable: Precipitation, Station: "Minneapolis Area" (threaded record, MSP), and a date range of July 2025 to June 2026. Add the monthly column.
4. **CoCoRaHS (hyper-local).** Go to dex.cocorahs.org > "Station Search" and look for stations in Rosemount (55068), Apple Valley, Farmington, and Eagan (zip filter). Open a station's "Climatology" tab and select a custom date range of 7/1/2025 – 6/30/2026. Check the listed days-reporting count. A station with many missing days will under-count, and a gauge that reports only on rain days is fine only if zero days were also logged.
5. **Your own gauge.** A $10–$20 clear 4-inch rain gauge in an open spot (away from trees and eaves) read at a consistent time each morning gives a true local record. You can join CoCoRaHS to submit it. In winter, melt the snow in the cylinder or use the "10:1" snow-to-water rule of thumb, which is only approximate.
6. **State-wide context.** The DNR "HydroClim Minnesota" newsletters (dnr.state.mn.us/hydroclim) summarize each season versus normal in plain language, and the UMN Extension WeatherTalk blog posts a monthly "climate summary".

Caveats: Snow water equivalent is hard to measure; undercatch in wind is typical. DNR/NWS figures for the most recent months can be "preliminary" and be revised slightly. The airport is about 15 mi north-northwest of Rosemount.


## Uncertainties and caveats
- The totals are for the airport, not Rosemount; the local figure could be about ±3 in.
- The Rosemount R&OC data gap means no verified station within a few miles in the DNR monthly tables. CoCoRaHS volunteers nearby may fill this but were not retrieved here.
- Normals are derived from the published departures rather than read directly; they match known 1991–2020 MSP values (e.g. June 4.58, July 4.06).
- Early monthly values are final; the last months (May–June 2026) were retrieved from preliminary summaries and could shift by a few hundredths.
- The Feb 2026 departure sign was inferred from the DNR table (+0.28).

## Sources
1. [DNR State Climatology Office – monthly summaries, July 2025](https://files.dnr.state.mn.us/natural_resources/climate/historical/monthly_summaries/monthly_202507.pdf) (and the sibling files for 202508 through 202606)
2. [NWS Twin Cities MSP monthly report – April 2026](https://www.weather.gov/media/mpx/Climate/MSP/apr2026.pdf)
3. [NWS Twin Cities MSP monthly report – May 2026](https://www.weather.gov/media/mpx/Climate/MSP/may2026.pdf)
4. [NWS Twin Cities MSP monthly report – March 2026](https://www.weather.gov/media/mpx/Climate/MSP/mar2026.pdf)
5. [NWS Twin Cities MSP monthly report – February 2026](https://www.weather.gov/media/mpx/Climate/MSP/feb2026.pdf)
6. [CoCoRaHS Data Explorer](https://dex.cocorahs.org/)
