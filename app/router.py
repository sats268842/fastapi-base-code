from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

class ErrorMessage(BaseModel):
    msg: str


class ErrorResponse(BaseModel):
    detail: Optional[List[ErrorMessage]]


api_router = APIRouter(
    prefix="/v1",
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)

# api router
# api_router.include_router(field_type_router)


@api_router.get("/healthcheck", tags=["Health"])
def healthcheck():
    return {"status": "ok"}
