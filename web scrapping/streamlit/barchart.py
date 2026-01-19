import requests
import pandas as pd
import streamlit as st

def bitcoin_line_chart(days=7):
    """
    Displays a true Streamlit line chart of Bitcoin price
    using CoinGecko's API (interactive, not an image).
    """
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days}"

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except Exception as e:
        st.error(f"Error fetching chart data: {e}")
        return

    # Extract [timestamp, price]
    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    df = df.set_index("timestamp")

    st.line_chart(df["price"])



st.subheader("📈 Bitcoin Price Line Chart")
bitcoin_line_chart(days=100)
