[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [string]$Ticker
)

$scriptPath = Join-Path $PSScriptRoot "stock_trend_predictor.py"

if (-not $Ticker) {
    Write-Host "No ticker provided. Please provide a ticker symbol (e.g., INFY.NS or AAPL)."
    Write-Host "Usage: .\run_stock_trend_predictor.ps1 INFY.NS"
} else {
    $venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

    if (Test-Path $venvPython) {
        & $venvPython -u $scriptPath --ticker $Ticker
    } else {
        Write-Host ".venv not found. Running with system python..."
        python -u $scriptPath --ticker $Ticker
    }
}
