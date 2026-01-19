import streamlit as st
import requests
from datetime import datetime

BASE_URL = "https://hn.algolia.com/api/v1/"

# ------------------------------
# Helper: Fetch data with pagination
# ------------------------------
@st.cache_data
def fetch_stories(endpoint, query="", page=0):
    if endpoint == "search":
        url = f"{BASE_URL}search?query={query}&page={page}"
    elif endpoint == "top":
        url = f"{BASE_URL}search?tags=front_page&page={page}"
    else:  # latest
        url = f"{BASE_URL}search_by_date?tags=story&page={page}"
    
    response = requests.get(url)
    return response.json()

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🚀 Hacker News Browser")
st.write("Browse Hacker News stories using the public Algolia API")

# Session state for pagination
if "page" not in st.session_state:
    st.session_state.page = 0

# Tabs for modes
tab1, tab2, tab3 = st.tabs(["🔥 Top Stories", "🆕 Latest", "🔍 Search"])

# ------------------------------
# Top Stories TAB
# ------------------------------
with tab1:
    st.header("🔥 Top Stories")
    
    data = fetch_stories("top", page=st.session_state.page)

    for item in data["hits"]:
        st.subheader(item["title"] or "No title")
        st.write(f"⭐ {item['points']}  | 👤 {item['author']}")
        st.write(f"🔗 [View Post]({item['url']})")
        st.markdown("---")

    # Pagination buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Previous"):
            st.session_state.page = max(st.session_state.page - 1, 0)
    with col2:
        if st.button("Next ➡"):
            st.session_state.page += 1

# ------------------------------
# Latest Stories TAB
# ------------------------------
with tab2:
    st.header("🆕 Latest Stories")
    st.session_state.page = 0  # reset page for new tab
    data = fetch_stories("latest")

    for item in data["hits"]:
        title = item["title"] or "<no title>"
        date = datetime.fromtimestamp(item["created_at_i"]).strftime("%Y-%m-%d %H:%M")
        st.subheader(title)
        st.write(f"🗓 {date} | 👤 {item['author']}")
        st.write(f"🔗 [View Post]({item['url']})")
        st.markdown("---")

# ------------------------------
# Search TAB
# ------------------------------
with tab3:
    st.header("🔍 Search Hacker News")

    query = st.text_input("Enter search keyword (e.g. 'python', 'AI')", "")
    
    if query:
        data = fetch_stories("search", query=query, page=st.session_state.page)

        for item in data["hits"]:
            st.subheader(item["title"] or "No title")
            st.write(f"⭐ {item['points']} | 👤 {item['author']}")
            st.write(f"🔗 [View Post]({item['url']})")
            st.markdown("---")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅ Previous", key="search_prev"):
                st.session_state.page = max(st.session_state.page - 1, 0)
        with col2:
            if st.button("Next ➡", key="search_next"):
                st.session_state.page += 1
