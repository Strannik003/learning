import fastapi, uvicorn, sqlite3, bcrypt, jwt, time, os, logging
from dotenv import load_dotenv
from pydantic import BaseModel, Field, EmailStr
from fastapi import Depends

app = fastapi.FastAPI()
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_ACCESS_TOKEN = os.getenv("JWT_ACCESS_TOKEN")

logging.basicConfig(level=logging.INFO,filename="log.log",filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

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
               email TEXT UNIQUE,
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
    cursor.execute("SELECT id, name, mail FROM users")
    export = cursor.fetchall()
    for row in export:
        result.append(row)
    return result

@app.post("/identity/reg")
def reg(request: RegRequest, connection_instance = Depends(connection_to_db)):
    connection, cursor = connection_instance
 
 
    byted_passoword = request.password.encode("utf-8")
    sol = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(byted_passoword,sol)

    try:
        cursor.execute("INSERT into users(name, age, email, password) VALUES (?,?,?,?)", (request.name, request.age, request.email, hashed_password.decode("utf-8")))
    except sqlite3.IntegrityError:
        logger.info("Registration failed: Email's already resistered")
        return {"msg": "Email's already resistered, try a new one"}


    cursor.execute("SELECT id from users WHERE email = ?", (request.email,))
    id_extracted = cursor.fetchone()

    connection.commit()

    logger.info(f'New user is added to database, user_id: {id_extracted[0]}')
    return {"msg":"New user is added to database"}



@app.post("/identity/sign-in")
def auth(request: LoginRequest, connection_instance = Depends(connection_to_db)):
    connection, cursor = connection_instance

    byted_passoword = request.password.encode("utf-8")


    cursor.execute("SELECT id, name, password FROM Users WHERE email = ?", (request.email, ))
    log_data_extracted = cursor.fetchone()
   
    
    if log_data_extracted is None:
        return {"msg": "The mail is incorect, try another one"}
    
    hashed_password = log_data_extracted[2]

    result = bcrypt.checkpw(byted_passoword, hashed_password= bytes(hashed_password,"utf-8"))

    
    if result is False:
        logger.info("Logging failed: incorrect password")
        return {"msg": "Password is incorect, try another one"}
    
    response = f'Welcome {log_data_extracted[1]}'

    payload_refresh = {"id": log_data_extracted[0],
               "type": "refresh",
               "exp": time.time()+604800
               }
    token_refresh = jwt.encode(payload_refresh, JWT_SECRET_KEY, JWT_ALGORITHM)

    payload_access = {"id": log_data_extracted[0],
                   "type": "access",
                   "exp": time.time()+900
                   }
    token_access = jwt.encode(payload_access,JWT_ACCESS_TOKEN, JWT_ALGORITHM)


    logger.info(f'Logging is succesful: user_id: {log_data_extracted[0]}')
    return {"msg": response, "Refresh Token": token_refresh, "Access token": token_access}


@app.post("/identity/decode")
def decode(access_token):
    try:
        decoded_token = jwt.decode(access_token, JWT_ACCESS_TOKEN, JWT_ALGORITHM)
        return decoded_token, {"status":"Valid"} 
    except jwt.ExpiredSignatureError:
        return {"status":"Invalid"}
    except jwt.InvalidTokenError:
        return {"msg":"Incorrect token"}

@app.post("/identity/refresh")
def refresh(refresh_token):
    try:
       decoded_token = jwt.decode(refresh_token, JWT_SECRET_KEY, JWT_ALGORITHM)
    except jwt.ExpiredSignatureError:
        return {"msg":"Refresh token is expired, log again"}
    except jwt.InvalidTokenError:
        return {"msg":"Incorrect toke"}

    
     
    payload_access = {"id": decoded_token["id"],
    "type": "access",
    "exp": time.time()+900}

    new_access_token = jwt.encode(payload_access,JWT_ACCESS_TOKEN, JWT_ALGORITHM)
    response = f'New refresh token: {new_access_token}'
    return {"msg": response}

        

    




if __name__ == '__main__':
    create_db()
    uvicorn.run("main:app",port=8001)






