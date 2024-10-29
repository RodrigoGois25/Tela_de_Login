"""
A função carregar_banco_de_dados realiza a leitura de todas as linhas do aquivo. Observe
que o modo de operação para manipulação do arquivo é o R, indicando que será realizada
manipulação de leitura. Para ler todas as linhas do arquivo, utilizamos a função
readlines() que retorna uma lista de string. Estamos iterando cada linha do arquivo,
e realizando o mapeamento com a função map_usuario(). No final do mapeamento, temos
uma lista de dicionário, em que cada elemento é um dicionário com as chaves nome e
telefone.
No escopo da função map_usuario(linha) estamos utilizando a função split para construir
uma lista de string a partir da linha. Estamos considerando como critério de split a 
vírgula. Assim, a string 'Renato,123' gera a lista ['Renato', '123']. Considerando os
valores da lista, montamos o dicionário com chave nome e telefone.
"""
def carregar_banco_de_dados():
    with open('banco_de_dados', mode='r') as bd:
        return [
            map_usuario(linha)
            for linha in bd.readlines() 
            if linha.strip()  
        ]


def map_usuario(linha):
    values = linha.split(',')
    if len(values) < 7:  
        raise ValueError(f"Linha inválida no banco de dados: {linha.strip()}")
    return {
        'nome': values[0].strip(),
        'email': values[1].strip(),
        'telefone': values[2].strip(),
        'uf': values[3].strip(),
        'sexo': values[4].strip(),
        'login': values[5].strip(),
        'senha': values[6].strip(),
    }


"""
A função salvar está manipulando o arquivo com o modo de operação A, indicando que iremos
acrescentar conteúdo ao arquivo já existente. Estamos escrevendo uma nova linha no
arquivo, utilizando a função write. Esta função recebe como argumento uma string.
Observe que a string passada como argumento termina com \n. Isso né necessário para poder
quebrar a linha. No retorno da função salvar, estamos chamando a função 
carregar_banco_de_dados() que retorna a lista de dicionários.

"""
def salvar(usuario):
    with open('banco_de_dados', mode='a') as bd:
        bd.write(f"{usuario['nome']},{usuario['email']},{usuario['telefone']},{usuario['uf']},{usuario['sexo']},{usuario['login']},{usuario['senha']}\n")
    return carregar_banco_de_dados()


"""
A função atualizar_banco_de_dados está manipulando o arquivo com o modo de operação W,
indicando que o conteúdo do arquivo será zerado e reescrito. Estamos iterando a lista
de dicionário e utiizando a função write para escrever as linhas do arquivo.
"""
def atualizar_banco_de_dados(lista):
    with open('banco_de_dados', mode='w') as bd:
        for usuario in lista:
            bd.write(f"{usuario['nome']},{usuario['telefone']}\n")    

