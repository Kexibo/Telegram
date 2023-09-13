from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import kb
import config
from aiogram import flags
from aiogram.fsm.context import FSMContext

from states import Gen

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(config.greet, reply_markup=kb.menu)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(config.menu, reply_markup=kb.menu)


@router.callback_query(F.data == "find_schedule")
async def find_schedule(clbck: CallbackQuery):
    await clbck.message.answer(config.change, reply_markup=kb.group)


# Тут типа основная функция работы приложения
# Нажал хочу расписание, далее выбор группы и запрос
# Или же сделать для кажого личное указание группы в условных настройках
@router.message(F.text == "Инфобез")
async def get_schedule(msg: Message):
    await msg.answer(get_schedule("infsec"), reply_markup=kb.exit_kb)

@router.message(F.text == "Прогер")
async def get_schedule(msg: Message):
    await msg.answer(get_schedule("prog"), reply_markup=kb.exit_kb)

def get_schedule(group) -> str:
    if group == "infsec":
        with open("data/infsec.txt", "r") as f:
            data = f.read()
            if data:
                return data
            else:
                return "Ошибка. Расписание отсутствует"

    elif group == "prog":
        with open("data/prog.txt", "r") as f:
            data = f.read()
            if data:
                return data
            else:
                return "Ошибка. Расписание отсутствует"

