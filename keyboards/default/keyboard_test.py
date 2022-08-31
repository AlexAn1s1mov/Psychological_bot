from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_test = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Тест на канал восприятия')],
        [KeyboardButton(text='Оценка уровня реактивной и личностной тревожности')],
        [KeyboardButton(text='Диагностика психических состояний и свойств личности')],
        [KeyboardButton(text='Опросник «САН»')],
        [KeyboardButton(text='Теста Г. Айзенка')],
        [KeyboardButton(text='Шкала позитивного и негативного аффекта')],
        [KeyboardButton(text='Шкалы депрессии, тревоги и стресса')],
        [KeyboardButton(text='Шкала самооценки')],
        [KeyboardButton(text='Тест самообладания')],
        [KeyboardButton(text='Методика «Спектр психического здоровья»')],
        [KeyboardButton(text='Тест жизнестойкости')],
        [KeyboardButton(text='Шкала отчуждения от учебы и выгорания')],
        [KeyboardButton(text='Шкала субъективного счастья и удовлетворенности жизнью')],
        [
            KeyboardButton(text='/menu')
        ]
    ],
    resize_keyboard=True
)