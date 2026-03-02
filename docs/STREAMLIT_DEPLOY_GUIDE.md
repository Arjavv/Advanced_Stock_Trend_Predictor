# Streamlit Deploy Guide

## Run locally

1. Open terminal in project root
2. Activate environment
   - `& ".\.venv\Scripts\Activate.ps1"`
3. Install dependencies
   - `python -m pip install -r requirements.txt`
4. Start app
   - `streamlit run .\streamlit_app.py`

Open the URL shown in terminal (usually `http://localhost:8501`).

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub
2. Go to `https://share.streamlit.io`
3. Sign in with GitHub
4. Click **New app**
5. Select:
   - Repository: `Arjavv/Advanced_Stock_Trend_Predictor`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
6. Click **Deploy**

## App settings

- Python dependencies are read from `requirements.txt`
- Python version is pinned via `runtime.txt` (`python-3.12.10`)
- Keep `streamlit_app.py` at repo root for easiest deployment

## Notes

- This app relies on live Yahoo Finance data through `yfinance`
- Some tickers may have incomplete fundamental fields
- Add disclaimer in app/repo: educational use, not financial advice
