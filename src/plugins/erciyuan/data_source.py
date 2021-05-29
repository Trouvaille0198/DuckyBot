from src.utils.request import get_text, get_bytes
import json
from random import choice


async def get_erciyuan():
    licking_url = 'https://api.mtyqx.cn/api/random.php?return=json'
    data = json.loads(
        await get_text(licking_url))
    print(data)
    if data['code'] == '200':
        return data['imgurl']
    else:
        return ''
