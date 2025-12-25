import time
import jwt
from src.config import Config

# general token algorithm
GEN_TOKEN_ALGORITHM = "HS256"

# access token options
ACCESS_TOKEN_EXPIRE_TIME = Config.get_access_token_expire_time()
ACCESS_TOKEN_SECRET = Config.get_access_token_secret()

# refresh token options
REFRESH_TOKEN_EXPIRE_TIME = Config.get_refresh_token_expire_time()
REFRESH_TOKEN_SECRET = Config.get_refresh_token_secret()


def create_token(uid: int, expire_time: int, secret: str) -> str:
    return jwt.encode(
        {
            "uid": uid,
            "exp": int(time.time()) + expire_time,
        },
        secret,
        algorithm=GEN_TOKEN_ALGORITHM,
    )


def parse_token(token: str, secret: str) -> dict | None:
    try:
        return jwt.decode(token, secret, algorithms=GEN_TOKEN_ALGORITHM)
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception:
        return None


class Jwt:
    @staticmethod
    def gen_access_token(uid: int) -> str:
        return create_token(uid, ACCESS_TOKEN_EXPIRE_TIME, ACCESS_TOKEN_SECRET)

    @staticmethod
    def gen_refresh_token(uid: int) -> str:
        return create_token(uid, REFRESH_TOKEN_EXPIRE_TIME, REFRESH_TOKEN_SECRET)

    @staticmethod
    def parse_access_token(token: str) -> dict:
        return parse_token(token, ACCESS_TOKEN_SECRET)  # pyright: ignore[reportReturnType]

    @staticmethod
    def parse_refresh_token(token: str) -> dict:
        return parse_token(token, REFRESH_TOKEN_SECRET)  # pyright: ignore[reportReturnType]

    @staticmethod
    def get_uid_from_access_token(access_token: str) -> int | None:
        payload = parse_token(access_token, ACCESS_TOKEN_SECRET)
        if payload:
            return payload["uid"]

    @staticmethod
    def get_uid_from_refresh_token(refresh_token: str) -> int | None:
        payload = parse_token(refresh_token, REFRESH_TOKEN_SECRET)
        if payload:
            return payload["uid"]
