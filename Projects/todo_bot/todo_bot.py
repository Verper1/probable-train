import asyncio
import os
from aiogram import Bot, Dispatcher, types
from datetime import datetime
import logging
from dotenv import find_dotenv, load_dotenv
from aiogram.filters import CommandStart

load_dotenv(find_dotenv())

# Инициализация логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

# Словарь для хранения событий
events = {}


# Хэндлер для команды /start
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.reply('Привет! Напиши мне сообщение в формате (текст, время, дд:мм)')


# Хэндлер для сообщений
@dp.message()
async def handle_message(message: types.Message):
    if message.text.startswith('/'):
        return
    try:
        text = message.text
        parts = text.split(', ')
        if len(parts) != 3:
            await message.reply('Неправильный формат сообщения!')
            return
        text, time, date = parts
        day, month = date.split('.')
        event_time = datetime.strptime(f'{day}.{month}.2024 {time}', '%d.%m.%Y %H:%M')
        if message.chat.id not in events:
            events[message.chat.id] = []
        events[message.chat.id].append({'text': text, 'time': event_time})
        await message.reply('Событие добавлено!')
        print(events, event_time)
    except ValueError:
        await message.reply('Неправильный формат сообщения!')

    counter = 0

    while counter != 1:
        current_time = datetime.now()
        print(datetime.now())
        for chat_id, event_list in events.items():
            for event in event_list:
                event_time = event['time']
                if current_time >= event_time:
                    await bot.send_message(chat_id, f'Уведомление: {event["text"]}')
                    event_list.remove(event)
                    counter += 1
                    print(events)
        await asyncio.sleep(5)


# Запуск бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
