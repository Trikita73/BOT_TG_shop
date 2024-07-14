from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

# from app.database.requests import get_all_contacts

import app.keyboards as kb
import app.database.requests as rq

contact_data = None 

router = Router()

'''
class Register(StatesGroup):
     name = State()
     age = State()
     number = State()
'''

# Start 
@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаровать!', reply_markup=kb.main)

#Catalog_Button
@router.message(F.text == 'Каталог')
async def catalog (message: Message):
    await message.answer('Выберите категорую товара', reply_markup=await kb.categories())
#Category
@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории', 
                                  reply_markup=await kb.items(callback.data.split('_')[1]))
#Item
@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}$', 
                                  reply_markup=await kb.items(callback.data.split('_')[1]))

#ComeBack
@router.callback_query(F.data.startswith('to_main'))
async def category(callback: CallbackQuery):
    await callback.answer('Главное меню, категории товара')
    await callback.message.answer('Выберите категорую товара', 
                                  reply_markup=await kb.categories())


#Сontact_Button
@router.message(F.text == 'Контакты')
async def contact(message: Message):
    #contact_text = "**Наши контакты:**\n"
    contact_text = f"ул. Пушкина\n"
    contact_text += f"дом. Колотушкина\n"
    contact_text += f"Телефон: +3 999 999 99 99\n"
    await message.answer('Наши контакты')
    await message.answer(contact_text)

#Contact_Button with Error (problem db)
'''
@router.message(F.text == 'Контакты')
async def contact(message: Message):
    contacts_data = await get_all_contacts()  
    message_text = ''
    if contacts_data:  # Check if list is not empty
        for contact in contacts_data:
            message_text += f"Название: {contact.name}\n"
            message_text += f"Город: {contact.city}\n"
            message_text += f"Адрес: {contact.street}\n\n"
    else:
        message_text = "В базе данных нет контактов"  # Inform user if no contacts found
    await message.answer(message_text)
'''

'''
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категрию товара', reply_markup=kb.catalog)


@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорю', show_alert=True)
    await callback.message.answer('Вы выбрали категорию футболок')


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Отправьте ваш номер телефона', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nВаш номер: {data["number"]}')
    await state.clear() 
'''