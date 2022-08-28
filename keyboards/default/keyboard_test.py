from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Тест 1'),
            KeyboardButton(text='Тест 2'),
            KeyboardButton(text='Тест 3'),
            KeyboardButton(text='Тест 4')
        ],
        [
            KeyboardButton(text='Тест 5'),
            KeyboardButton(text='Тест 6'),
            KeyboardButton(text='Тест 7'),
            KeyboardButton(text='Тест 8')
        ],
        [
            KeyboardButton(text='Тест 9'),
            KeyboardButton(text='Тест 10'),
            KeyboardButton(text='Тест 11'),
            KeyboardButton(text='Тест 12'),
            KeyboardButton(text='Тест 13')
        ],
        [
            KeyboardButton(text='/menu')
        ]
    ],
    resize_keyboard=True
)