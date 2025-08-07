import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

ativos_csv = 'data\sp500_data.csv.gz'
setores_csv = 'data\sp500_sectors.csv'

df_ativos = pd.read_csv(ativos_csv, index_col = 0)
print(df_ativos.head())
df_setores = pd.read_csv(setores_csv)
print(df_setores.head())

df_telecom = df_setores[df_setores['sector'] == 'telecommunications_services']['symbol']

print(df_telecom.head())

telecom_ativos = df_ativos.loc[df_ativos.index >= '2012-07-01', df_telecom]
print(telecom_ativos.head())

dados_correlacionados = telecom_ativos.corr()
print(dados_correlacionados.head())