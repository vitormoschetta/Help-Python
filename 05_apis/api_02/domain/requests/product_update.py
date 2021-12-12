from pydantic import BaseModel


class ProductUpdate(BaseModel):
    id: str
    name: str
    price: float
    active: bool
