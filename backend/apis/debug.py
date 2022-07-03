#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : zxiaosi
# @Time : 2022/7/1 14:46
# @desc : 调试接口
from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError

from models.user import User, UserIn, UserOut
from schemas.result import Status

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.get("/user/", response_model=List[UserOut])
async def get_users():
    return await UserOut.from_queryset(User.all())


@router.post("/user/create", response_model=UserOut)
async def create_user(user: UserIn):
    result = await User.create(**user.dict(exclude_unset=True))
    return await UserOut.from_tortoise_orm(result)


@router.get("/user/{user_id}", response_model=UserOut, responses={404: {"model": HTTPNotFoundError}})
async def get_user(user_id: int):
    return await UserOut.from_queryset_single(User.get(id=user_id))


@router.put("/user/{user_id}", response_model=UserOut, responses={404: {"model": HTTPNotFoundError}})
async def update_users(user_id: int, user: UserIn):
    await User.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await UserOut.from_queryset_single(User.get(id=user_id))


@router.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
