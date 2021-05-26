# import nonebot
from nonebot import get_driver
from .config import Config
from nonebot.log import logger

from nonebot import on_command, on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

import json

global_config = get_driver().config
config = Config(**global_config.dict())

with open(r'src/assets/area.txt') as file_obj:
    areas = file_obj.read().split()

weather = on_regex("(天气)|(天气如何)|(天气怎么样)", rule=to_me(), priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):

    msg = str(event.get_message())  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    # await weather.send(cities[0]['cityName'])
    for area in areas:
        area = area[:-1] if (len(area) > 2) else area
        if area in msg:
            await weather.send(area)
            break

    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    if city not in ["上海", "北京"]:
        await weather.reject("你想查询的城市暂不支持，请重新输入！")
    city_weather = await get_weather(city)
    await weather.finish(city_weather)


async def get_weather(city: str):
    return f"{city}的天气是..."
