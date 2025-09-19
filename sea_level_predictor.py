# Importando as bibliotecas necessárias
import pandas as pd # Ferramenta de manipulação e análise de dados
import matplotlib.pyplot as plt # Ferramenta de visualização de dados
from scipy.stats import linregress # Função para calcular regressão linear

def draw_plot(): # Função principal para gerar e salvar o gráfico de nível do mar

    # Carregando o arquivo CSV em um DataFrame do pandas, definindo como df
    df = pd.read_csv('epa-sea-level.csv') 

    # Criando o gráfico de dispersão (scatter plot)
    plt.figure(figsize=(10, 6)) # Define o tamanho do gráfico com altura e laugura
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')
    # Plota os pontos dos dados originais, usando o ano como eixo x e o nível do mar ajustado como eixo y

    # Calculando a linha de tendência (regressão linear) para todos os dados
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Aplica a regressão linear nos dados completos para obter inclinação (slope) e interceptação (intercept)
    years_extended = pd.Series(range(1880, 2051))
    # Cria uma série de anos de 1880 até 2050 para prever o futuro
    sea_level_pred_all = res_all.intercept + res_all.slope * years_extended
    # Calcula os valores previstos do nível do mar usando a equação da reta: y = mx + b
    plt.plot(years_extended, sea_level_pred_all, 'r', label='Best Fit: All Data')
    # Plota a linha de tendência para todos os dados em vermelho

    # Calculando a linha de tendência apenas para dados a partir do ano 2000
    df_2000 = df[df['Year'] >= 2000]
    # Filtra o DataFrame para considerar apenas os dados do ano 2000 em diante
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    # Aplica a regressão linear nos dados filtrados
    years_2000 = pd.Series(range(2000, 2051))
    # Cria uma série de anos de 2000 até 2050 para prever o futuro com base nos dados mais recentes
    sea_level_pred_2000 = res_2000.intercept + res_2000.slope * years_2000
    # Calcula os valores previstos do nível do mar para esse período
    plt.plot(years_2000, sea_level_pred_2000, 'green', label='Best Fit: 2000+')
    # Plota a linha de tendência para os dados desde 2000 em verde

    # Adicionando rótulos e título ao gráfico conforme esperado pelos testes
    plt.xlabel('Year') # Define o rótulo do eixo x
    plt.ylabel('Sea Level (inches)') # Define o rótulo do eixo y
    plt.title('Rise in Sea Level') # Define o título do gráfico
    plt.legend() # Adiciona a legenda para identificar cada linha

    # NÃO MUDAR
    # Salvando o gráfico gerado como imagem PNG e retornando o objeto do gráfico (para testes)
    plt.savefig('sea_level_plot.png') # Salva o gráfico como arquivo de imagem
    return plt.gca() # Retorna o objeto do eixo atual para possíveis testes