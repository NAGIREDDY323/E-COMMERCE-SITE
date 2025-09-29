from products.models import Product

products_data = [
    {"name": "Stylish Men's Jacket", "description": "Warm and trendy jacket for men.", "price": 99.99, "stock": 10, "category": "M", "image": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c"},
    {"name": "Elegant Women's Dress", "description": "Perfect dress for any occasion.", "price": 120.00, "stock": 15, "category": "W", "image": "https://images.unsplash.com/photo-1521334884684-d80222895322"},
    {"name": "Casual Men's T-Shirt", "description": "Comfortable cotton t-shirt.", "price": 19.99, "stock": 20, "category": "M", "image": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f"},
    {"name": "Women's Summer Hat", "description": "Light and stylish sun hat.", "price": 25.00, "stock": 12, "category": "W", "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"},
    {"name": "Men's Denim Jeans", "description": "Classic slim fit jeans.", "price": 49.99, "stock": 15, "category": "M", "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb"},
    {"name": "Women's Casual Blouse", "description": "Soft fabric and elegant design.", "price": 35.50, "stock": 18, "category": "W", "image": "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91"},
    {"name": "Men's Leather Shoes", "description": "Durable and stylish shoes.", "price": 89.99, "stock": 8, "category": "M", "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23"},
    {"name": "Women's Evening Gown", "description": "Elegant gown for special events.", "price": 199.99, "stock": 5, "category": "W", "image": "https://images.unsplash.com/photo-1520975691094-f2679f178ce8"},
    {"name": "Men's Casual Hoodie", "description": "Comfort and style combined.", "price": 59.99, "stock": 20, "category": "M", "image": "https://images.unsplash.com/photo-1530845647919-0cf15927c6d1"},
    {"name": "Women's Running Shoes", "description": "Lightweight and supportive.", "price": 75.00, "stock": 12, "category": "W", "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"},
    {"name": "Men's Watch", "description": "Elegant wrist watch.", "price": 250.00, "stock": 7, "category": "M", "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"},
    {"name": "Women's Sunglasses", "description": "Stylish UV protection.", "price": 49.00, "stock": 14, "category": "W", "image": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f"},
    {"name": "Men's Backpack", "description": "Durable and spacious backpack.", "price": 65.00, "stock": 9, "category": "M", "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb"},
    {"name": "Women's Scarf", "description": "Soft and warm scarf.", "price": 19.99, "stock": 20, "category": "W", "image": "https://images.unsplash.com/photo-1521334884684-d80222895322"},
    {"name": "Men's Casual Shorts", "description": "Comfortable and stylish.", "price": 29.99, "stock": 15, "category": "M", "image": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c"},
    {"name": "Women's Handbag", "description": "Elegant leather handbag.", "price": 130.00, "stock": 7, "category": "W", "image": "https://images.unsplash.com/photo-1520975691094-f2679f178ce8"},
    {"name": "Men's Formal Shirt", "description": "Perfect for office wear.", "price": 40.00, "stock": 10, "category": "M", "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23"},
    {"name": "Women's Sandals", "description": "Comfortable and trendy.", "price": 45.00, "stock": 13, "category": "W", "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"},
    {"name": "Men's Belt", "description": "Classic leather belt.", "price": 22.00, "stock": 25, "category": "M", "image": "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91"},
    {"name": "Women's Watch", "description": "Elegant wrist watch for women.", "price": 260.00, "stock": 6, "category": "W", "image": "https://images.unsplash.com/photo-1530845647919-0cf15927c6d1"},
]

for item in products_data:
    Product.objects.create(
        name=item['name'],
        description=item['description'],
        price=item['price'],
        stock=item['stock'],
        category=item['category'],
        image=item['image'],
    )

print("Inserted 20 products with Unsplash image URLs.")
