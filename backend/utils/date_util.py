#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/3 15:00
# @desc : 时间工具类
from datetime import datetime


def handle_datetime(time: datetime):
    """
    处理时间格式
    :param time: 带时区的时间
    :return: datetime类型
    """
    # 方法一
    # tz_time = datetime.strptime(str(time), "%Y-%m-%d %H:%M:%S.%f+08:00")
    # tz_time_str = tz_time.strftime("%Y-%m-%d %H:%M:%S")

    # 方法二
    # isoformat用法: https://vimsky.com/examples/usage/python-datetime-isoformat-method-with-example-02.html
    tz_time = time.replace(tzinfo=None)
    tz_time_str = tz_time.isoformat(" ", timespec='seconds')

    return tz_time_str
