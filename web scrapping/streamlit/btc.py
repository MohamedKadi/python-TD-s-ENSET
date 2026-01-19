import requests
import streamlit as st

API_URL = "https://api.coingecko.com/api/v3/coins/bitcoin"

# ---------------------------
# Fetching function (API instead of scraping)
# ---------------------------
def fetch_bitcoin_data():
    """
    Fetch Bitcoin metrics using the official CoinGecko API.
    This avoids scraping problems entirely.
    """
    try:
        res = requests.get(API_URL, timeout=10)
        res.raise_for_status()
        data = res.json()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

    try:
        return {
            "price": f"${data['market_data']['current_price']['usd']:,}",
            "change_24h": f"{data['market_data']['price_change_percentage_24h']:.2f}%",
            "market_cap": f"${data['market_data']['market_cap']['usd']:,}",
            "volume_24h": f"${data['market_data']['total_volume']['usd']:,}",
            "rank": data["market_cap_rank"],
        }
    except KeyError:
        st.error("Unexpected response structure from API.")
        return None


# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Simple Bitcoin Price Tracker", page_icon="₿", layout="wide")
st.title("₿ Simple Bitcoin Price Tracker (CoinGecko API)")
st.write("Real-time Bitcoin metrics pulled from the official CoinGecko API (100% reliable).")

# Button
if st.button("Refresh Data", help="Click to load the latest Bitcoin data"):
    
    with st.spinner('Fetching latest Bitcoin data...'):
        btc = fetch_bitcoin_data()

    if btc:
        st.success("Data updated successfully!")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Bitcoin Price", btc["price"], btc["change_24h"])
        with col2:
            st.metric("Market Cap", btc["market_cap"])
        with col3:
            st.metric("24h Volume", btc["volume_24h"])
        with col4:
            st.metric("Rank", btc["rank"])
            
        st.markdown("---")
        st.info("Bar chart removed as requested — no historical data or Plotly used.")

    else:
        st.error("Failed to retrieve data.")

else:
    st.info("Click 'Refresh Data' to load the latest Bitcoin data.")
