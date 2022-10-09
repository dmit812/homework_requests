import requests

from bs4 import BeautifulSoup


class Superhero:

    def get_superhero(self, hero_list):
        url = "https://akabab.github.io/superhero-api/api/all.json"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        hero = []
        intelligence = []
        for words in soup:
            for word in words:
                lists = str(word).split('\n')
                for data in lists:
                    if '"name":' in data:
                        lists = data[13:].replace('",', '')
                        hero.append(lists)
                    if '"intelligence":' in data:
                        lists2 = data[22:].replace(',', '')
                        intelligence.append(int(lists2))
        heroes = hero_list
        heroes_intelligence = []
        count = 0
        while count < len(heroes):
            heroes_intelligence.append(intelligence[hero.index(heroes[count])])
            count += 1
        print(f'Самый умный герой из списка: {heroes[heroes_intelligence.index(max(heroes_intelligence))]}')
