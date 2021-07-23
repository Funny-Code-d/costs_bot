from aiogram.types import Message

#local imports
from loader import dp
from moduls.Keyboard_class import Keyboard


@dp.message_handler(commands=['menu', 'start'])
async def get_menu(message: Message):
	kb = Keyboard()
	kb.get_menu_keyboard()
	await message.reply("Выберите пункт", reply_markup=kb.reply_keyboard)