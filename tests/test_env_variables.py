import pytest

from lolinfos.settings import Settings


@pytest.mark.env
def test_se_a_variavel_de_ambiente_access_key_esta_disponivel():
    access_key = Settings().ACCESS_KEY
    assert type(access_key) == str
    assert len(access_key) > 0
