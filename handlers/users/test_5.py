

from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.utils.db_api import tests_results
from keyboards.default import kb_test
from keyboards.default.keyboard_tests import *
from keyboards.default.keyboard_test_enter import *
from psy_tests.psycho_tests import *
from psy_tests.scores import *


from loader import dp

from states.test_5_states import test_5

cnt = 0
name = 'test5'



@dp.message_handler(text='Прервать прохождение теста Г. Айзенка', state='*')
async def test5_answers_end(message: types.Message):
    await message.answer(f'Вы уверены?', reply_markup=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Прервать тест Г. Айзенка')
        ],
        [
            KeyboardButton(text='Продолжить тест Г. Айзенка')
        ]
    ],
    resize_keyboard=True
))

@dp.message_handler(text='Прервать тест Г. Айзенка', state='*')
async def test5_answers_end_(message: types.Message, state: FSMContext):
    global cnt
    cnt = 0
    await message.answer(f'Тест прерван', reply_markup=kb_test)
    await state.finish()

@dp.message_handler(text='Продолжить тест Г. Айзенка', state='*')
async def test5_answers_end__(message: types.Message, state: FSMContext):
    global cnt
    cnt-=1
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}', reply_markup=test5_menu)
    cnt+=1

@dp.message_handler(text='Теста Г. Айзенка')
async def test5_answers(message: types.Message):
    global cnt
    await message.answer(f'<b>Тест "{about_tests[name]["name"]}"</b>\n'
                         f'<b>О тесте:</b> {about_tests[name]["info"]}\n'
                        f'<b>В тесте {len(about_tests[name]["questions"])} вопросов</b>\n'
                        f'<i>{about_tests[name]["instruction"]}</i>\n')
    await message.answer(f'Вопрос №{cnt + 1}: {about_tests[name]["questions"][cnt]}', reply_markup=test5_menu)
    cnt += 1
    await test_5.first()

@dp.message_handler(state=test_5.answer1)
async def state1(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer2)
async def state2(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer3)
async def state3(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer4)
async def state4(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer5)
async def state5(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer6)
async def state6(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer7)
async def state7(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer8)
async def state8(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer9)
async def state9(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer10)
async def state10(message: types.Message, state: FSMContext):
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
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer11)
async def state11(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer12)
async def state12(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer13)
async def state13(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer14)
async def state14(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer15)
async def state15(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer16)
async def state16(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer17)
async def state17(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer18)
async def state18(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer19)
async def state19(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer20)
async def state20(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer21)
async def state21(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer22)
async def state22(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer23)
async def state23(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer24)
async def state24(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer25)
async def state25(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer26)
async def state26(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer27)
async def state27(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer28)
async def state28(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer29)
async def state29(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer30)
async def state30(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer31)
async def state31(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer32)
async def state32(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer33)
async def state33(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer34)
async def state34(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer35)
async def state35(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer36)
async def state36(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer37)
async def state37(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer38)
async def state38(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer39)
async def state39(message: types.Message, state: FSMContext):
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
        await test_5.next()

@dp.message_handler(state=test_5.answer40)
async def state40(message: types.Message, state: FSMContext):
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
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer41)
async def state41(message: types.Message, state: FSMContext):
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
    await state.update_data(answer41 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer42)
async def state42(message: types.Message, state: FSMContext):
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
    await state.update_data(answer42 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer43)
async def state43(message: types.Message, state: FSMContext):
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
    await state.update_data(answer43 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer44)
async def state44(message: types.Message, state: FSMContext):
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
    await state.update_data(answer44 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer45)
async def state45(message: types.Message, state: FSMContext):
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
    await state.update_data(answer45 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer46)
async def state46(message: types.Message, state: FSMContext):
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
    await state.update_data(answer46 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer47)
async def state47(message: types.Message, state: FSMContext):
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
    await state.update_data(answer47 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer48)
async def state48(message: types.Message, state: FSMContext):
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
    await state.update_data(answer48 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer49)
async def state49(message: types.Message, state: FSMContext):
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
    await state.update_data(answer49 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer50)
async def state50(message: types.Message, state: FSMContext):
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
    await state.update_data(answer50 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer51)
async def state51(message: types.Message, state: FSMContext):
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
    await state.update_data(answer51 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer52)
async def state52(message: types.Message, state: FSMContext):
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
    await state.update_data(answer52 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer53)
async def state53(message: types.Message, state: FSMContext):
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
    await state.update_data(answer53 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer54)
async def state54(message: types.Message, state: FSMContext):
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
    await state.update_data(answer54 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer55)
async def state55(message: types.Message, state: FSMContext):
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
    await state.update_data(answer55 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer56)
async def state56(message: types.Message, state: FSMContext):
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
    await state.update_data(answer56 = answer)
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}')
    cnt+=1
    data = await state.get_state()
    if data != None:
        await test_5.next()

@dp.message_handler(state=test_5.answer57)
async def state57(message: types.Message, state: FSMContext):
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
    await state.update_data(answer57 = answer)
    data = await state.get_data()
    list = []
    for i in range(len(data)):
        string = 'answer' + f'{i + 1}'
        list.append(data[string])

    id_ = message.from_user.id + 5
    await tests_results.new_result(id=id_,
                                   user_id=message.from_user.id,
                                   test_number=name,
                                   test_name=about_tests[name]["name"],
                                   results=test5_score(list),
                                   status='created')
    await tests_results.update_result(id=id_, results=test5_score(list))

    await message.answer(f'{test5_score(list)}', reply_markup=kb_test)
    data = await state.get_state()
    if data != None:
        cnt = 0
        await state.finish()

