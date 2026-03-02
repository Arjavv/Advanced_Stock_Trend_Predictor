import pandas as pd
import numpy as np
import yfinance as yf
from ta import add_all_ta_features
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings
import argparse

warnings.filterwarnings('ignore')

PREDICTION_HORIZONS = {
    '3_Months': 63,
    '6_Months': 126,
    '1_Year': 252
}

def get_ticker_input():
    parser = argparse.ArgumentParser(description="Stock Trend Predictor")
    parser.add_argument("--ticker", type=str, help="Stock Ticker (e.g. INFY.NS, RELIANCE.NS, AAPL)")
    args = parser.parse_args()
    
    ticker_symbol = args.ticker
    if not ticker_symbol:
        print("Stock Trend Predictor")
        print("Enter a stock ticker to analyze.")
        print("Note: For Indian stocks on NSE, append '.NS' (e.g., INFY.NS, RELIANCE.NS, TCS.NS)")
        print("      For Indian stocks on BSE, append '.BO' (e.g., INFY.BO)")
        print("      For US stocks, just enter the ticker (e.g., AAPL, NVDA)")
        ticker_symbol = input("Ticker Symbol: ").strip().upper()
        
    return ticker_symbol

def fetch_data_and_fundamentals(ticker_symbol):
    print(f"\n[1] Fetching live data for {ticker_symbol} from Yahoo Finance...")
    ticker = yf.Ticker(ticker_symbol)

    df = ticker.history(period="5y")
    
    if df.empty:
        raise ValueError(f"Could not fetch data for {ticker_symbol}. Please check the ticker symbol.")
        
    df = df.reset_index()
    if df['Date'].dt.tz is not None:
        df['Date'] = df['Date'].dt.tz_localize(None)

    print("\n" + "="*50)
    print(f"FUNDAMENTAL ANALYSIS: {ticker_symbol}")
    print("="*50)
    try:
        info = ticker.info
        print(f"Company:        {info.get('shortName', 'N/A')}")
        print(f"Sector:         {info.get('sector', 'N/A')}")
        print(f"Industry:       {info.get('industry', 'N/A')}")
        print(f"Market Cap:     ${info.get('marketCap', 0):,}")
        print(f"P/E Ratio:      {info.get('trailingPE', 'N/A')} (Trailing) / {info.get('forwardPE', 'N/A')} (Forward)")
        print(f"Dividend Yield: {info.get('dividendYield', 0)*100:.2f}%" if info.get('dividendYield') else "Dividend Yield: N/A")
        print(f"52-Week High:   {info.get('fiftyTwoWeekHigh', 'N/A')}")
        print(f"52-Week Low:    {info.get('fiftyTwoWeekLow', 'N/A')}")

        pe_ratio = info.get('trailingPE')
        if pe_ratio:
           if float(pe_ratio) > 30:
               print("\nFundamental Note: High P/E ratio indicates the stock might be overvalued or a high-growth stock.")
           elif float(pe_ratio) < 15:
               print("\nFundamental Note: Low P/E ratio indicates the stock might be undervalued or a value play.")
    except Exception as e:
        print(f"\nCould not fetch fundamental data: {e}")
        
    return df

def add_ta_features(df):
    print("\n[2] Calculating Technical Analysis (TA) Indicators...")

    df = add_all_ta_features(
        df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True
    )

    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()

    latest = df.iloc[-1]
    
    print("\n" + "="*50)
    print("CURRENT TECHNICAL INDICATORS")
    print("="*50)
    
    rsi = latest.get('momentum_rsi', 50)
    macd = latest.get('trend_macd', 0)
    macd_signal = latest.get('trend_macd_signal', 0)
    close_price = latest['Close']
    sma50 = latest['SMA_50']
    
    print(f"Current Price:   {close_price:.2f}")
    
    rsi_status = "Neutral"
    if rsi >= 70: rsi_status = "OVERBOUGHT (Bearish Signal)"
    elif rsi <= 30: rsi_status = "OVERSOLD (Bullish Signal)"
    print(f"RSI (14-day):    {rsi:.2f} -> {rsi_status}")
    
    macd_status = "Bullish Crossover" if macd > macd_signal else "Bearish Crossover"
    print(f"MACD:            {macd:.2f} (Signal: {macd_signal:.2f}) -> {macd_status}")
    
    if not pd.isna(sma50):
        trend = "UPTREND" if close_price > sma50 else "DOWNTREND"
        print(f"Trend (50d SMA): {trend} (Price vs SMA: {close_price:.2f} vs {sma50:.2f})")
    
    return df

def prepare_targets(df):
    print("\n[3] Preparing Multi-Horizon Prediction Targets...")

    for name, days in PREDICTION_HORIZONS.items():
        future_column_name = f'Future_Close_{name}'
        df[future_column_name] = df['Close'].shift(-days)

        target_name = f'Target_{name}'
        df[target_name] = (df[future_column_name] > df['Close']).astype(int)

    latest_data = df.iloc[-1:].copy()

    df_train = df.dropna(subset=[f'Future_Close_{name}' for name in PREDICTION_HORIZONS.keys()])
    
    return df_train, latest_data

def train_and_predict(df_train, latest_data):
    print("\n[4] Training models for long-term forecasting...")

    exclude_cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']
    exclude_cols += [col for col in df_train.columns if 'Future_Close' in col or 'Target' in col]
    
    features = [col for col in df_train.columns if col not in exclude_cols]
    
    X = df_train[features]
    
    print("\n" + "="*50)
    print("PREDICTION RESULTS (RANDOM FOREST)")
    print("="*50)
    
    for name, days in PREDICTION_HORIZONS.items():
        y = df_train[f'Target_{name}']

        tscv = TimeSeriesSplit(n_splits=3)
        
        accuracy_scores = []
        model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
        
        for train_index, test_index in tscv.split(X):
            X_train, X_test = X.iloc[train_index], X.iloc[test_index]
            y_train, y_test = y.iloc[train_index], y.iloc[test_index]
            
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            accuracy_scores.append(accuracy_score(y_test, preds))
            
        avg_accuracy = np.mean(accuracy_scores)
        
        model.fit(X, y)

        X_latest = latest_data[features]
        prediction = model.predict(X_latest)[0]
        probability = model.predict_proba(X_latest)[0]

        horizon_label = name.replace('_', ' ')
        trend = "UP" if prediction == 1 else "DOWN"
        confidence = probability[prediction] * 100
        
        print(f"\n--- {horizon_label} Horizon ---")
        print(f"Historical Model Accuracy: {avg_accuracy*100:.2f}%")
        print(f"Prediction:                STOCK WILL GO {trend}")
        print(f"Confidence:                {confidence:.2f}%")

if __name__ == "__main__":
    try:
        ticker = get_ticker_input()

        df = fetch_data_and_fundamentals(ticker)
        df_ta = add_ta_features(df)
        df_train, latest_data = prepare_targets(df_ta)
        train_and_predict(df_train, latest_data)
        
        print("\n" + "="*50)
        print("Analysis Complete.")
        print("="*50 + "\n")
        
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")