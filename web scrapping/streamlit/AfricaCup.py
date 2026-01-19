import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

st.set_page_config(page_title="African National Teams Scraper", layout="wide")

@st.cache_data
def get_african_teams():

    url = "https://en.wikipedia.org/wiki/2025_Africa_Cup_of_Nations"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        teams = {}
        teams_data = []
        
        table = soup.find('table', class_='wikitable sortable jquery-tablesorter')
        
        if not table:
            table = soup.find('table', class_='wikitable sortable')
        
        if not table:
            table = soup.find('table', class_='wikitable')
        
        if table:
            rows = table.find_all('tr')[1:]  
            
            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 2:
                    team_cell = cols[0]
                    link = team_cell.find('a')
                    
                    if link and link.get('href'):
                        team_name = link.get_text(strip=True)
                        team_url = "https://en.wikipedia.org" + link['href']
                        teams[team_name] = team_url
                        
                        team_info = {
                            'Team': team_name,
                            'Qualification Method': cols[1].get_text(strip=True) if len(cols) > 1 else '',
                            'Date of Qualification': cols[2].get_text(strip=True) if len(cols) > 2 else '',
                            'Total Appearances': cols[3].get_text(strip=True) if len(cols) > 3 else '',
                            'First Appearance': cols[4].get_text(strip=True) if len(cols) > 4 else '',
                            'Last Appearance': cols[5].get_text(strip=True) if len(cols) > 5 else '',
                            'Current Streak': cols[6].get_text(strip=True) if len(cols) > 6 else '',
                            'Previous Best': cols[7].get_text(strip=True) if len(cols) > 7 else ''
                        }
                        teams_data.append(team_info)
        
        return teams, teams_data
    except Exception as e:
        st.error(f"Error fetching teams: {e}")
        return {}, []

@st.cache_data
def get_team_squad(team_url):
    """Scrape squad/players for a specific team"""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(team_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        print(team_url)
        players = []
        
        tables = soup.find_all('table', class_='wikitable')
        
        for table in tables:

            headers = [th.text.strip().lower() for th in table.find_all('th')]
            
            if any(keyword in ' '.join(headers) for keyword in ['player', 'name', 'position', 'squad', 'no.']):
                rows = table.find_all('tr')[1:]  
                
                for row in rows:
                    cols = row.find_all(['td', 'th'])
                    if len(cols) >= 2:
                        player_data = {}
                        
                        for i, col in enumerate(cols):
                            text = col.get_text(strip=True)
                            
                            if i < len(headers):
                                header = headers[i]
                            else:
                                header = f"Column {i}"
                            
                            player_data[header] = text
                        
                        if player_data:
                            players.append(player_data)
        
        return players
    except Exception as e:
        st.error(f"Error fetching squad: {e}")
        return []

st.title("2025 Africa Cup of Nations - Teams & Players")
st.markdown("Scrape qualified teams and player information from Wikipedia")

with st.spinner("Loading qualified teams from 2025 AFCON..."):
    teams, teams_data = get_african_teams()

if teams:
    st.success(f"Found {len(teams)} qualified teams for AFCON 2025")
    
    st.header("Qualified Teams")
    if teams_data:
        df_teams = pd.DataFrame(teams_data)
        st.dataframe(df_teams, use_container_width=True, hide_index=True, height=600)
    else:
        st.warning("Teams loaded but no detailed data available. Showing team names:")
        st.write(list(teams.keys()))
        
        csv_teams = df_teams.to_csv(index=False)
        st.download_button(
            label="Download Teams List as CSV",
            data=csv_teams,
            file_name="afcon_2025_qualified_teams.csv",
            mime="text/csv"
        )
    
    st.markdown("---")
    
    st.header("Get Squad Information")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_team = st.selectbox(
            "Choose a team to view their squad:",
            options=sorted(teams.keys())
        )
    
    with col2:
        get_squad_btn = st.button("Get Squad", type="primary", use_container_width=True)
    
    if get_squad_btn and selected_team:
        st.subheader(f"🏃 {selected_team} Squad")
        
        with st.spinner(f"Scraping squad for {selected_team}..."):
            team_url = teams[selected_team]
            st.info(f"Source: {team_url}")
            
            players = get_team_squad(team_url)
            
            if players:
                st.success(f"Found {len(players)} players/entries")
                
                df_players = pd.DataFrame(players)
                st.dataframe(df_players, use_container_width=True, hide_index=True)
                
                csv = df_players.to_csv(index=False)
                st.download_button(
                    label="Download Squad as CSV",
                    data=csv,
                    file_name=f"{selected_team.replace(' ', '_')}_squad.csv",
                    mime="text/csv"
                )
            else:
                st.warning("No squad information found.")
                st.info("Try visiting the team page directly to check if squad information exists.")
else:
    st.error("Failed to load teams. Please check your internet connection.")



