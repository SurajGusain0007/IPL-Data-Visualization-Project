import streamlit as st
import pandas as pd
import plotly.express as px

team = pd.read_csv("teams.csv")
player_info = pd.read_csv("most_runs_average_strikerate.csv")
home_away = pd.read_csv("teamwise_home_and_away.csv")
team['team1'] = team['team1'].replace("Delhi Daredevils", "Delhi Capitals")
team['team1'] = team['team1'].replace("Rising Pune Supergiant", "Rising Pune Supergiants")

list_team = team['team1'].unique()

matches = pd.read_csv("matches.csv")
matches['team1'] = matches['team1'].replace("Delhi Daredevils", "Delhi Capitals")
matches['team2'] = matches['team2'].replace("Delhi Daredevils", "Delhi Capitals")

matches['team1'] = matches['team1'].replace("Rising Pune Supergiant", "Rising Pune Supergiants")
matches['team2'] = matches['team2'].replace("Delhi Daredevils", "Delhi Capitals")

matches['winner'] = matches['winner'].replace("Delhi Daredevils", "Delhi Capitals")
matches['winner'] = matches['winner'].replace("Rising Pune Supergiant", "Rising Pune Supergiants")


def team(y):
    st.text(y + " " + " " + "Team Analysis 2008-2019")
    x = matches[(matches['team1'] == y) | (matches['team2'] == y)].sort_values(by='Season').reset_index()
    x1 = x[['Season', 'team1', 'team2', 'winner', 'player_of_match']]
    st.dataframe(x1)
    st.text("Total Match Wins Against" + " " + y + " " + "from 2008-2019")
    winning_match = x['winner'].value_counts().reset_index().rename(
        columns={'index': "Team", 'winner': "Total Match Wins"})
    result = winning_match.iloc[1:, 0:]
    fig = px.bar(result, result['Team'], result['Total Match Wins'],
                 color='Total Match Wins')
    st.plotly_chart(fig)
    st.text("Matches played by" + " " + y + " " + "in different venue")
    venue_match = x['venue'].value_counts().reset_index().rename(
        columns={'index': "Venue", 'venue': "Total Matches played"})
    venue_result = venue_match.iloc[1:, 0:]
    fig1 = px.bar(venue_result, venue_result['Venue'], venue_result['Total Matches played'],
                  color='Total Matches played', width=800, height=800)
    st.plotly_chart(fig1)

    toss_decision1 = x['toss_decision'].value_counts().reset_index().rename(
        columns={'index': "toss_decision", 'toss_decision': "count"})
    fig2 = px.pie(toss_decision1, values='count', names='toss_decision', title="Toss_decision ")
    st.plotly_chart(fig2)

    city_result = x['city'].value_counts().reset_index().rename(columns={'index': "city", "city": "total"})
    fig3 = px.pie(city_result, values='total', names='city', title="Total number of cities where match has played")
    st.plotly_chart(fig3)

    st.text("Winning Toss by each team ")
    toss_result = x['toss_winner'].value_counts().reset_index().rename(
        columns={'index': "Toss_winner", "toss_winner": "count"})
    fig4 = px.pie(toss_result, values='count', names='Toss_winner')
    st.plotly_chart(fig4)

    st.text("Top 10 player name who wins most of the Player of the match ")
    result_player = x['player_of_match'].value_counts().reset_index().rename(
        columns={'index': "Player_of_match", "player_of_match": "total"}).head(10)
    fig5 = px.pie(result_player, values='total', names='Player_of_match')
    st.plotly_chart(fig5)

    st.text("Matches win in each year by each team")
    fig7 = px.line(x, x['date'], x['winner'], width=800, height=400)
    fig7.update_xaxes(showgrid=False)
    fig7.update_yaxes(showgrid=False)

    fig7.show()
    st.plotly_chart(fig7)

    st.text("Stand Umpire1 for Match ")
    result_umpire = x['umpire1'].value_counts().reset_index().rename(
        columns={'index': "umpire name", "umpire1": "total"})
    fig8 = px.bar(result_umpire, result_umpire['umpire name'], result_umpire['total'], color='total')

    st.plotly_chart(fig8)

    st.text("Stand Umpire2 for Match ")
    result_umpire = x['umpire2'].value_counts().reset_index().rename(
        columns={'index': "umpire name", "umpire2": "total"})
    fig9 = px.bar(result_umpire, result_umpire['umpire name'], result_umpire['total'], color='total')

    st.plotly_chart(fig9)

    st.text("Match Result")
    match_result = x['result'].value_counts().reset_index().rename(columns={'index': "Match result", "result": "total"})
    fig10 = px.pie(match_result, values='total', names="Match result")
    st.plotly_chart(fig10)


st.sidebar.title("IPL 2008-2019 Analysis")

selected_team = st.sidebar.selectbox('Select a team', list_team)
btnl = st.sidebar.button("Find Select Team Analysis")

if btnl:

    if selected_team == 'Delhi Capitals':
        team(selected_team)
    elif selected_team == "Mumbai Indians":
        team(selected_team)
    elif selected_team == "Rajasthan Royals":
        team(selected_team)
    elif selected_team == "Chennai Super Kings":
        team(selected_team)
    elif selected_team == 'Sunrisers Hyderabad':
        team(selected_team)
    elif selected_team == 'Rising Pune Supergiants':
        team(selected_team)
    elif selected_team == 'Kolkata Knight Riders':
        team(selected_team)
    elif selected_team == 'Gujarat Lions':
        team(selected_team)
    elif selected_team == "Deccan Chargers":
        team(selected_team)
    elif selected_team == "Kings XI Punjab":
        team(selected_team)

    elif selected_team == "Royal Challengers Bangalore":
        team(selected_team)
    elif selected_team == "Pune Warriors":
        team(selected_team)

    elif selected_team == "Kochi Tuskers Kerala":
        team(selected_team)

button3 = st.sidebar.button("Find _home_and_away scorecard")

if button3:
    st.text("Team wise Home and away scorecard")
    # st.dataframe(home_away)

    fig23 = px.bar(home_away, home_away['team'], home_away['home_wins'], color='home_wins', title='Teamwise Home wins')
    fig23.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
    fig23.show()
    st.plotly_chart(fig23)

    fig24 = px.bar(home_away, home_away['team'], home_away['away_wins'], color='away_wins', title='teamwise away wins')
    fig24.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})
    fig24.show()
    st.plotly_chart(fig24)

    fig25 = px.bar(home_away, home_away['team'], home_away['home_matches'], color='home_matches',
                   title='Team-wise home matches')
    fig25.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})
    fig25.show()
    st.plotly_chart(fig25)

    fig26 = px.bar(home_away, home_away['team'], home_away['away_matches'], color='away_matches',
                   title='Team-wise away matches')
    fig26.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})
    fig26.show()
    st.plotly_chart(fig26)

    fig27 = px.pie(home_away, names='team', values='home_win_percentage', title="Team wise home win percentage")
    st.plotly_chart(fig27)

    fig28 = px.pie(home_away, names='team', values='away_win_percentage', title="Team wise away win percentage")
    st.plotly_chart(fig28)

centuary = pd.read_csv("Fastest Centuries All Seasons Combine.csv").sort_values(by='BF', ascending=True).reset_index()
centuary.drop(columns="Unnamed: 0", inplace=True)
centuary.drop(columns='index', inplace=True)
b = pd.read_csv("Fastest Fifties All Seasons Combine.csv").sort_values(by='BF', ascending=True).reset_index()
b.drop(columns='Unnamed: 0', inplace=True)
b.drop(columns="index", inplace=True)
c = pd.read_csv("Most Wickets All Seasons Combine.csv")
c.drop(columns='Unnamed: 0', inplace=True)
d = pd.read_csv("Best Bowling Economy Per Innings All Seasons Combine.csv")
d.drop(columns='Unnamed: 0', inplace=True)
e = pd.read_csv("Most Sixes Per Innings All Seasons Combine.csv")
e.drop(columns='Unnamed: 0', inplace=True)
f = pd.read_csv("Most Fours Per Innings All Seasons Combine.csv")
f.drop(columns='Unnamed: 0', inplace=True)

list_name = ['Fastest century scorecard', 'Fastest fifties scorecard', 'Most wickets scorecard', 'Best Bowling Economy',
             'Most Sixes per innings', 'Most Fours per innings']
xx = st.sidebar.selectbox("Select Any Category ", list_name)
btnl3 = st.sidebar.button("Find  All Seasons Combine Scorecard")
if btnl3:
    if xx == 'Fastest century scorecard':
        st.text("Fastest Centuries All Season Combine")
        st.dataframe(centuary)
    elif xx == 'Fastest fifties scorecard':
        st.text("Fastest Fifties All seasons Combined")
        st.dataframe(b)
    elif xx == 'Most wickets scorecard':
        st.text("Most wickets All Seasons Combined")
        st.dataframe(c)
    elif xx == 'Best Bowling Economy':
        st.text("Best Bowling Economy Per innings All Seasons Combine")
        st.dataframe(d)
    elif xx == 'Best Bowling Economy':
        st.text("Best Bowling Economy Per innings All Seasons Combine")
        st.dataframe(d)

    elif xx == 'Most Sixes per innings':
        st.text("Most Sixes Per innings All Seasons")
        st.dataframe(e)
    elif xx == 'Most Fours per innings':
        st.text("Most Fours Per innings All Seasons")
        st.dataframe(f)

most_run = pd.read_csv("Most Runs All Seasons Combine.csv")
player_bio = most_run['Player'].unique()

most_run1 = most_run.groupby('Player')[['Mat', 'Inns', 'Runs', 'NO', 'BF', '100', '50', '4s', '6s']].sum().sort_values(
    by='Runs',
    ascending=False).reset_index()
selected_player = st.sidebar.selectbox('Select a player', player_bio)
button6 = st.sidebar.button("Find Player Statistics")

if button6:
    z1 = most_run1[most_run1['Player'] == selected_player]
    st.subheader("Player Statistics")
    st.metric("Total Matches", z1['Mat'])
    st.metric("Total Innings", z1['Inns'])
    st.metric('Total Runs', z1['Runs'])
    st.metric("Total Not Out", z1['NO'])
    st.metric("Ball Faced", z1['BF'])
    st.metric("Total century", z1['100'])
    st.metric("Total Fifties", z1['50'])
    st.metric("Total Sixes", z1['6s'])
    st.metric("Total Fours", z1['4s'])

