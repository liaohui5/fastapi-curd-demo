from fastapi import APIRouter

# 所有路由的公共前缀
API_V1_PREFIX = "/api/v1"

# tags:用于接口文档的分组标签
api_v1 = APIRouter(prefix=API_V1_PREFIX, tags=["v1"])
