from lolinfos.clean import ChampionClean


def test_se_champions_com_letras_maiusculas_no_nome_sao_limpos():
    name = 'AlisTar'
    assert ChampionClean().name_clean(name) == 'alistar'


def test_se_champions_com_espaco_no_nome_sao_limpos():
    name = 'Master Yi'
    assert ChampionClean().name_clean(name) == 'masteryi'


def test_se_champions_com_apostrofo_no_nome_sao_limpos():
    name = "Rek'Sai"
    assert ChampionClean().name_clean(name) == 'reksai'


def test_se_nomes_com_espaco_antes_e_depois_do_nome_sao_limpos():
    name = '    Viego '
    assert ChampionClean().name_clean(name) == 'viego'


def test_se_champions_com_roles_invalidas_sao_limpos():
    role = 'Jangu'
    assert ChampionClean().role_clean(role) == ''


def test_se_as_roles_validas_nao_serao_limpas():
    roles = ['support', 'adc', 'mid', 'jungle', 'top']

    for role in roles:
        assert ChampionClean().role_clean(role) == role
