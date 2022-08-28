from aiogram import types
from loader import dp

@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Тебе доступны следующие команды: \n'
                         f'/start - запуск бота \n'
                         f'/menu - переход в меню \n'
                         f'/profile - получение информации о пользователе из базы данных \n\n'
                         f'Кнопка "Тесты" открывает меню с доступными психологическими тестами \n\n'
                         f'Чтобы приступить к выполнению теста - нажмите на кнопку с названием теста \n\n'
                         f'Начатый тест необходимо пройти до конца')