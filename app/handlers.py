from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)
    await message.reply('Как дела?')

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
