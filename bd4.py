import pandas as pd
import matplotlib.pyplot as plt

#Biểu đồ Phân phối Sản phẩm theo Giá
#Mục đích: Hiển thị phân phối sản phẩm theo giá.

# Đọc dữ liệu từ CSV
product_df = pd.read_csv('product.csv')

# Vẽ biểu đồ phân phối giá sản phẩm
plt.figure(figsize=(12, 6))
plt.hist(product_df['product_Price'], bins=20, color='coral', edgecolor='black')
plt.title('Phân phối giá sản phẩm')
plt.xlabel('Giá (USD)')
plt.ylabel('Số lượng sản phẩm')
plt.grid(True)
plt.tight_layout()
plt.show()
