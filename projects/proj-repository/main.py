from product import Product
from productRepository import ProductRepository

repository = ProductRepository()

prod = Product('Product C', 22)
repository.create(prod)

for item in repository.getall():
    print(item.name)
    


