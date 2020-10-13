from aiogram import types
from aiogram.utils.markdown import hbold

from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    text = hbold('выключено режим ехо: ')
    await message.answer(f'{text}\n\n{message.text}')
