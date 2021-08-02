from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from moduls.expences import get_today_buy, get_yesterday_buy, get_deptor_list_people

class Keyboard:
	def __init__(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
		
# ----------------------------------------------------------------------------------------
# Create start menu keyboard
	def get_menu_keyboard(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		# menu_items = [
		# KeyboardButton("Добавить покупку"),
		# KeyboardButton("Удалить покупку"),
		# KeyboardButton("Вывести покупки за сегодня"),
		# KeyboardButton("Вывести покупки за неделю"),
		# KeyboardButton("Вывести покупки за месяц"),
		# KeyboardButton("Книга задолжностей")
		# ]
		menu_items = ['Добавить покупку', "Удалить покупку", "Вывести покупки за сегодня", "Вывести покупки за неделю", "Вывести покупки за месяц", "Книга задолжностей"]
		
		# Appending items in keyboard
		self.reply_keyboard.add(*menu_items)
# ----------------------------------------------------------------------------------------
# Create keyboard with categoryes
	def kb_append_buy_1(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		menu_items = [
		KeyboardButton("Продукты"),
		KeyboardButton("Табак, жидкость, испаритель"),
		KeyboardButton("Телефон\\Интренет\\Яндекс плюс"),
		KeyboardButton("Проезд"),
		KeyboardButton("Копилка"),
		KeyboardButton("Прочее\\Развлечения"),
		KeyboardButton("Одежда"),
		KeyboardButton("Отмена")
		]
		
		# Appending items in keyboard
		self.reply_keyboard.add(*menu_items)
# ----------------------------------------------------------------------------------------
# Create keyboard for remove buy
	def kb_remove_buy(self, user_id):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		menu_items = [
		KeyboardButton("Сегодня")
		]

		today_buy = get_today_buy(user_id)
		yesterday_buy = get_yesterday_buy(user_id)

		for item in today_buy:
			item_buy = f"{item[0]}----{item[1]}"
			menu_items.append(KeyboardButton(item_buy))

		menu_items.append(KeyboardButton("Вчера"))


		for item in yesterday_buy:
			item_buy = f"{item[0]}----{item[1]}"
			menu_items.append(KeyboardButton(item_buy))
		menu_items.append(KeyboardButton("Отмена"))

		# Appending items in keyboard
		self.reply_keyboard.add(*menu_items)
# ----------------------------------------------------------------------------------------
# Create keyboard for confirm
	def kb_confirm(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		menu_items = [
		KeyboardButton("Подтвеждаю"),
		KeyboardButton("Отмена")
		]

		# Appending items in keyboard
		self.reply_keyboard.add(*menu_items)
# ----------------------------------------------------------------------------------------
# Create keyboard for choise type report
	def kb_out_buy(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		self.reply_keyboard.add(KeyboardButton("Краткий"))
		self.reply_keyboard.add(KeyboardButton("Подробный"))
# ----------------------------------------------------------------------------------------

	def kb_deptor_note_step_1(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		self.reply_keyboard.add(KeyboardButton("Дал в долг"))
		self.reply_keyboard.add(KeyboardButton("Взял в долг"))
# ----------------------------------------------------------------------------------------

	def kb_deptor_note_step_2(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		self.reply_keyboard.add(KeyboardButton("Добавить"))
		self.reply_keyboard.add(KeyboardButton("Погасить"))
# ----------------------------------------------------------------------------------------

	def kb_deptor_note_step_3(self, user_id):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		menu_items = get_deptor_list_people(user_id)

		# Appending items in keyboard
		self.reply_keyboard.add(*menu_items)

		self.reply_keyboard.add(KeyboardButton("Добавить человека"))
# ----------------------------------------------------------------------------------------

	def kb_deptor_note_step_4(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard = True)

		