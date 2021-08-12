from src.utils.request import get_text, get_bytes
import json
from random import choice


async def get_setu(key: str):
    old_setu_url = 'https://api.lolicon.app/setu/?&r18=2&size1200=true'
    setu_url = 'https://api.lolicon.app/setu/v2/?&r18=2&size=regular'
    print(key)
    params = {
        "apikey": key
    }
    data = json.loads(
        await get_text(setu_url, params=params))
    print(data)
    if not data['error']:
        pic_url = data['data'][0]['urls']['regular']
        return pic_url
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
