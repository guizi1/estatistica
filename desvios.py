import pandas as pd
import numpy as np
from faker import Faker


fake = Faker('pt-BR')

media_notas = 70
desvio_padrao_notas = 10
num_alunos = 100
notas = np.random.normal(loc = media_notas, scale = desvio_padrao_notas, size = num_alunos)
print(f'notas random: {notas}')
notas = np.clip(notas, 0, 100)
media= np.mean(notas)
mediana = np.median(notas)
desvios = notas - media
desvios_absolutos = np.abs(notas - media)
variancias_individuais = (notas - media)**2
variancia = np.var(notas, ddof=1)
desvio_padrao = np.std(notas)
desvios_abs_em_relacao_mediana_individuais = np.abs()