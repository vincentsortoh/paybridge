import time
from datetime import datetime
from typing import Callable
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.routing import APIRoute
from loguru import logger
from pydantic import BaseModel

from command_loader import load_and_execute


class CommandPayload(BaseModel):
    class Config:
        extra = "allow"


def to_human_date(epoch_time: str):
    return datetime.fromtimestamp(epoch_time).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            response: Response = await original_route_handler(request)
            after = time.time()
            duration = after - before
            response.headers["X-Response-Time"] = str(duration)
            logger.info(
                f"START:{to_human_date(before)} |FINISH:{to_human_date(after)} Process Duration: {duration}"
            )
            return response

        return custom_route_handler


router = APIRouter(
    prefix="/api/v1",
    tags=["gtwy"],
    route_class=TimedRoute,
    responses={404: {"description": "Not found"}},
)


@router.post("/api/{provider}/{command}")
async def run_command(provider: str, command: str, payload: CommandPayload):
    data = payload.model_dump()
    try:
        result = load_and_execute(provider, command, **data)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
