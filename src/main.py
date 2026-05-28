from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"status": "todo api is running"}