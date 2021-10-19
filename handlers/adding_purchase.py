from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

#local imports
from moduls.Question import append_buy_q
from loader import dp
from loader import kb as keyboard
from moduls.expences import BuyAction, GetInfoPurchases


@dp.message_handler(lambda message: message.text.startswith('Добавить покупку'))
async def command_append_buy(message: Message):
	keyboard.kb_append_buy_1()
	await message.answer("Выберите категорию", reply_markup=keyboard())
	await append_buy_q.category.set()


@dp.message_handler(state = append_buy_q.category)
async def append_buy_1(message: Message, state: FSMContext):

	if message.text in  GetInfoPurchases.getPersonalCategory(message.from_user.id):
		await state.update_data(
			{'category' : message.text}
			)
		await message.reply("Введите сумму", reply_markup=ReplyKeyboardRemove())
		await append_buy_q.next()
	elif message.text == "Отмена":
		
		keyboard.get_menu_keyboard()
		await message.answer("Отмена", reply_markup=keyboard())
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

	data = await state.get_data()
	category = data.get("category")
	price = data.get("price")
	description = message.text
	BuyAction.RegistNewBuy(message.from_user.id, category, price, description)
	await state.finish()
	keyboard.get_menu_keyboard()
	await message.reply("Покупка добавлена", reply_markup=keyboard())
