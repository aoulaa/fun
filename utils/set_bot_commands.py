from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("restart", "Перзапустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("add_users", "толко админ"),
    ])
