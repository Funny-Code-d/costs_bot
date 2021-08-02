import psycopg2
from query import Base_query


class Output_buy(Base_query):
	
	def __init__(self, datebase_name, user_name, password_db, host_address):
		print("Call out class")
		super().__init__(datebase_name, user_name, password_db, host_address)



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