from main import bot, dp
from config import id

from aiogram.types import Message
from config import id

async def send_to_admin(dp):
    await bot.send_message(chat_id = id, text = 'Hey, what is your name?')

@dp.message_handler()
async def echo(message: Message):
    # await bot.send_message()
    if message.text == 'the best teacher?':
        await bot.send_message(chat_id=message.from_user.id, text='mr.Qabdushev')
    # if message.text == 'cool':
    #     await bot.send_message(chat_id=message.from_user.id, text = 'aitpa')
    # if message.text == True:
    #     await bot.send_message(chat_id=message.from_user.id, text='molodec')
    # if message.text == True:
    #     await bot.send_message(chat_id=message.from_user.id, text='ai krasava')
