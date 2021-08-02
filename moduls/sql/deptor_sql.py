import psycopg2
from query import Base_query



class Deptor(Base_query):
	def __init__(self, datebase_name, user_name, password_db, host_address):
		print("Call deptor class")
		super().__init__(datebase_name, user_name, password_db, host_address)

	def print_deptor(self):
		print("This deptor")
