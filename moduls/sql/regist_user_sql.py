import psycopg2
from query import Base_query

class Regist_user:

	def __init__(self, datebase_name, user_name, password_db, host_address):
		print("Call out class")
		super().__init__(datebase_name, user_name, password_db, host_address)



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