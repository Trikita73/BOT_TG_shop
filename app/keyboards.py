from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                                InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')]
                                    ],
                            resize_keyboard=True,
                            input_field_placeholder='Choise menu item...')


# inline keyboard 


catalog = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='T-shirt', callback_data='t-shirt')],
        [InlineKeyboardButton(text='Shoes', callback_data='shoes')],
        [InlineKeyboardButton(text='Caps', callback_data='cap')]])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                                           resize_keyboard=True)