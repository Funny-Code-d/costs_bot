from aiogram import executor
from aiogram.dispatcher import FSMContext
from loader import dp
import handlers, moduls
#from utils.notify_admins import on_startup_notify
from utils.bot_commands import set_default_commands


async def on_startup(dispatcher):
   # Устанавливаем дефолтные команды
   await set_default_commands(dispatcher)

#    # Уведомляет про запуск
#    await on_startup_notify(dispatcher)
#

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
