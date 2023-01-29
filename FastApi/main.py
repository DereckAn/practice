from fastapi import FastAPI

app = FastAPI()

# uvicorn main:app --reload
# Documentacion con Swagger: /docs
# Documentacion con Redocly: /redocs
# http://127.0.0.1:8000
# postman par ainteractuar con el api. Y con el backend. 


# POST : para crear datos
# GET : para leer datos
# PUT : para actualizar datos 
# DELETE :  para borrar datos


@app.get("/")
async def root():
    return "Hola"


@app.get("/url")
async def root():
    return {"url_curso" : "https://mouredev.com/python"}


