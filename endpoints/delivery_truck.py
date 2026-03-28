from fastapi import APIRouter
from typing import List
import math

router = APIRouter()


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def tsp_recursive(points):
    n = len(points)
    visited = [False] * n

    best_path = []
    min_distance = float("inf")

    def backtrack(current, count, curr_distance, path):
        nonlocal min_distance, best_path

        # If all points visited, return to origin
        if count == n:
            total_dist = curr_distance + distance(current, (0, 0))
            if total_dist < min_distance:
                min_distance = total_dist
                best_path = path + [(0, 0)]
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                next_point = points[i]

                backtrack(
                    next_point,
                    count + 1,
                    curr_distance + distance(current, next_point),
                    path + [next_point],
                )

                visited[i] = False

    # Start from (0,0)
    backtrack((0, 0), 0, 0, [(0, 0)])

    return best_path, min_distance


@router.post("/optimal_route")
async def optimal_route(points: List[List[int]]):
    if len(points) > 12:
        return {
            "error": "Too many points for recursive solution (limit ~12)"
        }

    points_tuple = [tuple(p) for p in points]

    path, total_distance = tsp_recursive(points_tuple)

    return {
        "path": path,
        "total_distance": round(total_distance, 2)
    }
