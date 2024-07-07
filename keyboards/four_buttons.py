import os
import dotenv

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


dotenv.load_dotenv("secrets/.env")

url_button = InlineKeyboardButton(
    text='Ленина 1.',
    url='https://yandex.ru/maps/67/tomsk/?ll=84.951979%2C56.455644&z=19'
)

pay_button = InlineKeyboardButton(
    text='C Вас 2 рубля',
    url=os.getenv('PAY_LINK')
)

pic_button = InlineKeyboardButton(
    text='Мемасик',
    callback_data='take_a_pic'
)

A2_button = InlineKeyboardButton(
    text='А2 значение',
    callback_data='take_A2_value'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button, pay_button],
                     [pic_button, A2_button]]
)
