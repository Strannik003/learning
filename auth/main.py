import fastapi, uvicorn, sqlite3, bcrypt, jwt, time, os
from dotenv import load_dotenv
from pydantic import BaseModel, Field, EmailStr
from fastapi import Depends

load_dotenv()
app = fastapi.FastAPI()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")


def connection_to_db():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    try:
        yield connection, cursor
    finally:
        connection.close()


def create_db():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               email TEXT,
               password BINARY
               ) """)
    finally:
        connection.close()


class RegRequest(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    age: int = Field(ge=18,le=120)
    email: EmailStr 
    password: str = Field(min_length=8)


class LoginRequest(BaseModel):
    email: EmailStr 
    password: str = Field(min_length=8)


@app.get("/identity/view")
def view_all_users(connection_instance = fastapi.Depends(connection_to_db)):
    connection, cursor = connection_instance
    result = []
    cursor.execute("SELECT * FROM users")
    export = cursor.fetchall()
    for row in export:
        result.append(row)
    return result
        



@app.post("/identity/reg")
def reg(request: RegRequest, connection_instance = fastapi.Depends(connection_to_db)):
    connection, cursor = connection_instance
    cursor.execute("SELECT 1 FROM users WHERE email = ?", (request.email, ))
    user_exists = cursor.fetchone()
    if user_exists:
        return {"msg":"Email's already resistered, try a new one"}
    
    
    byted_passoword = request.password.encode("utf-8")
    sol = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(byted_passoword,sol)

   
    cursor.execute("INSERT into users(name, age, email, password) VALUES (?,?,?,?)", (request.name, request.age, request.email, hashed_password.decode("utf-8")))
    connection.commit()
    
    return {"msg":"New user is added to database"}




@app.post("/identity/sign-in")
def auth(request: LoginRequest, connection_instance = fastapi.Depends(connection_to_db)):
    
    connection, cursor = connection_instance

    byted_passoword = request.password.encode("utf-8")



    cursor.execute("SELECT id, name, password FROM Users WHERE email = ?", (request.email, ))
    log_data_extracted = cursor.fetchone()
   
    
    if log_data_extracted is None:
        return {"msg": "The mail is incorect, try another one"}
    
    hashed_password = log_data_extracted[2]


    result = bcrypt.checkpw(byted_passoword, hashed_password= bytes(hashed_password,"utf-8"))

    
    if result is False:
        return {"msg": "Password is incorect, try another one"}
    
    response = f'Welcome {log_data_extracted[1]}'

    payload = {"id": log_data_extracted[0],
               "exp": time.time()+900
               }
    token = jwt.encode(payload, JWT_SECRET_KEY, JWT_ALGORITHM)

    
    return {"msg": response, "JWT_Token": token}
    



@app.post("/identity/decode")
def decode(token):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return decoded_token, {"status":"Invalid"}
    except jwt.ExpiredSignatureError:
        return {"status":"Invalid"}



if __name__ == '__main__':
    create_db()
    uvicorn.run("main:app")





