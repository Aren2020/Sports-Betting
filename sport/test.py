import requests
from pprint import pprint

# get token...
user_data = {
    'username': 'Aren',
    'password': 'Aren2020',
}
token_request = requests.post('http://localhost:8000/account/login/', json = user_data)
token_json = token_request.json()
token = token_json['token']
print(token + '\n' + ('-'*40))

# get news...
news_headers = {
    'Authorization': f'Token {token}',
}
news_request = requests.get('http://localhost:8000/sport/news/football/', headers = news_headers)
news_json = news_request.json()
pprint(news_json, indent = 2)
