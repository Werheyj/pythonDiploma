import numpy as np
import plotly.figure_factory as ff

np.random.seed(0)

random_matrix = np.random.rand(10, 10)

rounded_matrix = np.round(random_matrix, 3)

fig = ff.create_annotated_heatmap(z=rounded_matrix, colorscale='Viridis')

fig.update_layout(
    title='Тепловой график случайной матрицы 10x10',
    xaxis_title='Столбцы',
    yaxis_title='Строки'
)

fig.show()
