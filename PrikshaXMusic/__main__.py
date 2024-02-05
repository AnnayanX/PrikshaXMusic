import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from PrikshaXMusic import LOGGER, app, userbot
from PrikshaXMusic.core.call import PrikshaX
from PrikshaXMusic.misc import sudo
from PrikshaXMusic.plugins import ALL_MODULES
from PrikshaXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PrikshaXMusic.plugins" + all_module)
    LOGGER("PrikshaXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await PrikshaX.start()
    try:
        await PrikshaX.stream_call("https://telegra.ph/file/a9bee668f448253a32020.jpg")
    except NoActiveGroupCall:
        LOGGER("PrikshaXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await PrikshaX.decorators()
    LOGGER("PrikshaXMusic").info(
        "Music Bot Started Successfully, Love From @PrikshaX"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("PrikshaXMusic").info("Stopping PrikshaXMusic Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
