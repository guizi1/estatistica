import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

dataframe = pd.DataFrame({
    'alunos' : ['Matheus', 'Fernando', 'Ana', 'Beatriz', 'Bruna'],
    'horas' : [2, 4, 6, 8, 10],
    'notas' : [50, 60, 85, 85, 100]
})

print(dataframe) 

plt.figure(figsize=(10, 6))
sns.regplot(x = 'horas', y = 'notas', data = dataframe)

plt.xlabel('Horas de Estudo')
plt.ylabel('Notas da Prova')
plt.title('Gráfico de Regressão: Horas de Estudo vs Desempenho nas Provas')

plt.show()