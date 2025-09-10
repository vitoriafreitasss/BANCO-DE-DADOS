import sqlite3

    try:
        con = sqlite3.connect("segundo_banco.db")
        cur = con.cursor()

        cur.execute("CREATE TABLE funcionario("+
                    "id INTEGER PRIMARY KEY ASC AUTOINCREMENT, "+
                    "nome VARCHAR(400))")
        cur.execute("CREATE TABLE setor("+
                    "id INTEGER PRIMARY KEY ASC AUTOINCREMENT),"+
                    "nome VARCHAR(100),"+
                    "id_funcionario INTEGER,"+
                    "FOREING KEY (id_funcionario) REFERENCES funcionario(id))")
        con.commit()
        
        cur.execute("INSERT INTO funcionario (nome) VALUES ('Ana')")
        cur.execute("INSERT INTO funcionario (nome) VALUES ('Bruno')")
        cur.execute("INSERT INTO funcionario (nome) VALUES ('Carla')")
        cur.execute("INSERT INTO setor (nome) VALUES ('Recepção', 1)")
        cur.execute("INSERT INTO setor (nome) VALUES ('Financeiro', 2)")
        cur.execute("INSERT INTO setor (nome) VALUES ('Depósito', 3)")

        cur.execute("SELECT * FROM funcionario, setor WHERE funcionario.id = %d" % 1)
        res= cur.fetchone()
        print(res)
        con.commit()
        cur.close()
        con.close()
    except ConnectionRefusedError as C:
        print('Erro de conexão:', c)