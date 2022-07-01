#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/1 14:33
# @desc : 主函数
import uvicorn
from fastapi import FastAPI
from loguru import logger

from apis import debug
from core.config import settings

app = FastAPI(title=settings.PROJECT_DESC, version=settings.PROJECT_VERSION)

app.include_router(debug.router)


@app.on_event("startup")
async def startup_event():
    logger.success('🎉🎉🎉 项目启动 🎉🎉🎉')


@app.on_event("shutdown")
async def shutdown_event():
    logger.success('项目关闭')


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000)
