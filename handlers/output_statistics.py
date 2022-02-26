from aiogram.types import Message, ParseMode
from aiogram.dispatcher import FSMContext

#local imports
from loader import dp
from loader import kb as keyboard
from moduls.expences import GetInfoPurchases
from moduls.Question import out_statictics, display_statistics

# @dp.message_handler(lambda message: message.text.startswith('Вывести покупки за сегодня'))
# async def get_statistics_day(message: Message, state: FSMContext):
# 	await state.update_data({'interval' : "today"})
# 	keyboard.kb_out_buy()
# 	await message.reply("Выберите тип", reply_markup=keyboard())
# 	await out_statictics.type_out.set()




# @dp.message_handler(lambda message: message.text.startswith('Вывести покупки за неделю'))
# async def get_statistics_week(message: Message, state: FSMContext):
# 	await state.update_data({'interval' : "week"})
# 	keyboard.kb_out_buy()
# 	await message.reply("Выберите тип", reply_markup=keyboard())
# 	await out_statictics.type_out.set()



# @dp.message_handler(lambda message: message.text.startswith("Вывести покупки за месяц"))
# async def get_statistics_month(message: Message, state: FSMContext):
# 	keyboard.kb_list_month(message.from_user.id)
# 	await message.answer("Выберите месяц", reply_markup=keyboard())
# 	await out_statictics.choise_month.set()



# @dp.message_handler(state = out_statictics.type_out)
# async def get_output(message: Message, state: FSMContext):
	
# 	if message.text in ("Краткий", "Подробный"):
	
# 		data = await state.get_data()
# 		interval = data.get("interval")
	
# 		if message.text == 'Краткий':
# 			answer = GetInfoPurchases.OutputBuyShort(message.from_user.id, interval)
	
# 		else:
# 			answer = GetInfoPurchases.OutputBuyLong(message.from_user.id, interval)
# 		keyboard.get_menu_keyboard()
# 		for a in answer:
# 			await message.answer(a, reply_markup=keyboard(), parse_mode=ParseMode.MARKDOWN)
# 		await state.finish()
	
# 	else:
# 		await message.answer("Повторите ввод, выберите из клавиатуры бота")
# 		return


# @dp.message_handler(state = display_statistics.choiseMonth)
# async def get_statistics_month_step_2(message: Message, state: FSMContext):
# 	if message.text in GetInfoPurchases.GetMonthList(message.from_user.id):
# 		month = message.text
# 		answer = GetInfoPurchases.GetMonthPurchases(message.from_user.id, month)
# 		keyboard.get_menu_keyboard()
# 		for a in answer:
# 			await message.answer(a, reply_markup=keyboard(), parse_mode=ParseMode.MARKDOWN)
# 		await state.finish()
# 	elif message.text == "Отмена":
# 		keyboard.get_menu_keyboard()
# 		await message.answer("Выберите пункт меню", reply_markup=keyboard())
# 		await state.finish()
# 	else:
# 		await message.answer("Повторите, выберите из клавиатуры бота")




@dp.message_handler(lambda message: message.text.startswith('Вывод покупок'))
async def start_output(message: Message, state: FSMContext):
	keyboard.createKeyboardList(("Общий вывод", "По шаблону", "Настроить шаблоны", "Помощь"))
	await message.answer("Выберите:", reply_markup=keyboard())
	await display_statistics.actionChoice.set()
 

@dp.message_handler(state = display_statistics.actionChoice)
async def funcChoiceAction(message: Message, state: FSMContext):
	userChoice = message.text
	
	if userChoice == "Общий вывод":
		# keyboard.kb_list_month(message.from_user.id)
		keyboard.createKeyboardList(("Сегодня", "Неделя", "Месяц"))
		await message.answer("Выберите интервал:", reply_markup=keyboard())
		await display_statistics.choiseIntervalGeneralDisplay.set()

	elif userChoice == "По шаблону":
		pass
	elif userChoice == "Настроить шаблоны":
		pass
	elif userChoice == "Помощь":
		pass # print help
		return None # Остаться в том же состоянии и вызвать снова текущую функцию
	else:
		return None

#     keyboard.kb_list_month(message.from_user.id)
#     await message.answer("Выберите месяц:", reply_markup=keyboard())
#     await display_statistics.choiseIntervalGeneralDisplay.set()

@dp.message_handler(state = display_statistics.choiseIntervalGeneralDisplay)
async def funcDisplayGeneral(message: Message, state: FSMContext):
    userChoice = message.text
    
    if userChoice == "Сегодня":
        answer = GetInfoPurchases.OutputBuyShort(message.from_user.id, "today")
    elif userChoice == "Неделя":
        answer = GetInfoPurchases.OutputBuyShort(message.from_user.id, "week")
    elif userChoice == "Месяц":
        keyboard.kb_list_month(message.from_user.id)
        await message.answer("Выберите месяц", reply_markup=keyboard())
        await display_statistics.choiseMonth.set()
    else:
        return None

    keyboard.get_menu_keyboard()
    for a in answer:
        await message.answer(a, reply_markup=keyboard(), parse_mode=ParseMode.MARKDOWN)
    await state.finish()
    

@dp.message_handler(state = display_statistics.choiseMonth)
async def get_statistics_month_step_2(message: Message, state: FSMContext):
	if message.text in GetInfoPurchases.GetMonthList(message.from_user.id):
		month = message.text
		answer = GetInfoPurchases.GetMonthPurchases(message.from_user.id, month)
		keyboard.get_menu_keyboard()
		for a in answer:
			await message.answer(a, reply_markup=keyboard(), parse_mode=ParseMode.MARKDOWN)
		await state.finish()
	elif message.text == "Отмена":
		keyboard.get_menu_keyboard()
		await message.answer("Выберите пункт меню", reply_markup=keyboard())
		await state.finish()
	else:
		await message.answer("Повторите, выберите из клавиатуры бота")	
