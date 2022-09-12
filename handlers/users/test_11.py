

from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.utils.db_api import tests_results
from keyboards.default import kb_test
from keyboards.default.keyboard_tests import *
from keyboards.default.keyboard_test_enter import *
from psy_tests.psycho_tests import *
from psy_tests.scores import *


from loader import dp

from states.test_11_states import test_11

cnt = 0
name = 'test11'



@dp.message_handler(text='Прервать прохождение теста 11', state='*')
async def test11_answers_end(message: types.Message, state: FSMContext):
    global cnt
    cnt = 0
    await message.answer(f'Тест прерван', reply_markup=kb_test)
    await state.finish()

@dp.message_handler(text='Тест жизнестойкости')
async def test11_answers(message: types.Message):
    global cnt
    await message.answer(f'Тест "{about_tests[name]["name"]}"')
    await message.answer(f'О тесте: {about_tests[name]["info"]}')
    await message.answer(f'В тесте {len(about_tests[name]["questions"])} вопросов')
    await message.answer(f'{about_tests[name]["instruction"]}')
    await message.answer(f'Вопрос №{cnt + 1}: {about_tests[name]["questions"][cnt]}', reply_markup=test11_menu)
    cnt += 1
    await test_11.first()

@dp.message_handler(state=test_11.answer1)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer2)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer3)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer4)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer5)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer6)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer7)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer8)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer9)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer10)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer11)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer12)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer13)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer14)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer15)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer16)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer17)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer18)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer19)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer20)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer21)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer22)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer23)
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
    await test_11.next()

@dp.message_handler(state=test_11.answer24)
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
    data = await state.get_data()
    list = []
    for i in range(len(data)):
        string = 'answer' + f'{i + 1}'
        list.append(data[string])

    id_ = message.from_user.id + 11
    await tests_results.new_result(id=id_,
                                   user_id=message.from_user.id,
                                   test_number=name,
                                   test_name=about_tests[name]["name"],
                                   results=test11_score(list),
                                   status='created')
    await tests_results.update_result(id=id_, results=test11_score(list))

    await message.answer(f'{test11_score(list)}', reply_markup=kb_test)
    cnt = 0
    await state.finish()
