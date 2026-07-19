import fastapi, uvicorn, sqlite3
import bcrypt
from pydantic import BaseModel, Field, EmailStr

app = fastapi.FastAPI()

class RegRequest(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    age: int = Field(ge=18,le=120)
    email: EmailStr 
    password: str = Field(min_length=8)


class LoginRequest(BaseModel):
    email: EmailStr 
    password: str = Field(min_length=8)



@app.post("/identity/reg")
def reg(request: RegRequest):

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM users WHERE email = ?", (request.email, ))
    user_exists = cursor.fetchone()
    if user_exists:
        return {"msg":"Email's already resistered, try a new one"}
    
    
    Byted_passoword = request.password.encode("utf-8")
    sol = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(Byted_passoword,sol)

   
    cursor.execute("INSERT into users(name, age, email, password) VALUES (?,?,?,?)", (request.name, request.age, request.email, hashed_password))
    connection.commit()
    
    return {"msg":"New user is added to database"}




@app.post("/identity/sign-in")
def auth(request: LoginRequest):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    Byted_passoword = request.password.encode("utf-8")



    cursor.execute("SELECT name, password FROM Users WHERE email = ?", (request.email, ))
    Log_Data_extracted = cursor.fetchall()
   
    
    if Log_Data_extracted == []:
        return {"msg": "The mail is incorect, try another one"}
    

    result = bcrypt.checkpw(Byted_passoword, Log_Data_extracted[0][1])
    responce = f'Welcome {Log_Data_extracted[0][0]}'

    if result:
        return {"msg": responce}







if __name__ == '__main__':
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               email TEXT,
               password BINARY
               ) """)
    

    uvicorn.run("main:app")





