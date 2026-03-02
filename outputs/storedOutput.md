
  # Bangalore Rural Electrification Predictor
## Mini Project Pipeline


### Descriptive Statistics:
| Statistic | population | area_sqkm | pop_density | distance_from_grid_km | electrification_pct |
|-----------|-----------|-----------|-----------|-----------|----------|
| count | 238.000000 | 238.000000 | 238.000000 | 238.000000 | 238.000000 |
| mean | 7924.008403 | 18.948445 | 451.522269 | 22.642017 | 78.492479 |
| std | 4178.301224 | 6.065425 | 283.813066 | 13.499864 | 15.388862 |
| min | 1580.000000 | 8.450000 | 69.700000 | 2.100000 | 43.160000 |
| 25% | 4127.500000 | 13.325000 | 236.400000 | 10.295000 | 65.352500 |
| 50% | 7161.500000 | 18.360000 | 361.500000 | 20.600000 | 81.930000 |
| 75% | 11769.000000 | 23.787500 | 578.825000 | 34.297500 | 91.472500 |
| max | 15885.000000 | 31.400000 | 1433.200000 | 48.000000 | 98.000000 |

### DataFrame Info:
**Type:** pandas.core.frame.DataFrame
**RangeIndex:** 238 entries, 0 to 237
**Data columns:** 6 columns

| # | Column | Non-Null Count | Dtype |
|---|--------|--------|------|
| 0 | village_name | 238 non-null | object |
| 1 | population | 238 non-null | int64 |
| 2 | area_sqkm | 238 non-null | float64 |
| 3 | pop_density | 238 non-null | float64 |
| 4 | distance_from_grid_km | 238 non-null | float64 |
| 5 | electrification_pct | 238 non-null | float64 |

**dtypes:** float64(4), int64(1), object(1)
**memory usage:** 11.3+ KB

### EDA Summary:
- Electrification generally declines as distance from the main grid increases.
- Population density shows a mild positive relationship with electrification levels.
- The polynomial fit indicates slight non-linearity, with steeper decline at larger distances.
Training samples: 190
Testing samples: 48

### Model Parameters:
Intercept: 78.5373
Coefficients:
  distance_from_grid_km: -15.1505
  pop_density: 4.3120

### Evaluation Metrics:
R^2 Score: 0.9532
MAE: 2.6838
RMSE: 3.2858

### Metric Explanation Table:
| metric | value | meaning |
|--------|-------|----------|
| R^2 | 0.9532 | Explained variance ratio (higher is better). |
| MAE | 2.6838 | Average absolute error in electrification percentage points. |
| RMSE | 3.2858 | Root mean squared error, penalizing larger mistakes. |

### Sample Prediction Table (First 10 Rows):
| village_index | actual_pct | predicted_pct | error |
|---|---|---|---|
| 115 | 79.84 | 76.467968 | 3.372032 |
| 15 | 91.42 | 90.709156 | 0.710844 |
| 212 | 83.20 | 85.129138 | -1.929138 |
| 126 | 87.68 | 85.597429 | 2.082571 |
| 6 | 78.72 | 74.086190 | 4.633810 |
| 170 | 97.51 | 95.272589 | 2.237411 |
| 9 | 65.08 | 64.355774 | 0.724226 |
| 222 | 82.60 | 83.568986 | -0.968986 |
| 112 | 98.00 | 108.312678 | -10.312678 |
| 221 | 97.20 | 98.646736 | -1.446736 |
Plot saved: C:\IIMSTC-PROJECT\outputs\actual_vs_predicted.png
Plot saved: C:\IIMSTC-PROJECT\outputs\regression_result.png
