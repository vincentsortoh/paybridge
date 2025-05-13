import sys
from loguru import logger
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from asgi_correlation_id import correlation_id
from fastapi import FastAPI

from router import router


def configure_logger():

    def correlation_id_filter(record):
        record["correlation_id"] = correlation_id.get()
        return record["correlation_id"]

    logger.remove()
    logger.add(
        sys.stdout,
        level="INFO",
        format="[<cyan>{time:YYYY-MM-DD HH:mm:ss}</cyan> | <yellow>{level}</yellow> | <magenta>{correlation_id}</magenta> | <green>{function} </green> |{name}:{line}] ### {message}",
        filter=correlation_id_filter,
        colorize=True,
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logger()
    logger.info("Logger has been configured")
    yield
    logger.info("App is shutting down")


def create_app() -> FastAPI:
    tags_metadata = [
        {"name": "UBMI", "description": "Unified Bill Managment Interface"}
    ]

    app = FastAPI(
        lifespan=lifespan,
        openapi_tags=tags_metadata,
        debug=True,
        title="UBMI",
        summary="Unified API integration layer for collection and bill payment services",
        version="0.0.1",
        openapi_url="/openapi.json",
    )

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    return app


app = create_app()
