from src.utils.request import get_text, get_bytes
import json
from random import choice


async def get_what(word: str):
    what_url = 'https://api.muxiaoguo.cn/api/hybrid'
    print(word)
    params = {
        "word": word
    }
    data = json.loads(
        await get_text(what_url, params=params))
    if data['code'] == 200:
        return data['data']
    else:
        return ''
