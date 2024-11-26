import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Função para carregar os dados a partir de um arquivo CSV
def get_data_from_csv(file_path):
    try:
        df = pd.read_csv(file_path, sep=';', usecols=['intensidade_som', 'sinal_luz', 'risco_ambiente'])
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo CSV: {e}")
        return None



# Função para normalizar os dados dinamicamente com base no DataFrame
def normalize_data(df):

    max_som = df['intensidade_som'].max()
    min_som = df['intensidade_som'].min()

    max_luz = df['sinal_luz'].max()
    min_luz = df['sinal_luz'].min()

    # Normalizar intensidade_som e sinal_luz entre 0 e 10
    df['intensidade_som'] = (df['intensidade_som'] - min_som) / (max_som - min_som) * 10
    df['sinal_luz'] = (df['sinal_luz'] - min_luz) / (max_luz - min_luz) * 10

    return df

# Função para treinar o modelo de regressão linear
def train_model(df):

    X = df[['sinal_luz', 'intensidade_som']]
    y = df['risco_ambiente']  # prevista

    # Divida os dados em conjunto de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crie o modelo de regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Faça previsões no conjunto de teste
    y_pred = model.predict(X_test)

    # Avaliar o modelo
    mse = mean_squared_error(y_test, y_pred)
    print(f"Erro Quadrático Médio (MSE): {mse}")
    return model

# Função para fazer previsões com o modelo treinado
def predict(model, new_data):
    return model.predict(new_data)

def main():
    file_path = "informacao.csv"

    # Obter os dados do arquivo CSV
    df = get_data_from_csv(file_path)
    if df is None:
        return
    
    # Normalizar os dados
    df = normalize_data(df)

    print("Dados coletados (após normalização):")
    print(df.head())

    # Treinar o modelo de regressão
    model = train_model(df)

    
    new_data = pd.DataFrame([[6, 5], [8, 3]], columns=['sinal_luz', 'intensidade_som'])  # Novos dados já normalizados e previstos
    predicted_values = predict(model, new_data)

    print("Previsões para novos dados (risco):")
    print(predicted_values)

if __name__ == "__main__":
    main()