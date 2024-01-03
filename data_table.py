# classe principal para interface da tabela de dados
from flet import * 
from controls import add_to_control_reference

class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()
        
        
# precisa enviar as instâncias da tabela de dados para o dict
    def app_data_table_instances(self):
        add_to_control_reference("AppDataTable", self)
    
    def build(self):
        self.app_data_table_instances()
        return Row(
        #para fazer o controle da tabela de dados rolar, precisamos configurá-lo de uma forma especial, 
        #pois o controle não possui parâmetro para rolagem 
        
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1,"#ebebeb"),
                    # os argumentos das colunas definirão o número de colunas a serem exibidas
                    columns=[
                        DataColumn(
                            Text("Identificador", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Produto", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Quantidade", size=12,color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Valor", size=12,color="black", weight="bold")
                        ),
                    ],
                    # aqui, configuraremos o botão do formulário para anexar as linhas de dados
                    rows=[],
                )
            ],
        )
