import tela_cadastro
import tela_tabela
import tela_atualizar
import tela_login  # Importa a nova tela de login
import flet as ft
import banco_de_dados as bd
import controle as con
import datetime

def init(p):
    global page, telas, banco_de_dados
    page = p
    banco_de_dados = bd.carregar_banco_de_dados()
    telas = {
        '1': tela_login.view_login(),  # Adiciona a tela de login como a primeira tela
        '2': tela_cadastro.view(),
        '3': tela_tabela.view(),
        '4': tela_atualizar.view()
    }

def controle_de_rota(route_event):
    page.views.clear()
    page.views.append(telas[route_event.route])
    if route_event.route == "3":  # Verifique se estamos indo para a tela da tabela
        tela_tabela.init_tela()  # Chama a inicialização da tela da tabela
    page.update()


def barra_navegacao():
    return ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.SAVE, label="Cadastrar"),  # Botão de Cadastrar
            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Listar"),  # Botão para Listar
        ],
        on_change=navegacao
    )  # NavigationBar


def navegacao(e):
    if e.control.selected_index == 0:  # 0 para "Cadastrar"
        page.go('2')  # Supondo que a tela de cadastro seja '2'
    elif e.control.selected_index == 1:  # 1 para "Listar"
        tela_tabela.componentes["tabela"].current.rows = tela_tabela.atualizar_tabela()
        page.go('3')  # Supondo que a tela de tabela seja '3'



def salvar(usuario):        
    con.banco_de_dados = bd.salvar(usuario)

def remover(usuario):
    con.banco_de_dados.remove(usuario)
    bd.atualizar_banco_de_dados(con.banco_de_dados)

def atualizar(usuario, idx):
    con.banco_de_dados[idx] = usuario
    bd.atualizar_banco_de_dados(con.banco_de_dados)

def carregar_usuarios():
    usuarios = []
    try:
        with open("banco_de_dados", "r") as file:
            for linha in file:
                campos = linha.strip().split(",")  
                if len(campos) >= 7:  
                    usuario = {
                        'nome': campos[0],
                        'email': campos[1],
                        'telefone': campos[2],
                        'uf': campos[3],
                        'sexo': campos[4],
                        'login': campos[5],
                        'senha': campos[6]
                    }
                    usuarios.append(usuario)
    except FileNotFoundError:
        print("Arquivo de banco de dados não encontrado.")
    return usuarios

def registrar_log(login, senha, sucesso):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    resultado = "Sucesso" if sucesso else "Falha"
    
    with open("log.txt", "a") as log_file:
        log_file.write(f"{now} - Login: {login}, Senha: {senha}, Resultado: {resultado}\n")