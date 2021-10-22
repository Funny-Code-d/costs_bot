from aiogram.types import Message, ParseMode
from aiogram.dispatcher import FSMContext

#local imports
from loader import dp
from loader import kb as keyboard
from moduls.expences import RegistUser


@dp.message_handler(commands = ['start'])
async def registNewUser(message: Message):
    checkUserRegistration = RegistUser.checkUserRegistration(message.from_user.id)
    
    keyboard.get_menu_keyboard()
    
    if checkUserRegistration:
        await message.answer("Вы уже зарегистрированны", reply_markup=keyboard())
    else:
        RegistUser.registNewUser(message.from_user.id)
        await message.answer("Вы успешно зарегестрированы, и созданы 3 базовые категории покупок. Список категорий можно редактировать.", reply_markup=keyboard())