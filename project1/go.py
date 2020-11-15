import requests

length = 0
with open('file.txt', 'r') as file:
    url = file.read().strip()
    length = len(requests.get(url).text.splitlines())

with open('new.txt', 'w') as new:
    new.write(str(length))