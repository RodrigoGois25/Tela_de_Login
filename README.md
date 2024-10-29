Este projeto é um sistema de cadastro de usuários implementado com Flet, que inclui funcionalidades de cadastro, atualização, remoção e listagem de usuários. Ele também possui um sistema de autenticação, onde os usuários precisam fazer login com credenciais válidas para acessar as funcionalidades principais.

### Funcionalidades

1. **Tela de Login**:
   - O sistema solicita que o usuário insira um login e uma senha.
   - Se as credenciais estiverem corretas, o usuário é redirecionado para a tela principal do sistema, onde pode visualizar a tabela de usuários cadastrados.
   - Em caso de credenciais incorretas, uma mensagem de erro é exibida.

2. **Tela de Cadastro**:
   - Permite a adição de novos usuários ao sistema, com campos de preenchimento para informações como nome, email, telefone, etc.
   - O sistema valida campos obrigatórios e impede a duplicação de emails.

3. **Tela de Tabela**:
   - Exibe todos os usuários cadastrados em uma tabela.
   - Inclui uma barra de pesquisa para filtrar usuários com base no nome ou telefone.
   - Permite editar ou deletar usuários através de botões de ação na tabela.

4. **Funcionalidade de Log de Tentativas de Login**:
   - Cada tentativa de login é registrada em um arquivo chamado `log.txt`, contendo:
     - Data e hora da tentativa.
     - Login e senha inseridos.
     - Resultado da tentativa (sucesso ou falha).
   - Esse log permite que todas as tentativas de login sejam monitoradas, proporcionando uma visão de quem tentou acessar o sistema e com qual resultado.

### Estrutura de Arquivos

- **`tela_login.py`**: Define a interface de login e realiza a verificação das credenciais.
- **`tela_cadastro.py`**: Gerencia o cadastro de novos usuários com validação de dados.
- **`tela_tabela.py`**: Exibe a lista de usuários cadastrados e permite ações de edição e exclusão.
- **`controle.py`**: Contém funções de controle para navegação e manipulação dos dados dos usuários, além de registrar tentativas de login.
- **`log.txt`**: Arquivo onde cada tentativa de login é registrada, com informações detalhadas sobre a tentativa.

### Exemplo de Registro no Arquivo de Log

Cada tentativa de login gera uma linha no arquivo `log.txt` no seguinte formato:

```
14:23:45 - Login: usuario123, Senha: senha123, Resultado: Sucesso
14:24:02 - Login: usuario321, Senha: senha321, Resultado: Falha
```

Este sistema é útil para aplicações que exigem controle de acesso e monitoramento de tentativas de login, e pode ser expandido com novos recursos conforme necessário.
