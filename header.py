# este é o cabeçalho do aplicativo de desktop
from flet import *
from controls import add_to_control_reference, return_control_reference

# estas são as funções que acabamos de criar no script control.py

# podemos definir o dict retornado como variável no topo da classe.

Control_map= return_control_reference()


# classe principal
class AppHeader(UserControl):
    def __init__(self):
        super().__init__()
        
        
    def app_header_instance(self):
        #esta função define a instância da classe como par de valores-chave no ditado global
        add_to_control_reference('AppHeader', self)
        #então a chave => "AppHeader"
        #e o valor=> self (que é a instância, por exemplo, a localização do objeto na memória)
        
    def app_header_brand(self):
        return Container(
            content=Text(
                "Cadastro de Produtos",
                size=15
            )
        )    
        
    def app_header_search(self):
        return Container(
            width=320,
            bgcolor="white10",
            border_radius=6,
            opacity=0,
            animate_opacity=320,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment= CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=17, opacity=0.85),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=1,
                        color="white",
                        hint_text="Search",
                    ),
                ],
            ),
        )
        
    def app_header_avatar(self):
        return Container(content= IconButton(icons.PERSON))    
    
    # queremos mostrar a barra de pesquisa sempre que o usuário passar o mouse sobre o cabeçalho
    def show_search_bar(self, e):
        if e.data=='true':
            self.controls[0].content.controls[1].opacity=1
            self.controls[0].content.controls[1].update()
        else:
            # queremos remover o texto quando a barra de pesquisa desaparecer
            self.controls[0].content.controls[1].content.controls[1].value=""
            self.controls[0].content.controls[1].opacity = 0
            self.controls[0].content.controls[1].update()
    
        
    def build(self):
        self.app_header_instance()
        
        return Container(
            expand=True,
            on_hover= lambda e: self.show_search_bar(e),
            height=60,
            bgcolor="#081d33",
            border_radius= border_radius.only(top_left=15, top_right=15),
            padding=padding.only(left=15,right=15),
            content=Row(
                expand=True, 
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.app_header_brand(),
                    self.app_header_search(),
                    self.app_header_avatar(),
                    ],
            ),
        )