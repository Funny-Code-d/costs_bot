from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

#local imports
from moduls.Question import append_buy_q
from loader import dp
from moduls.Keyboard_class import Keyboard
from moduls import expences


@dp.message_handler(lambda message: message.text.startswith('Добавить покупку'))
async def command_append_buy(message: Message):
	kb = Keyboard()
	kb.kb_append_buy_1()
	await message.answer("Выберите категорию", reply_markup=kb.reply_keyboard)
	del kb
	await append_buy_q.category.set()


@dp.message_handler(state = append_buy_q.category)
async def append_buy_1(message: Message, state: FSMContext):
	kb = Keyboard()
	if message.text in ['Продукты', 'Табак, жидкость, испаритель', "Телефон\\Интренет\\Яндекс плюс", "Проезд", "Копилка", "Прочее\\Развлечения", "Одежда"]:
		await state.update_data(
			{'category' : message.text}
			)
		await message.reply("Введите сумму", reply_markup=ReplyKeyboardRemove())
		await append_buy_q.next()
	elif message.text == "Отмена":
		
		kb.get_menu_keyboard()
		await message.answer("Отмена", reply_markup=kb.reply_keyboard)
		await state.finish()
		return
	else:
		await message.answer("Повторите ввод, выберите категорию из клавиатуры бота")
		return


@dp.message_handler(state = append_buy_q.price)
async def append_buy_2(message: Message, state: FSMContext):
	await state.update_data(
		{'price' : message.text}
		)
	await message.reply("Введите описание", reply_markup=ReplyKeyboardRemove())
	await append_buy_q.next()


@dp.message_handler(state = append_buy_q.description)
async def append_buy_3(message: Message, state: FSMContext):
	kb = Keyboard()
	data = await state.get_data()
	category = data.get("category")
	price = data.get("price")
	description = message.text
	expences.regist_new_buy(message.from_user.id, category, price, description)
	await state.finish()
	kb.get_menu_keyboard()
	await message.reply("Покупка добавлена", reply_markup=kb.reply_keyboard)
