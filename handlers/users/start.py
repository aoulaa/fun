import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu_buttons import menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        db.add_user(id=message.from_user.id)
    except sqlite3.IntegrityError as err:
        print(err)
    await message.answer(f'Привет, {message.from_user.full_name}!',
                         reply_markup=menu)


@dp.message_handler(text='⬅Назад')
async def go_back(message: types.Message):
    await message.answer('Вы находитесь в главном меню',
                         reply_markup=menu)


@dp.message_handler(text='🔎 Инфо о нас')
async def info_about_company(message: types.Message):
    await message.answer('бла бла бла бла бла бла бла блабла бла бла блабла бла бла блабла бла бла блабла бла бла бла ')

