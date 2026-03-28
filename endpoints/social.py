from fastapi import APIRouter, Header
from typing import List, Dict


router = APIRouter()

# Storing Posts in a array for simplicity
posts: List[Dict] = []


@router.post("/add_post")
async def add_post(
    comment: int = Header(...),
    views: int = Header(...),
    likes: int = Header(...),
    category: str = Header(...),
    description: str = Header(...)
):
    post = {
        "comment": comment,
        "views": views,
        "likes": likes,
        "category": category,
        "description": description
    }

    posts.append(post)

    return {
        "message": "Post stored successfully",
        "total_posts": len(posts)
    }


@router.get("/top_posts")
async def get_top_posts(category: str):
    # Filter posts by category
    filtered_posts = [p for p in posts if p["category"] == category]

    if not filtered_posts:
        return {
            "category": category,
            "top_posts": []
        }

    # Sort by (likes + comments + views)
    sorted_posts = sorted(
        filtered_posts,
        key=lambda x: x["likes"] + x["comment"] + x["views"],
        reverse=True
    )

    return {
        "category": category,
        "top_posts": sorted_posts[:20]
    }
