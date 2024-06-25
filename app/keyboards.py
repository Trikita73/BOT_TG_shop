from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                                InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')]
                                    ],
                            resize_keyboard=True,
                            input_field_placeholder='Choise menu item...')



async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def items(category_id):
    all_categories = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item{item.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main')) 
    return keyboard.adjust(2).as_markup()


# inline keyboard 

'''
catalog = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='T-shirt', callback_data='t-shirt')],
        [InlineKeyboardButton(text='Shoes', callback_data='shoes')],
        [InlineKeyboardButton(text='Caps', callback_data='cap')]])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                                           resize_keyboard=True)
'''