import requests


NO_OF_QUESTIONS = 10


parameters = {
    'amount': NO_OF_QUESTIONS,
    'type': 'boolean',
    'category': 9
}

response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
question_data = response.json()['results']
print(response.json())