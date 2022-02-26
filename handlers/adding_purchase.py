from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

#local imports
from moduls.Question import append_buy_q
from loader import dp
from loader import kb as keyboard
from moduls.expences import BuyAction, GetInfoPurchases


@dp.message_handler(lambda message: message.text.startswith('Добавить покупки'))
async def command_append_buy(message: Message):
	# keyboard.getPersonalCategoriesKeyboard(message.from_user.id)
	keyboard.createKeyboardList(("Вручную", "Сканировать чек"))
	await message.answer("Выберите способ добавления", reply_markup=keyboard())
	await append_buy_q.typeAppend.set()
 
 
@dp.message_handler(state = append_buy_q.typeAppend)
async def append_buy_0(message: Message, state: FSMContext):
    type_action_append = message.text

    if type_action_append == "Вручную":
        keyboard.getPersonalCategoriesKeyboard(message.from_user.id)
        await message.answer("Выберите категорию", reply_markup=keyboard())
        await append_buy_q.category.set()

    elif type_action_append == "Сканировать чек":
        await message.answer("Сфотографируйте чек и отправьте", reply_markup=ReplyKeyboardRemove())
        await append_buy_q.scan_action.set()

    else:
        keyboard.createKeyboardList(("Вручную", "Сканировать чек"))
        await message.answer("Повторите ввод, выберите вариант из клавиатуры", reply_markup=keyboard())
        return None


@dp.message_handler(state = append_buy_q.scan_action, content_types=['photo'])
async def append_buy_scan(message: Message, state: FSMContext):
    await message.photo[-1].download(f'scans/{message.from_user.id}.jpg')
    # print(message)
    await state.finish()
    
# @dp.message_handler(content_types=['photo'])
# async def handle_docs_photo(message):

    # await message.photo[-1].download('test.jpg')

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
