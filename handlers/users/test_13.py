

from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.utils.db_api import tests_results
from keyboards.default import kb_test
from keyboards.default.keyboard_tests import *
from keyboards.default.keyboard_test_enter import *
from psy_tests.psycho_tests import *
from psy_tests.scores import *

from loader import dp

from states.test_13_states import test_13

cnt = 0
name = 'test13'


@dp.message_handler(text='Прервать прохождение теста ШССУЖ', state='*')
async def test13_answers_end(message: types.Message):
    await message.answer(f'Вы уверены?', reply_markup=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Прервать тест ШССУЖ')
        ],
        [
            KeyboardButton(text='Продолжить тест ШССУЖ')
        ]
    ],
    resize_keyboard=True
))

@dp.message_handler(text='Прервать тест ШССУЖ', state='*')
async def test13_answers_end_(message: types.Message, state: FSMContext):
    global cnt
    cnt = 0
    await message.answer(f'Тест прерван', reply_markup=kb_test)
    await state.finish()

@dp.message_handler(text='Продолжить тест ШССУЖ', state='*')
async def test13_answers_end__(message: types.Message, state: FSMContext):
    global cnt
    cnt-=1
    await message.answer(f'Вопрос №{cnt+1}: {about_tests[name]["questions"][cnt]}', reply_markup=test13_menu)
    cnt+=1


@dp.message_handler(text='Шкала субъективного счастья и удовлетворенности жизнью')
async def test13_answers(message: types.Message):
    global cnt
    await message.answer(f'<b>Тест "{about_tests[name]["name"]}"</b>\n'
                         f'<b>О тесте:</b> {about_tests[name]["info"]}\n'
                        f'<b>В тесте {len(about_tests[name]["questions"])} вопросов</b>\n'
                        f'<i>{about_tests[name]["instruction"]}</i>\n')
    await message.answer(f'Вопрос №{cnt + 1}: {about_tests[name]["questions"][cnt]}', reply_markup=test13_menu)
    cnt += 1
    await test_13.first()

@dp.message_handler(state=test_13.answer1)
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
        await test_13.next()

@dp.message_handler(state=test_13.answer2)
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
        await test_13.next()

@dp.message_handler(state=test_13.answer3)
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
        await test_13.next()

@dp.message_handler(state=test_13.answer4)
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
        await test_13.next()

@dp.message_handler(state=test_13.answer5)
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
        await test_13.next()

@dp.message_handler(state=test_13.answer6)
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
        await test_13.next()

@dp.message_handler(state=test_13.answer7)
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
        await test_13.next()

@dp.message_handler(state=test_13.answer8)
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
        await test_13.next()

@dp.message_handler(state=test_13.answer9)
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
    data = await state.get_data()
    list = []
    for i in range(len(data)):
        string = 'answer' + f'{i + 1}'
        list.append(data[string])

    id_ = message.from_user.id + 1
    await tests_results.new_result(id=id_,
                                   user_id=message.from_user.id,
                                   test_number=name,
                                   test_name=about_tests[name]["name"],
                                   results=test13_score(list),
                                   status='created')
    await tests_results.update_result(id=id_, results=test13_score(list))

    await message.answer(f'{test13_score(list)}', reply_markup=kb_test)
    data = await state.get_state()
    if data != None:
        cnt = 0
        await state.finish()



