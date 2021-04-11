"""
Falar aqui do que trata esse arquivo ou modulo criado
"""

from setuptools import find_packages, setup

"""
O Setup é muito importante caso haja a necessidade de publicar o projeto no pip (repositorio oficial python)
"""
setup(
    name='MyApp',
    version='0.1.0',
    packages=find_packages(),
    url='http://localhost:80',
    license='',
    author='vitormoschetta',
    description='API for example',
    keywords=['python', 'teste', 'api'],
    # Os pacotes abaixo são instalados quando for executado 'pip install setup.py'
    install_requires=[
        'fastapi',                          # Framework para construir APIs
        'uvicorn',                          # servidor http local
        'pydantic',
    ]
)