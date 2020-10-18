import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu_buttons import menu, serve
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name_user=name)
    except sqlite3.IntegrityError as err:
        print(err)

    await message.answer(f'Привет, {message.from_user.full_name}!',
                         reply_markup=menu)


@dp.message_handler(text='⬅Назад')
async def go_back(message: types.Message):
    await message.answer('Вы находитесь в главном меню',
                         reply_markup=menu)


@dp.message_handler(text='⬅Нaзад')
async def go_back_to_post_menu(message: types.Message):
    await message.answer('что вы ищите?',
                         reply_markup=serve)


@dp.message_handler(text='Инфо о нас 🔎')
async def info_about_company(message: types.Message):
    await message.answer('бла бла бла бла бла бла бла блабла бла бла блабла бла бла блабла бла бла блабла бла бла бла ')


@dp.message_handler(commands=['getuser'])
async def number(message: types.message):
    count = db.count_users()[0]
    user_table = db.select_from_table()
    name = db.select_name()
    await message.answer(f'каличство усеров: {count}')

    await message.answer(f'user id: {user_table}')
    await message.answer(f'имя усеров: {name}')


@dp.message_handler(Command(['cancel', 'start', 'help']), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('если что но пошло не так можете нажмат на /start')
