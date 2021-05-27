# import nonebot
from nonebot import get_driver
from .config import Config
from nonebot.log import logger

from nonebot import on_command, on_regex, on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_now_weather, areas

global_config = get_driver().config
config = Config(**global_config.dict())

# weather = on_regex('天气|气温|温度')

weather = on_keyword(('天气', '气温', '温度'), permission=PRIVATE)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    msg = str(event.get_message())
    for area in areas:
        area = area[:-1] if (len(area) > 2) else area
        if area in msg:
            state['location'] = area
            break


@weather.got("location", prompt="哪儿的天气呀？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    await weather.send('正在查询{}天气...'.format(state['location']))
    data = await get_now_weather(state['location'])
    await weather.send('{}天气{}，气温{}℃，{}{}级，相对湿度{}%'.format(
        state['location'], data['text'], data['temp'], data['windDir'], data['windScale'], data['humidity']))


# async def get_weather(city: str):
#     return f"{city}的天气是..."
