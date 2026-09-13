# Data Sources 
All files in this folder are raw, exactly as downloaded. Nothing here is edited by hand. 

All cleaning happens in the `analysis.ipynb`. 

| File | Source | Series / table ID | URL | Data pulled | Units | Notes| 
|---|---|---|---|---|---|---|
|`cpi-all-items.csv`| BLS via FRED | `CPIAUCSL` | https://fred.stlouisfed.org/series/CPIAUCSL | 2026-08-17 | Index, 1982-1984=100 | Seasonally adjusted, monthly | 
|`jewelry.csv`| BEA via FRED | `DJRYRC1A027NBEA` | https://fred.stlouisfed.org/series/DJRYRC1A027NBEA | 2026-09-08 | Billions of dollars, not seasonally adjusted, annual | PCE, durable goods: jewelry and watches. Current dollars (BEA Table 2.4.5). Series last updated 2026-04-09; next release 2026-09-30. |
|`jewelry.csv`| BEA via FRED | `DJRYRG3A086NBEA` | https://fred.stlouisfed.org/series/DJRYRG3A086NBEA | 2026-09-08 | Index 2017=100, not seasonally adjusted, annual | Jewelry and watches chain-type price index (BEA Table 2.4.4). Series last updated 2026-02-20; next release 2026-09-30. Same file as the row above. | `pce-nominal-t24505.csv` | BEA | Table 2.4.5U | https://apps.bea.gov/iTable/ | 2026-09 -10 | Millions of dollars, monthly | PCE by type of product, underlying detail, current dollars | `pce-real-t24506.csv` | BEA | Table 2.4.6U | https://apps.bea.gov/iTable/ | 2026-09-10 | Millions of chained (2017) dollars, monthly | PCE by type of product, undrelying detail, real |

## Known issues with these sources: 
1. Census MARTS advance estimates are revised in later releases. Figures here are as of the pull date and may differ from what's on the site now.
2. BEA revises PCE. Same caveat.
3. CPI Category definitions have changed over time; comparisons across long spans are approximate. 

