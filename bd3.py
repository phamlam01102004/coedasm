import pandas as pd
import matplotlib.pyplot as plt

#Biểu đồ Tổng doanh thu theo Khách hàng
#Mục đích: Hiển thị tổng doanh thu của từng khách hàng.

# Đọc dữ liệu từ CSV
customer_df = pd.read_csv('customer.csv')
sale_df = pd.read_csv('Sale.csv')

# Tính tổng doanh thu cho từng khách hàng
total_sales_per_customer = sale_df.groupby('customer_id')['sale_amount'].sum().reset_index()
total_sales_per_customer = total_sales_per_customer.merge(customer_df[['customer_id', 'customer_name']], on='customer_id')

# Vẽ biểu đồ
plt.figure(figsize=(12, 6))
plt.bar(total_sales_per_customer['customer_name'], total_sales_per_customer['sale_amount'], color='lightgreen')
plt.title('Tổng doanh thu theo Khách hàng')
plt.xlabel('Tên Khách hàng')
plt.ylabel('Tổng doanh thu (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
