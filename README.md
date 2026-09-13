# How Inflation Rewired Consumer Spending, 2024 - 2026 
Analysis and data behind [this post](https://saisathvikaramaraju.substack.com/p/inflation-slowed-but-your-grocery)

## The question 
Between January 2024 and June 2026 (BEA quarters 2024 Q1 – 2026 Q2), did US household spending rise because people bought more - or because things cost more? 

## The finding 
Across the ten quarters from 2024 Q1 to 2026 Q2, dollars moved and quantity barely did. Spending on gasoline and other energy goods rose **19.1% in dollars and 0.03% in volume** — a gap of 19.1 percentage points. Household utilities: 14.9% in dollars, 3.0% in volume. Groceries: 7.6% and 3.1%. Inflation slowed over this window, but prices did not fall, and spending never reverted.


## What's in here 
| File | what it is |
|---|---|
| `analysis-inflation-24-26.ipynb` | The full analysis - load, clean, define, chart | 
| `data/` | Raw files exactly as downloaded. See `data/data.md`|
|`charts/`| Exported PNGs used in the post |
| `chai_style.py` | Chart styling |

## Method 
1. Pull nominal spending by category (BEA Table 2.4.5U).
2. Pull the matching real, chained-dollar series for the same categories (BEA Table 2.4.6U).
3. Rebase both to 2024 Q1 = 100 so they are comparable.
4. The gap between the two is the price effect: dollars that moved without quantity moving.
5. Chart CPI separately (BLS via FRED, `CPIAUCSL`) to show the rate falling while the level does not.

## How to run this 
Open `analysis-inflation-24-26.ipynb` and Restart Kernel and Run all Cells. 
Every chart in the post regenerates into `charts/`. 

## Limitations 
1. Aggregate data hides distribution: These are averages across all US households. The median household's experience may look nothing like this.
2. Real spending here is BEA's own chained-dollar series, not a deflator I built. The split between price and quantity is BEA's modelling choice, which I am inheriting rather than testing. Chained dollars are also not additive, so category real figures do not sum to the real total.
3. Seasonal adjustment is a modelling choice, not a fact. I used the seasonally adjusted series throughout.
4. Three years is a short window. I cannot distinguish a permanent shift from a slow reversion with this much data.
5. Substitution and reduction look identical in aggregate data. When real spending falls, I cannot tell whether people bought fewer items or cheaper ones.

## Data as of 
September 10, 2026 - see `data/data.md` for per-file pull dates. 

## Author 
Sai Sathvika Ramaraju 
