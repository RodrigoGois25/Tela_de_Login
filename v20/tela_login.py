import flet as ft
import controle as con

componentes = {
    'tf_login': ft.Ref[ft.TextField](),
    'tf_senha': ft.Ref[ft.TextField](),
}

def view_login():
    return ft.View(
        "tela_login",
        [
            ft.Container(content=ft.Text("Login", size=20)),
            ft.TextField(label='Login', ref=componentes['tf_login'], autofocus=True),
            ft.TextField(label='Senha', ref=componentes['tf_senha'], password=True),
            ft.Row(
                [
                    ft.ElevatedButton('Entrar', icon='login', on_click=realizar_login),
                ],
                alignment=ft.MainAxisAlignment.END
            ),
        ],
        appbar=ft.AppBar(
            title=ft.Text("Sistema de Cadastro"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
        ),
    )

def realizar_login(e):
    login = componentes['tf_login'].current.value
    senha = componentes['tf_senha'].current.value
    
    usuario_encontrado = next((u for u in con.banco_de_dados if u['login'] == login and u['senha'] == senha), None)

    if usuario_encontrado:
        con.registrar_log(login, senha, True) 
        con.page.go("3")  
    else:
        con.registrar_log(login, senha, False)  
        ft.toast("Login ou senha inválidos.")  


def exibir_mensagem(mensagem):
    con.page.snack_bar = ft.SnackBar(
        content=ft.Text(mensagem),
        action="Fechar",
        open=True
    )
    con.page.update()
