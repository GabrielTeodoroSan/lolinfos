import requests
from bs4 import BeautifulSoup

from lolinfos.clean import ChampionClean
from lolinfos.settings import Settings


class Champion:
    def __init__(self, name, role):
        self.name = ChampionClean().name_clean(name)
        self.role = ChampionClean().role_clean(role)


class ChampionData:
    def __init__(self, champion: Champion, data: list):
        self.name = champion.name
        self.role = champion.role
        self.wr = data[0]
        self.pr = data[1]
        self.br = data[2]


class Html:
    def __init__(self, champion: Champion):
        self.url = f'https://www.op.gg/champions/{champion.name}/build/{champion.role}'
        self.champion = champion
        self.html = self.collect()
        self.bs = BeautifulSoup(self.html, 'html.parser')

    def search(self) -> dict:
        return self.bs.find_all('div', {'class': 'css-oxevym'})

    def clear_data(self, data) -> ChampionData:
        data = [value.text for value in data]
        return ChampionData(self.champion, data)

    def collect(self):
        response = requests.get(
            url=Settings().PROXY_SERVICE_URL,
            params={'api_key': Settings().ACCESS_KEY, 'url': self.url},
        )
        return response.content
