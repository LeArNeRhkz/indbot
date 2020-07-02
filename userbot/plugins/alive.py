"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
INDIANBOT_IS_ALIVE = ("**Have a great day ^.^** \n`🇮🇳BOT Status : ` **indbot**\n\n"
                     f"`My owner`: {DEFAULTUSER}\n\n"
                     "`Indian Bot Version:` [1.0](https://telegra.ph/INDIAN-06-15-6)\n`Python:` **3.7.4**\n"
                     "`Database Status:` **😀ALL OK**\n\n`Always with you, my master!\n`"
                     "**Bot Creator:** [🇮🇳indbot](t.me/pureindialover)\n"
                     "**Co-Owner:** [🇮🇳mani](t.me/AKASH_AM1)\n\n"
                     "     [🇮🇳Deploy This indbot🇮🇳](https://github.com/LeArNeRhkz/indbot)") 


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_message(chat, INDIANBOT_IS_ALIVE) 
