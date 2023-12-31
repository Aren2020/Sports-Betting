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

# create bet...
# bet_headers = {
#     'Authorization': f'Token {token}',
# }
# bet_json = {
#     'game_id': 2,
#     'user_choice': 'w',
#     'amount': 50000,
# }

# bet_request = requests.post('http://localhost:8000/bets/create/', 
#                             headers = bet_headers, 
#                             data = bet_json)
# bet_request_json = bet_request.json()
# pprint(bet_request_json, indent = 2)

# bet list
bet_headers = {
    'Authorization': f'Token {token}',
}
bet_request = requests.get('http://localhost:8000/bets/', 
                            headers = bet_headers)
bet_request_json = bet_request.json()
pprint(bet_request_json, indent = 2)

# # bet winner
# bet_headers = {
#     'Authorization': f'Token {token}',
# }
# bet_request = requests.get('http://localhost:8000/bets/winner/', 
#                             headers = bet_headers)
# bet_request_json = bet_request.json()
# pprint(bet_request_json, indent = 2)