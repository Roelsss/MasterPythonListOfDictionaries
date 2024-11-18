# List of product dictionaries
products = [
    {"product_name": "Laptop", "category": "Electronics", "price": 750, "stock": 50, "supplier_email": "supplier1@gmail.com"},
    {"product_name": "Desk Chair", "category": "Furniture", "price": 100, "stock": 200, "supplier_email": "supplier2@gmail.com"},
    {"product_name": "Smartwatch", "category": "Electronics", "price": 200, "stock": 150, "supplier_email": "supplier3@gmail.com"},
    {"product_name": "Notebook", "category": "Stationery", "price": 55, "stock": 0, "supplier_email": "supplier4@gmail.com"},
    {"product_name": "Running Shoes", "category": "Apparel", "price": 80, "stock": 100, "supplier_email": "supplier5@gmail.com"}
]

# Print product data
for product in products:
    print(f"Product Name: {product['product_name']}, Category: {product['category']}, Price: ${product['price']}, Stock: {product['stock']}, Supplier Email: {product['supplier_email']}")
