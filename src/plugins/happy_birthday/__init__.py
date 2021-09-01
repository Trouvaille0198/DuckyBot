import datetime
import random
import nonebot
from nonebot import require  # 导入nonebot.require模块
from nonebot import get_driver
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
from .config import Config
from .data_source import birthdays
from nonebot.log import logger

global_config = get_driver().config
config = Config(**global_config.dict())


# 使用nonebot.require模块导入nonebot_plugin_apscheduler的scheduler
scheduler = require('nonebot_plugin_apscheduler').scheduler
# 设置在几点启动脚本


@scheduler.scheduled_job('cron', hour=1)
# 启动的脚本
async def run_every_1_hour():
    date_str = datetime.date.today().strftime("%m-%d")

    wishes = ["祝XXX生日快乐昂", "祝XXX先生福如东海寿比南山",
              "有请寿星XXX发一份生日涩图", "今天是XXX的生日，大家把这条消息发到朋友圈就可以获得寿星专属涩图两份",
              "XXX有无生日涩图特别企划？"]
    for b in birthdays:
        if b["birthday"] == date_str:
            bot = nonebot.get_bot()
            group_id = 920016259
            # group_id = 1041386205 # 测试群

            name = random.choice(b["name"]) if isinstance(
                b["name"], list) else b["name"]
            message = random.choice(wishes).replace('XXX', name)

            await bot.send_group_msg(group_id=group_id, message=message)
