
import pandas as pd
import seaborn as sns

FILE = 'gasolina.csv'

data = pd.read_csv(FILE)

grafico = sns.lineplot(data=data, x='dia', y='venda')
grafico.set(title='Sequências de preços da gasolina por dia',xlabel='Dias de Julho', ylabel='R$')

fig = grafico.get_figure()
fig.savefig('gasolina.png')
