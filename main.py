from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Lil"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}