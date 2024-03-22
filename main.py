from functools import lru_cache
from typing import Union
from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import todos

import config

app = FastAPI()

# router: comment out next lines till we create it
app.include_router(todos.router)

# origins = [
#    "http://localhost:3000",
#    "https://todo-frontend-khaki.vercel.app/",
# ]

# CORS configuration, needed for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# global http exception handler, to handle errors
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# dependency function to get the settings (tiny speedup)
@lru_cache()
def get_settings():
    return config.Settings()


# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}


@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    # print the app_name configuration
    # print(settings.APP_NAME)
    # print(settings.DATABASE_NAME)
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
