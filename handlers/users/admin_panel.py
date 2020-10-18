from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import admins, channels
from keyboards.default.menu_buttons import add_user_button
from loader import dp, bot


@dp.message_handler(user_id=admins, commands=["add_users"])
async def give_buttons(message: types.Message):
    await message.answer('Что вы хотите добавит',
                         reply_markup=add_user_button)


@dp.message_handler(user_id=admins, text='Добавит Админ')
async def add_user(message: types.message,  state: FSMContext):
    await message.answer('Пожалстя отправьте админ ид'
                         'в формате 8979879:')

    await state.set_state('Admin.add_admin')


@dp.message_handler(state='Admin.add_admin')
async def get_info_admin(message: types.Message, state: FSMContext):

    admin_id = message.text
    admins.append(admin_id)

    await message.answer('Админ добавлен!')
    await state.reset_state()


@dp.message_handler(user_id=admins, text='Добавит Канал')
async def add_channel_buttons(message: types.message,  state: FSMContext):
    await message.answer('Пожалстя отправьте админ ид'
                         'в формате @get_cat_channel:')

    await state.set_state('add_channel')


@dp.message_handler(state='add_channel')
async def get_info_admin(message: types.Message, state: FSMContext):

    channel_name = message.text
    channels.append(channel_name)

    await message.answer('Канал добавлен!')
    await state.reset_state()

