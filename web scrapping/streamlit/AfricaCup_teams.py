import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

st.set_page_config(page_title="African National Teams Scraper", layout="wide")

TRANSFERMARKT_TEAMS = {
    'Morocco': 3575,
    'Egypt': 3672,
    'Algeria': 3614,
    'Senegal': 3499,
    'Tunisia': 3670,
    'Nigeria': 3444,
    'Cameroon': 3434,
    'Ghana': 3441,
    'Ivory Coast': 3591,
    'Mali': 3674,
    'Burkina Faso': 5872,
    'South Africa': 3806,
    'Angola': 3585,
    'Zimbabwe': 3583,
    'Mozambique': 5129,
    'Tanzania': 14666,
    'Zambia': 3703,
    'Uganda': 13497,
    'Botswana': 15229,
    'Equatorial Guinea': 13485,
    'Comoros': 16430,
    'Sudan': 13313,
    'Benin': 3955,
    'Gabon': 5704
}

@st.cache_data
def get_african_teams():
    """Get qualified teams from Wikipedia"""
    url = "https://en.wikipedia.org/wiki/2025_Africa_Cup_of_Nations"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        teams = {}
        teams_data = []
        
        table = soup.find('table', class_='wikitable sortable jquery-tablesorter') \
                or soup.find('table', class_='wikitable sortable') \
                or soup.find('table', class_='wikitable')
        
        if table:
            rows = table.find_all('tr')[1:]
            
            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 2:
                    team_cell = cols[0]
                    link = team_cell.find('a')
                    
                    if link and link.get('href'):
                        team_name = link.get_text(strip=True)
                        team_id = None
                        for tm_team, tm_id in TRANSFERMARKT_TEAMS.items():
                            if tm_team.lower() in team_name.lower() or team_name.lower() in tm_team.lower():
                                team_id = tm_id
                                break
                        
                        if team_id:
                            transfermarkt_url = f"https://www.transfermarkt.com/{team_name.lower().replace(' ', '-')}/kader/verein/{team_id}/plus/0/galerie/0?saison_id=2024"
                            teams[team_name] = transfermarkt_url
                        
                        team_info = {
                            'Team': team_name,
                            'Qualification Method': cols[1].get_text(strip=True) if len(cols) > 1 else '',
                            'Date of Qualification': cols[2].get_text(strip=True) if len(cols) > 2 else '',
                            'Total Appearances': cols[3].get_text(strip=True) if len(cols) > 3 else '',
                            'First Appearance': cols[4].get_text(strip=True) if len(cols) > 4 else '',
                            'Last Appearance': cols[5].get_text(strip=True) if len(cols) > 5 else '',
                            'Current Streak': cols[6].get_text(strip=True) if len(cols) > 6 else '',
                            'Previous Best': cols[7].get_text(strip=True) if len(cols) > 7 else '',
                            'Transfermarkt Available': '✅' if team_id else '❌'
                        }
                        teams_data.append(team_info)
        
        return teams, teams_data
    except Exception as e:
        st.error(f"Error fetching teams: {e}")
        return {}, []

@st.cache_data
def get_team_squad_transfermarkt(team_url):
    """Scrape squad/players from Transfermarkt with updated image handling"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(team_url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        players = []
        table = soup.find('table', class_='items')
        if not table:
            st.warning("Could not find table with class 'items'")
            return []
        
        tbody = table.find('tbody')
        if not tbody:
            return []
        
        rows = tbody.find_all('tr', class_=['odd', 'even'])
        for row in rows:
            player_data = {}
            
            player_cell = row.find('td', class_='hauptlink')
            if player_cell:
                player_link = player_cell.find('a')
                if player_link:
                    player_data['Player Name'] = player_link.get_text(strip=True)
                    player_data['Profile URL'] = 'https://www.transfermarkt.com' + player_link['href']
            
            img = row.find('img', class_='bilderrahmen-fixed')
            if img:
                player_data['Image URL'] = img.get('data-src') or img.get('src')
            
            number_cell = row.find('div', class_='rn_nummer')
            if number_cell:
                player_data['Number'] = number_cell.get_text(strip=True)
            
            for cell in row.find_all('td'):
                if 'inline-table' in cell.get('class', []):
                    pos = cell.get_text(strip=True)
                    if pos:
                        player_data['Position'] = pos
            
            for cell in row.find_all('td'):
                text = cell.get_text(strip=True)
                if 'zentriert' in cell.get('class', []) and any(c.isdigit() for c in text):
                    player_data['Age'] = text
                if 'rechts' in cell.get('class', []) and ('€' in text or 'Th.' in text or 'm' in text):
                    player_data['Market Value'] = text
            
            flags = row.find_all('img', class_='flaggenrahmen')
            if flags:
                player_data['Nationality'] = ', '.join([f['title'] for f in flags if f.get('title')])
            
            if player_data and 'Player Name' in player_data:
                players.append(player_data)
        return players
    except Exception as e:
        st.error(f"Error fetching squad from Transfermarkt: {e}")
        return []


st.title("2025 Africa Cup of Nations - Teams & Players")
st.markdown("Scrape qualified teams from Wikipedia and player data from Transfermarkt")

with st.spinner("Loading qualified teams from 2025 AFCON..."):
    teams, teams_data = get_african_teams()

if teams:
    st.success(f"Found {len(teams)} qualified teams for AFCON 2025")
    
    st.header("Qualified Teams")
    if teams_data:
        df_teams = pd.DataFrame(teams_data)
        st.dataframe(df_teams, use_container_width=True, hide_index=True, height=600)
        csv_teams = df_teams.to_csv(index=False)
        st.download_button(
            label="Download Teams List as CSV",
            data=csv_teams,
            file_name="afcon_2025_qualified_teams.csv",
            mime="text/csv"
        )
    
    st.markdown("---")
    st.header("Get Squad Information from Transfermarkt")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        selected_team = st.selectbox(
            "Choose a team to view their squad:",
            options=sorted(teams.keys())
        )
    with col2:
        get_squad_btn = st.button("Get Squad", type="primary", use_container_width=True)
    
    if get_squad_btn and selected_team:
        st.subheader(f"{selected_team} Squad (Transfermarkt)")
        with st.spinner(f"Scraping squad for {selected_team} from Transfermarkt..."):
            team_url = teams[selected_team]
            st.info(f"Source: {team_url}")
            players = get_team_squad_transfermarkt(team_url)
            
            if players:
                st.success(f"Found {len(players)} players")
                df_players = pd.DataFrame(players)
                
                column_order = ['Number', 'Player Name', 'Position', 'Age', 'Nationality', 'Market Value', 'Profile URL', 'Image URL']
                existing_cols = [col for col in column_order if col in df_players.columns]
                other_cols = [col for col in df_players.columns if col not in column_order]
                df_players = df_players[existing_cols + other_cols]
                
                def show_image(url):
                    return f"<img src='{url}' width='50'>" if url else ""
                
                if 'Image URL' in df_players.columns:
                    df_players['Image'] = df_players['Image URL'].apply(show_image)
                    df_players.drop(columns=['Image URL'], inplace=True)
                
                st.write(df_players.to_html(escape=False, index=False), unsafe_allow_html=True)
                
                csv = df_players.to_csv(index=False)
                st.download_button(
                    label="Download Squad as CSV",
                    data=csv,
                    file_name=f"{selected_team.replace(' ', '_')}_squad_transfermarkt.csv",
                    mime="text/csv"
                )
            else:
                st.warning("No squad information found.")
else:
    st.error("Failed to load teams. Please check your internet connection.")
