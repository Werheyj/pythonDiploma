import pandas as pd
import plotly.express as px


data = pd.read_csv('files/sales_dataset.csv')

data['Date'] = pd.to_datetime(data['Date'])

daily_sales = data.groupby('Date')['Total Amount'].sum().reset_index()

fig = px.line(daily_sales, x='Date', y='Total Amount',
              title='Общая сумма продаж по датам',
              labels={'Total Amount': 'Общая сумма продаж', 'Date': 'Дата'},
              markers=True)

fig.show()
