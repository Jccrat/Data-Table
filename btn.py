# este é o arquivo principal onde lidamos com os dados de entrada do usuário
from flet import *
from controls import return_control_reference
from form_helper import FormHelper

# get the global map dict
control_map= return_control_reference()


'''este método tratará os principais dados do usuário.
mas antes de começarmos a coletar dados, precisamos de um local para armazená-los'''
#agora que a tabela de dados está definida, podemos começar a pegar os dados do campo do formulário e exibi-los
def get_input_data(e):
    # lembre-se que a instância do formulário está salva no dicionário, podemos acessá-la agora
    for key, value in control_map.items():
    #obtenha a chave chamada AppForm, pois é onde estão os valores
        if key=='AppForm':
            #assim que tivermos a chave, podemos agora percorrer os campos de texto e obter os valores
            # primeiro for loop é a primeira linha
            # uma vez que estamos na chave, precisamos criar um DataRow
            data = DataRow(cells=[])
            
            for user_input in value.controls[0].content.controls[0].controls[:]:    
            
                
                # aqui, agora podemos acrescentar esse DataRow
                data.cells.append(
                    # chame a classe FormHelp
                    DataCell(FormHelper(user_input.content.controls[1].value))
                )
            # primeiro for loop é a primeira linha
            for user_input in value.controls[0].content.controls[0].controls[:]:
        
                data.cells.append(
                    # chame a classe FormHelp
                    DataCell(FormHelper(user_input.content.controls[1].value))
                )
            # agora que temos acesso aos valores, devemos criar uma linha de dados + célula para inseri-la na tabela de dados
            # precisamos atualizar os dados depois de anexar
            
        if key == "AppDataTable":
            value.controls[0].controls[0].rows.append(data)
            value.controls[0].controls[0].update()
            
            

# para a interface do botão, isso pode ser alterado para se adequar ao tema do aplicativo
def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click= lambda e: get_input_data(e),
            bgcolor="#081d33",
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12,
                    ),
                    Text(
                        "Salvar",
                        size=11,
                        weight="bold",
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=220,
        ),
    )