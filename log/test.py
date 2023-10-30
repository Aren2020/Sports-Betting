import requests

result = requests.post('http://127.0.0.1:8000/account/login/', data = {'username':'Batman',
                                                                                'password': 'Aren2020'})

print(result.json().get('token'))