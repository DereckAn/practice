from fastapi import APIRouter, HTTPException
from pydantic import BaseModel # nos da la capacidad de crear un aentidad




router = APIRouter()





# Entidad user
class User(BaseModel):
    id : int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id = 1,name="Dereck", surname="Angeles", url="https://www.google.com",age=24),
         User(id = 2,name="Sadie",surname="Angeles",url="https://www.google.com", age=22),
         User(id = 3,name="Jabir",surname="Angeles",url="https://www.google.com",age=20),
         User(id = 4,name="Joao",surname="Villela",url="https://www.google.com",age=24)]

@router.get("/")
async def root():
    return "Hola"

@router.get("/usersjson")
async def usersjson():
    return [{"name" : "Dereck", "Surname" : "Angeles", "url": "https://www.google.com", "age":24},
            {"name" : "Sadie", "Surname" : "Angeles", "url": "https://www.google.com", "age":22},
            {"name" : "Jabir", "Surname" : "Angeles", "url": "https://www.google.com", "age":20},
            {"name" : "Joao", "Surname" : "Villela", "url": "https://www.google.com", "age":24}]


@router.get("/users")
async def users():
    # return User(name="Dereck", surname="Angeles", urs="https://www.google.com", age = 24)
    return users_list

# http://127.0.0.1:8000/user/1   --  Asi es el parametro 
@router.get("/user/{id}")  # Esto es llamar por path. 
async def id(id: int):
    return (find_user(id))
  
  

# http://127.0.0.1:8000/userquery/?id=1     --   fijate bien en el simbolo de interrogacion 
@router.get("/userquery/")  # Esto es llamar por query
async def id(id: int):   # esto solo es un ejemplo para cuando haya mas parametros  http://127.0.0.1:8000/userquery/?id=1&name=dereck
   return (find_user(id))



@router.post("/adduser/", response_model=User, status_code=201)  # Esto es para agregar usuarios
async def user(user: User):
    if type(find_user(user.id)) == User:
        raise HTTPException(status_code= 404 , detail="User already exists") # Cuando lanzamos un error lo hacemos con el "raise"
        # return {"Error": "User already exists"}
    
    users_list.append(user)
    return user
        
        
        
@router.put("/updateuser/")  # Esto es para actualizar usuarios
async def updateU(user: User):
    found = False
    for i,k in enumerate(users_list):
        if k.id == user.id:
            users_list[i] = user
            found = True
    if not found:
         return {"Error": "User not found"}
     
    return user
            
@router.delete("/deleteuser/{id}")  # Esto es para eliminar usuarios
async def deleteU(id: int):
    found = False
    for i,k in enumerate(users_list):
        if k.id == id:
            del users_list[i]
            found = True
    if not found:
        return {"Error": "User not found"}




    
def find_user(id: int):
    user = filter(lambda x: x.id == id, users_list) # Esto es para buscar dentro de una lista. Estudiar mas adelante. 
    try:
        return list(user)[0]
    except:
        return {"Error": "User not found"}


    