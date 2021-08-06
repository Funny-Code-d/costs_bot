from aiogram.types import Message, ParseMode
from aiogram.dispatcher import FSMContext

#local imports
from loader import dp
from loader import kb
from moduls import expences
from moduls.Question import out_statictics

@dp.message_handler(lambda message: message.text.startswith('Вывести покупки за сегодня'))
async def get_statistics_day(message: Message, state: FSMContext):
	await state.update_data({'interval' : "today"})
	kb.kb_out_buy()
	await message.reply("Выберите тип", reply_markup=kb.reply_keyboard)
	await out_statictics.type_out.set()




@dp.message_handler(lambda message: message.text.startswith('Вывести покупки за неделю'))
async def get_statistics_week(message: Message, state: FSMContext):
	await state.update_data({'interval' : "week"})
	kb.kb_out_buy()
	await message.reply("Выберите тип", reply_markup=kb.reply_keyboard)
	await out_statictics.type_out.set()



@dp.message_handler(lambda message: message.text.startswith("Вывести покупки за месяц"))
async def get_statistics_month(message: Message, state: FSMContext):
	kb.kb_list_month(message.from_user.id)
	await message.answer("Выберите месяц", reply_markup=kb.reply_keyboard)
	await out_statictics.choise_month.set()
	# await state.update_data({'interval' : "month"})
	# kb.kb_out_buy()
	# await message.reply("Выберите тип", reply_markup=kb.reply_keyboard)
	# await out_statictics.type_out.set()

@dp.message_handler(state = out_statictics.type_out)
async def get_output(message: Message, state: FSMContext):
	
	if message.text in ("Краткий", "Подробный"):
	
		data = await state.get_data()
		interval = data.get("interval")
	
		if message.text == 'Краткий':
			answer = expences.output_buy_short(message.from_user.id, interval)
	
		else:
			answer = expences.output_buy_long(message.from_user.id, interval)
		kb.get_menu_keyboard()
		for a in answer:
			await message.answer(a, reply_markup=kb.reply_keyboard, parse_mode=ParseMode.MARKDOWN)
		await state.finish()
	
	else:
		await message.answer("Повторите ввод, выберите из клавиатуры бота")
		return


@dp.message_handler(state = out_statictics.choise_month)
async def get_statistics_month_step_2(message: Message, state: FSMContext):
	if message.text in expences.get_month_list(message.from_user.id):
		month = message.text
		answer = expences.get_month_out_buy(message.from_user.id, month)
		kb.get_menu_keyboard()
		for a in answer:
			await message.answer(a, reply_markup=kb.reply_keyboard, parse_mode=ParseMode.MARKDOWN)
		await state.finish()
	elif message.text == "Отмена":
		kb.get_menu_keyboard()
		await message.answer("Выберите пункт меню", reply_mutkup=kb.reply_keyboard)
	else:
		await message.answer("Повторите, выберите из клавиатуры бота")