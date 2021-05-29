from src.utils.request import get_text
import json
from random import choice


async def get_boast(name: str):
    boast_url = 'https://el-bot-api.vercel.app/api/words/niubi'

    data = json.loads(
        await get_text(boast_url))
    if data:
        return data[0].replace(r'${name}', name)
    else:
        return ''
