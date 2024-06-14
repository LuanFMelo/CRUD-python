from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/GET")
async def get():
    return {"message": "GET something"}

@app.post("/POST")
async def post():
    return {"message": "GET something"}

@app.put("/PUT")
async def put():
    return {"message": "PUT something"}

@app.delete("/DELETE")
async def delete():
    return {"message": "DELETE something"}