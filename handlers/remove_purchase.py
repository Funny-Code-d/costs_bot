from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

#local imports
from loader import dp
from loader import kb as keyboard
from moduls.expences import BuyAction
from moduls.Question import remove_buy_q
from moduls.Keyboard_class import Keyboard
from moduls import expences


@dp.message_handler(lambda message: message.text.startswith('Удалить покупку'))
async def command_del_buy(message: Message):
	keyboard.kb_remove_buy(message.from_user.id)
	await message.reply("Выберите покупку которую нужно удалить", reply_markup=keyboard())
	await remove_buy_q.choise_buy.set()


@dp.message_handler(state = remove_buy_q.choise_buy)
async def remove_buy_1(message: Message, state: FSMContext):

	if message.text == "Отмена":
		keyboard.get_menu_keyboard()
		await message.answer("Отмена", reply_markup=keyboard())
		await state.finish()
		return

	list_message = message.text.split("----")
	category = list_message[0]
	price = int(list_message[1])

	await state.update_data(
		{"category" : category, 'price' : price}
		)
	keyboard.kb_confirm()
	await message.reply("Подтвердите", reply_markup=keyboard())
	await remove_buy_q.next()

@dp.message_handler(state = remove_buy_q.confirm)
async def remove_buy_2(message: Message, state: FSMContext):

	data = await state.get_data()
	category = data.get("category")
	price = data.get("price")
	if message.text == "Подтвеждаю":
		BuyAction.RemoveRecordCost(category, price, message.from_user.id)
		await state.finish()
		keyboard.get_menu_keyboard()
		await message.reply("Покупка удалена", reply_markup=keyboard())
	elif message.text == "Отмена":
		await state.finish()
		keyboard.get_menu_keyboard()
		await message.reply("Отмена", reply_markup=keyboard())
	else:
		await message.answer("Повторите ввод")
		return
