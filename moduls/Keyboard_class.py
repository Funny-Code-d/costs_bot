from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from moduls.expences import GetInfoPurchases
class Keyboard:
	def __init__(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
		
# ----------------------------------------------------------------------------------------
# Create start menu keyboard
	def get_menu_keyboard(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		menu_items = (
				'Добавить покупку',
				"Удалить покупку",
				"Вывести покупки за сегодня",
				"Вывести покупки за неделю",
				"Вывести покупки за месяц",
				"Книга задолжностей",
				)
		
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

		today_buy = GetInfoPurchases.GetTodayBuy(user_id)
		yesterday_buy = GetInfoPurchases.GetYesterdayBuy(user_id)

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

	def kb_list_month(self, user_id):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)

		months = GetInfoPurchases.GetMonthList(user_id)

		months.append("Отмена")

		self.reply_keyboard.add(*months)

	
	def __call__(self):
		return self.reply_keyboard
	
	def __repr__(self):
		return f"{__class__} {self.reply_keyboard}"