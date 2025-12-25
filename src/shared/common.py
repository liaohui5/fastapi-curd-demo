from fastapi import Query


def parse_pagination_query(
    page: int = Query(default=1, ge=1), limit: int = Query(default=10, ge=10, le=50)
):
    """
    解析分页参数
    """
    return {
        "page": page,
        "limit": limit,
    }
