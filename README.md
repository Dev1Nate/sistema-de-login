# Sistema de Login em Python

Este projeto é um **sistema simples de gerenciamento de usuários** utilizando Python, SQLAlchemy e MySQL. Ele permite cadastrar, logar e deletar usuários, com verificação de senha e email.

---

## Funcionalidades

- **Cadastro de usuários** com verificação de email único.
- **Login** com autenticação de senha criptografada.
- **Exclusão de conta** mediante confirmação de email e senha.
- **Validação de senha** (mínimo 8 caracteres e máximo 14).

---

## Como usar

1. Configure seu banco MySQL e atualize os parâmetros de conexão no arquivo Python:

```python
USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "exercicio_login"
PORT = 3306
```

2. Execute o script principal com Python 3:

```bash
python main.py
```

3. Escolha uma opção no menu:

```
[1] Cadastrar novo usuário
[2] Logar na sua conta
[3] Excluir sua conta
```

4. Siga as instruções no terminal:

- Cadastro: insira nome, email e senha.
- Login: insira email e senha.
- Exclusão: insira email e senha.

---

## Mensagens de retorno

- **1:** Email já cadastrado.
- **2:** Senha muito curta ou muito longa (8 a 14 caracteres).
- **3:** Dados de senha incorretos.
- **4:** Login realizado com sucesso.
- **5:** Informações de login incorretas.
- **6:** Usuário excluído com sucesso.

---

## Estrutura do banco de dados

Tabela `Usuario`:

| Campo | Tipo     | Observação          |
|-------|---------|-------------------|
| id    | INTEGER | Primary Key        |
| nome  | STRING  | Nome do usuário    |
| email | STRING  | Email único        |
| senha | STRING  | Senha criptografada|

---

## Requisitos

- Python 3.x  
- SQLAlchemy  
- PyMySQL  
- MySQL

---

## Licença

Este projeto está licenciado sob a MIT License.
