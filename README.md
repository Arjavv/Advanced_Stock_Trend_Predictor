# Stock Trend Predictor

A Python-based command-line project that fetches live market data from Yahoo Finance, computes technical indicators, and predicts multi-horizon trend direction using a Random Forest model.

LIVE: https://advancedstocktrendpredictor-vwuzsargxd4jvxfvvorjct.streamlit.app/

## What this project does

- Pulls historical stock data from Yahoo Finance via `yfinance`
- Computes technical indicators using `ta`
- Builds targets for:
  - 3 months (~63 trading days)
  - 6 months (~126 trading days)
  - 1 year (~252 trading days)
- Trains and evaluates Random Forest classifiers with time-series split
- Prints fundamental snapshot + technical summary + model predictions

## Project structure

- `stock_trend_predictor.py` - main CLI application
- `streamlit_app.py` - Streamlit web app
- `run_stock_trend_predictor.ps1` - PowerShell wrapper script
- `requirements.txt` - pinned dependencies
- `debug_ta.py` - quick indicator/debug helper
- `docs/` - setup, user, technology, and finance documentation

## Quick start (Windows / PowerShell)

1. Open terminal in project root.
2. Activate virtual environment:
   - `& ".\.venv\Scripts\Activate.ps1"`
3. Install dependencies:
   - `python -m pip install -r requirements.txt`
4. Run prediction:
   - `python -u .\stock_trend_predictor.py --ticker SUZLON.NS`

Or use wrapper script:

- `.\run_stock_trend_predictor.ps1 -Ticker SUZLON.NS`

## Run with Streamlit (web UI)

Use Python 3.12 (recommended for Streamlit compatibility).

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start Streamlit app:
   - `streamlit run .\streamlit_app.py`
3. Open browser URL shown in terminal (usually `http://localhost:8501`)

## Example tickers

- India (NSE): `INFY.NS`, `RELIANCE.NS`, `SUZLON.NS`
- India (BSE): `INFY.BO`
- US: `AAPL`, `NVDA`, `MSFT`

## Documentation

- Setup Guide: `docs/SETUP_GUIDE.md`
- User Guide: `docs/USER_GUIDE.md`
- Technology Guide: `docs/TECHNOLOGY_GUIDE.md`
- Finance Guide: `docs/FINANCE_GUIDE.md`
- Streamlit Deploy Guide: `docs/STREAMLIT_DEPLOY_GUIDE.md`

## Important note

This tool is for educational/research use. It is not financial advice.
