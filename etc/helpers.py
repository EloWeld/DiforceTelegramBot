
import datetime
from io import BytesIO

from aiogram import types

class rdotdict(dict):
    """
    a dictionary that supports dot notation
    as well as dictionary access notation
    usage: d = DotDict() or d = DotDict({'val1':'first'})
    set attributes: d.val2 = 'second' or d['val2'] = 'second'
    get attributes: d.val2 or d['val2']
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct):
        for key, value in dct.items():
            if hasattr(value, 'keys'):
                value = rdotdict(value)
            self[key] = value


def formatDate(user, date):
    return (date + datetime.timedelta(hours=user.settings.timezone.time)).strftime('%d.%m.%Y, %H:%M')

def wrap_media(media_bytes: bytes, **kwargs):
    """Wraps plain Bytes objects into InputMediaPhoto"""
    # First, rewind internal file pointer to the beginning so the contents
    #  can be read by InputFile class
    bytesio = BytesIO(media_bytes)
    bytesio.seek(0)
    return types.InputMediaPhoto(types.InputFile(bytesio), **kwargs)