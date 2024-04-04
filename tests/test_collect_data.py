from bs4 import BeautifulSoup

from lolinfos.collect import Champion, Html


def test_se_e_possivel_criar_um_campeao_com_a_classe_champion(champion):
    assert type(champion) == Champion


def test_se_e_possivel_criar_um_campeao_com_letra_maiuscula(champion):
    assert champion.name == champion.name.lower()


def test_se_e_possivel_adicionar_champions_com_espaco_no_nome():
    champion = Champion('Master Yi', 'jungle')
    assert champion.name == 'masteryi'


def test_se_e_possivel_adicionar_champions_com_apostofro():
    champion = Champion("Rek'Sai", role='jungle')
    assert champion.name == 'reksai'


def test_se_e_possivel_criar_champion_com_muitos_espacos_antes_do_nome():
    champion = Champion('    Viego  ', 'jungle')
    assert champion.name == 'viego'


def test_se_nao_e_possivel_criar_champion_em_rota_inesistente():
    champion = Champion('Malphite', 'Casa da sua mãe')
    assert champion.role == ''


def test_se_a_classe_html_esta_gerando_objetos_de_forma_correta(champion):
    html = Html(champion)
    assert (
        html.url
        == f'https://www.op.gg/champions/{champion.name}/build/{champion.role}'
    )
    assert champion == html.champion
    assert type(html.bs) == BeautifulSoup


def test_se_os_dados_buscados_nas_paginas_estao_sendo_encontrados():
    champion = Champion("Rek'Sai", 'jungle')
    html = Html(champion)
    response = html.search()
    assert len(response) == 3


def test_se_os_dados_buscados_estão_sendo_limpos_pelo_metodo_clear():
    champion = Champion('Master Yi', 'jungle')
    html = Html(champion)
    response = html.search()
    response = html.clear_data(response)
    assert response.wr[-1] == '%'
    assert type(int(response.wr[0])) == int


def test_se_campeos_sem_role_sao_pesquisados_normalmente():
    champion = Champion('Alistar', 'supizin')
    html = Html(champion)
    response = html.search()
    assert len(response) == 3
