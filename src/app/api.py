from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import *

from src.app.service.references import VERSION

app = FastAPI()


@app.post("/")
@app.post("/team")
async def team():
    return JSONResponse(content={"vendor": "pjlab", "version": VERSION, "available_apis": [
        "text2img", "img2img", "inpaint", "img2text", "help"
    ]})


@app.post("/help")
async def help_api(route: str):
    return JSONResponse(content={})


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
