from aiogram.dispatcher.filters.state import StatesGroup, State


class Data(StatesGroup):

    data1 = State()


class PostData(StatesGroup):

    save = State()
