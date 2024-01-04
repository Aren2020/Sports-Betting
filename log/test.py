import requests
from pprint import pprint

result = requests.post('http://127.0.0.1:8000/account/login/', data = {'username':'Aren',
                                                                       'password': 'Aren2020'})
token = result.json()['token']
print(result.json())

# add balance
# balance_headers = {
#     'Authorization': f'Token {token}',
# }
# balance_request = requests.post('http://localhost:8000/account/add/balance/', 
#                             headers = balance_headers,
#                             data = {'amount': 50000})
# balance_request_json = balance_request.json()
# pprint(balance_request_json, indent = 2)