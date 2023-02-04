from fastapi import APIRouter
from routers import products, users

app = APIRouter()

# uvicorn main:app --reload
# Documentacion con Swagger: /docs
# Documentacion con Redocly: /redocs
# http://127.0.0.1:8000
# postman par ainteractuar con el api. Y con el backend. 


# POST : para crear datos
# GET : para leer datos
# PUT : para actualizar datos 
# DELETE :  para borrar datos


#Routers
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hola"


@app.get("/url")
async def root():
    return {"url_curso" : "https://mouredev.com/python"}



