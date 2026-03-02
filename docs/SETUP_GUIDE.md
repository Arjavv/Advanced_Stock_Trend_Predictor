# Setup Guide

## 1) Prerequisites

- Python 3.11+ (project currently tested in a local virtual environment)
- Windows PowerShell (for the wrapper script)
- Internet connection (Yahoo Finance API access through `yfinance`)

## 2) Clone repository

- `git clone <your-repo-url>`
- `cd "Stock Trend Predictor"`

## 3) Create and activate environment

- `python -m venv .venv`
- `& ".\.venv\Scripts\Activate.ps1"`

If script execution is blocked:

- `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

## 4) Install dependencies

- `python -m pip install --upgrade pip`
- `python -m pip install -r requirements.txt`

## 5) Verify install

- `python -u .\stock_trend_predictor.py --ticker NVDA`

You should see sections for fundamental analysis, technical indicators, and prediction results.
