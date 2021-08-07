from loader import dp
from aiogram import types


@dp.message_handler()
async def echo(msg: types.Message):
    await msg.answer("Неизвестная команда, повторите ввод.\n/menu\n/help")
