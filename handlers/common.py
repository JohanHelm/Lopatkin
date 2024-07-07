import os
import dotenv
from aiogram.types import Message, CallbackQuery
from keyboards.four_buttons import keyboard
from lexicon.messages import main_message

dotenv.load_dotenv("secrets/.env")

async def process_start_command(message: Message):
    await message.answer(main_message, reply_markup=keyboard)


async def show_mem(callback: CallbackQuery):
    await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.bot.send_photo(chat_id=callback.from_user.id,
                                  photo=os.getenv('PIC_ID'),
                                  caption=main_message,
                                  reply_markup=keyboard)

async def show_A2_value(callback: CallbackQuery):
    await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer(
        text=f"какойто текст\n\n{main_message}",
        reply_markup=keyboard
    )


