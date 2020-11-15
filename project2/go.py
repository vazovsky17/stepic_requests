import requests

data = ''
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('file.txt', 'r') as file:
    url1 = file.read().strip()
    r = requests.get(url1)
    while True:
        url1 = url+r.text
        r = requests.get(url1)
        print(url1)
        if r.text.upper().startswith("WE"):
            data = r.text
            break

with open('new.txt', 'w') as new:
    new.write(data)
