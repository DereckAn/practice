from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return "Hola"

@app.get("/users")
async def users():
    return {"Hello": "World"}

