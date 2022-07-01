#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/1 14:46
# @desc : 调试接口
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
