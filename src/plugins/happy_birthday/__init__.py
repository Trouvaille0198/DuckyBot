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


@scheduler.scheduled_job('cron', second='5')
# 启动的脚本
async def run_every_1_hour():
    date_str = datetime.date.today().strftime("%m-%d")
    logger.debug(date_str)
    wishes = ["祝XXX生日快乐昂", "沙口XXX生日快乐"]
    for b in birthdays:
        if b["birthday"] == date_str:
            # 获取bot的id
            bot = nonebot.get_bot()
            # driver = get_driver()
            # BOT_ID = str(driver.config.bot_id)
            # logger.debug(BOT_ID)
            # bot = driver.bots[BOT_ID]

            # group_id = 920016259  # 这里写群号
            group_id = 1041386205
            message = random.choice(wishes).replace('XXX', b["name"])
            logger.debug(message)
            await bot.send_group_msg(group_id=group_id, message="测试消息")
