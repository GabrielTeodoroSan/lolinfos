from lolinfos.main import app
import pytest


@pytest.mark.cli
def test_se_os_valore_estão_sendo_retornados_corretamente_quando_busco_um_campeao_com_a_opcao_list_ativa(clirunner):
    result = clirunner.invoke(app, ['collectcmp', 'gragas', 'jungle', '--list'])
    assert result.exit_code == 0


@pytest.mark.cli 
def test_se_os_valore_estão_sendo_retornados_corretamente_quando_busco_um_campeao_com_a_opcao_table_ativa(clirunner):
    result = clirunner.invoke(app, ['collectcmp', 'gragas', 'jungle', '--table'])
    assert result.exit_code == 0