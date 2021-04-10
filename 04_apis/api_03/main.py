import uvicorn
from fastapi import FastAPI
from app.controllers.product_controller import PRODUCT_CONTROLLER

app = FastAPI(
    version='0.1.0',
    title='Training API',
    description='API for training',
    docs_url='/',
)


@app.get('/endpoint_test')
def endpoint_test():
    return 'test: hello'


# region Routers/Controllers
app.include_router(
    PRODUCT_CONTROLLER,
    prefix='/v1/product',
    tags=['product']
)


# Init do package
if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=7000, reload=True)


