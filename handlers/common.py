from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from keyboards.four_buttons import keyboard
from lexicon.messages import main_message



async def process_start_command(message: Message):
    await message.answer(main_message, reply_markup=keyboard)


async def show_mem(callback: CallbackQuery):
    image_from_pc = FSInputFile("media/photos/pic1.jpg")
    result = await callback.message.answer_photo(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )

async def show_A2_value(callback: CallbackQuery):

    # result = await callback.message.answer(
    #     text="какойто текст", show_alert=False
    # )
    await callback.message.edit_text(
        text="какойто текст",
        reply_markup=keyboard
    )


