import uvicorn
from fastapi import FastAPI

app = FastAPI(
    version='0.1.0',
    title='Training API',
    description='API for training',
    docs_url='/',
)

@app.get('/product')
def get_all():
    return 'name: teste'

# Esse 'if' é uma especificação do que deve ser executado instantaneaomente ao importar este módulo:
if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=7000, reload=True)


