from moduls.sql_class import SQL_requests
from aiogram.utils.markdown import bold, code, italic, text


Sql = SQL_requests('costs', 'costs_analysis', 'my_costs', '127.0.0.1')

# Class for getting configuration infornation about bot
class ConfigData:

	# getting token bot
	@staticmethod
	def GetToken():
		return Sql.get_token_bot()

	# getting password bot
	@staticmethod
	def GetPssswd():
		return Sql.get_password()

# Class for adding/removing purchases
class BuyAction:

	# remove a purchase record from the database
	@staticmethod
	def RemoveRecordCost(category, price, user_id):
		Sql.remove_buy(category, price, user_id)

	# Appending new buy in db
	@staticmethod
	def RegistNewBuy(user_id, category, price, description):
		Sql.insert_new_buy(user_id, category, price, description)

# Class for getting info about purhases
class GetInfoPurchases:

	# getting information about today's purchases
	@staticmethod
	def GetTodayBuy(user_id):
		return Sql.today_buy(user_id)

	# getting information about yesterday's purchases
	@staticmethod
	def GetYesterdayBuy(user_id):
		return Sql.yesterday_buy(user_id)

	# getting info about purchases (long format)
	@staticmethod
	def OutputBuyLong(user_id, type_out):
		
		if type_out == "today":
			table = Sql.statistics_today(user_id)
			sum_buy = Sql.sum_statistics_today(user_id)[0][0]
		elif type_out == "week":
			table = Sql.statistics_week(user_id)
			sum_buy = Sql.sum_statistics_week(user_id)[0][0]
		else:
			return None
	

		list_answer = []
		answer = ''
		for item_table in table:
			if len(answer) > 3000:
				list_answer.append(answer)
				answer = ''
			answer += text(bold(item_table[0]),"\n", italic(item_table[2]), '\n', bold(f"Дата:"),  f"{item_table[3].day}.{item_table[3].month}.{item_table[3].year}", "\n", f"Сумма: {item_table[1]}\n---------------------------------------\n")
		answer += text(bold(f"\nОбщая сумма:  {sum_buy}"))
		list_answer.append(answer)
		return list_answer

	# getting info about purchases (short format)
	@staticmethod
	def OutputBuyShort(user_id, type_out):
		
		if type_out == "today":
			table = Sql.statistics_today(user_id)
			sum_buy = Sql.sum_statistics_today(user_id)[0][0]
		elif type_out == "week":
			table = Sql.statistics_week(user_id)
			sum_buy = Sql.sum_statistics_week(user_id)[0][0]
		else:
			return None


		list_answer = []
		answer = ''
		for item_table in table:
			if len(answer) > 3000:
				list_answer.append(answer)
				answer = ''
			answer += text(italic(item_table[0]), "  |  ", bold(item_table[1]), "р   |  ", item_table[3], '\n')
		answer += text(bold(f"\nОбщая сумма:  {sum_buy}"))
		list_answer.append(answer)
		return list_answer

	# getting a list of months containing information about purchases
	@staticmethod
	def GetMonthList(user_id):
		return Sql.get_month_statistics(user_id)

	# getting information about purchases in the selected month
	@staticmethod
	def GetMonthPurchases(user_id, month):
		table = Sql.statistics_month(user_id, month)
		sum_buy = Sql.sum_statistics_month(user_id, month)[0][0]


		list_answer = []
		answer = ''
		for item_table in table:
			if len(answer) > 3000:
				list_answer.append(answer)
				answer = ''
			answer += text(italic(item_table[0]), "  |  ", bold(item_table[1]), "р   |  ", item_table[3], '\n')
		answer += text(bold(f"\nОбщая сумма:  {sum_buy}"))
		list_answer.append(answer)
		return list_answer

	
	@staticmethod
	def getPersonalCategory(userID):
		return Sql.getPersonalCategoryDB(userID)

	@staticmethod
	def addingPersonalCategory(userID, nameCategory):
		Sql.addingPersonalCategoryDB(userID, nameCategory)
		return None
	
	@staticmethod
	def removePresonalCategory(userID, nameCategory):
		Sql.removePersonalCategoryDB(userID, nameCategory)
		return None

# Class for work with Debtor notebook
class DebtorNotebook:
	
	# getting list of users in Debtor Notebook
	@staticmethod
	def GetDebtorListPeople(user_id, type_group):
		table = Sql.get_note_deptor(user_id, type_group)
		list_poeple = [item[0] for item in table]
		return list_poeple
	
	# Regist new debtors
	@staticmethod
	def InsertNewTranaction(user_id, deptor_name, deptor_sum, type_group):
		Sql.insert_new_tranaction(user_id, deptor_name, deptor_sum, type_group)
	
	# Getting information about debtor
	@staticmethod
	def GetInformationAboutDebtor(user_id, deptor_name, type_group):
		return Sql.get_info_deptor(user_id, deptor_name, type_group)
	
	# Appeding/remove debt to user
	@staticmethod
	def UpsertDeptor(user_id, name, new_sum, type_group, type_tran):
		Sql.update_deptor(user_id, name, new_sum, type_group, type_tran)

	# Regist new debtors
	@staticmethod
	def RegistrationNewUserDB(user_id, name_deptor, type_group):
		Sql.regist_new_user_in_dept_book(user_id, name_deptor, type_group)
