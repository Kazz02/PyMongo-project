from fastapi import FastAPI

app = FastAPI()

#  "@app.get" tells FastAPI that this function handles GET requests to the URL "/"
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

