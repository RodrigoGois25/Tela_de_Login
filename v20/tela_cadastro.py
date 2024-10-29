import flet as ft
import controle as con
import re

componentes = {
    'tf_nome': ft.Ref[ft.TextField](),
    'tf_email': ft.Ref[ft.TextField](),
    'tf_telefone': ft.Ref[ft.TextField](),
    'tf_uf': ft.Ref[ft.TextField](),
    'tf_sexo': ft.Ref[ft.TextField](),
    'tf_login': ft.Ref[ft.TextField](),
    'tf_senha': ft.Ref[ft.TextField](),
}

def view():
    return ft.View(
        "tela1",
        [
            ft.Container(content=ft.Text("Cadastro", size=20)),
            ft.TextField(label='Nome', ref=componentes['tf_nome'], autofocus=True),
            ft.TextField(label='E-mail', ref=componentes['tf_email']),
            ft.TextField(label='Telefone', ref=componentes['tf_telefone']),
            ft.TextField(label='UF', ref=componentes['tf_uf']),
            ft.TextField(label='Sexo', ref=componentes['tf_sexo']),
            ft.TextField(label='Login', ref=componentes['tf_login']),
            ft.TextField(label='Senha', ref=componentes['tf_senha'], password=True),
            ft.Row(
                [
                    ft.ElevatedButton('Cadastrar', icon='save', on_click=cadastrar),
                ],
                alignment=ft.MainAxisAlignment.END
            ),
        ],
        navigation_bar=con.barra_navegacao(),
        appbar=ft.AppBar(
            title=ft.Text("Sistema de cadastro"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
        ),
    )

def exibir_mensagem(mensagem):
    con.page.snack_bar = ft.SnackBar(
        content=ft.Text(mensagem),
        action="Fechar",
        open=True 
    )
    con.page.update()
    
def verificar_email_unico(email):
    usuarios = con.carregar_usuarios() 
    for usuario in usuarios:
        if usuario['email'] == email:
            return False 
    return True  


def cadastrar(e):
    nome = componentes['tf_nome'].current.value
    email = componentes['tf_email'].current.value
    telefone = componentes['tf_telefone'].current.value
    uf = componentes['tf_uf'].current.value
    sexo = componentes['tf_sexo'].current.value
    login = componentes['tf_login'].current.value
    senha = componentes['tf_senha'].current.value
    
    if not verificar_email_unico(email):
        exibir_mensagem("O e-mail já está cadastrado.")
        return

    if not nome:
        exibir_mensagem("O campo 'Nome' é obrigatório.")
        return
    if len(nome) < 4 or len(nome) > 30:
        exibir_mensagem("O campo 'Nome' deve ter entre 4 e 30 caracteres.")
        return
    if not email:
        exibir_mensagem("O campo 'E-mail' é obrigatório.")
        return
    if not telefone:
        exibir_mensagem("O campo 'Telefone' é obrigatório.")
        return
    if not telefone.isdigit() or len(telefone) != 9:
        exibir_mensagem("O campo 'Telefone' deve conter exatamente 9 dígitos numéricos.")
        return
    if not uf:
        exibir_mensagem("O campo 'UF' é obrigatório.")
        return
    if not sexo:
        exibir_mensagem("O campo 'Sexo' é obrigatório.")
        return
    if not login:
        exibir_mensagem("O campo 'Login' é obrigatório.")
        return
    if not senha:
        exibir_mensagem("O campo 'Senha' é obrigatório.")
        return

    if not re.match("^[A-Za-z\s]+$", nome):
        exibir_mensagem("O campo 'Nome' só pode conter letras e espaços.")
        return
    
    if len(login) < 5:
        exibir_mensagem("O campo 'Login' deve ter pelo menos 5 caracteres.")
        return
    if len(senha) < 5:
        exibir_mensagem("O campo 'Senha' deve ter pelo menos 5 caracteres.")
        return

    usuario = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'uf': uf,
        'sexo': sexo,
        'login': login,
        'senha': senha,
    }

    con.salvar(usuario)

    for key in componentes:
        componentes[key].current.value = ""
    con.page.update()

    exibir_mensagem("Usuário cadastrado com sucesso!")
