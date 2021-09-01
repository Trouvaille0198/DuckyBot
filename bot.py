#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
from nonebot.log import logger, default_format

# logger.add(r"logs/error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)


nonebot.init()
app = nonebot.get_asgi()


# 定时器配置
nonebot.init(apscheduler_autostart=True)
nonebot.init(apscheduler_config={
    "apscheduler.timezone": "Asia/Shanghai"
})

driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)

# nonebot.load_builtin_plugins()
nonebot.load_from_toml("pyproject.toml")
nonebot.load_plugins('src/plugins')  # 加载插件目录
# nonebot.load_plugin("src.plugins.weather")  # 加载单个插件


if __name__ == "__main__":
    nonebot.logger.warning(
        "Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
