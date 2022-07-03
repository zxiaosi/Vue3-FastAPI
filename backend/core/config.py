#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/1 14:47
# @desc : 配置文件
from pydantic import BaseSettings


class Settings(BaseSettings):
    PRJ_DESC: str = "接口文档"  # 描述
    PRJ_VERSION: int | str = 1.0  # 版本

    API_PRE: str = "/api"  # 接口前缀
    DB_URI: str = "mysql://root:123456@localhost:3306/demo?charset=utf8"  # MySQL
    DB_TZ: str = "Asia/Shanghai"  # 时区

    class Config:
        case_sensitive = True  # 区分大小写


settings = Settings()
