from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

test1_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True
)

test2_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Нет, это не так'),
            KeyboardButton(text='Пожалуй, так')
        ],
        [
            KeyboardButton(text='Верно'),
            KeyboardButton(text='Совершенно верно')
        ]
    ],
    resize_keyboard=True
)

test3_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Никогда или изредка'),
            KeyboardButton(text='Иногда')
        ],
        [
            KeyboardButton(text='Часто'),
            KeyboardButton(text='Почти всегда или постоянно')
        ]
    ],
    resize_keyboard=True
)

test4_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='-3', callback_data='1'),
            KeyboardButton(text='-2', callback_data='2'),
            KeyboardButton(text='-1', callback_data='3')
        ],
        [
            KeyboardButton(text='0', callback_data='4')
        ],
        [
            KeyboardButton(text='1', callback_data='5'),
            KeyboardButton(text='2', callback_data='6'),
            KeyboardButton(text='3', callback_data='7')
        ]
    ],
    resize_keyboard=True
)

test5_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет'),
        ]
    ],
    resize_keyboard=True
)

test6_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Почти или совсем нет'),
            KeyboardButton(text='Немного')
        ],
        [
            KeyboardButton(text='Умеренно')
        ],
        [
            KeyboardButton(text='Значительно'),
            KeyboardButton(text='Очень сильно')
        ]
    ],
    resize_keyboard=True
)

test7_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Никогда'),
            KeyboardButton(text='Редко')
        ],
        [
            KeyboardButton(text='Часто'),
            KeyboardButton(text='Почти всегда')
        ]
    ],
    resize_keyboard=True
)

test8_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Полностью не согласен(на)'),
            KeyboardButton(text='Не согласен(на)')
        ],
        [
            KeyboardButton(text='Cогласен(на)'),
            KeyboardButton(text='Полностью согласен(на)')
        ]
    ],
    resize_keyboard=True
)

test9_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='полностью соответствует (1)'),
            KeyboardButton(text='соответствует (1)'),
            KeyboardButton(text='скорее соответствует (1)')
        ],
        [
            KeyboardButton(text='если оба утверждения, на ваш взгляд, одинаково верны')
        ],
        [
            KeyboardButton(text='скорее соответствует (2)'),
            KeyboardButton(text='соответствует (2)'),
            KeyboardButton(text='полностью соответствует (1)')
        ]
    ],
    resize_keyboard=True
)

test10_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Никогда'),
            KeyboardButton(text='Один или два раза')
        ],
        [
            KeyboardButton(text='Примерно раз в неделю'),
            KeyboardButton(text='Примерно 2–3 раза в неделю')
        ],
        [
            KeyboardButton(text='Почти каждый день'),
            KeyboardButton(text='Каждый день')
        ]
    ],
    resize_keyboard=True
)

test11_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Нет'),
            KeyboardButton(text='Скорее нет')

        ],
        [
            KeyboardButton(text='Скорее да'),
            KeyboardButton(text='Да')
        ]
    ],
    resize_keyboard=True
)

test12_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Совершенно не согласен(на)'),
            KeyboardButton(text='Скорее не согласен(на)')
        ],
        [
            KeyboardButton(text='Нечто среднее')
        ],
        [
            KeyboardButton(text='Скорее согласен(на)'),
            KeyboardButton(text='Совершенно согласен(на)')
        ]
    ],
    resize_keyboard=True
)

test13_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Полностью не согласен'),
            KeyboardButton(text='Не согласен'),
            KeyboardButton(text='Скорее не согласен')
        ],
        [
            KeyboardButton(text='Нечно среднее')
        ],
        [
            KeyboardButton(text='Скорее согласен'),
            KeyboardButton(text='Согласен'),
            KeyboardButton(text='Полностью согласен')
        ]
    ],
    resize_keyboard=True
)
