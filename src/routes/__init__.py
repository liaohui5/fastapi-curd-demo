from src.shared.api_v1 import api_v1


def init_routes(app):
    from src.routes import articles, auth

    app.include_router(api_v1)
