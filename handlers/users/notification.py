from aiogram import types

from handlers.utils.db_api.quick_commands import select_all_users
from loader import dp, bot
from handlers.utils.db_api import quick_commands as commands
from aiogram import Dispatcher
import asyncio
import aioschedule
from data.config import admins

@dp.message_handler()
async def notice():
    users = await commands.select_all_users()
    for user in users:
        text = f'{user.first_name}, а ты давно проходил тесты?'
        await bot.send_message(chat_id = user.user_id, text = text)

async def scheduler():
    aioschedule.every().day.at("00:07").do(notice)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)