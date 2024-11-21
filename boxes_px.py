import pandas as pd
import plotly.express as px

df = pd.read_csv("files/Iris.csv")

fig = px.box(df,
              x='Species',
              y='SepalLengthCm',
              color='Species',
              title='Длина чашелистика ирисов по видам',
              labels={'Species': 'Вид ириса',
                      'SepalLengthCm': 'Длина чашелистика (см)'})

fig.show()
