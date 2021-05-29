# import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_command, on_regex, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent
from nonebot.adapters.cqhttp.permission import PRIVATE, GROUP

from .data_source import get_licking_dog

global_config = get_driver().config
config = Config(**global_config.dict())

licking_dog = on_regex("舔(.*?)一[舔下哈波]|(舔我)", permission=PRIVATE | GROUP)


@licking_dog.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    licking_sentence = await get_licking_dog()
    await licking_dog.send(licking_sentence)
