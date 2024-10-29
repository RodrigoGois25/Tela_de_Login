import flet as ft
import controle as con

componentes = {        
    'tabela': ft.Ref[ft.DataTable](),   
    'tf_pesquisa': ft.Ref[ft.TextField]()    
}

def view():     
    return ft.View(
        "tela2",
        [             
            ft.TextField(ref=componentes['tf_pesquisa'], label='Pesquisar', icon='search', on_change=pesquisar),              
            ft.DataTable(
                width=float('inf'),
                ref=componentes['tabela'],                                                    
                columns=[
                    ft.DataColumn(ft.Text("Nome")),
                    ft.DataColumn(ft.Text("E-mail")),  
                    ft.DataColumn(ft.Text("Telefone")),      
                    ft.DataColumn(ft.Text("Ações")),                                                       
                ],
                rows=[],  
                ),                                                                         
        ],
        navigation_bar=con.barra_navegacao(), 
        appbar=ft.AppBar(            
            title=ft.Text("Sistema de Cadastro"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,                    
        ),                   
    )

def atualizar_tabela():
    if componentes['tabela'].current:
        componentes['tabela'].current.rows.clear()
    
    usuarios = con.carregar_usuarios() 
    for usuario in usuarios:
        if componentes['tabela'].current:  
            componentes['tabela'].current.rows.append(
                ft.DataRow(cells=preencher_linha_tabela(usuario))
            )

    con.page.update()  
    return componentes['tabela'].current.rows  
def preencher_linha_tabela(cadastro):
    return [
        ft.DataCell(ft.Text(cadastro['nome'])),
        ft.DataCell(ft.Text(cadastro['email'])), 
        ft.DataCell(ft.Text(cadastro['telefone'])),
        ft.DataCell(ft.Row(
            [
                ft.IconButton(icon=ft.icons.EDIT, on_click=atualizar, key=cadastro['login']), 
                ft.IconButton(icon=ft.icons.REMOVE_CIRCLE, on_click=deletar, key=cadastro['login']),  
            ]
        )),
    ]

def filtrar_dados(query):
    return [
        ft.DataRow(cells=preencher_linha_tabela(cadastro))
        for cadastro in con.banco_de_dados
        if query.lower() in cadastro['nome'].lower() or query in cadastro['telefone']
    ]

def pesquisar(e):
    query = componentes['tf_pesquisa'].current.value
    if componentes['tabela'].current:  
        componentes['tabela'].current.rows = filtrar_dados(query)
        con.page.update()

def deletar(e):
    usuario = e.control.key  
    con.remover(usuario)
    if componentes['tabela'].current:  
        componentes['tabela'].current.rows = atualizar_tabela()  
        con.page.update()

def atualizar(e):
    usuario = e.control.key  
    con.tela_atualizar.init(usuario)
    con.page.go('3')

def init_tela():
    atualizar_tabela()  