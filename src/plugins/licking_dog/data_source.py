from src.utils.request import get_text
import json
from random import choice


async def get_licking_dog():
    licking_url = 'https://api.muxiaoguo.cn/api/tiangourj'
    data = json.loads(
        await get_text(licking_url))
    if data['code'] == '200':
        return data['data']['comment']
    else:
        return choice('笑死，你舔我才对', '舔你🐎')
