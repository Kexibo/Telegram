"""This file contains all buttons."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="Узнать расписание", callback_data="find_schedule"),
    InlineKeyboardButton(text="Сходить н@х#й", callback_data="go_away")],
    [InlineKeyboardButton(text="Задонатить разработчикам", callback_data="money")],
    [InlineKeyboardButton(text="Хрень 2", callback_data="xx"),
    InlineKeyboardButton(text="Залупа 3", callback_data="xxx")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]

group = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Инфобез"),
    KeyboardButton(text="Прогер")], [KeyboardButton(text="◀️ Выйти в меню")]
], resize_keyboard=True)

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
#kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Узнать расписание", callback_data="find_schedule")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
