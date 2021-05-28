# import nonebot
from nonebot import get_driver
from .config import Config
from nonebot.log import logger

from nonebot import on_command, on_regex, on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_now_weather, areas, is_location, get_tomorrow_forcast
import re

global_config = get_driver().config
config = Config(**global_config.dict())


weather = on_keyword(('天气', '气温', '温度', '今天下雨'), permission=PRIVATE)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    msg = str(event.get_message())
    if any(keyword in msg for keyword in ('明天', '明日')):
        state['forecast'] = '明日'
    elif any(keyword in msg for keyword in ('今天', '今日')):
        state['forecast'] = '今日'
    else:
        state['forecast'] = None
    area = is_location(msg, areas)
    if area:
        state['location'] = area


@weather.got("location", prompt="哪儿的天气呀？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    msg = str(event.get_message())
    if any(keyword in msg for keyword in ('了', '不')):
        await weather.finish('那告辞')

    area = is_location(msg, areas)
    if area:
        state['location'] = area
    else:
        await weather.reject('{}是哪儿鸭, 我好像不认识...'.format(msg))

    if state['forecast']:
        await weather.send('正在查询{}{}天气...'.format(state['location'], state['forecast']))
        data = await get_tomorrow_forcast(state['location'], state['forecast'], key=global_config.weather_key)
        if data:
            await weather.send(
                '{}{}天气预报:\n气温 {}℃-{}℃\n白天{}，夜间{}\n相对湿度{}%\n云量{}%'
                .format(state['location'], state['forecast'],
                        data['tempMax'], data['tempMin'],
                        data['textDay'], data['textNight'],
                        data['humidity'], data['cloud']))
        else:
            await weather.finish('好像出了一点问题...再试一遍叭')
    else:
        await weather.send('正在查询{}实时天气...'.format(state['location']))
        data = await get_now_weather(state['location'], key=global_config.weather_key)
        if data:
            await weather.send('{}天气{}，气温{}℃，{}{}级，相对湿度{}%'.format(
                state['location'], data['text'], data['temp'],
                data['windDir'], data['windScale'], data['humidity']))
        else:
            await weather.finish('好像出了一点问题...再试一遍叭')
