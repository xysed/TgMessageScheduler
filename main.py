import asyncio
from datetime import datetime
import os
from pyrogram.client import Client
from config import (
    API_ID,
    API_HASH,
    CHAT_ID,
    SEND_DELAY,
    SEND_MESSAGE,
    SEND_OFFSET,
    MESSAGES_NUM,
    MAX_WORKERS,
)


async def schedule_message(client: Client, chat_id: int, text: str, date: datetime):
    print(f"schedule_message | {chat_id} | {date}")
    await client.send_message(chat_id=chat_id, text=text, schedule_date=date)


async def schedule_message_limited(
    semaphore: asyncio.Semaphore,
    client: Client,
    chat_id: int,
    text: str,
    date: datetime,
):
    async with semaphore:
        await schedule_message(client, chat_id, text, date)


async def main():
    if not os.path.exists("sessions"):
        os.makedirs("sessions")

    client = Client(name="main", api_id=API_ID, api_hash=API_HASH, workdir="sessions/")

    await client.start()

    print("Creating tasks...")

    semaphore = asyncio.Semaphore(MAX_WORKERS)
    tasks = []

    now = int(datetime.now().timestamp())
    for i in range(MESSAGES_NUM):
        date = now + 15 + (i * SEND_DELAY) + SEND_OFFSET
        tasks.append(
            schedule_message_limited(
                semaphore, client, CHAT_ID, SEND_MESSAGE, datetime.fromtimestamp(date)
            )
        )

    await asyncio.gather(*tasks)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Interrupted")
