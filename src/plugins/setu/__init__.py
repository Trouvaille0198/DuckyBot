# import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_command, on_regex, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent, MessageSegment, Message
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_setu
from random import choice

global_config = get_driver().config
config = Config(**global_config.dict())

setu = on_regex("来(一?)[张份个波点][色涩射蛇🐍][图的🤮]", permission=PRIVATE | GROUP)


@setu.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await setu.send(choice(('来咯', '别急，来了', '这就冲')))
    setu_url = await get_setu(key=choice(global_config.setu_key))
    print(global_config.setu_key)
    if setu_url == '达到次数限制':
        await setu.finish(choice(('冲太多了，下次再来吧', '色图容量不足!')))
    else:
        await setu.send("喏："+setu_url)
        img = MessageSegment.image(setu_url, proxy=False)
        await setu.send(Message(img))
