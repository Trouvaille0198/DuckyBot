# import nonebot
from nonebot import get_driver
from .config import Config

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event


matcher = on_command("test", rule=to_me(), priority=2)


@matcher.args_parser
# 修改默认参数处理
async def parse(bot: Bot, event: Event, state: T_State):
    # 让got只接受再次输入的第一个参数
    state[state["_current_key"]] = str(event.get_message()).split()[0]


@matcher.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).split()
    if args:
        # state['has_arg'] = 'true'
        for arg in args:
            state[str(arg)] = arg  # 如果用户发送了参数则直接赋值
        await matcher.finish('The args you send: ' + ', '.join([arg for arg in args]))


@matcher.got("has_arg", prompt="You didn't give a arg")
async def handle_city(bot: Bot, event: Event, state: T_State):
    await matcher.send('The arg you give is: ' + state['has_arg'])
    if state['has_arg'] not in ['a']:
        await matcher.reject('The arg must be "a", plz try again!')
    else:
        await matcher.finish('You\'ve given a right arg! How smart r u ~')
