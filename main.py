# criando a tela inicial
import flet
from flet import *
from header import AppHeader  # cabeçalho do aplicativo
from form import AppForm  # formulário de entrada de aplicativo
from data_table import AppDataTable  # formulário da banco de dados


def main(page: Page):
    page.bgcolor = '#fdfdfd'
    page.padding = 20
    page.add(
        # coluna principal onde cada componente do aplicativo será colocado e exibido
        Column(
            expand=True,
            controls=[
                # instâncias de classe acesse aqui
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppForm(),
                # chamamos a classe da tabela de dados dentro desta coluna
                Column(
                    scroll='hidden',
                    expand=True,
                    controls=[AppDataTable()],
                ),
            ],
        )

    )
    page.update()
    pass


if __name__ == '__main__':
    flet.app(target=main)
