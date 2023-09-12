from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def start_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="✅Я ознакомлен",
        callback_data="oznak")
    return builder.as_markup()

def payment_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="получить ссылку для оплаты",
        callback_data="payment")
    return builder.as_markup()