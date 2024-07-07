import os
import dotenv
from datetime import datetime
from aiogram.types import Message, CallbackQuery

from keyboards.four_buttons import keyboard
from lexicon.messages import main_message
from services.google_sheets.g_sheets_interaction import GoogleSheetsManager

dotenv.load_dotenv("secrets/.env")
gsm = GoogleSheetsManager("secrets/serviceacct_spreadsheet.json", os.getenv('SHEET_URL'))


async def process_start_command(message: Message):
    await gsm.auth_spread_work()
    await message.answer(main_message, reply_markup=keyboard)


async def show_mem(callback: CallbackQuery):
    await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.bot.send_photo(chat_id=callback.from_user.id,
                                  photo=os.getenv('PIC_ID'),
                                  caption=main_message,
                                  reply_markup=keyboard)


async def show_a2_value(callback: CallbackQuery):
    a2_value = await gsm.get_a2_from_g_sheets()
    await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer(
        text=f"{a2_value}\n\n{main_message}",
        reply_markup=keyboard
    )


async def get_user_date(message: Message):
    try:
        user_date = datetime.strptime(message.text, '%d.%m.%y').date()
        await gsm.b2_update(user_date.strftime('%d.%m.%y'))
        await message.answer(text=f"Дата верна.\n\n{main_message}",
                             reply_markup=keyboard)
    except ValueError:
        await message.answer(text=f"Дата не верна.\n\n{main_message}",
                             reply_markup=keyboard)
