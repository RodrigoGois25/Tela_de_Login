"""
    V 20.0
    Nesta versão estamos persistindo os dados em um arquivo de texto. Para isso, foi criado
    o arquivo banco_de_dados.py. Esse arquivo possui 5 funções: carregar_banco_de_dados,
    map_usuario, atualizar_banco_de_dados, salvar.    
"""
import flet as ft
import controle as con

def main(page: ft.Page):   
    con.init(page)         
    page.title = "Sistema de cadastro"           
    page.on_route_change = con.controle_de_rota  
    page.theme_mode  = "light"
    page.go('1')


ft.app(target=main)

