# Importar a biblioteca sqlite3
import sqlite3

# Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

# Criar objeto do tipo cursor
cursor = conexao.cursor()

# Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

# Executar o comando SQL no SQLite, no cursor
cursor.execute(sql)

# Exibir a consulta com todos os nomes de heróis e vilões do BD
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")

