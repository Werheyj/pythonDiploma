import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("files/Iris.csv")

plt.figure(figsize=(7, 4))
sns.boxplot(data=df, x='Species', y='SepalLengthCm', palette='Set2')

plt.title('Длина чашелистика ирисов по видам')
plt.xlabel('Вид ириса')
plt.ylabel('Длина чашелистика (см)')
plt.grid(True)

plt.show()
