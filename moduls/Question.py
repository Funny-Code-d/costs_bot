from aiogram.dispatcher.filters.state import StatesGroup, State


class registration_user(StatesGroup):
    user_id = State()
    passwd = State()

class append_buy_q(StatesGroup):
    category = State()
    price = State()
    description = State()
class remove_buy_q(StatesGroup):
    choise_buy = State()
    confirm = State()