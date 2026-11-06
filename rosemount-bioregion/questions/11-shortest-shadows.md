---
id: "11"
slug: shortest-shadows
question: "On what day of the year are the shadows the shortest where you live?"
category: sky
short_answer: "Around the June solstice (June 20-21), at local solar noon, which in Rosemount is about 1:10-1:14 p.m. daylight time, not 12:00. December 21 is the opposite: it has the longest noon shadows of the year. A 6-ft person casts a noon shadow of about 2.3 ft on the June solstice and about 15 ft on December 21."
location_specific: true
time_sensitive: true
confidence: high
last_researched: 2026-11-06
sources:
  - title: "Wikipedia - June solstice"
    url: "https://en.wikipedia.org/wiki/June_solstice"
  - title: "timedate.org - June solstice 2027"
    url: "https://timedate.org/events/june-solstice-2027"
---

# On what day of the year are the shadows the shortest where you live?

## Short answer
The shortest shadows of the year happen at **solar noon on the June solstice**, which falls on **Monday, June 21, 2027** (about 14:10-14:11 UTC, roughly 9:10 a.m. CDT) and on June 20-21 in other years. **December 21 is not the shortest. It is the longest.** That is a common mix-up, because the winter solstice is the shortest *day* (least daylight), but it is also when the sun is lowest in the sky, which stretches shadows.

Rosemount is at about 44.7-44.8 N. The sun is never directly overhead there (that only happens between the tropics, 23.44 N and 23.44 S), so shadows never vanish at noon. They just get shortest in late June.

## The details

### Why
Earth's axis is tilted about 23.44 degrees. The sun's declination (the latitude where it is directly overhead) swings between +23.44 (June solstice) and -23.44 (December solstice). At solar noon:

**noon altitude = 90 - latitude + declination**
**shadow length = object height / tan(altitude)**

With latitude about 44.74 N (central Rosemount; any spot in the city changes results by a hundredth of a degree or so):

| Date | Declination | Noon sun altitude | Shadow : height | 6-ft (1.83 m) person | 1 m stick |
|---|---|---|---|---|---|
| June solstice (Jun 21) | +23.44 | 68.7 deg | 0.39 | **2.3 ft (28 in)** | 0.39 m |
| Equinoxes (Mar 20, Sep 22-23) | 0 | 45.3 deg | 0.99 | **6.0 ft** | 0.99 m |
| December solstice (Dec 21) | -23.44 | 21.8 deg | 2.50 | **15.0 ft** | 2.50 m |
| Nov 6, 2026 (today) | about -16.5 | about 28.8 deg | about 1.8 | about 10.9 ft | about 1.8 m |

So the December noon shadow is about **6.4 times** longer than the June one. Around the June solstice the change is very slow: the noon sun altitude is within 1 degree of its maximum for about 3 weeks (roughly June 1 to July 10 it stays above about 67.3 degrees), so "shortest" is a broad flat minimum, not a sharp spike.

### Solar noon is not 12:00
The shortest shadow *each day* occurs at **local solar noon**, when the sun crosses the meridian due south. In Rosemount (longitude about 93.12 W) solar noon is shifted from clock noon by two things: the distance from the time-zone meridian (Central time uses 90 W, so Rosemount is about 3.1 degrees west, 12.5 minutes later) and the equation of time (up to about 16 minutes either way). Approximate solar noon values (calculated with a standard equation-of-time formula; expect about 1-minute accuracy):

| Date | Clock time zone | Solar noon |
|---|---|---|
| Jun 21, 2027 | CDT | about 1:14 p.m. |
| Dec 21, 2026 | CST | about 12:11 p.m. |
| Mar 20, 2027 | CDT | about 1:20 p.m. |
| Sep 23, 2026 | CDT | about 1:04 p.m. |
| Nov 6, 2026 (today) | CST | about 11:56 a.m. |

The June 2027 solstice instant (14:10 UTC) is about 9:10 a.m. CDT, hours before solar noon, so the date that matters for shadows is June 21 (local), and the day-to-day difference around then is tiny. On the June 2026 solstice (June 21, 08:25 UTC), local date is also June 21 (3:25 a.m. CDT).

The December 2026 solstice is on December 21, 2026 (I believe about 14:50 UTC; I could not fetch a source for this, so check timeanddate.com).

## How to find and verify this yourself

### DIY gnomon (stick) experiment
1. Find level ground in the open (a driveway or patio works) and place a straight stick or pole vertically. Check it with a plumb line or a level on two sides. Measure its height.
2. Starting about 30 minutes before expected solar noon, mark the tip of the shadow with chalk every 5-10 minutes (write the time). Shadows get shorter until noon, then lengthen.
3. The **shortest** mark is solar noon, and the line from the stick base to that tip points **true north**. (This also answers question 19.)
4. Divide shadow length by stick height. Compare with the table (0.39 in June, 1.0 at equinox, 2.5 in December). Repeat monthly to watch the change.
5. Accuracy tip: use a pinhole or a small ball at the top of the stick to get a sharp tip, because the sun's disk blurs the shadow tip.

### Check against an authority
- timeanddate.com: search "Rosemount, Minnesota sun" for solar noon times and sun altitude, and use their "Sun and Moon" table for any date.
- NOAA Solar Calculator (gml.noaa.gov/grad/solcalc): enter 44.74, -93.12. It gives solar noon and solar elevation for any date.
- US Naval Observatory (aa.usno.navy.mil) "Sun or Moon Altitude/Azimuth Table" for an exact degrees-per-minute table.

### Caveats
Roads, trees and buildings can shorten your usable window. Atmospheric refraction raises apparent altitude by a negligible amount at 20-70 degrees altitude. Clock time matters too: Daylight Saving Time adds an hour.


## Uncertainties and caveats
- The figures use central-Rosemount coordinates; results differ by under 0.1 degree anywhere in Rosemount.
- Table values come from my own Python calculation using simple formulas and a 23.436 degree obliquity, not from an almanac. They should match published sun altitude within about 0.3 degrees.
- December 2026 solstice time is unsourced (see above).

## Sources
1. [Wikipedia - June solstice](https://en.wikipedia.org/wiki/June_solstice) (2026: 08:25 UTC; 2027: 14:11 UTC)
2. [timedate.org - June solstice 2027](https://timedate.org/events/june-solstice-2027) (June 21, 2027, 14:10 UTC)
