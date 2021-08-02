import psycopg2
from query import Base_query

class Config_data:

	def __init__(self, datebase_name, user_name, password_db, host_address):
		print("Call out class")
		super().__init__(datebase_name, user_name, password_db, host_address)


	
	def get_token_bot(self):
		select = f"""SELECT token FROM conf WHERE name_bot = 'costs_bot'"""
		return self._get_table_from_db(select)[0][0]

	
	def get_password(self):
		select = f"""SELECT password FROM conf WHERE name_bot = 'costs_bot'"""
		table_passwd = self._get_table_from_db(select)
		#return table_passwd[0][0]
		return self._get_table_from_db(select)[0][0]

	
	def append_user(self, id_user):
		id_user = int(id_user)
		insert = f"""INSERT INTO list_users VALUES ({id_user})"""
		self._insert_to_db(insert)

	
	def select_id_list_users(self):
		select = f"""SELECT telegram_id FROM list_users"""
		# table = self._get_table_from_db(select)
		return self._get_table_from_db(select)