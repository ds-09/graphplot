from fastapi import FastAPI, HTTPException
import re
import mysql.connector
from pydantic import BaseModel, EmailStr
import bcrypt

app=FastAPI()

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str

"""def validate_email(email: str) -> bool:
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
"""
def get_db():
    conn= mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="UserData"
    )
    return conn

@app.post("/register")
def register_user(user: UserCreate):
    if not validate_email(user.email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    conn=get_db()
    cursor=conn.cursor()

    values="INSERT INTO users (username, email, password)  VALUES (%s, %s, %s)"
    values=(user.username, user.email, hashed_password.decode("utf-8"))
    cursor.execute(query, values)

    conn.commit()

    return {"message": "User created succesfully"}

@app.post("/login")
def authenticate_user(username: str, password: str):
    conn= get_db()
    cursor= conn.cursor()
    query="SELECT * FROM users WHERE username = %s"
    values=(username,)
    cursor.execute(query, values)
    user= curson.fetchone()

    if user is None or not bcrypt.checkpw(password.encode("utf-8"), user[2].encode("utf-8")):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": "Login successful"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port="8000")