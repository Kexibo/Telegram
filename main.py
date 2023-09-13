"""Main file of project."""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

import config
import parser
from handlers import router

load_dotenv()


async def main():
    """
    This function started over app.
    """
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def async_req_to_schedule() -> None:
    """
    This function sends a request to the server
    once an hour and caches it to a file.
    :return:
    """
    while True:
        # progs_file - расписание прогеров
        # infsec_file - расписание инфобесов
        # TODO переделать в цикл для всех специальностей или вынести в метод и список туда
        # TODO сделать проверку актуальности расписания. Если поменялось -> всем кто подписан отправить
        # TODO Сделать проверку записи файла

        # Запросы и кеширование к прогерам и инфбезникам
        with open(config.progs_file, 'w') as file:
            # Записываем результат запроса в файл
            file.write(parser.gen_schedule(config.prog_login, config.prog_password))
        with open(config.infsec_file, 'w') as file:
            # Записываем результат запроса в файл
            file.write(parser.gen_schedule(config.infsec_login, config.infsec_password))
        print("Вроде как все файлы записаны")
        # Пауза на 1 час (3600 секунд)
        await asyncio.sleep(3600)


async def run_tasks():
    await asyncio.gather(main(), async_req_to_schedule())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run_tasks())
