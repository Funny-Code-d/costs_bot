from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

#local imports
from moduls.Question import append_buy_q
from loader import dp
from loader import kb as keyboard
from moduls.Question import ChangeCategory
from moduls.expences import GetInfoPurchases

def outPersonalCategory(userID):
    listCategory = GetInfoPurchases.getPersonalCategory(userID)

    strCategory = 'Ваши категории:\n\n'
    for item in listCategory:
        strCategory += " - " +  item + '\n'

    strCategory += '\n'
    return strCategory


@dp.message_handler(lambda message: message.text.startswith('Настроить категории'))
async def changeCategoriesList(message: Message):
    keyboard.changeCategoriesChoiseAction()
    await message.answer(outPersonalCategory(message.from_user.id) + 'Добавить или удалить категорию?', reply_markup=keyboard())
    await ChangeCategory.action.set()


@dp.message_handler(state = ChangeCategory.action)
async def choiseAction(message: Message, state: FSMContext):
    if message.text == 'Добавить':
        await state.update_data({"action" : message.text})
        await message.answer("Введите название категории", reply_markup=ReplyKeyboardRemove())
        await ChangeCategory.nameCategory.set()

    elif message.text == "Удалить":
        await state.update_data({"action" : message.text})
        keyboard.kb_append_buy_1()
        await message.answer("Выьерите категорию которую удалить (при удалении категории, удаляться и покупки связанные с этой категорией", reply_markup=keyboard())
        await ChangeCategory.removeCategory.set()
    
    elif message.text == "Отмена":
        keyboard.get_menu_keyboard()
        await message.answer("Выберите пункт меню", reply_markup=keyboard())
        await state.finish()

    else:
        await message.answer("Повторите ввод (выбрать из клавиатуры бота)")
        return None

@dp.message_handler(state = ChangeCategory.nameCategory)
async def changeListCategoryInDB(message: Message, state: FSMContext):
    await state.update_data({'nameCategory' : message.text})
    keyboard.validNewCategory()
    await message.answer("Проверьте правильность новой категории: " + message.text, reply_markup=keyboard())
    await ChangeCategory.checkValidNames.set()


# check valid name input category
@dp.message_handler(state = ChangeCategory.checkValidNames)
async def checkValueNewCategory(message: Message, state: FSMContext):
    if message.text == "Верно":
        # Добавление категории
        data = await state.get_data()
        nameCategory = data.get("nameCategory")
        GetInfoPurchases.addingPersonalCategory(message.from_user.id, nameCategory)
        await state.finish()
        keyboard.get_menu_keyboard()
        await message.answer("Категория добавлена", reply_markup=keyboard())

    elif message.text == "Ввести заново":
        await message.answer("Введите название категории")
        await ChangeCategory.nameCategory.set()
    else:
        await message.answer("Повторите ввод")
        return

# remove personal category
@dp.message_handler(state = ChangeCategory.removeCategory)
async def removeCategory(message: Message, state: FSMContext):
    if message.text in  GetInfoPurchases.getPersonalCategory(message.from_user.id):
        # remove
        data = await state.get_data()
        nameCategory = data.get("nameCategory")
        GetInfoPurchases.removePresonalCategory(message.from_user.id, message.text)
        await state.finish()
        keyboard.get_menu_keyboard()
        await message.answer("Категория удалена", reply_markup=keyboard())
    else:
        await message.answer("Повторите ввод (выберите в клавиатуре бота)")
        return