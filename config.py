from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID",
"حط ايبي ايدي الي تريد تنصبله هنا")
APP_HASH = os.environ.get("APP_HASH",
"حط ايبي هاش الي تريد تنصبله هنا")
BOT_USERNAME = os.environ.get("BOT_USERNAME",
                           "حط يوزر بوت الي تريد تنصبله بدون @")
session = os.environ.get("TERMUX",
                        "حط كود تيرمكس الي تريد تنصبله هنا")
SESSION = os.environ.get("TERMUX",
                        "حط كود تيرمكس الي تريد تنصبله هنا")
token = os.environ.get("TOKEN",
                      "حط توكن بوت الي تريد تنصبله هنا")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
#كل الكودات تنحط بين ال ""
