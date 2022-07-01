#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/1 14:47
# @desc : 配置文件
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_DESC: str = "接口文档"  # 描述
    PROJECT_VERSION: int | str = 1.0  # 版本

    API_PREFIX: str = "/api"  # 接口前缀


settings = Settings()
