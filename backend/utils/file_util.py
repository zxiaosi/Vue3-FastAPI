#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/3 16:28
# @desc : 文件工具类
import os
from typing import List

from loguru import logger


def get_models_file(dir_name: str, exclude: List = []) -> List:
    """
    获取models目录下的 .py 文件
    :return: 文件列表 eg: [models.user.py, models.user_in.py]
    """
    current_path = os.path.dirname(__file__)  # 获取当前文件夹
    models_path = os.path.abspath(os.path.join(current_path, "..", dir_name))  # 获取当前文件夹的上一层文件

    try:
        file_list = []
        for file in os.listdir(models_path):
            # 下面可简写
            if file == '__pycache__' or file == '__init__.py':
                continue
            if file in exclude:
                continue
            if file.endswith('.py'):
                file_list.append(f"{dir_name}.{file[:-3]}")
        return file_list
    except Exception as e:
        logger.error(f"获取{dir_name}目录失败 -- {e}")
        return []
