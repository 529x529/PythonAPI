import requests


payload = {"name": "Misha"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)




