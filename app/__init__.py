from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.model import generate_models
from app.router import user as user_route, task as task_route, item as item_route

app = FastAPI()

generate_models()

app.include_router(router=user_route.router)
app.include_router(router=task_route.router)
app.include_router(router=item_route.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

if __name__ == "__main__":
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
