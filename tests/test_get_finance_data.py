import yfinance as yf
from tradingagents.dataflows.config import get_config, set_config
from tradingagents.dataflows.interface import route_to_vendor

# yf.config.network.proxy = "http://127.0.0.1:7897"

print("Yahoo proxy:", yf.config.network.proxy)

set_config({
    "data_vendors": {
        "core_stock_apis": "yfinance,alpha_vantage",
    }
})

print("配置", get_config()["data_vendors"]["core_stock_apis"])

result = route_to_vendor(
    'get_stock_data',
    'AAPL',
    '2026-07-01',
    '2026-07-10',
)

print(result[:2000])
