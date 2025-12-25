import string
import random
import bcrypt


def get_random_str(len: int = 10):
    """
    获取随机字符串: 包含大小写字母和数字
    """
    characters = string.ascii_letters + string.digits
    random_str = "".join(random.choices(characters, k=len))
    return random_str


def password_encode(password: str) -> str:
    """
    bcrypt 加密密码字符串
    """
    password_bytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode("utf-8")


def password_verify(origin_password: str, hashed_password: str) -> bool:
    """
    对比加密后的密码字符串
    """
    password_bytes = origin_password.encode("utf-8")
    hashed_password_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)
