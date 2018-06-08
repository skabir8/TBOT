import requests
from bs4 import BeautifulSoup
import ast
import random
import os
import difflib

player_names = ['Giannis Antetokounmpo', 'Anthony Davis', 'Kristaps Porzingis', 'DeMarcus Cousins', 'Blake Griffin', 'Stephen Curry', 'James Harden', 'Nikola Vucevic', 'John Wall', 'Dennis Schroder', 'LaMarcus Aldridge', 'Bradley Beal', 'Kemba Walker', 'LeBron James', 'Paul George', 'Tobias Harris', 'Carmelo Anthony', 'Marc Gasol', 'Damian Lillard', 'Kevin Durant', 'Andrew Wiggins', "D'Angelo Russell", 'Eric Gordon', 'Victor Oladipo', 'DeMar DeRozan', 'Klay Thompson', 'Goran Dragic', 'Kyrie Irving', 'Brook Lopez', 'Evan Fournier', 'Karl-Anthony Towns', 'Otto Porter Jr.', 'Will Barton', 'Brandon Ingram', 'Mike Conley', 'Paul Millsap', 'Trevor Booker', 'Jordan Clarkson', 'Harrison Barnes', 'Jaylen Brown', 'Dion Waiters', 'Kevin Love', 'Robin Lopez', 'Devin Booker', 'Reggie Jackson', 'Lonzo Ball', 'Malcolm Brogdon', 'Ben Simmons', 'Clint Capela', 'Eric Bledsoe', 'Jerryd Bayless', 'Gary Harris', 'Robert Covington', 'Darren Collison', 'Dwight Howard', 'Jeremy Lamb', 'Justin Holiday', 'Lauri Markkanen', 'Lou Williams', 'Joe Ingles', 'Ricky Rubio', 'Rudy Gobert', 'Kyle Lowry', 'Rondae Hollis-Jefferson', 'Serge Ibaka', 'Derrick Favors', 'Dillon Brooks', 'Jonas Valanciunas', 'Larry Nance Jr.', 'Yogi Ferrell', "De'Aaron Fox", 'George Hill', 'J.J. Barea', 'Jonathon Simmons', 'Khris Middleton', 'TJ Warren', 'CJ Miles', 'DeMarre Carroll', 'Delon Wright', 'Enes Kanter', 'Jamal Crawford', 'Russell Westbrook', 'Evan Turner', 'Al Horford', 'Danny Green', 'Jusuf Nurkic', 'Marcin Gortat', 'Rudy Gay', 'Thaddeus Young', 'Andre Drummond', 'Avery Bradley', 'Terry Rozier', 'Frank Kaminsky', 'James Johnson', 'Jimmy Butler', 'Marco Belinelli', 'Patrick Beverley', 'Taurean Prince', 'Domantas Sabonis', 'JJ Redick', 'Jayson Tatum', 'Dejounte Murray', 'Buddy Hield', 'Josh Jackson', 'Mike James', 'Pat Connaughton', 'Danilo Gallinari', 'Jodie Meeks', 'Kelly Olynyk', 'Kyle Kuzma', 'Tyreke Evans', 'Josh Richardson', 'Skal Labissiere', 'Tim Hardaway Jr.', 'Willie Cauley-Stein', 'Bojan Bogdanovic', 'Allen Crabbe', 'Caris LeVert', 'Jeff Teague', "Kyle O'Quinn", 'Steven Adams', 'Tony Snell', 'DeAndre Jordan', 'Dewayne Dedmon', 'Jerian Grant', 'Kenneth Faried', 'Willie Reed', 'D.J. Augustin', 'Joe Johnson', 'PJ Tucker', 'Terrence Ross', 'John Collins', 'Nemanja Bjelica', 'Emmanuel Mudiay', 'James Ennis III', 'Jordan Crawford', 'Kelly Oubre Jr.', 'Kent Bazemore', 'Nerlens Noel', 'Spencer Dinwiddie', 'Al-Farouq Aminu', 'Cory Joseph', 'Ish Smith', 'Maurice Harkless', 'Nick Young', 'Ryan Anderson', 'Wesley Matthews', 'Ian Clark', 'Jrue Holiday', 'Julius Randle', 'Norman Powell', 'Pau Gasol', 'Iman Shumpert', 'Jae Crowder', 'Alec Burks', 'Denzel Valentine', 'Jakob Poeltl', 'Justise Winslow', 'Kyle Anderson', 'Lance Stephenson', 'Luc Mbah a Moute', 'Tyler Johnson', 'Ed Davis', 'Jeff Green', 'Tyson Chandler', 'Mario Chalmers', 'Mike Scott', 'Dirk Nowitzki', 'Draymond Green', 'Markelle Fultz', 'TJ Leaf', 'Chandler Parsons', 'Dario Saric', 'Dwayne Bacon', 'Manu Ginobili', 'Stanley Johnson', 'Treveon Graham', 'Wilson Chandler', 'Aron Baynes', 'Bismack Biyombo', 'Jon Leuer', 'Matthew Dellavedova', 'Thabo Sefolosha', 'Courtney Lee', 'Dante Cunningham', 'Mike Muscala', 'Ramon Sessions', 'David West', 'JR Smith', 'Kyle Korver', 'Brandan Wright', 'Greg Monroe', 'Jonathan Isaac', 'Kay Felder', 'Luke Babbitt', 'Mason Plumlee', 'OG Anunoby', 'Quincy Acy', 'Trevor Ariza', 'Wesley Johnson', 'Dwyane Wade', 'Garrett Temple', 'Tristan Thompson', "E'Twaun Moore", 'Ian Mahinmi', 'Milos Teodosic', 'Sindarius Thornwell', 'Wayne Ellington', 'Dorian Finney-Smith', 'John Henson', 'Shaun Livingston', 'Alex Abrines', 'Dwight Powell', 'Jamal Murray', 'Jarell Martin', 'Paul Zipser', 'Raymond Felton', 'Shabazz Napier', 'Taj Gibson', 'Donovan Mitchell', 'Marquese Chriss', 'Troy Daniels', 'Zaza Pachulia', 'Andre Roberson', 'David Nwaba', 'Doug McDermott', 'Joffrey Lauvergne', 'Malik Monk', 'Ron Baker', 'Jerami Grant', 'Jordan Bell', 'Justin Jackson', 'Malcolm Delaney', 'Michael Beasley', 'Mirza Teletovic', 'Montrezl Harrell', 'Thon Maker', 'Timofey Mozgov', 'Vince Carter', 'Amir Johnson', 'Timothe Luwawu-Cabarrot', 'Andrew Harrison', 'Austin Rivers', 'Corey Brewer', 'Marvin Williams', 'Nikola Jokic', 'Sam Dekker', 'Cristiano Felicio', 'Ersan Ilyasova', 'Julyan Stone', 'Dragan Bender', 'T.J. McConnell', 'Fred VanVleet', 'Gorgui Dieng', 'Patty Mills', 'Trey Lyles', 'Ekpe Udoh', 'Kosta Koufos', 'Bryn Forbes', 'Darius Miller', 'Pascal Siakam', 'Shabazz Muhammad', 'Josh Huestis', 'Josh Magette', 'Tyus Jones', 'Damien Wilkins', 'Alex Caruso', 'Terrance Ferguson', 'Tyler Ennis', 'Andrew Bogut', 'Brandon Paul', 'Juan Hernangomez', 'Malik Beasley', 'Patrick Patterson', 'Tim Frazier', 'Tony Allen']



def get_player_season_link(player_name):
    global player_names
    try:
        player_name = difflib.get_close_matches(player_name, player_names)[0]
    except:
        player_name = "Kristaps Porzingis"
    player_name = player_name.lower()
    base_name = player_name.split(' ')
    alpha = base_name [1][0] + '/'
    base_name = base_name[1][0:5]+ base_name[0][0:2] + '01' + '.html'
    stat_url = 'https://www.basketball-reference.com/players/' + alpha + base_name
    return stat_url

def get_player_log_link(player_name):
    global player_names
    try:
        player_name = difflib.get_close_matches(player_name, player_names)[0]
    except:
        player_name = "Kristaps Porzingis"
    player_name = player_name.lower()
    base_name = player_name.split(' ')
    alpha = base_name [1][0] + '/'
    base_name = base_name[1][0:5]+ base_name[0][0:2] + '01' + '/gamelog/2018'
    stat_url = 'https://www.basketball-reference.com/players/' + alpha + base_name
    return stat_url

def open_name_file():
    f = open('../data/pnames.txt','r')
    message = f.readlines()
    ret_list = []
    for x in message:
        ret_list.append(x.strip('\n'))
    return (ret_list)

#open_name_file()
#print (player_names)

#print(get_player_link("lebrn jams"))
