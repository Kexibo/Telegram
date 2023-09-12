"""This file contains all states of chat-bot."""

from aiogram.fsm.state import StatesGroup, State


class Gen(StatesGroup):
    text_prompt = State()
