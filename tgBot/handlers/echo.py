from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext


async def bot_echo(message: types.Message):
    text = [
        "Эхо без состояния",
        "Сообщение",
        message.text
    ]
    await message.answer("\n".join(text))


async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        f"Эхо в состоянии {state_name}",
        "Сообщение",
        message.text
    ]
    await message.answer("\n".join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentType.ANY)
