import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

print(response.history)
print(response.url)
