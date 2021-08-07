from aiogram.types import Message, ParseMode, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.types.inline_keyboard import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, callback_query
from aiogram.utils.markdown import quote_html, hbold, hunderline, text
# --------------------------------------------------------------------------------------------------
from loader import dp
from loader import kb
from moduls.expences import DebtorNotebook
from moduls import expences
from moduls.Question import Deptor_note
# --------------------------------------------------------------------------------------------------

@dp.message_handler(lambda message: message.text.startswith("Книга задолжностей"))
async def send_start_deptor(message: Message):
	markup_inline = InlineKeyboardMarkup(row_width=1)
	keyboard = [
				InlineKeyboardButton(text="Дал в долг", callback_data='give'),
				InlineKeyboardButton(text="Взял в долг", callback_data='take'),
				InlineKeyboardButton(text="Выход", callback_data="exit"),
				]
	for item in keyboard:
		markup_inline.insert(item) 

	await message.answer("Выберите тип", reply_markup=markup_inline)
	await Deptor_note.group_deptor.set()
# --------------------------------------------------------------------------------------------------

def create_str_deptors(name_deptor: list, bold_name: int, user_id: int, type_group: str):
	
	if len(name_deptor) == 0:
		return 'Книга должников\\задолжностей пуст', 1
	out_answer = text('Книга должников\\задолжностей\n\n')

	if bold_name <= 0: 
		bold_name = len(name_deptor)
	elif bold_name > len(name_deptor):
		bold_name = 1

	for dept in range(len(name_deptor)):
		if (dept + 1) == bold_name:
			out_answer += text(f'{dept + 1}.***',hbold(f'{name_deptor[dept]}'.upper()), '***\n')
		else:
			out_answer += text((f'{dept + 1}. {name_deptor[dept]}\n'))

	out_answer += text("-----------------\n\n")
	info_deptor = DebtorNotebook.GetInformationAboutDebtor(user_id, name_deptor[bold_name - 1], type_group)

	out_answer += text(f"Имя:   {info_deptor[0][0]}\nСумма:   {info_deptor[0][1]}")
	return out_answer, bold_name
# --------------------------------------------------------------------------------------------------
def create_keyboard_deptors(user_id, number_user, type_group):

	DeptList = DebtorNotebook.GetDebtorListPeople(user_id, type_group)

	deptors = [item for item in DeptList]

	out_answer, bold_name = create_str_deptors(deptors, number_user, user_id, type_group)
	markup_inline = InlineKeyboardMarkup(row_width=1)
	keyboard = [
				InlineKeyboardButton(text="⬆️", callback_data='back'),
				InlineKeyboardButton(text="Добавить долг", callback_data='add_dept'),
				InlineKeyboardButton(text="Погасить долг", callback_data='rm_dept'),
				InlineKeyboardButton(text="⬇️", callback_data='next'),
				InlineKeyboardButton(text="Добавить новую запись", callback_data='new_user'),
				InlineKeyboardButton(text="Назад", callback_data="back_menu"),
				]
	for item in keyboard:
		markup_inline.insert(item)

	return markup_inline, out_answer, bold_name
# --------------------------------------------------------------------------------------------------

def get_name_deptor_for_change(user_id, number_user, type_group):
	DeptList = DebtorNotebook.GetDebtorListPeople(user_id, type_group)
	deptors = [item for item in DeptList]

	return deptors[number_user]
# --------------------------------------------------------------------------------------------------

@dp.callback_query_handler(state = Deptor_note.group_deptor)
async def edit_message_deptor_1(call: callback_query, state: FSMContext):
	answer = call.data
	await call.answer(cache_time=0)
	if answer == 'give':
		markup_inline, out_answer, _ = create_keyboard_deptors(call.from_user.id, 1, 'give')
		await state.update_data({"number_user" : 1, 'type' : 'give'})
	elif answer == 'take':
		markup_inline, out_answer, _ = create_keyboard_deptors(call.from_user.id, 1, 'take')
		await state.update_data({"number_user" : 1, 'type' : 'take'})
	elif answer == 'exit':
		await state.finish()
		kb.get_menu_keyboard()
		await call.message.edit_text("Блокнот закрыт")
		await call.message.answer("Выберите пункт", reply_markup=kb.reply_keyboard)
		return
	else:
		return
	await call.message.edit_text(out_answer, reply_markup=markup_inline, parse_mode="HTML")
	await Deptor_note.next()
# --------------------------------------------------------------------------------------------------

@dp.callback_query_handler(state = Deptor_note.name_deptor)
async def edit_message_deptor_2(call: callback_query, state: FSMContext):
	action = call.data
	await call.answer(cache_time=0)
	# choosing next name deptor
	if action == 'next':
		data = await state.get_data()
		num = data.get('number_user')
		type_group = data.get("type")
		markup_inline, out_answer, bold_name = create_keyboard_deptors(call.from_user.id, num + 1, type_group)
		await state.update_data({"number_user" : bold_name})

		await call.message.edit_text(out_answer, reply_markup=markup_inline, parse_mode='HTML')
		
		return None
	# choosing previous name deptor
	elif action == 'back':
		data = await state.get_data()
		num = data.get('number_user')
		type_group = data.get("type")
		markup_inline, out_answer, bold_name = create_keyboard_deptors(call.from_user.id, num - 1, type_group)
		await state.update_data({"number_user" : bold_name})

		await call.message.edit_text(out_answer, reply_markup=markup_inline, parse_mode='HTML')
		
		return None
	# choosing adding dept
	elif action == 'add_dept':
		data = await state.get_data()
		num = data.get("number_user")
		type_group = data.get("type")
		get_name_deptor = get_name_deptor_for_change(call.from_user.id, num - 1, type_group)
		await state.update_data({'name' : get_name_deptor, 'type_tran' : "positiv"})
		await call.message.answer("Введите сумму")
		await Deptor_note.get_sum.set()

	# choosing remove dept
	elif action == 'rm_dept':
		data = await state.get_data()
		num = data.get("number_user")
		type_group = data.get("type")
		get_name_deptor = get_name_deptor_for_change(call.from_user.id, num - 1, type_group)
		await state.update_data({'name' : get_name_deptor, "type_tran" : "negativ"})
		await call.message.answer("Введите сумму")
		await Deptor_note.get_sum.set()

	# choosing adding new user in dept book
	elif action == 'new_user':
		await call.message.answer("Введите имя")
		await Deptor_note.regist_new_user.set()

	elif action == 'back_menu':
		markup_inline = InlineKeyboardMarkup(row_width=1)
		keyboard = [
					InlineKeyboardButton(text="Дал в долг", callback_data='give'),
					InlineKeyboardButton(text="Взял в долг", callback_data='take'),
					InlineKeyboardButton(text="Выход", callback_data="exit"),
					]
		for item in keyboard:
			markup_inline.insert(item) 

		await call.message.edit_text("Выберите тип", reply_markup=markup_inline)
		await Deptor_note.group_deptor.set()

	return

@dp.message_handler(state = Deptor_note.get_sum)
async def edit_message_deptor_3(message: Message, state: FSMContext):
	answer_sum = message.text

	data = await state.get_data()
	name = data.get("name")
	type_group = data.get("type")
	type_tran = data.get("type_tran")
	DebtorNotebook.UpsertDeptor(message.from_user.id, name, answer_sum, type_group, type_tran)
	await message.answer("Записано")

	num = data.get("number_user")
	type_group = data.get("type")
	markup_inline, out_answer, _ = create_keyboard_deptors(message.from_user.id, num, type_group)
	await message.answer(out_answer, reply_markup=markup_inline, parse_mode="HTML")
	await Deptor_note.name_deptor.set()


@dp.message_handler(state = Deptor_note.regist_new_user)
async def edit_message_deptor_4(message: Message, state: FSMContext):
	name_new_deptor = message.text

	data = await state.get_data()
	type_group = data.get('type')

	DebtorNotebook.RegistrationNewUserDB(message.from_user.id, name_new_deptor, type_group)
	await message.answer("Запись добавлена")
	num = data.get("number_user")
	type_group = data.get("type")
	markup_inline, out_answer, _ = create_keyboard_deptors(message.from_user.id, num, type_group)
	await message.answer(out_answer, reply_markup=markup_inline, parse_mode="HTML")
	await Deptor_note.name_deptor.set()