# User Guide

## Run the predictor

### Option A: Direct Python command

- `python -u .\stock_trend_predictor.py --ticker SUZLON.NS`

### Option B: PowerShell wrapper

- `.\run_stock_trend_predictor.ps1 -Ticker SUZLON.NS`

### Option C: Interactive mode

- `python -u .\stock_trend_predictor.py`
- Then enter ticker when prompted.

## Ticker format

- NSE: append `.NS` (example: `TCS.NS`)
- BSE: append `.BO` (example: `INFY.BO`)
- US stocks: no suffix (example: `AAPL`)

## Output interpretation

The program prints:

1. Fundamental snapshot
   - Company, sector, industry, market cap, P/E, dividend yield, 52-week high/low
2. Technical snapshot
   - RSI, MACD, 50-day SMA trend
3. Model predictions
   - Direction (UP/DOWN) for 3m, 6m, 1y
   - Model confidence for each horizon
   - Historical cross-validation accuracy for each horizon

## Common issues

- `ModuleNotFoundError`
  - Run: `python -m pip install -r requirements.txt`
- Empty data / invalid ticker
  - Check ticker format and exchange suffix
- Slow run time
  - First run can be slower due to data fetch and model training
