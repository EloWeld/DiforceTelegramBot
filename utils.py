from loader import MDB, bot


async def notifyAdmins(text: str):
    for admin in MDB.Users.find(dict(IsAdmin=True)):
        await bot.send_message(admin['TGID'], text)
