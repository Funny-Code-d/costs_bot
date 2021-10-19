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

class out_statictics(StatesGroup):
    type_out = State()
    choise_month = State()

class Deptor_note(StatesGroup):
    group_deptor = State()
    name_deptor = State()
    get_sum = State()
    regist_new_user = State()

class ChangeCategory(StatesGroup):
    action = State()
    nameCategory = State()
    checkValidNames = State()
    removeCategory = State()