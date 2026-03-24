from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "hello world"}

@app.get("/about")
def about():
    return {"message": "THis is about page"}

@app.get("/services")
def services():
    return {"message": "this is services page"}

@app.get("/contact")
def contact():
    return {"message": "this is contact page"}
