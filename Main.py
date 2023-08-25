import requests 
# input
query = input('')
#url for requests
url = 'https://en.wikipedia.org/w/api.php'

#Hashmap
params = {
        'action': 'query',
        'format': 'json',
        'titles': query,
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
    }
# get
response = requests.get(url, params=params)
# http response
# print(response)
# converts to string
data = response.json()
# print(data) 
# 
# print(data['query']['pages'].values())
page = next(iter(data['query']['pages'].values()))

# print(page)
#
print(page['extract'][:10000])

