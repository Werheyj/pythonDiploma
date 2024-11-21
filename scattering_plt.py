import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("files/Iris.csv")

plt.figure(figsize=(7, 4))

species = df['Species'].unique()
colors = ['blue', 'orange', 'green']

for i, sp in enumerate(species):
    subset = df[df['Species'] == sp]
    plt.scatter(subset['SepalLengthCm'], subset['SepalWidthCm'],
                color=colors[i], label=sp, s=100)

plt.title('Длина и ширина чашелистика ирисов')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Ширина чашелистика (см)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
