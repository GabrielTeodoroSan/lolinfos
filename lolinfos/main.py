import os
import sys

import typer
from rich import print
from rich.panel import Panel
from rich.table import Table

sys.path.insert(0, os.getcwd())

from lolinfos.collect import Champion, Html

app = typer.Typer(no_args_is_help=True)


@app.command()
def collectcmp(
    name: str = typer.Argument(help='Nome do campeão.'),
    role: str = typer.Argument(help='A posição do campeão.'),
    list: bool = typer.Option(
        False, is_flag=True, help='Irá mostrar os dados em forma de lista.'
    ),
    table: bool = typer.Option(
        False, is_flag=True, help='Irá mostrar os dados em forma de tabela.'
    ),
):
    """
    Este comando serve para mostrar informações de um campeão na tela.
    --list e --table são flags utilizados para customizar a visualização
    dos dados.
    """

    html = Html(Champion(name=name, role=role))
    champion = html.clear_data(html.search())

    if list:
        print(
            Panel(
                f"""
                    ✅ role     = {champion.role}
                    ✅ winrate  = {champion.wr}
                    ✅ pickrate = {champion.pr}
                    ✅ banrate  = {champion.br}
            """,
                border_style='green',
                title=f'INFORMAÇÕES SOBRES {(champion.name).upper()}',
                padding=(1, 2),
            )
        )

    if table:
        table = Table()

        table.add_column('Nome', style='dim')
        table.add_column('Role')
        table.add_column('Winrate')
        table.add_column('Pickrate')
        table.add_column('Banrate')

        table.add_row(
            champion.name, champion.role, champion.wr, champion.pr, champion.br
        )
        print(table)


@app.command()
def sayby(name: str = typer.Argument('Teodoro')):
    print(f'By, {name}')


if __name__ == '__main__':
    app()
