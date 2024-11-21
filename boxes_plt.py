import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("files/Iris.csv")

plt.figure(figsize=(10, 6))

df.boxplot(column='SepalLengthCm', by='Species', grid=False)

plt.title('Длина чашелистика ирисов по видам')
plt.suptitle('')
plt.xlabel('Вид ириса')
plt.ylabel('Длина чашелистика (см)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()
