from src.utils.request import get_text, get_bytes
import json
from random import choice


async def get_xiaojiejie():
    licking_url = 'https://api.muxiaoguo.cn/api/meinvtu?num=1'
    data = json.loads(
        await get_text(licking_url))
    print(data)
    if data['code'] == 200:
        return data['data'][0]['imgurl']
    else:
        return choice(('无了'))
