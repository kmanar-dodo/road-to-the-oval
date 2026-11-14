# Road to the Oval

A browser game: build a candidate and a policy platform, win the primary and general election state by state, then govern, with real constitutional rules (12th, 20th, 22nd and 25th Amendments). No dependencies, no build step needed to play.

**Play locally:** open `index.html`. **Single file:** `python3 build.py` writes `dist/index.html`.
**Host free:** push to GitHub, then Settings → Pages → Source: GitHub Actions. The included workflow deploys on every push to `main`.

## Layout
| File | Contents |
|---|---|
| `js/core.js` | data (states, issues, policies), pixel avatars, margin model, map, HUD |
| `js/setup.js` | character creator, platform builder |
| `js/qte.js` | quick-time debates and speeches |
| `js/primary.js` | primary, running mate |
| `js/campaign.js` | weekly campaign, rival AI, fundraising and merch, events |
| `js/election.js` | election night, Electoral College, House contingent election |
| `js/presidency.js` | events, governing hub, budget, midterms, succession, re-election |
| `css/style.css` | theme and UI |

## Roadmap
Voter blocs, opposition research on past positions, expressions on avatars, legislative procedure, cabinet and courts, primary calendar with delegates.

## Changelog
- **3.1** Sleeker UI, easier Normal and Hard, project split into files.
- **3.0** Rival AI, correlated polling error, policy platform builder, pixel avatars.
- **2.0** State map, difficulty, quick-time events, live feed, merch, governing hub.
