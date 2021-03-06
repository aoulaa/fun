from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_send = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="отправ админу📤", callback_data='admin_msg'),
            InlineKeyboardButton(text="Отменит❌", callback_data='cancel')
        ],

    ], resize_keyboard=True)

admin_photo_admin = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="отправ админу📤", callback_data='admin_photo'),
            InlineKeyboardButton(text="Отменит❌", callback_data='cancel')
        ],

    ], resize_keyboard=True)


reply_1 = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="подтвердить✅", callback_data='confirm'),
            InlineKeyboardButton(text="Отменит❌", callback_data='cancel_admin')
        ],
    ], resize_keyboard=True)


reply_photo = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="подтвердить✅", callback_data='confirm_photo'),
            InlineKeyboardButton(text="Отменит❌", callback_data='cancel_admin')
        ],
    ], resize_keyboard=True)


send_to_channel = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="сделать пост✅", callback_data='post_in_channel'),
        ],
    ], resize_keyboard=True)

