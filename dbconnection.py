import mysql.connector

def conectar_db():
    conexao = mysql.connector.connect(
        user='neurocomfort',
        password='Neurocomfort2024@',
        host='localhost',
        database='neurocomfort'
    )
    cursor = conexao.cursor()
    return conexao, cursor

def inserir_dados(cursor, conexao, sinal_som, intensidade_som, sinal_luz, brilho_led):
    add_sinais = """INSERT INTO sinais (sinal_som, intensidade_som, sinal_luz, brilho_led) 
                    VALUES (%s, %s, %s, %s)
                """
    data_insert = (sinal_som, intensidade_som, sinal_luz, brilho_led)
    cursor.execute(add_sinais, data_insert)
    conexao.commit()


def fechar_conexao(conexao, cursor):
    cursor.close()
    conexao.close()
