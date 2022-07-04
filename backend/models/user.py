#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/1 15:19
# @desc : 用户表
from enum import Enum

from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import IntField, CharField, CharEnumField, SmallIntField, ReverseRelation

from models.base import Base


class SexEnum(str, Enum):
    """ 性别枚举 """
    man = "1"
    woman = "0"


class User(Base):
    name = CharField(max_length=20, unique=True, description="用户名")
    sex: SexEnum = CharEnumField(SexEnum, default=SexEnum.man, description="性别 1: 男 0: 女")
    phone = CharField(max_length=11, description="手机号")
    email = CharField(max_length=50, description="邮箱")
    password = CharField(max_length=60, description="密码")
    is_del = SmallIntField(default=0, description="是否删除 0: 正常 1: 已删")

    user_role = ReverseRelation["models.user_role"]

    def gender(self) -> str:  # 返回类型一定要带
        return SexEnum(self.sex).name

    class PydanticMeta:
        computed = ["gender"]

    class Meta:
        table = "user"
        table_description = "用户表"


UserOut = pydantic_model_creator(User, name="User", exclude=tuple(["sex", ]))
UserIn = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
