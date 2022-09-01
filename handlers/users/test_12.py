

from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.utils.db_api import tests_results
from keyboards.default import kb_test
from keyboards.default.keyboard_tests import *
from keyboards.default.keyboard_test_enter import *
from psy_tests.psycho_tests import *
from psy_tests.scores import *


from loader import dp

from states.test_12_states import test_12

cnt = 0
name = 'test12'

@dp.message_handler(text='Шкала отчуждения от учебы и выгорания')
async def test12_e(message: types.Message):
    await message.answer(f'Тест "{about_tests[name]["name"]}"')
    await message.answer(f'О тесте: {about_tests[name]["info"]}')

    await message.answer(f'В тесте {len(about_tests[name]["questions"])} вопросов \n'
                         f'Приступить к тесту?', reply_markup=test12_enter)

@dp.message_handler(text='Прервать прохождение теста 12', state='*')
async def test12_answers_end(message: types.Message, state: FSMContext):
    global cnt
    cnt = 0
    test_12.answer12
    await message.answer(f'Тест прерван', reply_markup=kb_test)
    await state.finish()

@dp.message_handler(text='Приступить к тесту 12')
async def test12_answers(message: types.Message):
    global cnt
    await message.answer(f'{about_tests[name]["instruction"]}')
    await message.answer(f'Вопрос №{cnt + 1}: {about_tests[name]["questions"][cnt]}', reply_markup=test12_menu)
    cnt += 1
    await test_12.first()

@dp.message_handler(state=test_12.answer1)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer2)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer3)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer4)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer5)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer6)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer7)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer8)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer9)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer10)
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
    cnt+=1
    await test_12.next()

@dp.message_handler(state=test_12.answer11)
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
    await test_12.next()

@dp.message_handler(state=test_12.answer12)
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
    data = await state.get_data()
    list = []
    for i in range(len(data)):
        string = 'answer' + f'{i + 1}'
        list.append(data[string])

    id_ = message.from_user.id + 12
    await tests_results.new_result(id=id_,
                                   user_id=message.from_user.id,
                                   test_number=name,
                                   test_name=about_tests[name]["name"],
                                   results=test12_score(list),
                                   status='created')
    await tests_results.update_result(id=id_, results=test12_score(list))

    await message.answer(f'{test12_score(list)}', reply_markup=kb_test)
    cnt = 0
    await state.finish()
