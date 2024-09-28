from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import base, video

app = FastAPI()

# Настройка CORS
origins = [
    "http://localhost:3000",  # Добавьте сюда все необходимые источники
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты
app.include_router(base.router)
app.include_router(video.router)
