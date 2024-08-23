import pandas as pd
import matplotlib.pyplot as plt

# Biểu đồ Số lượng Sản phẩm theo Danh mục
#Mục đích: Hiển thị số lượng sản phẩm theo danh mục. Dữ liệu giả lập không có danh mục cho sản phẩm,
#nên sẽ giả định rằng tất cả sản phẩm thuộc cùng một danh mục.


# Đọc dữ liệu từ CSV
product_df = pd.read_csv('Product.csv')

# Giả định rằng tất cả sản phẩm thuộc cùng một danh mục trong dữ liệu giả lập
# Vẽ biểu đồ số lượng sản phẩm theo tên sản phẩm
plt.figure(figsize=(12, 6))
plt.bar(product_df['product_name'], product_df['product_Quantitystock'], color='skyblue')
plt.title('Số lượng Sản phẩm theo Tên Sản phẩm')
plt.xlabel('Tên Sản phẩm')
plt.ylabel('Số lượng')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
