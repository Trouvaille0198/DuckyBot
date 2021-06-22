# import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_command, on_regex, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent, MessageSegment, Message
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_xiaojiejie
from random import choice

global_config = get_driver().config
config = Config(**global_config.dict())

xiaojiejie = on_regex("来(一?)[张份点个]小姐姐", permission=PRIVATE | GROUP)


@xiaojiejie.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    xiaojiejie_url = await get_xiaojiejie()
    await xiaojiejie.send("喏："+xiaojiejie_url)
    img = MessageSegment.image(file=xiaojiejie_url, proxy=False)
    await xiaojiejie.send(Message(img))

negative_comment = on_keyword(('一般', '普通', '就这'), permission=PRIVATE | GROUP)


@negative_comment.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await negative_comment.finish('那你来❤')
