import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.app.api import app as api_app
from src.app.service.references import BASE_DIR, PORT

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR.joinpath("static")), name="static")
app.mount("/api", api_app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=PORT, reload=False, workers=1)