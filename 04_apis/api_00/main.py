import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    version='0.1.0',
    title='Training API',
    description='API for training',
    docs_url='/',
)


class Product(BaseModel):
    id: int
    name: str
    price: float


products = [
        {'id': 1, 'name': 'product a', 'price': 5.99},
        {'id': 2, 'name': 'product b', 'price': 10.99},
        {'id': 3, 'name': 'product c', 'price': 8.00},
    ]


@app.get("/test")
def test():
    return {"message": "Hello!"}


@app.get("/products")
def get_all():
    return products


@app.get("/products/{id}")
def get_id(id: int):
    for product in products:
        if product['id'] == id:
            return product
    return 'Produto não encontrado'


@app.post("/products")
def add(item: Product):
    products.append({'id': item.id, 'name': item.name, 'price': item.price})
    return products


@app.put("/products/{id}")
def update(id: int, item: Product):
    for product in products:
        if product['id'] == id:
            product['name'] = item.name
            product['price'] = item.price
    return products


# Init package
if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=7000, reload=True)
