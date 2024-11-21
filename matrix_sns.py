import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)

random_matrix = np.random.rand(10, 10)

plt.figure(figsize=(7, 5))
sns.heatmap(random_matrix, cmap='viridis', annot=True, fmt=".2f", cbar=True)
plt.title('Тепловой график случайной матрицы 10x10')
plt.xlabel('Столбцы')
plt.ylabel('Строки')
plt.show()
