# Finance Guide

## What this predictor means

This project predicts directional probability (UP/DOWN) over medium and long horizons based on historical price/volume patterns and technical indicators.

It does **not** guarantee returns, entry/exit timing, or capital protection.

## How to read model output

- **Prediction**: expected direction for a specific horizon
- **Confidence**: model probability for the predicted class
- **Historical Model Accuracy**: backtested cross-validation metric on past data

A high confidence with low historical accuracy should be treated cautiously.

## Practical usage approach

Use this as a screening signal, not a standalone trading system:

1. Validate trend signal against broader market context
2. Check valuation and fundamentals
3. Confirm liquidity and news flow
4. Define risk limits before taking positions

## Risk and compliance notes

- Markets are uncertain; past performance does not imply future performance.
- Always apply position sizing and stop-loss discipline.
- Verify tax, brokerage, and regulatory requirements for your jurisdiction.

## Suggested next improvements

- Add walk-forward testing and out-of-sample reports
- Add risk metrics (max drawdown, Sharpe-like measures)
- Add feature importance reporting for transparency
- Add alerting/report export for reproducible analysis
