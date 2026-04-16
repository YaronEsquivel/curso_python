import logging

from fastapi import Request

logger = logging.getLogger(__name__)


async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.url}")
    response = await call_next(request)
    return response
