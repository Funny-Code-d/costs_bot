import psycopg2
from output_buy import Output_buy
from deptor import Deptor

class Sql_Requests(Output_buy, Deptor):
	def __init__(self, datebase_name, user_name, password_db, host_address):
		super().__init__(datebase_name, user_name, password_db, host_address)

a = Sql_Requests('costs', 'costs_analysis', 'my_costs', 'localhost')

