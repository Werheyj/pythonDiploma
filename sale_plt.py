import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('files/sales_dataset.csv')

data['Date'] = pd.to_datetime(data['Date'])

daily_sales = data.groupby('Date')['Total Amount'].sum().reset_index()

plt.figure(figsize=(9, 5))
plt.plot(daily_sales['Date'], daily_sales['Total Amount'], marker='o', color='skyblue')

plt.title('Общая сумма продаж по датам')
plt.xlabel('Дата')
plt.ylabel('Общая сумма продаж')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
