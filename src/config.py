def parse_int(v: str | int | None, default_v: int) -> int:
    return int(v) if v else default_v


def parse_bool(v: str | None, default_v: bool) -> bool:
    if not v:
        return False
    str = v.lower()
    if str in ["true", "1", "yes", "on"]:
        return True  # true
    elif str in ["false", "0", "no", "off"]:
        return False  # false
    else:
        return default_v


class Config:
    # app
    APP_DEBUG = None
    APP_CORS = None
    APP_PORT = None

    # jwt
    ACCESS_TOKEN_EXPIRE_TIME = None
    REFRESH_TOKEN_EXPIRE_TIME = None
    ACCESS_TOKEN_SECRET = None
    REFRESH_TOKEN_SECRET = None

    # database
    DB_URL = None

    @staticmethod
    def load_env(env: dict):
        for key, value in env.items():
            setattr(Config, key, value)

    @staticmethod
    def get_app_port() -> int:
        return parse_int(Config.APP_PORT, 8000)

    @staticmethod
    def is_cors_mode() -> bool:
        print(f"========\nAPP_CORS: {Config.APP_CORS}")
        return parse_bool(Config.APP_CORS, True)

    @staticmethod
    def is_debug_mode() -> bool:
        return parse_bool(Config.APP_DEBUG, False)

    @staticmethod
    def get_access_token_expire_time() -> int:
        return parse_int(Config.ACCESS_TOKEN_EXPIRE_TIME, 60)

    @staticmethod
    def get_refresh_token_expire_time() -> int:
        return parse_int(Config.REFRESH_TOKEN_EXPIRE_TIME, 7 * 24 * 60 * 60)  # 7days

    @staticmethod
    def get_access_token_secret() -> str:
        return Config.ACCESS_TOKEN_SECRET or "d3157a5812d456910c9b26a1647963bf"

    @staticmethod
    def get_refresh_token_secret() -> str:
        return Config.REFRESH_TOKEN_SECRET or "ed71580c1d2f1d7c5c49278f20e136c5"

    @staticmethod
    def get_db_url() -> str:
        if not Config.DB_URL:
            raise ValueError("DB_URL is required")
        return Config.DB_URL
