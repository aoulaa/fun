from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, CallbackQuery, KeyboardButton
from aiogram.utils.markdown import hbold
import re
from data.config import admins, channels
from keyboards.default.menu_buttons import serve, menu
from keyboards.inline.butons import admin_send, reply_1
from loader import dp, db, bot
from states import Data


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
             hbold(user1[9]) + '\n\n' +
             hbold('Название вашей фирмы/компании:  ') + f'{user1[10]}',
             hbold('Обязанности:  ') + f'{user1[11]}',
             hbold('График работы:  ') + f'{user1[12]}',
             hbold('Зарплата:  ') + f'{user1[13]}',
             hbold('Адрес:  ') + f'{user1[14]}',
             hbold('Контакт:  ') + f'{user1[15]}',
             ]
        )
    await message.answer(msg_text, reply_markup=admin_send)
    await state.finish()


@dp.callback_query_handler(text="admin_msg")
async def send_to_admin(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = call.message.html_text
    admin = admins[0]
    await bot.send_message(admin, text, reply_markup=reply_1)
    await call.message.delete_reply_markup()
    await call.message.answer('Ваше ответ отправлен админу ждите ответа.')


@dp.callback_query_handler(text="confirm")
async def confirm(call: CallbackQuery):
    await call.answer('вы одобрли этот пост', show_alert=True)
    user = re.findall(r'%[1-9].+%', call.message.html_text)
    user = user[0][1:-1]
    if len(user) == 10:
        target_channel = channels[0]
        text = call.message.html_text
        text = text[12:]
        await call.answer(cache_time=20)
        await bot.send_message(user, 'Админ подтвердил ваш запрос.',
                               reply_markup=menu)
        await bot.send_message(target_channel, text)
        await call.message.delete_reply_markup()
    elif len(user) <= 8:
        target_channel = channels[0]
        text = call.message.html_text
        text = text[11:]
        await call.answer(cache_time=20)
        await bot.send_message(user, 'Админ подтвердил ваш запрос.',
                               reply_markup=menu)
        await bot.send_message(target_channel, text)

        await call.message.delete_reply_markup()


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer(cache_time=20)

    await call.message.delete_reply_markup()
    await call.message.answer('вы отменили пост. '
                              'можете заполнять заново',
                              reply_markup=serve)


@dp.callback_query_handler(text="cancel_admin")
async def cancel_admin(call: CallbackQuery, state: FSMContext):
    user_id = re.findall(r'%[1-9].+%', call.message.text)
    user_id = user_id[0][1:-1]
    await call.answer(cache_time=20)
    await call.message.answer(hbold('Вы отменили пост, оставьте комментарий почему❗'))

    await call.message.delete_reply_markup()
    await Data.data1.set()
    await state.update_data(
        {"user_id": user_id}
    )


@dp.message_handler(state=Data.data1)
async def send_comment(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id_user = data.get("user_id")
    comment = message.text
    text = hbold('Ваш пост отменили по причине❗')
    await bot.send_message(id_user, f'{text}\n\n{comment}',
                           reply_markup=serve)
    await state.finish()
