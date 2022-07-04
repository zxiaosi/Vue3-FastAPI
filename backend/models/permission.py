#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/4 22:06
# @desc : 权限表
from tortoise.fields import IntField, CharField, ReverseRelation

from models.base import Base


class Permission(Base):
    name = CharField(max_length=30, unique=True, description="菜单名")
    pid = IntField(description="父级id")
    code = CharField(max_length=20, description="权限编号")
    page = CharField(max_length=50, description="菜单url")
    z_index = IntField(description="排序")

    role_permission = ReverseRelation["models.role_permission"]

    class Meta:
        table = "permission"
        table_description = "权限表"
