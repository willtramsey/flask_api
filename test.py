import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name":"ake rest API", "views":2816, "likes":1000}, {"name":"swimming lessons", "views":564346, "likes":10},
        {"name":"cat videos", "views":347734,"likes":175}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + 'video/6')
print(response.json())