#
import os



def get_players():
    r = requests.get("https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2017-18&SeasonType=Regular+Season&StatCategory=PTS")
    data = r.json()
    player = []
    outfile = open('../data/player_name.txt','w')
    for x in data['resultSet']['rowSet']:
        player.append(x[2])
    outfile.write('\n'.join(player))
    outfile.close()
    return player


def build_frequency_vector(s):
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / float(num_letters))
    return v

def distance(l1,l2):
    length = len(l1)
    if length>len(l2):
        length = len(l2)
    sum=0
    for i in range(length):
        sum = sum + (l1[i]-l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d


def build_name_vector():
    if (os.path.isfile('../data/player_name.txt') == True):
        pass
    else:
