import items 
import books
from fastapi import FastAPI

app = FastAPI()

app.include_router(books.router)
app.include_router(items.router)
