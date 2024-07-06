from aiogram import Dispatcher
from aiogram import F
from aiogram.filters import Command

from handlers.common import process_start_command, show_mem, show_A2_value


def register_common(dp: Dispatcher):
    dp.message.register(process_start_command, Command(commands='start'))
    dp.callback_query.register(show_mem, F.data == 'take_a_pic')
    dp.callback_query.register(show_A2_value, F.data == 'take_A2_value')


