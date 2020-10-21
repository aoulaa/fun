from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import admins, channels
from keyboards.default.menu_buttons import add_user_button
from loader import dp


@dp.message_handler(user_id=admins, commands=["add_users"])
async def give_buttons(message: types.Message):
    await message.answer('Что вы хотите добавит',
                         reply_markup=add_user_button)


@dp.message_handler(user_id=admins, text='Добавит Канал')
async def add_channel_buttons(message: types.message,  state: FSMContext):
    await message.answer('Пожалстя отправьте админ ид'
                         'в формате @get_cat_channel:')

    await state.set_state('add_channel')


@dp.message_handler(state='add_channel')
async def get_info_admin(message: types.Message, state: FSMContext):

    channel_name = message.text
    channels.append(channel_name)

    await message.answer(f'Канал добавлен!\n {channels}')
    await state.reset_state()



