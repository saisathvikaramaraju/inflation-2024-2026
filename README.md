# How Inflation Rewired Consumer Spending, 2024 - 2026 
Analysis and data behind [this post](LINK-TO-SUBSTACK-POST)

## The question 
Between January 2024 and August 2026, did US household spending rise because people bought more - or because things cost more? 

## The finding 
[1 - 2 sentences, actual result with a number] 

## What's in here 
| File | what it is |
|---|---|
| `analysis-inflation-24-26.ipynb` | The full analysis - load, clean, define, chart | 
| `data/` | Raw files exactly as downloaded. See `data/data.md`|
|`charts/`| Exported PNGs used in the post |
| `chai_style.py` | Chart styling |

## Method 
1. Pull nominal spending by category (BEA Table, 2.4.5U, Census MARTS)
2. Pull a matching CPI series for each spending category (BLS)
3. Deflate nominal spending by its category price index to get real spending.
4. Rebase every series to 2024 Q1 = 100 so they are comparable.
5. Cross-check my deflated figures against BEA's published real PCE (Table 2.4.6)

## How to run this 
Open `analysis-inflation-24-26.ipynb` and Restart Kernel and Run all Cells. 
Every chart in the post regenerates into `charts/`. 

## Limitations 
1. Aggregate data hides distribution: These are averages across all US households. The median household's experience may look nothing like this.
2. Category definitions differ slightly between BLS, Census, and BEA, so matching a price index to a spending category is approximate.
3. Seasonal adjustment is a modelling choice, not a fact. I used the seasonally adjusted series throughout.
4. Three years is a short window. I cannot distinguish a permanent shift from a slow reversion with this much data.
5. Substitution and reduction look identical in aggregate data. When real spending falls, I cannot tell whether people bought fewer items or cheaper ones.

## Data as of 
August 15, 2026 - see `data/data.md` for per-file pull dates. 

## Author 
Sai Sathvika Ramaraju 
