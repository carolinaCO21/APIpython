
"""
Teclea Ctrl+Shift+P una vez esté abierto el VSCode.
Selecciona “Python: Create Environment”:

pip install "fastapi[standard]"

autenticación vamos a usar JWT (JSON Web Tokens): pip install pyjwt

hash contraseña: pip install "pwdlib[argon2]" 

fastapi dev main.py

Vamos a trabajar con MongoDB en local, así que para eso nos tenemos que descargar un servidor de MongoDB:
https://www.mongodb.com/try/download/community
También necesitaremos instalar la siguiente herramienta, mongosh:
https://www.mongodb.com/docs/mongodb-shell/

 pip install pymongo

# mongodb compass 

fastapi dev main.py
"""



from fastapi import FastAPI
from routers import users, products, auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth_users.router)
app.include_router(users_db.router)
#app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"Hello": "World"}


