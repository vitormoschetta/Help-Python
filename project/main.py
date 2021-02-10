from product import Product
from productRepository import ProductRepository

prod = Product('Product A', 5)

repository = ProductRepository()
repository.create(prod)

for item in repository.getall():
    print(item.name)
    


