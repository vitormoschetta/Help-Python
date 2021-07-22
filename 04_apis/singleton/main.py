import uvicorn
from datetime import date
from fastapi import FastAPI
from models.singleton_wase_count import SingletonWaseCount
from models.singleton_weg_count import SingletonWegCount


app = FastAPI(
    version='1.0.0',
    title='Fake Skalena API',
    docs_url='/',
)


@app.post("/v1/oauth/token")
def oauth():
    return {
        "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImY2UzFtM0x0ZWdfV3ZsN01YcVRaZyJ9.eyJpc3MiOiJodHRwczovL3NrYWxlbmEuYXV0aDAuY29tLyIsInN1YiI6InRXYXlGMkNTNjZkVUVxUnc1MkdqbW52MnVHRDJ4V0diQGNsaWVudHMiLCJhdWQiOiJodHRwOi8vYXBpLmV4YW1wbGUuY29tIiwiaWF0IjoxNjIxNjIwODI5LCJleHAiOjE2MjE3MDcyMjksImF6cCI6InRXYXlGMkNTNjZkVUVxUnc1MkdqbW52MnVHRDJ4V0diIiwic2NvcGUiOiJhZG1pbiB1c2VyIGFjZXNzbyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImFkbWluIiwidXNlciIsImFjZXNzbyJdfQ.tgua6bAptR4LL7HROJ8gl9oIRDderdiRz4np2fdutOlc5PhvaVzxcDe8T1cKSkxw27rpJrMoUULUIgWAqE5zI53-MvRMq8ulk-I0T7N2v3Iou81Yv8OeTfI9JMlP4EinJHEFSffL3bn46uaYn_b_kJFbsHGluSLGhmF8b8fhzxySet1UVDwTGkeecaLnt7JLY4DpyU7yzDx_8jOtz2llWAaNTX6WRpyySiNwM2zvlj4yscSNqxyG9Er31yFoHvRQfBOJEtImRrC5pr4hA0DcmdCbzzcC1I2FSBHWeNUHGpHaiAZZP9L2i2EOq90glarz7835_txZvAUdj7fvyFYpcg",
        "scope": "admin user acesso",
        "expires_in": "86400",
        "token_type": "Bearer"
    }


@app.post("/v1/compradores/wip")
def wip():
    return {
        "status": "1",
        "data_processamento": date.today(),
        "mensagem": "0"
    }


@app.post("/v1/compradores/wase")
def wase():
    if SingletonWaseCount().COUNT < 1002:
        SingletonWaseCount().COUNT += 1
        return {
            "status": "1",
            "data_processamento": date.today(),
            "mensagem": SingletonWaseCount().COUNT
        }
    else:
        SingletonWaseCount().COUNT = 1001
        return {
            "status": "1",
            "data_processamento": date.today(),
            "mensagem": 1001
        }


@app.post("/v1/compradores/was")
def was():
    return {
        "status": "1",
        "data_processamento": date.today(),
        "mensagem": "2001"
    }


@app.get("/v1/compradores/weg/{pdcBio}")
def weg(pdcBio):
    return {
        "status": "1",
        "data_processamento": "21/06/2021 11:30:47",
        "retorno": {
            "Cabecalho": {
                "PDC": pdcBio,
                "Requisicao": "453455",
                "Data_Vencimento": "09/04/2021",
                "Hora_Vencimento": "16:46",
                "Campo_Extra": [
                    {
                        "Nome": "justificativa",
                        "Valor": "-"
                    }
                ]
            },
            "Fornecedores": [
                {
                    "Razao_Social": "Classic Automation Web Supplyer",
                    "CNPJ": "60.648.261/0001-44",
                    "Faturamento_Minimo": "2",
                    "Prazo_Entrega": "2",
                    "Validade_Proposta": "08/07/2021",
                    "Id_Forma_Pagamento": 4,
                    "Frete": "FOB",
                    "Data_Confirmacao": "09/04/2021"
                }
            ],
            "Itens": [
                {
                    "Id_Artigo": 56663026,
                    "Cod_Produto": "12345",
                    "Quantidade": 300,
                    "Programacao_Entrega": [
                        {
                            "Data": "21/2/2022",
                            "Quantidade": "150"
                        },
                        {
                            "Data": "21/3/2022",
                            "Quantidade": "150"
                        }
                    ],
                    "Campo_Extra": [
                        {
                            "Nome": "justificativa",
                            "Valor": "-"
                        }
                    ],
                    "Resposta": {
                        "CNPJ": "60.648.261/0001-44",
                        "Fabricante": "MARCA TESTE",
                        "Embalagem": "CAIXA",
                        "Preco_Unitario": "150",
                        "Preco_Total": "15000",
                        "Comentario": "comentario teste online."
                    }
                },
                {
                    "Id_Artigo": 56663026,
                    "Cod_Produto": "12346",
                    "Quantidade": 500,
                    "Programacao_Entrega": [
                        {
                            "Data": "21/2/2022",
                            "Quantidade": "200"
                        },
                        {
                            "Data": "21/3/2022",
                            "Quantidade": "200"
                        },
                        {
                            "Data": "21/4/2022",
                            "Quantidade": "100"
                        }
                    ],
                    "Campo_Extra": [
                        {
                            "Nome": "justificativa",
                            "Valor": "-"
                        }
                    ],
                    "Resposta": {
                        "CNPJ": "60.648.261/0001-44",
                        "Fabricante": "MARCA TESTE",
                        "Embalagem": "CAIXA",
                        "Preco_Unitario": "150",
                        "Preco_Total": "15000",
                        "Comentario": "comentario teste online."
                    }
                }
            ]
        }
    }


@app.get("/v1/compradores/weg")
def weg():
    if SingletonWegCount().COUNT < 1002:
        SingletonWegCount().COUNT += 1
        return {
            "status": "1",
            "data_processamento": "21/06/2021 11:30:47",
            "retorno": {
                "Cabecalho": {
                    "PDC": SingletonWegCount().COUNT,
                    "Requisicao": "144",
                    "Data_Vencimento": "09/04/2021",
                    "Hora_Vencimento": "16:46",
                    "Campo_Extra": [
                        {
                            "Nome": "justificativa",
                            "Valor": "-"
                        }
                    ]
                },
                "Fornecedores": [
                    {
                        "Razao_Social": "Classic Automation Web Supplyer",
                        "CNPJ": "60.648.261/0001-44",
                        "Faturamento_Minimo": "2",
                        "Prazo_Entrega": "2",
                        "Validade_Proposta": "08/07/2021",
                        "Id_Forma_Pagamento": 4,
                        "Frete": "FOB",
                        "Data_Confirmacao": "09/04/2021"
                    }
                ],
                "Itens": [
                    {
                        "Id_Artigo": 56663026,
                        "Cod_Produto": "12345",
                        "Quantidade": 300,
                        "Programacao_Entrega": [
                            {
                                "Data": "21/2/2022",
                                "Quantidade": "150"
                            },
                            {
                                "Data": "21/3/2022",
                                "Quantidade": "150"
                            }
                        ],
                        "Campo_Extra": [
                            {
                                "Nome": "justificativa",
                                "Valor": "-"
                            }
                        ],
                        "Resposta": {
                            "CNPJ": "99.999.999/0001-99",
                            "Fabricante": "MARCA TESTE",
                            "Embalagem": "CAIXA",
                            "Preco_Unitario": "150",
                            "Preco_Total": "15000",
                            "Comentario": "comentario teste online."
                        }
                    },
                    {
                        "Id_Artigo": 56663026,
                        "Cod_Produto": "12346",
                        "Quantidade": 500,
                        "Programacao_Entrega": [
                            {
                                "Data": "21/2/2022",
                                "Quantidade": "200"
                            },
                            {
                                "Data": "21/3/2022",
                                "Quantidade": "200"
                            },
                            {
                                "Data": "21/4/2022",
                                "Quantidade": "100"
                            }
                        ],
                        "Campo_Extra": [
                            {
                                "Nome": "justificativa",
                                "Valor": "-"
                            }
                        ],
                        "Resposta": {
                            "CNPJ": "99.999.999/0001-98",
                            "Fabricante": "MARCA TESTE",
                            "Embalagem": "CAIXA",
                            "Preco_Unitario": "2.50",
                            "Preco_Total": "1250.00",
                            "Comentario": "comentario teste online."
                        }
                    }
                ]
            }
        }
    else:
        SingletonWegCount().COUNT = 1000
        return {
            "status": "1",
            "data_processamento": "21/06/2021 11:30:47",
            "retorno": {}
        }


@app.get("/v1/compradores/wmg/{cnpj}")
def weg(cnpj):
    return {
        "status": "1",
        "data_processamento": "21/06/2021 11:30:47",
        "retorno": {
            "Empresas": [
                {
                    "Razao_Social": "Razão Social fornecedor 1",
                    "Nome_Fantasia": "Nome Fantasia fornecedor",
                    "CNPJ": "99999999999999",
                    "Inscricao_Estadual": "000.000.000.000",
                    "CEP": "00000-000",
                    "Logradouro": "Rua",
                    "Cidade": "São Paulo",
                    "Estado": "Sao Paulo",
                    "Estado_Sigla": "SP",
                    "Pais": "Brasil",
                    "Pais_Sigla": "BR",
                    "Telefone": "(00) 0000-0000",
                    "Fax": "(00) 0000-0000",
                    "Contato": "usuário Teste",
                    "Email": "usuario@teste.com.br",
                    "Tipo_Empresa": "Distribuidor",
                    "Categoria": "Materiais Medicos, Medicamentos"
                }
            ]
        }
    }



# Init package
if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=7000, reload=True)

