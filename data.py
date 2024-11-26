import serial
from dbconnection import conectar_db, inserir_dados, fechar_conexao

comport = serial.Serial('COM5', 9600)
print('Serial Iniciada...\n')

conexao, cursor = conectar_db()

try:
    while True:
        serialValue = str(comport.readline())
        characters = "b'r\\n"

        for char in characters:
            serialValue = serialValue.replace(char, "")

        data_sinais = serialValue.split("|")
        print(data_sinais)

        
        sinal_luz = int(data_sinais[0].strip())
        brilho_led = int(data_sinais[1].strip())
        sinal_som = int(data_sinais[2].strip())
        intensidade_som = int(data_sinais[3].strip())


        inserir_dados(cursor, conexao, sinal_som, intensidade_som, sinal_luz, brilho_led)
        print("Dados inseridos com sucesso no banco de dados")

except KeyboardInterrupt:
    print("\nEncerrando leitura serial e conexão com o banco.")

finally:
    
    fechar_conexao(conexao, cursor)
    comport.close()
    print("Conexão com o banco e a serial fechadas.")
    
