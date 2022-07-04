#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/4 22:15
# @desc : 用户角色表
from tortoise import Model
from tortoise.fields import ForeignKeyRelation, ForeignKeyField

from models.role import Role
from models.user import User


class UserRole(Model):
    user_id: ForeignKeyRelation[User] = ForeignKeyField(
        "models.User",
        related_name="user_role",
        description="用户id"
    )

    role_id: ForeignKeyRelation[Role] = ForeignKeyField(
        "models.Role",
        related_name="user_role",
        description="角色id"
    )

    class Meta:
        table = "user_role"
        table_description = "用户角色表"
