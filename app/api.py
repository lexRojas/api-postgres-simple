from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#---IMPORTACION DE RUTAS 

from routes.route_presupuesto import route_presupuesto



app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return 'hola a todos'
    

# app.include_router(route_user)
# app.include_router(route_usuarios)
app.include_router(route_presupuesto)
