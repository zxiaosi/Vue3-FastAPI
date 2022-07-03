#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/3 17:58
# @desc : 返回消息模型
from pydantic import BaseModel


class Status(BaseModel):
    message: str
