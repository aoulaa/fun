import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentType
from aiogram.utils.markdown import hbold

from data.config import admins, channels
from keyboards.default.menu_buttons import menu, serve, post_buttons
from keyboards.inline.butons import reply_1, admin_send
from loader import bot, dp, db
from states import Data, PostData


@dp.callback_query_handler(text="admin_msg")
async def send_to_admin(call: CallbackQuery):
    await call.answer(cache_time=60)

    text = call.message.html_text
    admin = admins[0]
    await bot.send_message(admin,  text, reply_markup=reply_1)
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
        await bot.send_message(user, 'Админ подтвердил ваш запрос.',
                               reply_markup=menu)
        await bot.send_message(target_channel, text)
        await call.message.delete_reply_markup()
    elif len(user) <= 8:
        target_channel = channels[0]
        text = call.message.html_text
        text = text[11:]
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


# sending ready post
@dp.message_handler(text='Отправить готовый пост 📄')
async def post_any(message: types.message):
    await message.answer('выбрие тип поста',
                         reply_markup=post_buttons)


@dp.message_handler(text='Пост без Фото📄')
async def send_ready_post(message: types.message):
    await message.answer('Отправьте мне текст поста на публикацию', )

    await PostData.save.set()


@dp.message_handler(state=PostData.save)
async def ready_post(message: types.Message, state: FSMContext):
    ready_post = message.html_text
    db.update_ready_post(ready_post=ready_post, id=message.from_user.id)
    user1 = db.select_user(id=message.from_user.id)

    msg_text = "\n".join(
        [f'%{user1[0]}%',
         user1[17]
         ]
    )
    await message.answer(msg_text, reply_markup=admin_send)
    await state.finish()


# send post with photo
@dp.message_handler(text='Пост с Фото📄')
async def send_post_with_photo(message: types.message, state: FSMContext):
    await message.answer('Отправьте фото на публикацию', )

    await state.set_state('photo_state')


@dp.message_handler(state='photo_state', content_types=ContentType.PHOTO)
async def catch_photo(message: types.message, state: FSMContext):
    await message.photo[-1].download()
    photo_id = message.photo[-1].file_id
    db.update_save_id(save_id=photo_id, id=message.from_user.id)
    await message.answer('отправьте текст')
    await state.set_state('text_state')


@dp.message_handler(state='text_state')
async def ready_post(message: types.Message, state: FSMContext):
    ready_post = message.html_text
    db.update_ready_post(ready_post=ready_post, id=message.from_user.id)
    user1 = db.select_user(id=message.from_user.id)
    print(user1[18])
    msg_text = "\n".join(
        [
            f'%{user1[0]}%',
            user1[17]
        ]
    )
    await message.answer_photo(photo=user1[18], caption=msg_text, reply_markup=admin_send)
    # await message.answer(msg_text, reply_markup=admin_send)
    await state.finish()
