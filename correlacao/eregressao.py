import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

EXPOSICAO_ALGODAO = 'data/LungDisease.csv'
dataframe = pd.read_csv(EXPOSICAO_ALGODAO)
print(dataframe.head())

#dataframe.plot.scatter(x = 'Exposure', y = 'PEFR')
#plt.show()

predictors = ['Exposure']
outcome = 'PEFR'
model = LinearRegression()
model.fit(dataframe[predictors], dataframe[outcome])

print(f'Intercept: {model.intercept_:.3f}')
print(f'Coeficiente Angular: {model.coef_[0]}')
fig, (reg, ax, res) = plt.subplots(1, 3, figsize = (12, 4))
reg = sns.regplot(x = 'Exposure', y = 'PEFR', data = dataframe, ax = reg)

ax.set_xlim(0, 23)
ax.set_ylim(295, 450)

ax.set_xlabel('Exposure')
ax.set_ylabel('PERF')
ax.plot(dataframe['Exposure'], model.predict(dataframe[predictors]), '-')
ax.text(0.4, model.intercept_, r'$b_0$', size = 'larger')
x = pd.DataFrame({'Exposure': [7.5, 17.5]})
y = model.predict(x)
ax.plot((7.5, 7.5, 17.5), (y[0], y[1], y[1]), '--')
ax.text(5, np.mean(y), r'$\Delta Y$', size = 'larger')
ax.text(12, y[1] - 10, r'$\Delta X$', size = 'larger')
ax.text(12, 390, r'$b_1 = \frac{\Delta Y}{\Delta X}$', size = 'larger')

fitted = model.predict(dataframe[predictors])
residuals = dataframe[outcome] - fitted
res = dataframe.plot.scatter(x = 'Exposure', y = 'PEFR', ax = res)
res.plot(dataframe.Exposure, fitted)
for x, yatual, yfitted in zip(dataframe.Exposure, dataframe.PEFR, fitted):
    res.plot((x, x), (yatual, yfitted), '--', color = 'C1')

plt.tight_layout()
plt.show()