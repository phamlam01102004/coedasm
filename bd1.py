import pandas as pd
import matplotlib.pyplot as plt

#Biểu đồ Doanh số bán hàng theo Ngày
#Mục đích: Hiển thị doanh số bán hàng theo ngày.


# Đọc dữ liệu từ CSV
sale_df = pd.read_csv('Sale.csv')
sale_df['sale_date'] = pd.to_datetime(sale_df['sale_date'])

# Vẽ biểu đồ
plt.figure(figsize=(12, 6))
plt.plot(sale_df.groupby('sale_date')['sale_amount'].sum().index,
         sale_df.groupby('sale_date')['sale_amount'].sum(), marker='o', linestyle='-')
plt.title('Doanh số bán hàng theo Ngày')
plt.xlabel('Ngày')
plt.ylabel('Doanh số (USD)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
