import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from handlers import questions
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup
from keyboards.for_questions import start_kb, payment_kb


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()


@dp.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "https://github.com/",
        reply_markup=start_kb(),
        disable_web_page_preview=False
    )



@dp.callback_query(F.data == "oznak")
async def answer_yes(callback: types.CallbackQuery):
    await callback.message.answer(
        "Это здорово!"
            
    )
    await callback.message.edit_reply_markup()
    await callback.message.answer(
        "Ссылка для оплаты:",
        reply_markup=payment_kb()
    )

@dp.callback_query(F.data == "payment")
async def answer_yes(callback: types.CallbackQuery):
    await callback.message.answer(
        "Ссылка отправлена"    
    )
    await callback.message.edit_reply_markup()

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())