from .test_answers import *

def counter(data, array):
    res = 0
    for i in array:
        if data[i-1] == 'yes':
            res +=1
    return res

def test1_score(data):
    audio = [2, 6, 7, 13, 15, 17, 20, 24, 26, 33, 34, 36, 37, 43, 46, 48]
    visual = [1, 5, 8, 10, 12, 14, 19, 21, 23, 27, 31, 32, 39, 40, 42, 45]
    kinest = [3, 4, 9, 11, 16, 18, 22, 25, 28, 29, 30, 35, 38, 41, 44, 47]

    audio_res = counter(data, audio)
    visual_res = counter(data, visual)
    kinest_res = counter(data, kinest)
    level = lambda x : 'Высокий' if x >= 13 else ('Низкий' if x <= 7 else 'Средний')
    message = f"Аудиальный канал восприятия: {audio_res}. {level(audio_res)} уровень.\n" \
                f"Визуальный канал восприятия: {visual_res}. {level(audio_res)} уровень.\n" \
                f"Кинестетический канал восприятия: {kinest_res}. {level(audio_res)} уровень.\n"
    return message

def test2_score(data):
    rt = [2, 3, 5, 6, 8, 11, 12, 13, 16, 17]
    lt = [21, 22, 23, 24, 27, 28, 30, 31, 33, 34, 36, 37, 39]
    rt_res = 35
    lt_res = 35
    for i in range(0, 20):
        if i in rt:
            rt_res += int(data[i])
        else: rt_res = rt_res - int(data[i])

    for i in range(20, 40):
        if i in lt:
            lt_res += int(data[i])
        else: lt_res = lt_res - int(data[i])

    if rt_res <= 30:
        message = "Низкая реактивная тревожность"
    elif 31 <= rt_res and rt_res <= 45:
        message = "Умеренная реактивная тревожность"
    else:
        message = "Высокая реактивная тревожность"
    if lt_res <= 30:
        message += ", низкая личностная тревожность"
    elif 31 <= lt_res and lt_res <= 45:
        message += ", умеренная личностная тревожность"
    else:
        message += ", высокая личностная тревожность"
    return message

def test3_score(data):
    ud = [0, 2, 3, 6, 7, 8, 9, 12, 14, 18]
    ud_res = 0
    for i in range(0, 20):
        if i in ud:
            ud_res += int(data[i])
        else: ud_res += 5 - int(data[i])

    if ud_res <= 50:
        message = "У вас отсутствует депрессия"
    elif 51 <= ud_res <= 60:
        message = "У вас легкая депрессия ситуативного или невротического генеза"
    elif 61 <= ud_res <= 70:
        message = "У вас субдепрессивное состояние или маскированная депрессия"
    else:
        message = "У вас истинное депрессивное состояние"
    return message

def test4_score(data):
    being_q = [0, 1, 6, 7, 12, 13, 18, 19, 24, 25]
    activity_q = [2, 3, 8, 9, 14, 15, 20, 21, 26, 27]
    mood_q = [4, 5, 10, 11, 16, 17, 22, 23, 28, 29]
    inverse_q = [0, 1, 4, 5, 6, 7, 10, 11, 13, 16, 17, 18, 19,
                    22, 23, 24, 25, 28, 29]

    counter = lambda questions: \
        sum(8 - int(data[i]) if i in inverse_q
            else int(data[i])
            for i in questions) / len(questions)

    being_res = counter(being_q)
    activity_res = counter(activity_q)
    mood_res = counter(mood_q)

    sum_of_res = activity_res + being_res + mood_res
    a_proc = activity_res / sum_of_res * 100
    b_proc = being_res / sum_of_res * 100
    m_proc = 100 - b_proc - a_proc
    message = "Активность = {}/7, \n" \
                  "самочувствие = {}/7, \n" \
                  "настроение = {}/7. \n" \
                  "В процентном соотношении:\n активность - {:.2f}%, \n" \
                  "самочувствие - {:.2f}%, \n" \
                  "настроение - {:.2f}%". \
        format(activity_res, being_res, mood_res, a_proc, b_proc, m_proc)
    return message

def test5_score(data):
    sinc_q_yes = [5, 23, 35]
    sinc_q_no = [11, 17, 29, 41, 47, 53]
    extrav_q_yes = [0, 2, 7, 9, 12, 16, 21, 26, 38, 43, 45, 48, 52, 55]
    extrav_q_no = [4, 14, 19, 28, 31, 33, 36, 40, 50]
    neuro_q = [1, 3, 6, 8, 10, 13, 15, 18, 20, 22, 25, 27, 30, 32, 34, 37, 39, 42, 44, 46, 49, 51, 54, 56]

    counter = lambda array, value: \
        sum(str(data[i]) == value for i in array)

    sinc_res = counter(sinc_q_yes, 'yes') + counter(sinc_q_no, 'no')
    extrav_res = counter(extrav_q_yes, 'yes') + counter(extrav_q_no, 'no')
    neuro_res = counter(neuro_q, 'yes')

    message = ['', '', '']
    message[0] = "Показатель искренности - " + str(sinc_res) + " из 9, что свидетельствует о"
    if sinc_res <= 3:
        message[0] += "б откровенности"
    elif 4 <= sinc_res <= 6:
        message[0] += " ситуативности"
    else:
        message[0] += " лживости"
    message[1] = "Показатель экстравертности - " + str(extrav_res) + " из 24. Это означает, что вы "
    if extrav_res <= 2:
        message[1] += "сверхинтроверт"
    elif 3 <= extrav_res <= 6:
        message[1] += "интроверт"
    elif 7 <= extrav_res <= 10:
        message[1] += "потенциальный интроверт"
    elif 11 <= extrav_res <= 14:
        message[1] += "амбиверт"
    elif 15 <= extrav_res <= 18:
        message[1] += "потенциальный экстраверт"
    elif 19 <= extrav_res <= 22:
        message[1] += "экстраверт"
    else:
        message[1] += "сверхэкстраверт"
    message[2] = "Показатель невротизма - " + str(neuro_res) + " из 24. Это означает, что вы "
    if neuro_res <= 2:
        message[2] += "сверхконкордант"
    elif 3 <= neuro_res <= 6:
        message[2] += "конкордант"
    elif 7 <= neuro_res <= 10:
        message[2] += "потенциальный конкордант"
    elif 11 <= neuro_res <= 14:
        message[2] += "нормостеник"
    elif 15 <= neuro_res <= 18:
        message[2] += "потенциальный дискордант"
    elif 19 <= neuro_res <= 22:
        message[2] += "дискордант"
    else:
        message[2] += "сверхдискордант"
    message1 = f'{message[0]} \n {message[1]} \n {message[2]} \n '
    return message1

def count_message_test6(effect: int, low: int, middle: int,
                        name_of_effect: str):
    if effect <= low:
        message = 'Низкий'
    elif effect <= middle:
        message = 'Средний'
    else:
        message = 'Высокий'
    return message + f' уровень {name_of_effect} аффекта.\n'

def test6_score(data):
    positive_effect = sum(int(data[i]) for i in [0, 2, 4, 8, 9, 11, 13, 15, 16, 18])
    negative_effect = sum(int(data[i]) for i in [1, 3, 5, 6, 7, 10, 12, 14, 17, 19])

    message = 'У вас:\n'
    message += count_message_test6(positive_effect, 22, 39, 'позитивного')
    message += count_message_test6(negative_effect, 15, 32, 'негативного')
    message += '\nВысокий уровень позитивного аффекта – состояние приятной вовлеченности, ' \
                   'высокой энергичности и полной концентрации. Низкий уровень - состояние уныния и вялости.\n\n' \
                   'Высокий уровень негативного аффекта – состояние субъективно переживаемого страдания, ' \
                   'неприятной вовлеченности (различной по содержанию – это может быть гнев, отвращение, презрение, ' \
                   'вина, страх, раздражительность). Низкий уровень - состояние спокойствия и безмятежности.'
    return message

def test7_score(data):
    counter = lambda array: sum(int(data[i]) for i in array)
    depression = counter([2, 4, 9, 12, 15, 16, 20])
    anxiety = counter([1, 3, 6, 8, 14, 18, 19])
    stress = counter([0, 5, 7, 10, 11, 13, 17])
    message = ''
    for name, answers, number in zip(
        ['Шкала депрессии', 'Шкала тревоги', 'Шкала стресса'],
        [depression_answers, anxiety_answers, stress_asnwers],
        [depression, anxiety, stress]
    ):
        message += f"{name}:\n"
        message += next(ans for scale, ans in answers.items() if number <= scale)
        message += '\n'

    return message

def test8_score(data):
    self_rating = sum(int(data[i]) for i in [0, 2, 3, 6, 9]) + \
                sum(3 - int(data[i]) for i in [1, 4, 5, 7, 8])
    message = 'Ваша самооценка на данный момент:\n'
    if self_rating <= 15:
        message += 'Ощущение неуверенности в себе. ' \
                    'Болезненное переживание критических замечаний в свой адрес.' \
                    ' Склонность подстраиваться под мнение других людей.' \
                    ' Избыточная застенчивость и скромность'
    else:
        message += 'Переживание уверенности в себе и своих поступках. ' \
                    'Склонность адекватно реагировать на критику и замечания других.' \
                    ' Способность трезво оценивать свои действия'
    return  message

def test9_score(data):
    # восходящие
    answers = {i: int(data[i]) for i in [1, 5, 7, 8, 9]}
    # низходящие
    answers.update({i: 8 - int(data[i]) for i in [2, 4]})

    personal = sum(answers[i] for i in [2, 4, 7])
    eventful = sum(answers[i] for i in [5, 8])
    existential = sum(answers[i] for i in [1, 9])
    general = sum(answers.values())

    message = ''
    for name, answers, number in zip(
        ['Шкала личностного самообладания', 'Шкала событийного самообладания',
        'Шкала экзистенциального самообладания', 'Общий показатель самообладания'],
        [personal_answers, eventful_answers, existential_answers, general_answers],
        [personal, eventful, existential, general]
    ):
        message += f'{name}:\n'
        message += next(ans for scale, ans in answers.items() if number <= scale)
        message += '\n\n'
    return message

def test10_score(data):
    emotional = sum(int(data[i]) for i in range(0, 3))
    social = sum(int(data[i]) for i in range(3, 8))
    psycho = sum(int(data[i]) for i in range(8, 14))
    general = emotional + social + psycho
    message = f'Эмоциональное благополучие: {emotional}/15\n' \
                f'Социальное благополучие: {social}/25\n' \
                f'Психологическое благополучие: {psycho}/30\n' \
                f'Общий показатель благополучия: {general}/70\n\n'

    message += 'Состояние благополучия по К. Кизу: '
    if all(int(data[i]) in [0, 1] for i in range(0, 3)) and \
            sum(int(data[i]) in [0, 1] for i in range(3, 14)) >= 6:
        message += 'угнетение'
    elif sum(int(data[i]) in [4, 5] for i in range(0, 3)) >= 1 and \
            sum(int(data[i]) in [4, 5] for i in range(3, 14)) >= 6:
        message += 'процветание'
    else:
        message += 'умеренное благополучие'

    message += '\n\nИнтерпретация общего показателя благополучия: {}'.format(
        next(ans for scale, ans in general_resilience.items() if general <= scale)
    )
    return message

def test11_score(data):
        # count answers
    answers = {i: int(data[i]) - 1 for i in
                [2, 6, 10, 11, 19, 22, 23]}
    answers.update(
        {i: 4 - int(data[i]) for i in
            [0, 1, 3, 4, 5, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 20, 21]}
    )

    # count results
    general = sum(answers.values())
    involvement = sum(answers[i] for i in
                        [1, 2, 3, 7, 10, 11, 14, 18, 19, 20])
    control = sum(answers[i] for i in
                    [0, 4, 6, 9, 16, 17, 21, 22])
    taking_risk = sum(answers[i] for i in
                        [5, 8, 12, 13, 15, 23])

    counter = lambda minimum, medium, number:\
        next(mes for num, mes in zip([minimum, medium, float('inf')],
                                    ['низкий', 'средний', 'высокий'])
                if number <= num)
    message = 'Показатели (актуальный для людей в возрасте 18-75):\n'
    for name, numbers, value in \
            zip(['Общий показатель жизнестойкости', 'Вовлеченность', 'Контроль', 'Принятие риска'],
                [(39, 62), (17, 27), (12, 21), (8, 15)],
                [general, involvement, control, taking_risk]):
        message += f'{name}: {counter(numbers[0], numbers[1], value)}\n'

    return message

def test12_score(data):
    burnout = 0
    for i in range(len(data)):
        burnout += (int(data[i]))
    grade, text = next(answer for number, answer in burnout_answers.items()
                        if burnout <= number).values()
    message = f'Ваш уровень выгорания: {burnout}/{len(data) * 5}, ' \
                f'{grade} уровень.\n{text}'
    return message

def test13_score(data):
    message = None
    satisfaction = sum(int(data[i]) for i in range(0, 5))
    # Пункт 9 - обратный
    happiness = sum(int(data[i]) for i in range(5, 8)) +\
                (7 - int(data[8]))
    message = 'Показатель удовлетворенности жизнью - {}\n' \
                'Показатель субъективного счастья - {}'.format(
        next(grade for number, grade in satisfaction_answers.items() if satisfaction <= number),
        next(grade for number, grade in happiness_answers.items() if happiness <= number)
    )

    return message
