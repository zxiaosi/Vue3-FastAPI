#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/1 16:20
# @desc : ORM抽象类
from tortoise import Model
from tortoise.fields import DatetimeField

from utils.date_util import handle_datetime


class Base(Model):
    created = DatetimeField(auto_now_add=True, description="创建时间")
    modified = DatetimeField(auto_now=True, description="修改时间")

    def created_at(self) -> str:  # 返回类型一定要带
        return handle_datetime(self.created)

    def modified_at(self) -> str:
        return handle_datetime(self.modified)

    class PydanticMeta:
        computed = ["created_at", "modified_at"]
        exclude = ["created", "modified"]

    class Meta:
        abstract = True  # 抽象类
