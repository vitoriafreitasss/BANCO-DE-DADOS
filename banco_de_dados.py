import sqlite3

con = sqlite3.connect("meu_banco.db")

try:
    con = sqlite3.connect("meu_banco.db")

    cur = con.cursor()

    #cur.execute("CREATE TABLE pessoa(id, nome, idade, CPF)")
    #cur.execute("INSERT INTO pessoa VALUES(1, 'vitoria', 17, 'XXX.XXX.XXX-XX')")
    res = cur.execute("SELECT * FROM pessoa")
    pessoas = res.fetchone()

    #cur.execute("DELETE FROM pessoa WHERE id = 1")  DELETAR PESSOA DA LISTA
    #con.commit()
    #cur.close()

    print(pessoas)

    cur.close()

    con.commit()

except ConnectionRefusedError as c:
    print("Erro de conexão com o banco.")
