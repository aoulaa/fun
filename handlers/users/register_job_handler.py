from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from keyboards.inline.butons import admin_send
from keyboards.default.menu_buttons import serve
from loader import dp, db


@dp.message_handler(text='Заполнять анкету 📋')
async def service(message: types.message):
    await message.answer('что вы ищите?',
                         reply_markup=serve)


@dp.message_handler(text='📝 ищу работу')
async def job_want(message: types.message, state: FSMContext):
    await message.answer('Название вашей объявление. например ищу работу в офисе: ',
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state("title")


@dp.message_handler(state='title')
async def add_state(message: types.message, state: FSMContext):
    title = message.text
    db.update_title(title=title, id=message.from_user.id)
    await message.answer('Введите ваше имя и год рождения \n'
                         'в формате: Олег, 25')

    await state.set_state("name")


@dp.message_handler(state='name')
async def add_name(message: types.message, state: FSMContext):
    name = message.text
    db.update_name(name=name, id=message.from_user.id)
    await message.answer('Напишите несколько слов о себе:\n'
                         '(личные и деловые качества).')
    await state.set_state('self.info')


@dp.message_handler(state='self.info')
async def add_about_self(message: types.message, state: FSMContext):
    self_info = message.text
    db.update_user_self_info(self_info=self_info, id=message.from_user.id)
    await message.answer('Образование: ')

    await state.set_state('education_state')


@dp.message_handler(state='education_state')
async def add_education(message: types.message, state: FSMContext):
    education = message.text
    db.update_education(education=education, id=message.from_user.id)
    await message.answer('Ваш(а)и профессия, умения, навыки: ')

    await state.set_state('job')


@dp.message_handler(state='job')
async def add_job(message: types.message, state: FSMContext):
    jobs = message.text
    db.update_profession(profession=jobs, id=message.from_user.id)
    await message.answer('Знание языков: ')

    await state.set_state('language_state')


@dp.message_handler(state='language_state')
async def add_language(message: types.message, state: FSMContext):
    language = message.text
    db.update_language(language=language, id=message.from_user.id)
    await message.answer('Желательная работа: ')

    await state.set_state('desirable_job_state')


@dp.message_handler(state='desirable_job_state')
async def add_desirable_job(message: types.message, state: FSMContext):
    desirable_job = message.text
    db.update_desirable_job(desirable_job=desirable_job, id=message.from_user.id)
    await message.answer('Контакт в формате +998901234567: ')

    await state.set_state('contact')


@dp.message_handler(state='contact')
async def number(message: types.message, state: FSMContext):
    contact_1 = message.text
    db.update_number(number=contact_1, id=message.from_user.id)
    user1 = db.select_user(id=message.from_user.id)

    msg_text_1 = "\n".join(
            [f'%{user1[0]}%',
             hbold(user1[2]) + '\n\n' +
             hbold('Имя, Лет:  ') + f'{user1[3]}',
             hbold('О себе:  ') + f'{user1[4]}',
             hbold('Образование:  ') + f'{user1[5]}',
             hbold('Профессия:  ') + f'{user1[6]}',
             hbold('Языки:  ') + f'{user1[7]}',
             hbold('Желательная работа:  ') + f'{user1[8]}',
             '📞 ' + f'{int(user1[9])}']
        )

    await message.answer(msg_text_1, reply_markup=admin_send)

    await state.finish()

