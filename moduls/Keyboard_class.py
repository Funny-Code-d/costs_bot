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
				"Настроить категории",
				)
		
		# Appending items in keyboard
		self.reply_keyboard.add(*menu_items)
# ----------------------------------------------------------------------------------------
	def getPersonalCategoriesKeyboard(self, userID):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		listCategory = GetInfoPurchases.getPersonalCategory(userID)
		self.reply_keyboard.add(*listCategory)
# ----------------------------------------------------------------------------------------
# Create keyboard with categoryes
	def kb_append_buy_1(self, userID = 691263908):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		# getting list personal categories from db
		listCategory = GetInfoPurchases.getPersonalCategory(userID)
		
		# Appending items in keyboard
		self.reply_keyboard.add(*listCategory)
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

	def changeCategoriesChoiseAction(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		menu_items = (
			KeyboardButton("Добавить"),
			KeyboardButton("Удалить"),
			KeyboardButton("Отмена")
		)
		self.reply_keyboard.add(*menu_items)
	
	def validNewCategory(self):
		self.reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		menu_items = (
			KeyboardButton("Верно"),
			KeyboardButton("Ввести заново")
		)
		self.reply_keyboard.add(*menu_items)

	
	def __call__(self):
		return self.reply_keyboard
	
	def __repr__(self):
		return f"{__class__} {self.reply_keyboard}"