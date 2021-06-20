from fastapi import FastAPI

app = FastAPI(
    version='1.0.0',
    title='Python FastAPI',
    docs_url='/',
)


@app.get("/v1/product")
def getall():
    return {
        "product": "Product A",
        "price": 5.99
    }