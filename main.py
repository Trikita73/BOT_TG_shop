import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message


bot = Bot(token='7083250219:AAHj6bwCq-RvWU3r6nmP1irXcWCwfoiwPOU')
dp = Dispatcher()


@dp.message()
async def cmd_start(message):
    await message.answer('Привет!')
    await message.reply('Как дела?')

async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
