#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

#open the csv file
"""
I know the traditional format should say 'football.csv', 
however, for some reason PyCharm recognized 'football' and not 'football.csv' in my project.
"""
f = open('football')
csv_f = csv.reader(f)

#create new lists and a dictionary to perform list and dictionary operations
goals_for = []
goals_against = []
teams = []
team_diff = {}

#append goals and goals allowed data to lists
for row in csv_f:
    goals_for.append(row[5])
    goals_against.append(row[6])
    teams.append(row[0])

#remove the column headings
del goals_for[0]
del goals_against[0]
del teams[0]

#turn strings into ints
goals_for = map(int, goals_for)
goals_against = map(int, goals_against)


#returns a list of the absolute value of score differences
def get_score_difference(list1, list2):
    score_diff = [x1 - x2 for (x1, x2) in zip(goals_for, goals_against)]
    abs_score_diff = map(abs, score_diff)
    return abs_score_diff


#combines the teams and their score differences into a dictionary
#sorts the dictionary and returns the key with the lowest value
def get_team(list1, list2):
    team_diff = dict(zip(teams, get_score_difference(goals_for, goals_against)))
    sort_team_diff = sorted(team_diff, key=team_diff.__getitem__)
    return sort_team_diff[0]

print get_team(teams, get_score_difference)

#will print 'Aston_Villa'
