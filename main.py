import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

bot = Bot(token='7083250219:AAHj6bwCq-RvWU3r6nmP1irXcWCwfoiwPOU')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')

@dp.message(F.text == 'Все хорошо')
async def nice(message: Message):
    await message.answer('Отлично!')

async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
