import requests

year = 2011

maximum_goals = 10
match_count = 0

for j in range(0, maximum_goals):
    url = 'https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team1goals='+str(j)+'&team2goals='+str(j)
    response = requests.get(url).json()
    match_count += response['total']
print(match_count)