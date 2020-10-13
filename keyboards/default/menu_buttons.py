from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# these buttons are main
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='наши услуги'), KeyboardButton(text='🔎 Инфо о нас')],

    ],
    resize_keyboard=True
)

back = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='⬅Назад'), ], ],
                           resize_keyboard=True,
                           one_time_keyboard=True
                           )

serve = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📝 ищу работу'), KeyboardButton(text='💼 нужен сотрудник')],
        [KeyboardButton(text='Отправить готовый пост 📄'), ],
        [KeyboardButton(text='⬅Назад')],

    ],
    resize_keyboard=True,
)
