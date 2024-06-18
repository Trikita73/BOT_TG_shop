import asyncio
from aiogram import Bot, Dispatcher, F

from app.handlers import router
from app.database.models import async_main

async def main():
    await async_main()
    bot = Bot(token='7083250219:AAHj6bwCq-RvWU3r6nmP1irXcWCwfoiwPOU') 
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
