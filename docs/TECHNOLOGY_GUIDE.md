# Technology Guide

## Stack overview

- Language: Python
- Data Source: Yahoo Finance (`yfinance`)
- Data Processing: `pandas`, `numpy`
- Technical Indicators: `ta`
- Machine Learning: `scikit-learn`
- Execution: CLI + PowerShell wrapper

## Model design

- Algorithm: `RandomForestClassifier`
- Validation strategy: `TimeSeriesSplit` (time-aware cross-validation)
- Multi-horizon binary classification:
  - Target = 1 if future close > current close, else 0
  - Horizons: 63, 126, 252 trading days

## Why these choices

- Random Forest handles nonlinear relationships and mixed feature behavior well.
- TimeSeriesSplit avoids look-ahead leakage in chronological data.
- `ta` provides a broad indicator set quickly for feature engineering.
- `yfinance` is easy to integrate for publicly available market data.

## Current limitations

- Data source depends on Yahoo Finance availability.
- Fundamentals can be incomplete for some symbols.
- No transaction-cost/slippage modeling.
- No portfolio-level risk framework yet.
