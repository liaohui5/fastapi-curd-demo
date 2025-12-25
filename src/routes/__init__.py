from src.shared.api_v1 import api_v1
from src.shared.response_fmt import ResponseFmt, ResponseStruct


def init_routes(app):
    @app.get("/", response_model=ResponseStruct[str])
    def ping():
        return ResponseFmt.success("server is running")

    # load routes
    from src.routes import articles, auth

    app.include_router(api_v1)
