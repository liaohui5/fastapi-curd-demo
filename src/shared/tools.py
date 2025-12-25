import string
import random


def get_random_str(len: int = 10):
    """
    获取随机字符串: 包含大小写字母和数字
    """
    characters = string.ascii_letters + string.digits
    random_str = "".join(random.choices(characters, k=len))
    return random_str
