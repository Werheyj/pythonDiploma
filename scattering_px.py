import pandas as pd
import plotly.express as px


df = pd.read_csv("files/Iris.csv")

fig = px.scatter(df,
                 x='SepalLengthCm',
                 y='SepalWidthCm',
                 color='Species',
                 title='Длина и ширина чашелистика ирисов',
                 labels={'SepalLengthCm': 'Длина чашелистика (см)',
                         'SepalWidthCm': 'Ширина чашелистика (см)'},
                 hover_data=['PetalLengthCm', 'PetalWidthCm'])

fig.show()
