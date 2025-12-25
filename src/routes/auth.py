from fastapi import Query, Body
from pydantic import BaseModel, Field
from src.shared.api_v1 import api_v1
from src.shared.response_fmt import ResponseFmt
from src.shared.tools import password_encode, password_verify
from src.shared.curd import Curd
from src.models import UserModel
from src.shared.jwt import Jwt


class LoginForm(BaseModel):
    account: str = Field(..., description="账号")
    password: str = Field(..., description="密码(md5)")


@api_v1.post("/register", description="登录")
async def register(
    data: LoginForm = Body(
        ...,
        description="注册数据",
        example={
            "account": "user1234@example.com",
            "password": "d41d8cd98f00b204e9800998ecf8427e",
        },
    ),
):
    password = password_encode(data.password)
    user_info = {
        "email": data.account,
        "password": password,
    }
    await Curd(UserModel).create(UserModel(**user_info))  # pyright: ignore[reportArgumentType]
    return ResponseFmt.success()


@api_v1.post("/login", description="登录")
async def login(
    data: LoginForm = Body(
        ...,
        description="登录数据",
        example={
            "account": "user-1@example.com",
            "password": "d41d8cd98f00b204e9800998ecf8427e",
        },
    ),
):
    user = await Curd(UserModel).find_one(
        {
            UserModel.email: data.account,
        }
    )
    if user is None:
        return ResponseFmt.failed("invalid account or password")

    if not password_verify(data.password, user.password):
        return ResponseFmt.failed("Invalid account or password!")

    access_token = Jwt.gen_access_token(user.id)
    refresh_token = Jwt.gen_refresh_token(user.id)

    result = user.dict()
    result["accessToken"] = access_token
    result["refreshToken"] = refresh_token
    return ResponseFmt.success(result)


@api_v1.get("/refresh_access_token")
async def refresh_access_token(
    refreshToken: str = Query(..., description="refresh token"),
):
    if not refreshToken:
        return ResponseFmt.failed("Invalid refresh token", None, 401)

    uid = Jwt.get_uid_from_refresh_token(refreshToken)
    if not uid:
        error = "Invalid refresh token or refresh token expired"
        return ResponseFmt.failed(error, None, 401)

    access_token = Jwt.gen_access_token(uid)
    return ResponseFmt.success({"accessToken": access_token})
