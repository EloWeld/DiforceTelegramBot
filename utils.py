from loader import MDB, bot
from services.userService import UserService


async def notifyAdmins(text: str):
    for admin in UserService.Admins():
        await bot.send_message(admin['id'], text)

def split_long_text(text: str, max_length: int = 4000):
    parts = []
    while len(text) > max_length:
        split_position = text.rfind('\n', 0, max_length)
        if split_position == -1:
            split_position = max_length
        part = text[:split_position]
        parts.append(part)
        text = text[split_position:]
    parts.append(text)
    return parts


def prepareUserToPrint(xUser):
    xUser.roles = ', '.join([Texts.rus(x) for x in xUser.roles])
    xUser.opt = Texts.rus(xUser.opt)
    return xUser