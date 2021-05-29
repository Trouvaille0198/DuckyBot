from src.utils.request import get_text, get_bytes
import json
from random import choice


async def get_setu(key: str):
    setu_url = 'https://api.lolicon.app/setu/?&r18=2&size1200=true'
    print(key)
    params = {
        "apikey": key
    }
    data = json.loads(
        await get_text(setu_url, params=params))
    print(data)
    if data['code'] == 0:
        return data['data'][0]['url'].replace('png', 'jpg')
    else:
        return '达到次数限制'


async def get_setu2(key: str):
    setu_url = 'https://el-bot-api.vercel.app/api/setu'
    data = json.loads(
        await get_text(setu_url))
    print(data)
    if data:
        return data['url'].replace('png', 'jpg')
    else:
        return '达到次数限制'
