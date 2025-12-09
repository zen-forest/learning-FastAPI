from pydantic import BaseModel, Field

# "..." means it's required
class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., gt=1900, lt=2100)

class BookResponse(BaseModel):
    title: str
    author: str
