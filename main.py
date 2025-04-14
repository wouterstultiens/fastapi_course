from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
def read_root():
    return {"Hello": "Lil"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createpost")
def create_post(post: Post):
    return {"new_post": f"title: {post.title}, content: {post.content}"}