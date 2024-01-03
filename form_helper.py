# esta classe irá gerar uma nova instância de campo de texto e inseri-la na 
# tabela de dados
from flet import *

class FormHelper(UserControl):
    def __init__(self, user_input):
        self.user_input= user_input
        super().__init__()
        
    
    def build(self):
        return TextField(
            # passamos os valores dos campos do formulário para aqui na configuração básica da Ui
            value=self.user_input,
            border_color="transparent",
            height=20,
            text_size=13,
            content_padding=0,
            cursor_color="black",
            cursor_width=1,
            color="black",
            # mudanças importantes
            # Precisamos torná-lo verdadeiro para que o usuário não possa alterá-lo on_blur lambda e: self.save_value(e) para mais tarde
            read_only=True,
            # on_blur=lambda e: self.save_value(e)
        )