import requests

result = requests.post('http://127.0.0.1:8000/account/api-token-auth/', data = {'username':'Batman',
                                                                                'password': 'Aren2020'})

print(result.json().get('token'))