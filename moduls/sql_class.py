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
#---------------------------------------------------------------------------------------------------
	def __del__(self):

		"""Деструктор, при удалении экземпляра, проиходит отключение от базы"""
		
		self.conn.close()
		print("Close connect to db  ")
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
#---------------------------------------------------------------------------------------------------
	def _insert_to_db(self, req):
		try:
			self.cursor = self.conn.cursor()
			self.cursor.execute(req, ())
			self.cursor.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
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

	def insert_new_buy(self, user_id, category, price, description):
		today = datetime.datetime.now()
		day = today.day
		month = today.month
		year = today.year
		today = f"{year}-{month}-{day}"
		insert = f"""INSERT INTO table_costs (user_id, sum, category, date_cost, description) VALUES ({user_id}, {price}, '{category}', '{today}', '{description}')"""
		self._insert_to_db(insert)

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

	def remove_buy(self, category, price, user_id):
		rm = f"""DELETE FROM table_costs WHERE category = '{category}' AND sum = {price} and user_id = {user_id}"""
		self._insert_to_db(rm)

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


	def statistics_month(self, user_id):
		today = datetime.datetime.now() - datetime.timedelta(days = 30)
		day = today.day
		month = today.month
		year = today.year

		today = f'{year}-{month}-{day}'
		select = f"""SELECT category, sum, description, date_cost FROM table_costs WHERE date_cost >= '{today}' and user_id = {user_id}"""
		return self._get_table_from_db(select)

	def sum_statistics_month(self, user_id):
		today = datetime.datetime.now() - datetime.timedelta(days = 30)
		day = today.day
		month = today.month
		year = today.year

		today = f'{year}-{month}-{day}'
		select = f"""SELECT sum(sum) FROM table_costs WHERE date_cost >= '{today}' and user_id = {user_id}"""
		return self._get_table_from_db(select)
