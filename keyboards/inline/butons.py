from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_send = InlineKeyboardMarkup(
    row_width=1,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="отправ админу📤", callback_data='admin_msg'),
            InlineKeyboardButton(text="Отменит❌", callback_data='cancel')
        ],

    ],resize_keyboard=True)

reply_1 = InlineKeyboardMarkup(
    row_width=1,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="подтвердить✅", callback_data='confirm'),
            InlineKeyboardButton(text="Отменит❌", callback_data='cancel_admin')
        ],
    ],resize_keyboard=True)
