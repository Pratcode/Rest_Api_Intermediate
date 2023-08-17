import requests
year = 2011
url = 'https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)
response = requests.get(url).json()

total = response['total_pages']

for i in range(1, total+1):
    url = 'https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&page='+str(i)
    response = requests.get(url).json()
    res = response['data']
    match_count = 0
    for r in res:
        if (r['team1goals'])==(r['team2goals']):
            match_count += 1
print(match_count)