from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
