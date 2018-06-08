import requests
import json


def get_players():
    r = requests.get("https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2017-18&SeasonType=Regular+Season&StatCategory=PTS")
    data = r.json()
    player = []
    outfile = open('data/player_name.txt','w')
    for x in data['resultSet']['rowSet']:
        player.append(x[2])
    outfile.write('\n'.join(player))
    outfile.close()
    return player
