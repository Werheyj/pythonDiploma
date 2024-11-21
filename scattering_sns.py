import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("files/Iris.csv")

plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x='SepalLengthCm', y='SepalWidthCm', hue='Species', style='Species', s=100)

plt.title('Длина и ширина чашелистика ирисов')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Ширина чашелистика (см)')
plt.grid(True)

plt.show()
