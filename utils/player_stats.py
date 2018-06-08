import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
import ast
import os
import player_link


def get_season_stats(player_name):
    url = player_link.get_player_season_link(player_name)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    season_splits = soup.find(class_="overthrow table_container")
    tables = soup.findAll('table')[0].findAll('tr')[1:]
    info_dic = make_season_dic(tables)
    return info_dic

def get_game_logs(player_name):
    url = player_link.get_player_log_link(player_name)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    game_logs = soup.find(class_="overthrow table_container").findAll('tr')[1:]
    #print(game_logs[1])
    x = make_game_dic(game_logs)
    print(x)

def make_game_dic(tables):
    info_dic = {}
    game_num = 1
    for games in tables:
        dat = games.findAll('td')
        info_dic[game_num] = {}
        for x in dat:
            info_dic[game_num][x.attrs['data-stat']] = x.find(text=True)
        game_num += 1
    return info_dic


def make_season_dic(tables):
    info_dic = {}
    season_num = 1
    for seasons in tables:
        dat = seasons.findAll('td')
        info_dic[season_num] = {}
        for x in dat:
            info_dic[season_num][str(x.attrs['data-stat'])] = x.find(text=True)
        season_num += 1
    return info_dic

print(get_game_logs("Emmanuel Mudiay"))
