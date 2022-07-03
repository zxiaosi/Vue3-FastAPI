#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/2 21:04
# @desc : 仿照tortoise-orm写的枚举
""" 本人太菜, 还待完善 """
from enum import Enum
from typing import Any, List, Union

from tortoise.fields import Field


class MyEnumField(Field[str], str):
    def __init__(self, enum_list: List, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.enum_list = enum_list
        print(f"字段名 {self.source_field}")

    @property
    def constraints(self) -> dict:
        return {"enum_list": self.enum_list}

    @property  # mysql, postgresql 的 enum 类型
    def SQL_TYPE(self) -> str:  # type: ignore
        return f"ENUM{tuple(self.enum_list)}"

    # class _db_oracle
    # class _db_mssql
    # class _db_mysql
    class _db_sqlite:  # 解决sqlite的check类型, 没生效。。。
        def __init__(self, field: "MyEnumField") -> None:
            self.field = field

        @property
        def SQL_TYPE(self) -> str:
            print(self.field.enum_list)
            return f"char(1) CHECK ({self.field.source_field} IN {tuple(self.field.enum_list)})"

    def to_python_value(self, value: Union[str, None]) -> Union[Enum, None]:
        self.validate(value)
        return value if value is not None else None

    def to_db_value(self, value: Union[Enum, None, str], instance: "Union[Type[Model], Model]") -> Union[str, None]:
        self.validate(value)
        if isinstance(value, str):
            return str(value)
        return value
