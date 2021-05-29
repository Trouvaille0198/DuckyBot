# import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_command, on_regex, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent, MessageSegment, Message
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_erciyuan
from random import choice

global_config = get_driver().config
config = Config(**global_config.dict())

erciyuan = on_regex("纸片人|二次元", permission=PRIVATE | GROUP)


@erciyuan.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await erciyuan.send(choice(
        ('二刺螈是吧😅', '这就来', '笑死，狗都不发',
         '不是很懂你们二次元', '差点给你们整下雨了😅', '扎不多得嘞🥵')))
    erciyuan_url = await get_erciyuan()
    img = MessageSegment.image(erciyuan_url, proxy=False)
    await erciyuan.send(Message(img))
