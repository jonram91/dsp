# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd

football = pd.read_csv('/Users/jonathanjramirez/GitHub/dsp/python/football.csv')

football.describe()

football.head()

football['net_goals'] = football['Goals'] - football['Goals Allowed']

football.head()

#Leicester has the lowest 'net goals' value meaning there were more against than for goals
# There were 64 goals allowed vs 30 goals scored

print(str(football[football['net_goals'] == football['net_goals'].min()]))

'''
>>          Team  Games  Wins  Losses  Draws  Goals  Goals Allowed  Points  \
19  Leicester     38     5      13     20     30             64      28   

    net_goals  
19        -34  
'''


#Aston_Villa has the smallest absolute difference between goals scored and allowed
#There were 46 goals scored vs 47 goals allowed

football.ix[abs(football['net_goals']) == 1]

'''

>>           Team  Games  Wins  Losses  Draws  Goals  Goals Allowed  Points  \
7  Aston_Villa     38    12      14     12     46             47      50   

   net_goals  
7         -1

'''