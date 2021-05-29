from src.utils.request import get_text
import json
from random import choice


async def get_rainbow_pi():
    rainbow_url = 'https://api.muxiaoguo.cn/api/caihongpi'
    data = json.loads(
        await get_text(rainbow_url))
    if data['code'] == '200':
        return data['data']['comment']
    else:
        return choice('累了，不想撒谎', '你给我放个？')
