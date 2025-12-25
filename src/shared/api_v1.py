from fastapi import APIRouter

# 所有路由的公共前缀
API_V1_PREFIX = "/api/v1"


PUBLIC_API_LIST = [
    f"{API_V1_PREFIX}/login",
    f"{API_V1_PREFIX}/register",
    f"{API_V1_PREFIX}/refresh_access_token",
]

# tags:用于接口文档的分组标签
api_v1 = APIRouter(prefix=API_V1_PREFIX, tags=["v1"])
