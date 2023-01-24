from handlers import *
from aiogram.utils import executor
from loader import dp, onBotStartup, V83

def test_V83():
    if V83:
        q = '''
        ВЫБРАТЬ
            Наименование КАК naimenovanie
        ИЗ
            Справочник.Номенклатура
        '''
        query = V83.NewObject("Query", q)
        selection = query.Execute().Choose()
        while selection.Next():
            print(f"Тут будет телеграм бот: {selection.naimenovanie}")


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=onBotStartup())
    test_V83()

if __name__ == "__main__":
    main()