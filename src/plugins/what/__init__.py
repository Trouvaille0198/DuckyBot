# import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_command, on_regex, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent, MessageSegment, Message
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_what
from random import choice

global_config = get_driver().config
config = Config(**global_config.dict())

what = on_regex("(.*?)是[(什么)|嘛|啥][(意思)|梗]", permission=PRIVATE | GROUP)


@what.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    word = str(state["_matched_groups"][0])
    data = await get_what(word)
    for datum in data:
        await what.send(
            "梗词：{}\n梗解释：{}".format(datum['name'], datum['desc'])
        )
        if datum['imgurl']:
            img = MessageSegment.image(datum['imgurl'], proxy=False)
            await what.send(Message(img))
