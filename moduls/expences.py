from moduls import sql_class
from aiogram.utils.markdown import bold, code, italic, text
sql = sql_class.SQL_requests('costs', 'costs_analysis', 'my_costs', 'localhost')


def get_token():
	return sql.get_token_bot()

def get_passwd():
	return sql.get_password()

def get_today_buy(user_id):
	return sql.today_buy(user_id)
def get_yesterday_buy(user_id):
	return sql.yesterday_buy(user_id)
def rm_record_cost(category, price, user_id):
	sql.remove_buy(category, price, user_id)

# Appending new buy in db
def regist_new_buy(user_id, category, price, description):
	sql.insert_new_buy(user_id, category, price, description)

# check correct input password, for rigistration new user
def check_correct_passwd(user_id, password):
	password_bot = get_passwd()
	if password == password_bot:
		sql.append_user(user_id)
		return 'Пользователь добавлен'
	else:
		return 'Пароль не верный, пользователь не добавлен'

# Loading users with access
def load_users():
	table_users = sql.select_id_list_users()
	list_id_user = []
	for user in table_users:
		list_id_user.append(int(user[0]))
	return list_id_user

# Display purchases within a certain interval
def output_buy_long(user_id, type_out):
	if type_out == "today":
		table = sql.statistics_today(user_id)
		sum_buy = sql.sum_statistics_today(user_id)[0][0]
	elif type_out == "week":
		table = sql.statistics_week(user_id)
		sum_buy = sql.sum_statistics_week(user_id)[0][0]
	elif type_out == "month":
		table = sql.statistics_month(user_id)
		sum_buy = sql.sum_statistics_month(user_id)[0][0]
	

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


def output_buy_short(user_id, type_out):
	if type_out == "today":
		table = sql.statistics_today(user_id)
		sum_buy = sql.sum_statistics_today(user_id)[0][0]
	elif type_out == "week":
		table = sql.statistics_week(user_id)
		sum_buy = sql.sum_statistics_week(user_id)[0][0]
	elif type_out == "month":
		table = sql.statistics_month(user_id)
		sum_buy = sql.sum_statistics_month(user_id)[0][0]

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

def get_deptor_list_people(user_id, type_group):
	table = sql.get_note_deptor(user_id, type_group)
	list_poeple = [item[0] for item in table]
	return list_poeple
def insert_new_tranaction(user_id, deptor_name, deptor_sum, type_group):
	sql.insert_new_tranaction(user_id, deptor_name, deptor_sum, type_group)

def get_info_deptor_interface(user_id, deptor_name, type_group):
	return sql.get_info_deptor(user_id, deptor_name, type_group)

def upsert_deptor(user_id, name, new_sum, type_group, type_tran):
	sql.update_deptor(user_id, name, new_sum, type_group, type_tran)

def regist_new_user_db(user_id, name_deptor, type_group):
	sql.regist_new_user_in_dept_book(user_id, name_deptor, type_group)