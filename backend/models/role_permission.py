#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/4 22:24
# @desc : 角色权限表
from tortoise import Model
from tortoise.fields import ForeignKeyRelation, ForeignKeyField

from models.permission import Permission
from models.role import Role


class RolePermission(Model):
    role_id: ForeignKeyRelation[Role] = ForeignKeyField(
        "models.Role",
        related_name="role_permission",
        description="角色id"
    )

    permission_id: ForeignKeyRelation[Permission] = ForeignKeyField(
        "models.Permission",
        related_name="role_permission",
        description="权限id"
    )

    class Meta:
        table = "role_permission"
        table_description = "角色权限表"
