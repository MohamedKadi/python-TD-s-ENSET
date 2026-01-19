import requests
from bs4 import BeautifulSoup
import streamlit as st

URL = "https://www.coingecko.com/en/coins/bitcoin"

# ---------------------------
# Scraping function
# ---------------------------
def scrape_bitcoin_data():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    data = {}

    # Price
    price_tag = soup.find("span", {"class": "no-wrap"})
    data["price"] = price_tag.text.strip() if price_tag else "N/A"

    # 24h change
    change_tag = soup.find("span", {"data-target": "percent-change.percent"})
    data["change_24h"] = change_tag.text.strip() if change_tag else "N/A"

    # Market cap
    mc_label = soup.find("span", string="Market Cap")
    if mc_label:
        mc_value = mc_label.find_next("span")
        data["market_cap"] = mc_value.text.strip()
    else:
        data["market_cap"] = "N/A"

    # 24h Volume
    vol_label = soup.find("span", string="24 Hour Trading Vol")
    if vol_label:
        vol_value = vol_label.find_next("span")
        data["volume_24h"] = vol_value.text.strip()
    else:
        data["volume_24h"] = "N/A"

    # Market Rank
    rank_tag = soup.find("span", {"class": "tw-text-gray-500"})
    data["rank"] = rank_tag.text.strip() if rank_tag else "N/A"

    return data


# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Bitcoin Price Tracker", page_icon="₿")
st.title("₿ Bitcoin Price Tracker")
st.write("Real-time Bitcoin metrics scraped from CoinGecko.")

# Button
if st.button("Refresh Data"):
    btc = scrape_bitcoin_data()
    st.success("Data updated!")

    st.metric("Bitcoin Price", btc["price"], btc["change_24h"])
    st.metric("Market Cap", btc["market_cap"])
    st.metric("24h Volume", btc["volume_24h"])
    st.metric("Rank", btc["rank"])

else:
    st.info("Click 'Refresh Data' to load the latest Bitcoin data.")
