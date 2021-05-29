# import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_command, on_regex, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent, MessageSegment, Message
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_boast
from random import choice

global_config = get_driver().config
config = Config(**global_config.dict())

boast = on_regex("给(.*?)吹个牛逼", permission=PRIVATE | GROUP)


@boast.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    name = state["_matched_groups"][0]
    data = await get_boast(name)
    await boast.finish(data)
