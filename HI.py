import pandas as pd
from faker import Faker
import random

fake = Faker()

# 1. Tạo Dữ liệu cho Bảng Trend
def create_trend_data(num_records):
    trends = []
    for _ in range(num_records):
        trend = {
            'trend_id': fake.unique.random_number(digits=3),
            'trend_name': fake.bs(),
            'trend_description': fake.sentence(),
            'trend_date': fake.date_this_year().strftime('%Y-%m-%d'),
            'trend_category': random.choice(['Technology', 'Business', 'Lifestyle']),
            'trend_start_date': fake.date_this_year().strftime('%Y-%m-%d'),
            'trend_end_date': fake.date_this_year().strftime('%Y-%m-%d'),
            'trend_impact': random.choice(['High', 'Medium', 'Low']),
            'trend_source': fake.company(),
            'trend_analysis_date': fake.date_this_year().strftime('%Y-%m-%d')
        }
        trends.append(trend)
    return trends

trend_data = create_trend_data(200)
trend_df = pd.DataFrame(trend_data)
trend_df.to_csv('Trend.csv', index=False)

# 2. Tạo Dữ liệu cho Bảng Customer
def create_customer_data(num_records):
    customers = []
    for _ in range(num_records):
        customer = {
            'customer_id': fake.unique.random_number(digits=3),
            'customer_name': fake.name(),
            'customer_address': fake.address(),
            'customer_contact': fake.phone_number(),
            'customer_email': fake.email(),
            'customer_city': fake.city(),
            'customer_country': fake.country(),
            'customer_segment': random.choice(['Retail', 'Wholesale', 'Corporate']),
            'customer_registration_date': fake.date_this_decade().strftime('%Y-%m-%d'),
            'customer_last_purchase_date': fake.date_this_year().strftime('%Y-%m-%d')
        }
        customers.append(customer)
    return customers

customer_data = create_customer_data(200)
customer_df = pd.DataFrame(customer_data)
customer_df.to_csv('customer.csv', index=False)

# 3. Tạo Dữ liệu cho Bảng Category
def create_category_data(num_records):
    categories = []
    for _ in range(num_records):
        category = {
            'category_id': fake.unique.random_number(digits=3),
            'category_name': fake.word(),
            'category_description': fake.sentence(),
            'category_access_level': random.choice(['High', 'Medium', 'Low']),
            'category_created_by': 'Admin',
            'category_creation_date': fake.date_this_year().strftime('%Y-%m-%d'),
            'category_last_modified_by': 'Admin',
            'category_last_modified_date': fake.date_this_year().strftime('%Y-%m-%d'),
            'category_status': random.choice(['Active', 'Inactive']),
            'category_priority': random.randint(1, 5)
        }
        categories.append(category)
    return categories

category_data = create_category_data(200)
category_df = pd.DataFrame(category_data)
category_df.to_csv('Category.csv', index=False)

# 4. Tạo Dữ liệu cho Bảng Sale
def create_sale_data(num_records):
    sales = []
    for _ in range(num_records):
        sale = {
            'sale_id': fake.unique.random_number(digits=3),
            'customer_id': fake.random_number(digits=3),
            'product_id': fake.random_number(digits=3),
            'sale_date': fake.date_this_year().strftime('%Y-%m-%d'),
            'sale_quantity': random.randint(1, 10),
            'sale_amount': round(random.uniform(50, 500), 2),
            'sale_discount': round(random.uniform(0, 50), 2),
            'sale_payment_method': random.choice(['Credit Card', 'PayPal', 'Bank Transfer']),
            'sale_delivery_status': random.choice(['Delivered', 'Shipped', 'Pending']),
            'sale_returned': random.choice(['Yes', 'No'])
        }
        sales.append(sale)
    return sales

sale_data = create_sale_data(200)
sale_df = pd.DataFrame(sale_data)
sale_df.to_csv('Sale.csv', index=False)

# 5. Tạo Dữ liệu cho Bảng Product
def create_product_data(num_records):
    products = []
    for _ in range(num_records):
        product = {
            'product_id': fake.unique.random_number(digits=3),
            'product_name': fake.word().capitalize(),
            'product_description': fake.sentence(),
            'product_Quantitystock': random.randint(1, 50),
            'product_Price': round(random.uniform(100, 1000), 2),
            'trend_start_date': fake.date_this_year().strftime('%Y-%m-%d'),
            'Product_Weight': round(random.uniform(0.5, 5.0), 2),
            'Product_sale_date': fake.date_this_year().strftime('%Y-%m-%d'),
            'Product_year': fake.year(),
            'remaining products': random.randint(0, 20)
        }
        products.append(product)
    return products

product_data = create_product_data(200)
product_df = pd.DataFrame(product_data)
product_df.to_csv('Product.csv', index=False)
