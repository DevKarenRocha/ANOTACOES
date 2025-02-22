import pandas as pd

dados = {'Nome': ['Ana', 'Bruno', 'Carlos'],
         'Idade': [25, 30, 22],
         'Cidade': ['SP', 'RJ', 'MG']}
df = pd.DataFrame(dados)

serie = pd.Series([10, 20, 30, 40]) 

df = pd.read_csv('arquivo.csv')   # Lendo um CSV
df = pd.read_excel('arquivo.xlsx') # Lendo um Excel
df = pd.read_json('arquivo.json')  # Lendo um JSON

df.to_csv('arquivo.csv', index=False)    # Salvando como CSV
df.to_excel('arquivo.xlsx', index=False) # Salvando como Excel
df.to_json('arquivo.json')               # Salvando como JSON

df.head()     # Exibe as 5 primeiras linhas
df.head(10)   # Exibe as 10 primeiras linhas
df.tail()     # Exibe as 5 últimas linhas
df.info()     # Exibe informações sobre o DataFrame
df.describe() # Estatísticas descritivas das colunas numéricas
df.shape      # Retorna o número de linhas e colunas (linhas, colunas)
df.columns    # Lista os nomes das colunas
df.dtypes     # Mostra os tipos de dados das colunas


df['Nome']         # Seleciona uma única coluna
df[['Nome', 'Idade']] # Seleciona múltiplas colunas
df.iloc[0]         # Seleciona a primeira linha
df.iloc[1:3]       # Seleciona um intervalo de linhas
df.loc[df['Idade'] > 25] # Filtra dados

df['Salário'] = [3000, 4000, 2500]
df.loc[df['Nome'] == 'Ana', 'Idade'] = 26

df.drop('Cidade', axis=1, inplace=True) # Remove a coluna "Cidade"
df.drop(1, axis=0, inplace=True)        # Remove a linha de índice 1

df.isnull().sum()     # Conta valores nulos por coluna
df.dropna(inplace=True) # Remove linhas com valores nulos
df.fillna(0, inplace=True) # Substitui valores nulos por 0

df.groupby('Cidade').mean()  # Média dos valores numéricos agrupados por Cidade
df['Idade'].mean()   # Média da idade
df['Idade'].sum()    # Soma da idade
df['Idade'].max()    # Valor máximo da idade
df['Idade'].min()    # Valor mínimo da idade
df['Idade'].count()  # Contagem de valores na coluna Idade

df.sort_values('Idade')         # Ordena por idade (ascendente)
df.sort_values('Idade', ascending=False) # Ordena por idade (descendente)

df['Data'] = pd.to_datetime(df['Data']) # Converte para datetime
df['Ano'] = df['Data'].dt.year  # Extrai o ano
df['Mês'] = df['Data'].dt.month # Extrai o mês
df['Dia'] = df['Data'].dt.day   # Extrai o dia
