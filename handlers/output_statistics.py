from aiogram.types import Message, ParseMode
from aiogram.dispatcher import FSMContext

#local imports
from loader import dp
from moduls.Keyboard_class import Keyboard
from moduls import expences


@dp.message_handler(lambda message: message.text.startswith('Вывести покупки за сегодня'))
async def get_statistics_day(message: Message):
	answer = expences.output_today_buy(message.from_user.id)
	if len(answer) > 4096:
    	for x in range(0, len(answer), 4096):
        	#bot.send_message(message.chat.id, info[x:x+4096])
        	await message.answer(answer[x:x+4096], parse_mode=ParseMode.MARKDOWN)
	else:
    	#bot.send_message(message.chat.id, info)
    	await message.answer(answer, parse_mode=ParseMode.MARKDOWN)
	#await message.answer(answer, parse_mode=ParseMode.MARKDOWN)

#--------------------------------------------------------------------------------------------

@dp.message_handler(lambda message: message.text.startswith('Вывести покупки за неделю'))
async def get_statistics_week(message: Message):
	answer = expences.output_week_buy(message.from_user.id)
	await message.answer(answer, parse_mode=ParseMode.MARKDOWN)
