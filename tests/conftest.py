from random import choice

from factory import Factory
from pytest import fixture
from typer.testing import CliRunner

from lolinfos.collect import Champion

normal_champions_name = [
    'Gragas',
    'Sejuani',
    'Wukong',
    'Diana',
    'Alistar',
    'Teemo',
    "Rek'Sai",
    'Aurelion Sol',
    'Master Yi',
    "Kai'Sa",
]


roles = ['support', 'adc', 'mid', 'jungle', 'top']


class NormalChampionFactory(Factory):
    class Meta:
        model = Champion

    name = choice(normal_champions_name)
    role = choice(roles)


@fixture()
def champion():
    return NormalChampionFactory()


@fixture()
def clirunner():
    runner = CliRunner()
    yield runner
