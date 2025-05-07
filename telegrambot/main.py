import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile
from aiogram.filters.command import Command

from data import *




logging.basicConfig(level=logging.INFO)
bot = Bot("token")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Здравствуйте, введите логин")


@dp.message(F.text)
async def handler(message: types.Message):
    id = message.from_user.id
    text = message.text


    lastBM = await get_LBM(id)
    
    if await check_id(id) == 0 or lastBM == "Неправильно введен логин":
        await set_id(id)

        #реквест на апи на существование логина вапще 
        #Сценарий что существует(функция возращ 1)
        if request == 1:
            await set_login(id)

    else:
        await bot.send_message(id, "Неправильно введен логин, попробуйте еще раз")
        await set_LBM(id, "логин")



     

    if lastBM == None or lastBM == "неверный пароль":
        await bot.send_message(id, "введите пароль")
        await set_LBM(id, "пароль")
        #реквест на апи на правильность пароля
        if request == 1:
            login = get_login(id)
            get_tokens(login)
        else:
            await bot.send_message(id, "Неправильно введен пароль, попробуйте еще раз")
            await set_LBM(id, "неверный пароль")


    


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
