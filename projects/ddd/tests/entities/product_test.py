from projects.ddd.domain.entities.product import Product

prod = Product('', 5.5)
assert len(prod._notifications) == 1, prod._notifications[0]

