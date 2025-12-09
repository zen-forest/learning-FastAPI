from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

from items.router import router as items_router
from books.router import router as books_router

app = FastAPI()

app.include_router(books_router)
app.include_router(items_router)

@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)

@app.exception_handler(HTTPException)
async def HTTP_exception_handler(request, exc):
    return JSONResponse(
            status_code=exc.status_code,
            content={
                "message": "you are very bad user"
                }
            )
