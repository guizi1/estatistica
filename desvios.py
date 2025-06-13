import pandas as pd
import numpy as np
from faker import Faker


fake = Faker('pt-BR')

media_notas = 70
desvio_padrao_notas = 10
num_alunos = 100
notas = np.random.normal(loc = media_notas, scale = desvio_padrao_notas, size = num_alunos)
notas = np.clip(notas, 0, 100)
media= np.mean(notas)
mediana = np.median(notas)
desvios = notas - media
desvios_absolutos = np.abs(notas - media)
variancias_individuais = (notas - media)**2
variancia = np.var(notas, ddof = 1)
desvio_padrao = np.std(notas)
desvios_abs_em_relacao_mediana_individuais = np.abs(notas - media)
mad = np.median(desvios_abs_em_relacao_mediana_individuais)
dam = np.mean(desvios_absolutos)


print('--- DataFrame 1: Dados Brutos, Desvios e Variâncias individuais')
df_detalhes = pd.DataFrame({
    'Dados Brutos': notas,
    'Desvio (x - média)': desvios,
    'Variância Individual (x - média)^2': variancias_individuais,
    'Desvio Absoluto (x - média)': desvios_absolutos,
    'Desvio Absoluto (x - mediana)': desvios_abs_em_relacao_mediana_individuais

})

resultados_estatisticos_unicos = {
    'Métrica Estatística': [
        'Média',
        'Mediana',
        'Desvio Padrão',
        'Varianc',
        'Desvio Absoluto Médio (DAM)',
        'Desvio Absoluto Mediano (MAD)'
    ],
    'Valor Calculado': [
        media,
        mediana,
        desvio_padrao,
        variancia,
        dam,
        mad
    ]
}
df_resultados_unicos = pd.DataFrame(resultados_estatisticos_unicos)
print(df_resultados_unicos.round(3))