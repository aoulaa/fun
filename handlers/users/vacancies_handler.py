from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from keyboards.inline.butons import admin_send
from loader import dp, db


@dp.message_handler(text='💼 нужен сотрудник')
async def job_want(message: types.message, state: FSMContext):
    await message.answer('Название вашей объявление:\n\n'
                         'например:  требуется менеджер по продажам.',
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state("needed_state")


@dp.message_handler(state='needed_state')
async def add_worker(message: types.message, state: FSMContext):
    worker = message.text
    db.update_needed(needed=worker, id=message.from_user.id)
    await message.answer('Название вашей фирмы/компании:')

    await state.set_state("company_name")


@dp.message_handler(state='company_name')
async def add_company_name(message: types.message, state: FSMContext):
    company = message.text
    db.update_company_name(company_name=company, id=message.from_user.id)
    await message.answer('Обязанности: ')

    await state.set_state('duties_state')


@dp.message_handler(state='duties_state')
async def add_duties(message: types.message, state: FSMContext):
    duties = message.text
    db.update_duties(duties=duties, id=message.from_user.id)
    await message.answer('График работы: ')

    await state.set_state('scheduled_state')


@dp.message_handler(state='scheduled_state')
async def add_scheduled(message: types.message, state: FSMContext):
    schedule = message.text
    db.update_schedule(schedule=schedule, id=message.from_user.id)
    await message.answer('Зарплата: ')

    await state.set_state('salary_state')


@dp.message_handler(state='salary_state')
async def add_salary(message: types.message, state: FSMContext):
    salary = message.text
    db.update_salary(salary=salary, id=message.from_user.id)
    await message.answer('Адрес: ')

    await state.set_state('address_state')


@dp.message_handler(state='address_state')
async def add_address(message: types.message, state: FSMContext):
    address = message.text
    db.update_address(address=address, id=message.from_user.id)
    await message.answer('Контакт: ')

    await state.set_state('contact_state')


@dp.message_handler(state='contact_state')
async def add_contact(message: types.message, state: FSMContext):

    contact = message.text
    db.update_contact(contact=contact, id=message.from_user.id)
    user1 = db.select_user(id=message.from_user.id)

    msg_text = "\n".join(
            [f'%{user1[0]}%',
             hbold(user1[10]) + '\n\n' +
             hbold('Название вашей фирмы/компании:  ') + f'{user1[11]}',
             hbold('Обязанности:  ') + f'{user1[12]}',
             hbold('График работы:  ') + f'{user1[13]}',
             hbold('Зарплата:  ') + f'{user1[14]}',
             hbold('Адрес:  ') + f'{user1[15]}',
             hbold('Контакт:  ') + f'{user1[16]}',
             ]
        )
    await message.answer(msg_text, reply_markup=admin_send)
    await state.finish()


