from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router

app = FastAPI(
    title="PAL Trading Buddy API",
    version="1.0.0",
    description="PAL Trading Buddy Backend",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "name": "PAL Trading Buddy",
        "version": "1.0.0",
        "status": "Running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }