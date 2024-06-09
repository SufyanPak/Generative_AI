from fastapi import FastAPI



app = FastAPI()

@app.get("/")
def Hellow_World():
    return {"Hello" : "World"}

@app.get("/pi")
def Hellow_World():
    return {"Hello" : "PIAIC"}

@app.post("/main")
def post(id:int, name:str, email:str):
    return {"Your Id ": id, "Name ": name, "and Email Add": email}
