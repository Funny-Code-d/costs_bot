import psycopg2
from psycopg2 import sql
import datetime

class SQL_requests:

	def __init__(self, datebase_name, user_name, password_db, host_address):
		self.database_name = datebase_name
		self.user_name = user_name
		self.password_db = password_db
		self.host_address = host_address
		self.conn = None
		self.cursor = None

		# Подключение к базе
		self.conn = psycopg2.connect(dbname=self.database_name, user=self.user_name, 
                        password=self.password_db, host=self.host_address)
		self.conn.autocommit = True
		print("Connect to db  ")

	def __del__(self):

		"""Деструктор, при удалении экземпляра, проиходит отключение от базы"""
		
		self.conn.close()
		print("Close connect to db  ")


#---------------------------------------------------------------------------------------------------
# Methods for query to db
#---------------------------------------------------------------------------------------------------
	def _get_table_from_db(self, req):
		try:
			self.cursor = self.conn.cursor()
			self.cursor.execute(req, ())
			return_obj = self.cursor.fetchall()
			self.cursor.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
		return return_obj

	def _insert_to_db(self, req):
		try:
			self.cursor = self.conn.cursor()
			self.cursor.execute(req, ())
			self.cursor.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)


#---------------------------------------------------------------------------------------------------
# Methods for get configuration data 
#---------------------------------------------------------------------------------------------------
	def get_token_bot(self):
		select = f"""SELECT token FROM conf WHERE name_bot = 'costs_bot'"""
		return self._get_table_from_db(select)[0][0]

	def get_password(self):
		select = f"""SELECT password FROM conf WHERE name_bot = 'costs_bot'"""

		table_passwd = self._get_table_from_db(select)

		return table_passwd[0][0]

	def append_user(self, id_user):
		id_user = int(id_user)
		insert = f"""INSERT INTO list_users VALUES ({id_user})"""
		self._insert_to_db(insert)

	def select_id_list_users(self):
		select = f"""SELECT telegram_id FROM list_users"""
		table = self._get_table_from_db(select)
		return table

#---------------------------------------------------------------------------------------------------
# Methods for registration new buy
#---------------------------------------------------------------------------------------------------

	def insert_new_buy(self, user_id, category, price, description):
		today = datetime.datetime.now()
		day = today.day
		month = today.month
		year = today.year
		today = f"{year}-{month}-{day}"
		insert = f"""INSERT INTO table_costs (user_id, sum, category, date_cost, description) VALUES ({user_id}, {price}, '{category}', '{today}', '{description}')"""
		self._insert_to_db(insert)

	def remove_buy(self, category, price, user_id):
		rm = f"""DELETE FROM table_costs WHERE category = '{category}' AND sum = {price} and user_id = {user_id}"""
		self._insert_to_db(rm)

#---------------------------------------------------------------------------------------------------
# Methods for output today\yesterday and statictics buy
#---------------------------------------------------------------------------------------------------
	def today_buy(self, user_id):
		today = datetime.datetime.now()
		day = today.day
		month = today.month
		year = today.year

		today = f'{year}-{month}-{day}'
		select = f"""SELECT category, sum FROM table_costs WHERE date_cost = '{today}' and user_id = {user_id}"""
		return self._get_table_from_db(select)

	def yesterday_buy(self, user_id):
		today = datetime.datetime.now()
		day = today.day - 1
		month = today.month
		year = today.year

		today = f'{year}-{month}-{day}'
		select = f"""SELECT category, sum FROM table_costs WHERE date_cost = '{today}' and user_id = {user_id}"""
		return self._get_table_from_db(select)

	def statistics_today(self, user_id):
		today = datetime.datetime.now()
		day = today.day
		month = today.month
		year = today.year

		today = f'{year}-{month}-{day}'
		select = f"""SELECT category, sum, description, date_cost FROM table_costs WHERE date_cost = '{today}' and user_id = {user_id}"""
		return self._get_table_from_db(select)

	def sum_statistics_today(self, user_id):
		today = datetime.datetime.now()
		day = today.day
		month = today.month
		year = today.year

		today = f'{year}-{month}-{day}'
		select = f"""SELECT sum(sum) FROM table_costs WHERE date_cost = '{today}' and user_id = {user_id}"""
		return self._get_table_from_db(select)

	def statistics_week(self, user_id):
		today = datetime.datetime.now() - datetime.timedelta(days = 7)
		day = today.day
		month = today.month
		year = today.year

		today = f'{year}-{month}-{day}'
		select = f"""SELECT category, sum, description, date_cost FROM table_costs WHERE date_cost >= '{today}' and user_id = {user_id}"""
		return self._get_table_from_db(select)

	def sum_statistics_week(self, user_id):
		today = datetime.datetime.now() - datetime.timedelta(days = 7)
		day = today.day
		month = today.month
		year = today.year

		today = f'{year}-{month}-{day}'
		select = f"""SELECT sum(sum) FROM table_costs WHERE date_cost >= '{today}' and user_id = {user_id}"""
		return self._get_table_from_db(select)

	def statistics_month(self, user_id, month_):
		month, year = month_.split(".")

		month_for_search = datetime.datetime(int(year), int(month), 1)

		if month == 12:
			end_date = datetime.datetime(int(year) + 1, 1, 1)
		else:
			end_date = datetime.datetime(int(year), int(month) + 1, 1)


		start_month = f'{month_for_search.year}-{month_for_search.month}-{month_for_search.day}'
		end_month = f'{end_date.year}-{end_date.month}-{end_date.day}'


		select = f"""SELECT category, sum, description, date_cost FROM table_costs WHERE date_cost >= '{start_month}' and date_cost < '{end_month}' and user_id = {user_id}"""
		return self._get_table_from_db(select)

	def sum_statistics_month(self, user_id, month_):

		month, year = month_.split(".")

		month_for_search = datetime.datetime(int(year), int(month), 1)

		if month == 12:
			end_date = datetime.datetime(int(year) + 1, 1, 1)
		else:
			end_date = datetime.datetime(int(year), int(month) + 1, 1)


		start_month = f'{month_for_search.year}-{month_for_search.month}-{month_for_search.day}'
		end_month = f'{end_date.year}-{end_date.month}-{end_date.day}'

		select = f"""SELECT sum(sum) FROM table_costs WHERE date_cost >= '{start_month}' and date_cost < '{end_month}' and user_id = {user_id}"""
		return self._get_table_from_db(select)

	def get_month_statistics(self, user_id):
		select = f"""SELECT date_cost, count(*) FROM table_costs WHERE user_id = {user_id} GROUP BY date_cost"""

		table = self._get_table_from_db(select)

		# print(table[0][0].month)
		return_table = []
		for item in table:
			if f'{item[0].month}.{item[0].year}' in return_table:
				continue
			else:
				return_table.append(f'{item[0].month}.{item[0].year}')
		
		return return_table

#---------------------------------------------------------------------------------------------------
# Methods for works with dept note
#---------------------------------------------------------------------------------------------------
	def get_note_deptor(self, user_id, type_group):

		select = f"""SELECT deptor_name FROM table_duty WHERE user_id = {user_id} and type_group = '{type_group}'"""
		return self._get_table_from_db(select)

	def insert_new_tranaction(self, user_id, deptor_name, deptor_sum, type_group):
		insert = f"""INSERT INTO table_duty VALUES ({user_id}, '{deptor_name}', '{type_group}', {deptor_sum})"""
		self._insert_to_db(insert)

	def get_info_deptor(self, user_id, deptor_name, type_group):
		select = f"""SELECT deptor_name, deptor_sum FROM table_duty WHERE user_id = {user_id} and deptor_name = '{deptor_name}' and type_group = '{type_group}'"""
		return self._get_table_from_db(select)

	def update_deptor(self, user_id, name, new_sum, type_group, type_tran):
		select = f"""SELECT deptor_sum FROM table_duty WHERE user_id = {user_id} and deptor_name = '{name}' and type_group = '{type_group}'"""
		deptor_sum = self._get_table_from_db(select)[0][0]
		
		if type_tran == 'positiv':
			deptor_sum = int(deptor_sum) + int(new_sum)

		elif type_tran == 'negativ':
			deptor_sum = int(deptor_sum) - int(new_sum)	
		

		update = f"""UPDATE table_duty SET deptor_sum = {deptor_sum} WHERE user_id = {user_id} and deptor_name = '{name}' and type_group = '{type_group}'"""
		self._insert_to_db(update)

		now = datetime.datetime.now()
		date = f"{now.year}-{now.month}-{now.day}"
		insert = f"INSERT INTO table_duty_history (user_id, deptor_name, summa, date_registration, type_group) VALUES ({user_id}, '{name}', {new_sum}, '{date}', '{type_group}')"
		self._insert_to_db(insert)

	def regist_new_user_in_dept_book(self, user_id, name_deptor, type_group,):
		insert = f"""INSERT INTO table_duty (user_id, deptor_name, type_group, deptor_sum) VALUES ({user_id}, '{name_deptor}', '{type_group}', 0)"""

		self._insert_to_db(insert)


	# Получение категорий пользователя

	def getPersonalCategoryDB(self, userID):
		query = f"SELECT name_category FROM category WHERE user_id = {userID}"

		select = self._get_table_from_db(query)

		listCategory = [item[0] for item in select]
		print(listCategory)

		return listCategory


	def addingPersonalCategoryDB(self, userID, nameCategory):
		query = f"INSERT INTO category (user_id, name_category) VALUES ({userID}, '{nameCategory}')"

		self._insert_to_db(query)

	def removePersonalCategoryDB(self, userID, nameCategory):
		query = f"DELETE FROM category WHERE user_id = {userID} AND name_category = '{nameCategory}'"

		self._insert_to_db(query)