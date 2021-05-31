# import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_command, on_regex, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_dirty_words


global_config = get_driver().config
config = Config(**global_config.dict())

dirty_word = on_keyword(('垃圾话', '对线', '嘴臭'), permission=PRIVATE | GROUP)


@dirty_word.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await dirty_word.send('来嗷')


@dirty_word.receive()
async def send_dirty_words(bot: Bot, event: Event, state: T_State):
    msg = str(event.get_message())
    if msg != '结束':
        await dirty_word.reject(get_dirty_words())
    else:
        await dirty_word.finish('骂不过我, 溜了溜了')
