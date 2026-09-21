import sqlite3


def salvar_faturamento_uber(inicio, fim, valor):
    conexao = sqlite3.connect("financeiro.db")

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faturamento_uber (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_inicio TEXT NOT NULL,
            data_fim TEXT NOT NULL,
            valor REAL NOT NULL
        )
    """)

    conexao.commit()
    print("Tabela faturamento_uber criada")

    cursor.execute("""
        INSERT INTO faturamento_uber(data_inicio, data_fim, valor)
        VALUES(?, ?, ?)""", (inicio, fim, valor))


    conexao.commit()
    print("Valores inseridos")
    cursor.execute(""" SELECT * FROM faturamento_uber""")
    #registros = cursor.fetchall()

    conexao.commit()
    print("Valores inseridos")

    conexao.close()

if __name__ == "__main__": #testes
    pass