import requests

response1 = requests.get('https://playground.learnqa.ru/api/hello')
print(response1.text)

response2 = requests.get('https://playground.learnqa.ru/api/get_text')
print(response2.text)



