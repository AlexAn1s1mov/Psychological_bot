

from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.utils.db_api import tests_results
from keyboards.default import kb_test
from keyboards.default.keyboard_tests import *
from keyboards.default.keyboard_test_enter import *
from psy_tests.psycho_tests import *
from psy_tests.scores import *


from loader import dp

from states.test_2_states import test_2


cnt = 0
name = 'test2'


@dp.message_handler(text='Прервать прохождение теста 2', state='*')
async def test2_answers_end(message: types.Message):
    await message.answer(f'Вы уверены?', reply_markup=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Прервать тест'),
            KeyboardButton(text='Продолжить тест 2')
        ]
    ],
    resize_keyboard=True
))

@dp.message_handler(text='Прервать тест', state='*')
async def test2_answers_end_(message: types.Message, state: FSMContext):
    global cnt
    cnt = 0
    await message.answer(f'Тест прерван', reply_markup=kb_test)
    await state.finish()

@dp.message_handler(text='Продолжить тест 2', state='*')
async def test2_answers_end__(message: types.Message, state: FSMContext):
    global cnt
    cnt-=1
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}', reply_markup=test2_menu)
    cnt+=1

@dp.message_handler(text='Оценка уровня реактивной и личностной тревожности')
async def test2_answers(message: types.Message):
    global cnt
    await message.answer(f'Тест "{about_tests[name]["name"]}"')
    await message.answer(f'О тесте: {about_tests[name]["info"]}')
    await message.answer(f'В тесте {len(about_tests[name]["questions"])} вопросов')
    await message.answer(f'{about_tests[name]["instruction"]}')
    await message.answer(f'Вопрос №{cnt + 1}: {about_tests[name]["questions"][cnt]}', reply_markup=test2_menu)
    cnt += 1
    await test_2.first()

@dp.message_handler(state=test_2.answer1)
async def test2_state1(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer1 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer2)
async def test2_state2(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer2 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer3)
async def test2_state3(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer3 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer4)
async def test2_state4(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer4 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer5)
async def test2_state5(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer5 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer6)
async def test2_state6(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer6 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer7)
async def test2_state7(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer7 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer8)
async def test2_state8(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer8 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer9)
async def test2_state9(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer9 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer10)
async def test2_state10(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer10 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer11)
async def test2_state11(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer11 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer12)
async def test2_state12(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer12 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer13)
async def test2_state13(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer13 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer14)
async def test2_state14(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer14 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer15)
async def test2_state15(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer15 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer16)
async def test2_state16(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer16 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer17)
async def test2_state17(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer17 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer18)
async def test2_state18(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer18 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer19)
async def test2_state19(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer19 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer20)
async def test2_state20(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer20 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer21)
async def test2_state21(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer21 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer22)
async def test2_state22(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer22 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer23)
async def test2_state23(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer23 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer24)
async def test2_state24(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer24 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer25)
async def test2_state25(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer25 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer26)
async def test2_state26(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer26 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer27)
async def test2_state27(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer27 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer28)
async def test2_state28(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer28 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer29)
async def test2_state29(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer29 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer30)
async def test2_state30(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer30 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer31)
async def test2_state31(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer31 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer32)
async def test2_state32(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer32 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer33)
async def test2_state33(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer33 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer34)
async def test2_state34(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer34 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer35)
async def test2_state35(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer35 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer36)
async def test2_state36(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer36 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer37)
async def test2_state37(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer37 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer38)
async def test2_state38(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer38 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer39)
async def test2_state39(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer39 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_2.next()

@dp.message_handler(state=test_2.answer40)
async def test2_state40(message: types.Message, state: FSMContext):
    global cnt
    answer = message.text.lower()
    flag = True
    for i in range(len(about_tests[name]["answers"])):
        if answer == about_tests[name]["answers"][i]['name'].lower():
            answer = about_tests[name]["answers"][i]['value'].lower()
            flag = False
            break
    if flag:
        await message.answer("Пожалуйста, выберите ответ, используя клавиатуру ниже.")
        return
    await state.update_data(answer40 = answer)
    data = await state.get_data()
    list = []
    for i in range(len(data)):
        string = 'answer' + f'{i + 1}'
        list.append(data[string])

    id_ = message.from_user.id + 2
    await tests_results.new_result(id=id_,
                                   user_id=message.from_user.id,
                                   test_number=name,
                                   test_name=about_tests[name]["name"],
                                   results=test2_score(list),
                                   status='created')
    await tests_results.update_result(id=id_, results=test2_score(list))

    await message.answer(f'{test2_score(list)}', reply_markup=kb_test)
    data = await state.get_state()
    if data != None:
        cnt = 0
        await state.finish()
