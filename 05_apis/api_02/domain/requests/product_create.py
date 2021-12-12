from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    active: bool = True
