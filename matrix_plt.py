import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

random_matrix = np.random.rand(10, 10)

plt.figure(figsize=(7, 5))
plt.imshow(random_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Тепловой график случайной матрицы 10x10')
plt.xlabel('Столбцы')
plt.ylabel('Строки')
plt.show()
