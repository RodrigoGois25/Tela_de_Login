import flet as ft
import controle as con
import uuid

componentes = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](),               
       }

def view():     
    return ft.View(
                "tela3",
                [      
                    ft.Container(content=ft.Text("Editar", size=20)),
                    ft.TextField(label='Nome', ref=componentes['tf_nome'], autofocus=True),
                    ft.TextField(label='Telefone', ref=componentes['tf_telefone'], on_submit=atualizar),
                    ft.Row(
                        [
                            ft.ElevatedButton('Atualizar', icon='save', on_click=atualizar),
                        ],
                        alignment=ft.MainAxisAlignment.END                   
                    ),                                                                                 
                ],
                navigation_bar=con.barra_navegacao(), 
                appbar= ft.AppBar(            
                    title=ft.Text("Sistema de cadastro"),
                    center_title=False,
                    bgcolor=ft.colors.SURFACE_VARIANT,                    
                ),                   
            )


def init(u):
    global usuario
    usuario = u
    componentes['tf_nome'].current.value = usuario['nome']
    componentes['tf_telefone'].current.value = usuario['telefone']


"""
A função atualizar foi modificada para utilizar a função salvar do arquivo controle
"""
def atualizar(e):
    nome = componentes["tf_nome"].current.value
    telefone = componentes["tf_telefone"].current.value    
    idx = con.banco_de_dados.index(usuario)
    con.atualizar({'nome':nome, 'telefone':telefone}, idx)
    con.tela_tabela.componentes["tabela"].current.rows = con.tela_tabela.atualizar_tabela()
    con.page.go('2')