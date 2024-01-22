import requests

api_key = '067c53a6-f122-4fcb-abef-6413eb5a5325'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

print(definitions)

for definition in definitions:
    print(definition)
    mongodb+srv://lucyarayikirana:lucya@cluster0.owq7clu.mongodb.net/?retryWrites=true&w=majority