"""
2
Histograma:
3
     Gráfico de barras que representa uma distribuição de frequência.
4
     - Eixo x (horiz): intervalos (classes) dos dados
5
     - Eixo y (vertc): frequência (contagem) de itens por intervalo
6
BoxPlot: 
7
     Diagrama de caixa que representa os extremos e mais os quartis
8
     - Min: O menor valor do conjunto de dados
9
     - Q1: Primeiro quartil dos dados (25%)
10
     - Q2: Segundo quartil dos dados, a mediana (50%)
11
     - Q3: Terceiro quartil dos dados (75%)
12
     - Max: O maior valor do conjunto de dados
13
Densidade:
14
     Gráfico que representa uma distribuição suavisada da frequência dos dados
15
     - Eixo x (horiz): intervalos (classes) dos dados
16
     - Eixo y (vertc): frequência (contagem) de itens por intervalo
17
Dispersão:
18
     Gráfico que representa a relação entre dois conjunto de dados
19
     - Eixos: Cada eixo representará um dos dois conjunto de dados
20
     - Pontos: Cada ponto representa a interseção entre as variáveis de ambos os conjuntos.
21
​
22
"""




import matplotlib.pyplot as plt
import pandas as pd
import graficos_estatisticos



print(graficos_estatisticos.__doc__)

df_dados_brutos = pd.read_csv('homicidios_por_populacao/taxa_homicidios.csv')

def histograma():
    bins_do_grafico = [1, 5, 10, 15]
    histograma = (df_dados_brutos['Taxa homicidios']).plot.hist(figsize=(6, 4), bins=bins_do_grafico)
    histograma.set_xlabel('Taxa de Homicidios')
    histograma.set_ylabel('Frequência (Número de cidades)')
    plt.show()

histograma()
