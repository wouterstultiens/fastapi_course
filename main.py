from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {"title": "Exploring the Stars", "content": "Join us as we delve into the mysteries of the cosmos and uncover the secrets of distant galaxies.", "id": 1},
    {"title": "The Art of Cooking", "content": "Discover the joy of culinary creations with our step-by-step guides to mastering delicious recipes.", "id": 2}
]

def find_post(id: int):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/")
def read_root():
    return {"Hello": "Lil"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id):
    post = find_post(int(id))
    print(post)
    return {"data": post}

@app.post("/posts")
def create_post(post: Post):
    post_dict = dict(post)
    post_dict["id"] = randrange(0, 9999999)
    my_posts.append(post_dict)
    return {"data": post_dict}