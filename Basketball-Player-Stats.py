'''
To run, will need to install:
requests
bs4
lxml
'''

import requests
import bs4

# Dictionary of HTML tags that each stat is represented by
tag_names = {"Age": "age",
			 "Team": "team_id",
			 "Position": "pos",
			 "Games Played": "g",
			 "Field Goals Per Game": "fg_per_g",
			 "Field Goal Attempts Per Game": "fga_per_g",
			 "Field Goal %": "fg_pct",
			 "3-Point Per Game": "fg3_per_g",
			 "3-Point Attempts Per Game": "fg3a_per_g",
			 "3-Point %": "fg3_pct",
			 "2-Point Per Game": "fg2_per_g",
			 "2-Point Attempts Per Game": "fg2a_per_g",
			 "2-Point %": "fg2_pct",
			 "Free Throws Per Game ": "ft_per_g",
			 "Free Throw Attempts Per Game": "fta_per_g",
			 "Free Throw %": "ft_pct",
			 "Offensive Rebounds Per Game": "orb_per_g",
			 "Defensive Rebounds Per Game": "drb_per_g",
			 "Total Rebounds Per Game": "trb_per_g",
			 "Assists Per Game": "ast_per_g",
			 "Steals Per Game": "stl_per_g",
			 "Blocks Per Game": "blk_per_g",
			 "Turnovers Per Game": "tov_per_g",
			 "Fouls Per Game": "pf_per_g",
			 "Points Per Game": "pts_per_g",
}


base_url = "https://www.basketball-reference.com/players/{}/{}{}0{}.html"
base_year = "#per_game\.{}"
i = 1


def ask_player(name_req):  # Formats url to take you to the page of the player
	name_req = name_req.lower()
	first, last = name_req.split(' ')
	return base_url.format(last[0], last[0:5], first[0:2], str(i))


def choose_year(year_req):  # Turns the year into the correct format to be searched for in a tag
	return base_year.format(year_req)


def convert_year(chosen_year):  # Converts into a format that can then be converted into a soup(HTML format)
	chosen_year = str(chosen_year)
	chosen_year = chosen_year.replace('[', '')
	chosen_year = chosen_year.replace(']', '')
	return chosen_year


def choose_stat():  # Asks user which stat they would like to see
	for key in tag_names.keys():
		print(key)
	stat_choice = input("Which stat would you like to see (copy and paste): ")
	stat_name = str(stat_choice)
	return [tag_names[stat_choice], stat_name]


name = input('Choose a player: ')

url = ask_player(name)
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Makes sure it has right person  e.g. Kemba != Kenny
while soup.select("span")[8].getText().lower() != name.lower():  # [8] is the span tag with the name of the player
	url = ask_player(name)
	res = requests.get(url)
	soup = bs4.BeautifulSoup(res.text, 'lxml')

	i += 1


year_info = input("What year of his career would you like to see: ")
year_info = soup.select(choose_year(year_info))  # gets all the info from that year
year_info = convert_year(year_info)

soup1 = bs4.BeautifulSoup(year_info, 'lxml')  #

stat = choose_stat()
result = soup1.findAll("td", {"data-stat": stat[0]})  # Find HTML tag with that stat as a tag
print(stat[1] + ': ' + result[0].getText())
