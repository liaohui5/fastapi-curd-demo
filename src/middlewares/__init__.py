from fastapi.middleware.cors import CORSMiddleware
from src.shared.api_v1 import PUBLIC_API_LIST, API_V1_PREFIX
from src.shared.response_fmt import ResponseFmt
from src.shared.jwt import Jwt
from fastapi import Request


def init_middlewares(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    @app.middleware("http")
    async def auth(request: Request, call_next):
        # allow cors preflight requests to pass through without authentication
        if request.method.lower() == "options":
            return await call_next(request)

        # only check api_v1 prefix routes
        path = request.url.path
        if not path.startswith(API_V1_PREFIX):
            return await call_next(request)

        # allow public endpoints without authentication
        if path in PUBLIC_API_LIST:
            return await call_next(request)

        # check login status
        authorization = request.headers.get("Authorization")
        if not authorization:
            return ResponseFmt.failed("please login first", None, 401)

        # Bearer xxxx.xxxx.xxxx
        access_token = authorization[7:]
        payload = Jwt.parse_access_token(access_token)
        if payload is None:
            return ResponseFmt.failed(
                "Invalid accessToken, please login first", None, 401
            )

        return await call_next(request)
