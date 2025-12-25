from pydantic import BaseModel
from fastapi import status
from fastapi.responses import JSONResponse
from typing import Any, Generic, TypeVar, Optional

# 定义泛型类型变量，用于data字段的类型安全
T = TypeVar("T")


# 基础响应结构
class ResponseStruct(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None


# 响应格式化工厂
class ResponseFmt:
    @staticmethod
    def success(
        data: Any = None,
        message: str = "success",
        status_code: int = status.HTTP_200_OK,
    ) -> JSONResponse:
        """创建成功的JSON响应"""
        response_model = ResponseStruct(success=True, message=message, data=data)
        return JSONResponse(
            content=response_model.model_dump(), status_code=status_code
        )

    @staticmethod
    def failed(
        message: str = "failed",
        data: Any = None,
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ) -> JSONResponse:
        """创建失败的JSON响应"""
        response_model = ResponseStruct(success=False, message=message, data=data)
        return JSONResponse(
            content=response_model.model_dump(), status_code=status_code
        )

    @staticmethod
    def error(
        message: str = "internal server error",
        data: Any = None,
    ) -> JSONResponse:
        """创建服务器错误的JSON响应"""
        return ResponseFmt.failed(
            message=message,
            data=data,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    @staticmethod
    def not_found(
        message: str = "Resource not found", data: Any = None
    ) -> JSONResponse:
        """创建服务器未找到资源响应"""
        return ResponseFmt.failed(
            message=message, data=data, status_code=status.HTTP_404_NOT_FOUND
        )

    @staticmethod
    def unauthorized(message: str = "Unauthorized") -> JSONResponse:
        """创建服务器登录验证错误响应"""
        return ResponseFmt.failed(
            message=message, status_code=status.HTTP_401_UNAUTHORIZED
        )
