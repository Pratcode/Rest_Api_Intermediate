import requests

name = 'UEFA Champions League'
year = 2011

url = 'https://jsonmock.hackerrank.com/api/football_competitions?name='+str(name)+'&year='+str(year)
response = requests.get(url).json()
res = response['data']
for r in res:
    team = r['winner']


match_count = 0

url1 = 'https://jsonmock.hackerrank.com/api/football_matches?competition='+str(name)+'&year='+str(year)+'&team1='+str(team)
response = requests.get(url1).json()
res = response['data']
for r in res:
    match_count += int(r['team1goals'])

url2 = 'https://jsonmock.hackerrank.com/api/football_matches?competition='+str(name)+'&year='+str(year)+'&team2='+str(team)
response = requests.get(url2).json()
res = response['data']
for r in res:
    match_count += int(r['team2goals'])

print(match_count)