from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status
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

def find_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i, p

@app.get("/")
def read_root():
    return {"Hello": "Lil"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    _, post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Post with id {id} not found"
        )
    return {"data": post}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = dict(post)
    post_dict["id"] = randrange(0, 9999999)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    _, post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"Post with id {id} was not found"
        )
    my_posts.remove(post)

@app.put("/posts/{id}", status_code=status.HTTP_201_CREATED)
def update_post(id: int, post: Post):
    post_dict = dict(post)
    index, _ = find_post(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"Post with id {id} was not found"
        )
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}