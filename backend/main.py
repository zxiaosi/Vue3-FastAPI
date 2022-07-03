#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/1 14:33
# @desc : 主函数
import uvicorn
from fastapi import FastAPI
from loguru import logger
from tortoise import Tortoise

from apis import debug
from core.config import settings
from models.user import User, SexEnum
from utils.file_util import get_models_file

app = FastAPI(title=settings.PRJ_DESC, version=settings.PRJ_VERSION)

app.include_router(debug.router, prefix=settings.API_PRE)


@app.on_event("startup")
async def startup_event():
    # https://github.com/tortoise/tortoise-orm/issues/872
    logger.success("💡💡💡 项目启动 💡💡💡")


    await Tortoise.init(db_url=settings.DB_URI,
                        modules={"models": get_models_file('models', ['base.py'])},
                        timezone=settings.DB_TZ)
    await Tortoise.generate_schemas()
    # 批量插入数据
    # await User.bulk_create([
    #     User(name="admin", sex=SexEnum.man),
    #     User(name="zxiaosi", sex=SexEnum.woman),
    # ])


@app.on_event("shutdown")
async def shutdown_event():
    await Tortoise.close_connections()
    logger.success("项目关闭")


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000)
    # uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True, debug=True, workers=5)
