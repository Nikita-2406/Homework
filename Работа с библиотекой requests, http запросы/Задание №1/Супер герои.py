import requests
url = "https://akabab.github.io/superhero-api/api/all.json"
dict_hero = {}
data = requests.get(url).json()
target_hero = ['Hulk', 'Captain America', 'Thanos']
for hero in data:
    if hero['name'] in target_hero:
        dict_hero[hero['name']] = hero['powerstats']['intelligence']
print(max(dict_hero, key=dict_hero.get))