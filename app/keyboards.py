from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')]
                                    ],
                            resize_keyboard=True,
                            imput_field_placeholder='Выберите пункт меню...')