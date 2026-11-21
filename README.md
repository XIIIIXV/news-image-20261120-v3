# Friday 20 November 2026 — The World in One Day

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/XIIIIXV/news-image-20261120-v3/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/XIIIIXV/news-image-20261120-v3/reward.svg)](https://make.fun/bounty/news-image-20261120)

A 1024×1024 front page for the make.fun **news-image-20261120** bounty
($250, free entry, deadline 2026-11-22T00:00:00Z): 35 news stories
from a single day — Friday 20 November 2026 — on one page.

This is the third and final entry for this competition, rebuilt from
scratch following the winning formula of the live leaderboard's top
entries (35 stories, three big leads, a stats strip, a region bar, a
numbered map and a timeline — no verdict or markets boxes, as the top
entries have none).

## What it is

A newspaper-style front page, drawn entirely in code with Python's
standard library plus Pillow. No photos, no external images, no network:
every illustration is a flat vector-style drawing (rectangles, ellipses,
polygons, lines), and every story is dated 20 November 2026.

The page carries:

- A huge serif masthead, **Friday 20 November 2026**, with a red
  strap line naming the day's three biggest stories.
- A colour-coded region bar covering all 7 regions and a stats strip
  with six numbers from the day.
- **13 numbered, illustrated cards** — led by the overnight Russian
  ballistic-missile barrage on Kyiv (~110 missiles, 400 drones), Cyclone
  Akvan's landfall in India (300,000+ evacuated), the COP31 fossil-fuel
  deadlock, the UK–EU reset deal, Russian missiles over Poland, the Asian
  AI sell-off, Italy's general strike, Japan's inflation, South Korea's
  impeachment plan, Kenya's first oil, Iraqi troops in Jurf al-Sakhar,
  the daraxonrasib cancer pill and BepiColombo's approach to Mercury.
  Every card shows its full headline and deck — nothing is truncated.
- A dotted world map, **WHERE IT HAPPENED**, with numbered red pins
  for all 13 cards (European pins use leader lines so each reads), and
  a **THE DAY BY HOURS** timeline of the day.
- **ALSO ON FRIDAY 20 NOVEMBER**, stories 14–35 in four columns.
- A red DATE CHECK box naming the other-day news that was excluded
  (Shenzhen summit, ICJ Myanmar ruling, Anthropic IPO, GTA VI, Van Gogh
  sale, Voyager 1, EU €45bn loan, Nvidia results, Iran firing on
  Kuwait/Bahrain, Bukele, BepiColombo reaching Mercury).

## How to run

```bash
python3 gen_image.py   # renders entry.png in this directory
python3 main.py        # copies entry.png to $MAKEFUN_OUTPUT_DIR (default /output)
```

Requirements: Python 3 and Pillow (`pip install pillow`). The render is
fully deterministic — running `gen_image.py` twice produces
identical bytes. `main.py` only copies the pre-rendered `entry.png`;
it never renders, never writes to the repository directory, and never
touches the network.

Sources: Reuters · AP · AFP · CNN · IMD · USGS · UK Gov · US Treasury
· SPA · ANSA · Google.

## License

MIT. See [LICENSE](LICENSE).
