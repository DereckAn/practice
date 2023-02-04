from fastapi import APIRouter

router = APIRouter(prefix= "/products", 
                   responses= {404:{"Mensaje":"No encontrado"}}, 
                   tags= ["products"]) # Con el prefijo ya no necesitaria idicarle la direccion a los demas metodos. 

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]


@router.get("/")
async def products():
    return products_list
    
@router.get("/{id}")
async def products(id: int):
    return products_list[id]