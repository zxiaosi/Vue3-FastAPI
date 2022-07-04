#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/4 22:00
# @desc : 角色表
from tortoise.fields import CharField, ReverseRelation

from models.base import Base


class Role(Base):
    name = CharField(max_length=30, unique=True, description="角色名")
    desc = CharField(max_length=50, description="描述")
    code = CharField(max_length=20, description="角色编号")

    user_role = ReverseRelation["models.user_role"]
    role_permission = ReverseRelation["models.role_permission"]

    class Meta:
        table = "role"
        table_description = "角色表"
