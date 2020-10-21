from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# these buttons are main
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Заполнять анкету 📋'), KeyboardButton(text='Инфо о нас 🔎')],

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
    one_time_keyboard=True
)

post_buttons = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Пост с Фото📄'), KeyboardButton(text='Пост без Фото📄')],
              [KeyboardButton(text='⬅Нaзад')]],
    one_time_keyboard=True,
    resize_keyboard=True,
)

add_user_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Добавит Канал')],
                                                ],
                                      one_time_keyboard=True,
                                      resize_keyboard=True,
                                      )
