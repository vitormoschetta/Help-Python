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
        'aiohttp',                          # Cliente / servidor HTTP assíncrono
        'aioresponses',                     # Simular chamadas http
        'alembic',                          # Ferramenta de Migrations
        'coloredlogs',                      # Logs coloridos
        'fastapi',                          # Framework para construir APIs
        'fsspec',                           # Unificar projetos e classes de arquivos remotos..
        'psycopg2-binary',                  # Conector de banco de dados PostgreSQL para Python
        'pydantic',                         # Semelhante ao Automapper? (determina o modelo de dados a receber)
        'PyYAML',
        'sqlalchemy',                       # ORM default Python
        'starlette',                        # Kit ferramentas para construção serviços assíncronos
        's3fs',                             # Serviço de comunicação S3 da AWS
        'uvicorn',                          # servidor http local
        'uuid',
    ],
    # Os pacotes abaixo são instalados apenas para desenvolvimento
    extras_require={
        'dev': [
            'mypy',                         # Analisador estático de código
            'pylint',                       # Verificar de bugs e qualidade de código (semelhante ao sonar?)
            'pytest',                       # Testes unitários
            'pytest-cov',                   # Saber a cobertura (coverage) de testes no nosso código
            'sphinx',                       # Documentação:
            'sphinx-autodoc-typehints',     # Geração de documentação automatica
            'sphinx_rtd_theme',             # Tema da documentação
            'sqlalchemy-stubs',             # Funcionalidade adicional ORM sqlalchemy (acho que de tipagem)
        ],
    }
)