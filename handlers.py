from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import kb
import config
from aiogram import flags
from aiogram.fsm.context import FSMContext
import utils

from Telegram import parser
from states import Gen

router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer('Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение')


# @router.message()
# async def message_handler(msg: Message):
#     await msg.answer(f'Твой ID: {msg.from_user.id}')


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "Выйти в меню")
async def menu(msg: Message):
    await msg.answer(config.menu, reply_markup=kb.menu)


# Тут типа основная функция работы приложения
# Нажал хочу расписание, далее выбор группы и запрос
# Или же сделать для кажого личное указание группы в условных настройках
@router.callback_query(F.data == "find_schedule")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.text_prompt)
    # TODO Тут он должен читать данные из кеша. Срочно переделать!!!
    await clbck.message.edit_text("Пока не работает")
    await clbck.message.answer(config.gen_exit, reply_markup=kb.exit_kb)


def get_schedule() -> str:
    pass


@router.message(Gen.text_prompt)
@flags.chat_action("typing")
async def generate_text(msg: Message, state: FSMContext):
    prompt = msg.text
    mesg = await msg.answer(config.gen_wait)
    res = await utils.generate_text(prompt)
    if not res:
        return await mesg.edit_text(config.gen_error, reply_markup=kb.iexit_kb)
    await mesg.edit_text(res[0] + config.text_watermark, disable_web_page_preview=True)
