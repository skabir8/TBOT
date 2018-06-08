import requests
import json
from bs4 import BeautifulSoup


def get_prev_day_info():
    r = requests.get('https://www.basketball-reference.com/boxscores/')
    data = r.text
    soup=BeautifulSoup(data, 'html.parser')
    game_dic = {}
    i = 0
    for x in soup.find_all('table',{'class':'teams'}):
        teams = x.find_all('a')
        scores = x.find_all('td', {'class':'right'})
        winner = [teams[0].string,scores[0].string]
        loser = [teams[2].string, scores[2].string]
        game_link = scores[1].find('a').get('href')
        game_dic['game'+str(i)] = {'winner':winner,'loser':loser,'link':game_link}
        i += 1
    return game_dic

def get_day_info(month,day,year):
    print("Getting Information for games on: " + str(month)+"/"+str(day)+"/"+str(year))
    base_url = "https://www.basketball-reference.com/boxscores/?"
    month = "month=" + str(month)
    day = "&day=" + str(day)
    year = "&year=" + str(year)
    url = base_url + month + day + year
    r = requests.get(url)
    data = r.text
    soup=BeautifulSoup(data, 'html.parser')
    game_dic = {}
    i = 0
    for x in soup.find_all('table',{'class':'teams'}):
        teams = x.find_all('a')
        scores = x.find_all('td', {'class':'right'})
        winner = [teams[0].string,scores[0].string]
        loser = [teams[2].string, scores[2].string]
        game_link = scores[1].find('a').get('href')
        game_dic['game'+str(i)] = {'winner':winner,'loser':loser,'link':game_link}
        print("Winner: " + str(winner) + " Loser: " + str(loser))
        i += 1
    return game_dic

def get_date_data(day,month,year):
    info = get_day_info(day,month,year)
    ret_dic = get_date_info(info)
    return ret_dic


def get_date_info(info):
    for x in info:
        base_url = "https://www.basketball-reference.com"
        url = base_url + info[x]['link']
        box_score_data = get_boxscore_data(url)
        info[x]['data'] = box_score_data
    return info



def get_prev_day_data():
    info = get_prev_day_info()
    for x in info:
        base_url = "https://www.basketball-reference.com"
        url = base_url + info[x]['link']
        box_score_data = get_boxscore_data(url)
        info[x]['data'] = box_score_data
    return info

def get_boxscore_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    box_scores_one = soup.findAll(class_="table_outer_container")[0].findAll('tr')[2:]
    box_scores_two = soup.findAll(class_="table_outer_container")[2].findAll('tr')[1:]
    info_dic = get_inner_box_data(box_scores_one,box_scores_two)
    return (info_dic)

def get_inner_box_data(table1,table2):
    info_dic = {'winner' : {}, 'loser' : {}}
    player_num = 0
    for players in table1:
        dat = players.findAll('td')
        if (players.find('a') != None):
            name = players.find('a').string
            info_dic['winner'][player_num] = {'player' : name}
            for x in dat:
                info_dic['winner'][player_num][x.attrs['data-stat']] = x.find(text=True)
            player_num += 1
    player_num = 0
    for players in table2:
        dat = players.findAll('td')
        if (players.find('a') != None):
            name = players.find('a').string
            info_dic['loser'][player_num] = {'player' : name}
            for x in dat:
                info_dic['loser'][player_num][x.attrs['data-stat']] = x.find(text=True)
            player_num += 1
    return info_dic



#print (get_prev_day_data())
print (get_date_data(2,5,2018))
