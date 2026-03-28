import uvicorn
from fastapi import FastAPI
from endpoints import router

app = FastAPI()

app.include_router(router)


@app.get("/health", tags=["Health Check"])
async def health():
    return {"status": "Healthy"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=5000,
        reload=False,
    )
