import logging
from info import NM_CHAT, NM_TIME
from pyrogram import Client, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions

TIMEZONE = Asia/Kolkata # you can change it.

NM_START = NM_TIME.split('-')[0]

NM_END = NM_TIME.split('-')[1]


async def group_close(client, message):
    try:
        await client.send_message(
                NM_CHAT,
                "Group is Closing!"
                )
        await client.set_chat_permissions(
                NM_CHAT,
                ChatPermissions()
                )
    except BaseException as e:
        await client.send_message(
                NM_CHAT,
                f"**Error while closing group:**"
                )

async def group_open(client, message):
    try:
        await client.send_message(
                NM_CHAT,
                "Opened group"
                )
        await client.set_chat_permissions(
                NM_CHAT,
                ChatPermissions(
                    can_send_messages=True
                    )
                )
    except BaseException as e:
        await client.send_message(
                NM_CHAT,
                f"**Error while opening group:**"
                )


scheduler = AsyncIOScheduler(timezone=TIMEZONE)
scheduler.add_job(group_close, trigger="cron", hour=21, minute=31)
scheduler.add_job(group_open, trigger="cron", hour=8, minute=1)
scheduler.start()