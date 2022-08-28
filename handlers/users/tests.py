from aiogram import types


from loader import dp
from keyboards.default import kb_test


@dp.message_handler(text='Тесты')
async def test(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, \n'
                         f'Выберите тест для прохождения.', reply_markup=kb_test)

@dp.message_handler(text='Вернуться в меню')
async def test_(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, \n'
                         f'Выберите тест для прохождения.', reply_markup=kb_test)

