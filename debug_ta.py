import yfinance as yf
from ta import add_all_ta_features

def run_debug_check():
    try:
        print("Fetching data...")
        df = yf.Ticker('INFY.NS').history(period='2y')
        df.reset_index(inplace=True)
        print("Data shape before TA:", df.shape)
        print("Columns before TA:", df.columns)
        
        print("Adding TA features...")
        df = add_all_ta_features(
            df, 
            open="Open", 
            high="High", 
            low="Low", 
            close="Close", 
            volume="Volume", 
            fillna=True
        )
        print("Data shape after TA:", df.shape)
        print("Columns after TA:", len(df.columns))
    except Exception as e:
        print(f"Debug check failed: {e}")

if __name__ == "__main__":
    run_debug_check()
