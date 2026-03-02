import io
from contextlib import redirect_stdout

import streamlit as st

from stock_trend_predictor import (
    add_ta_features,
    fetch_data_and_fundamentals,
    prepare_targets,
    train_and_predict,
)


def run_analysis(ticker: str) -> str:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        df = fetch_data_and_fundamentals(ticker)
        df_ta = add_ta_features(df)
        df_train, latest_data = prepare_targets(df_ta)
        train_and_predict(df_train, latest_data)
    return buffer.getvalue()


st.set_page_config(page_title="Stock Trend Predictor", page_icon="📈", layout="centered")

st.title("📈 Stock Trend Predictor")
st.write("Enter a ticker and run analysis.")

st.caption("Examples: SUZLON.NS, INFY.NS, INFY.BO, AAPL, NVDA")

col1, col2 = st.columns([3, 1], vertical_alignment="bottom")
with col1:
    ticker = st.text_input("Ticker", value="SUZLON.NS").strip().upper()
with col2:
    run_clicked = st.button("Run", use_container_width=True)

if run_clicked:
    if not ticker:
        st.error("Please enter a ticker symbol.")
    else:
        with st.spinner(f"Running analysis for {ticker}..."):
            try:
                result = run_analysis(ticker)
                st.success("Analysis complete")
                st.text(result)
                st.info("For educational/research use only. Not financial advice.")
            except Exception as exc:
                st.error(f"Analysis failed: {exc}")
