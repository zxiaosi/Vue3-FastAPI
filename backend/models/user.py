#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/1 15:19
# @desc : 用户表
from enum import Enum

from tortoise import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import IntField, CharField, CharEnumField, DatetimeField

from models.base import Base
from utils.check_enum import MyEnumField
from utils.date_util import handle_datetime


class SexEnum(str, Enum):
    """ 性别枚举 """
    man = "1"
    woman = "0"


class User(Model):
    id = IntField(pk=True, index=True, description="编号")
    name = CharField(max_length=20, unique=True, description="用户名")
    sex: SexEnum = CharEnumField(SexEnum, default=SexEnum.man, description="性别 \n 1: 男 0: 女")
    # sex = MyEnumField(source_field="sex", enum_list=["1", "0"])
    created = DatetimeField(auto_now_add=True, description="创建时间")
    modified = DatetimeField(auto_now=True, description="修改时间")

    def gender(self) -> str:  # 返回类型一定要带
        return SexEnum(self.sex).name

    def created_at(self) -> str:
        return handle_datetime(self.created)

    def modified_at(self) -> str:
        return handle_datetime(self.modified)

    class PydanticMeta:
        computed = ["gender", "created_at", "modified_at"]
        exclude = ["created", "modified"]

    class Meta:
        table = "user"
        table_description = "用户表"


UserOut = pydantic_model_creator(User, name="User", exclude=tuple(["sex", ]))
UserIn = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
