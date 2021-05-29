# import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_command, on_regex, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_rainbow_pi

global_config = get_driver().config
config = Config(**global_config.dict())

rainbow_pi = on_regex("夸(一?)[夸下波]|放(一?)[个放]彩虹屁", permission=PRIVATE | GROUP)


@rainbow_pi.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    rainbow_sentence = await get_rainbow_pi()
    await rainbow_pi.send(rainbow_sentence)
