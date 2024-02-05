from pyrogram import filters
from pyrogram.types import Message

from PrikshaXMusic import app
from PrikshaXMusic.core.call import PrikshaX

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await PrikshaX.stop_stream_force(message.chat.id)
