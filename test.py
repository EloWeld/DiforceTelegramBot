import json
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

# Инициализируйте SDK
default_app = firebase_admin.initialize_app(credentials.Certificate('firebase_creds.json'))


action_code_settings = auth.ActionCodeSettings(
    url='https://api-seller.ozon.ru/v2/posting/fbo/list',
    handle_code_in_app=True,
)
a = [
{
"ID": "RS0000001",
"FullName": "Романенко Вадим",
"Phone": "89994479138",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "RS0000002",
"FullName": "Уточкин Дмитрий",
"Phone": "89994458955",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "RS0000003",
"FullName": "ВТБ RedSale",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Нет"
},
{
"ID": "RS0000004",
"FullName": "ЗАКАЗЫ ИНТЕРНЕТ-МАГАЗИН",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "RS0000005",
"FullName": "Розничный покупатель",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "000000014",
"FullName": "Токарь Дмитрий",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "000000015",
"FullName": "Кузьмин Мирослав Владимирович(личная)",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "КРУПНЫЙ ОПТ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "000000016",
"FullName": "недостача",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "000000017",
"FullName": "НЕДОСТАЧА TREQA",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "000000018",
"FullName": "Частное лицо (возврат)",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000001",
"FullName": "НЕДОСТАЧА Hoco",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000002",
"FullName": "ИП Кузьмин В.И. ДиФорс",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000003",
"FullName": "ИП Кузьмин В.И. Июнь",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000004",
"FullName": "ХОЗКОМПЛЕКТ Толстоноженко Олег Владимирович",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000005",
"FullName": "ХОЗКОМПЛЕКТ Буш Олег",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000006",
"FullName": "ИП Казаков Степан Сергеевич",
"Phone": "",
"INN": "246314975850",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000007",
"FullName": "КРАСНОЯРСКОЕ ОТДЕЛЕНИЕ N 8646 ПАО СБЕРБАНК",
"Phone": "",
"INN": "7707083893",
"KPP": "246602001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000008",
"FullName": "общество с ограниченной ответственностью \"Лекс\"",
"Email": "<sgegechkori@regionsgroup.ru>",
"Phone": "",
"INN": "2466113042",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000009",
"FullName": "Общество с ограниченной ответственностью \"ЕнисейТехноСервис\"",
"Phone": "",
"INN": "2462201996",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000010",
"FullName": "ООО айцентр",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000011",
"FullName": "ХОЗКОМПЛЕКТ Ихсанов Роман",
"Phone": "89233641783",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000012",
"FullName": "ХОЗКОМПЛЕКТ Дарья",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000013",
"FullName": "Хоменко Сергей Николаевич",
"Phone": "89293015241",
"OrganizationType": "Физ. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000014",
"FullName": "ХОЗКОМПЛЕКТ Алексей Иванюков",
"Phone": "89607576257",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000015",
"FullName": "Железняков Николай Ильич",
"Phone": "89232770304",
"INN": "243400123170",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000016",
"FullName": "ИП Слободчиков Андрей Валерьевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000017",
"FullName": "ИП Каверзина З.Н. (Старая карта)",
"Phone": "89080135224",
"INN": "240716154411",
"KPP": "240701001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000018",
"FullName": "СНТ Погода",
"Phone": "89082229912",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000019",
"FullName": "ИП Овчаров Сергей Викторович",
"Phone": "9135321020",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000020",
"FullName": "ИП Меднова Мария Владимировна",
"Phone": "89135350936",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ИН0000001",
"FullName": "СбербанкИюнь",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Нет"
},
{
"ID": "DI0000021",
"FullName": "ИП Герасимов Александр Геннадьевич",
"Email": "2151688@mail.ru",
"Phone": "89233491000",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000023",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000024",
"FullName": "Сбербанк",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Нет"
},
{
"ID": "DI0000022",
"FullName": "Данилов Андрей Александрович",
"Phone": "89233017677",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000025",
"FullName": "ХОЗКОМПЛЕКТ Илья Касатов",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000026",
"FullName": "ИП Филимонов Александр",
"Phone": "9504373404",
"INN": "241300164997",
"KPP": "241301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000027",
"FullName": "ИП Бондаренко Светлана Вячеславовна",
"Email": "Teremokach@gmail.com",
"Phone": "9029792788",
"INN": "244306857584",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000027",
"FullName": "ИП Бондаренко Светлана Вячеславовна",
"Email": "Teremokach@gmail.com",
"Phone": "89029792785",
"INN": "244306857584",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000028",
"FullName": "ХОЗКОМПЛЕКТ Марина Самовьюк",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000029",
"FullName": "ХОЗКОМПЛЕКТ Чен",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000030",
"FullName": "ИП Горбунов Олег Витальевич",
"Phone": "89029423124",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000030",
"FullName": "ИП Горбунов Олег Витальевич",
"Phone": "2588369",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000031",
"FullName": "ИП Ахмадеев Гаделжан Галимзянович",
"Phone": "29220286",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000032",
"FullName": "ИП Уланов Анатолий Анатольевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000033",
"FullName": "ИП Гуляева Елена Анатольевна",
"Email": "hoztovarish24@yandex.ru",
"Phone": "",
"INN": "246602728825",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000034",
"FullName": "ИП Черноокова Наталья Сергеевна",
"Phone": "9135341373",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000035",
"FullName": "ИП Бореева Наталья Валерьевна",
"Phone": "9135614233",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000036",
"FullName": "ИП Филиппова Татьяна Михайловна",
"Email": "filippova_222@mail.ru",
"Phone": "89086589286",
"INN": "381301387338",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000037",
"FullName": "ИП Убельда Станислав Станиславович",
"Phone": "9029598062",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000038",
"FullName": "ИП Фролов Дмитрий Николаевич",
"Phone": "+79333354553",
"INN": "246307713878",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000039",
"FullName": "ИП Данилова Людмила Владимировна",
"Email": "lyudmila_danilov@mail.ru",
"Phone": "89233642394",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000040",
"FullName": "ИП Варданян Вардан Ашотович",
"Phone": "9233044473",
"INN": "312241111000",
"KPP": "312201001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000041",
"FullName": "ХОЗКОМПЛЕКТ Чернов Алексей Александрович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000042",
"FullName": "ХОЗКОМПЛЕКТ Марков Евгений",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000043",
"FullName": "ИП Кайдалова В.И.",
"Phone": "923324526",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000044",
"FullName": "ИП Маркова Татьяна Валерьевна",
"Email": "info@24domovenok.ru",
"Phone": "89632568899",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000045",
"FullName": "ИП Воронов Кирилл Сергеевич",
"Email": "k.voronov@mail.ru",
"Phone": "",
"INN": "24658932795",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000046",
"FullName": "ПОДАРКИ РОЗНИЦА (старая карточка)",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000047",
"FullName": "ИП Кулишова Маргарита Альбертовна",
"Phone": "",
"INN": "242800760171",
"KPP": "242801001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000048",
"FullName": "Резванцев Дмитрий",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000050",
"FullName": "ХОЗКОМПЛЕКТ Котов Константин Николаевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000051",
"FullName": "ИП Плавко Сергей Анатольевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000052",
"FullName": "ИП Тартынский Андрей Николаевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000053",
"FullName": "ООО  Тайга",
"Phone": "89631834445",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000054",
"FullName": "ООО \"Красгеосервис\"",
"Email": "nik41969@yandex.ru",
"Phone": "89620821602",
"INN": "2465076895",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000055",
"FullName": "ИП Пугачев Павел Валентинович",
"Phone": "89832861590",
"INN": "246500559134",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000056",
"FullName": "ИП Лысак Александр Викторович",
"Phone": "",
"INN": "24030005665",
"KPP": "240301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000057",
"FullName": "ХОЗКОМПЛЕКТ Мельников Станислав Сергеевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000058",
"FullName": "ИП Сусекова Марина Генадиевна",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000059",
"FullName": "ИП Евстафьева Ирина Леонидовна",
"Phone": "89333213350",
"INN": "240801782128",
"KPP": "240801001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000060",
"FullName": "ИП Вислов Виталий Валерьевич",
"Email": "v.v.vislov@mail.ru",
"Phone": "89233379977",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000061",
"FullName": "ИП Шмаль Елена Сергеевна",
"Phone": "89029170016",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000062",
"FullName": "ИП Шожап Р. Ш.",
"Phone": "9235984848",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000063",
"FullName": "ИП Шестакова Галина Алекасандровна",
"Phone": "89049472751",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000064",
"FullName": "ХОЗТОВАРЫ Максим Углов",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000065",
"FullName": "ХОЗКОМПЛЕКТ Силуянов Иван",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000066",
"FullName": "БРАК (ПРОЧИЕ БРЕНДЫ)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000067",
"FullName": "ИП AppStore",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000068",
"FullName": "УЦЕНКА ТОВАРА",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000069",
"FullName": "ИП Соруктуг Амир Эдуардович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000070",
"FullName": "ЗАЙМ 12% (Командор 02.07.2018г.)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000071",
"FullName": "ИП Мерзляков Николай Ильич",
"Email": "nikolm42@mail.ru",
"Phone": "89232770304",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000072",
"FullName": "Ч.А. Архипов Владислав Сергеевич",
"Phone": "89135690423",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Нет"
},
{
"ID": "DI0000073",
"FullName": "ИП Жданова Оксана Владимировна",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000074",
"FullName": "ИП Соколовский Сергей Васильевич",
"Phone": "",
"INN": "241600131103",
"KPP": "241601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000086",
"FullName": "ИП Храмченков Вячеслав Николаевич",
"Email": "hramchenkov2015@yandex.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000087",
"FullName": "ХОЗКОМПЛЕКТ Косинов Дмитрий",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000088",
"FullName": "ИП Кардаш Татьяна Ивановна",
"Email": "eplus-24@mail.ru",
"Phone": "89836113650",
"INN": "245302015067",
"KPP": "245301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000089",
"FullName": "Наушники AOMALE",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000090",
"FullName": "WOW",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000093",
"FullName": "Re-Sale",
"Email": "by_new_iphone@mail.ru",
"Phone": "89659058117",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000091",
"FullName": "ИП Алиханов Антип Иванович",
"Email": "killprice24@yandex.ru",
"Phone": "",
"INN": "246500578610",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000092",
"FullName": "ИП Сидоренков Владимир Олегович",
"Email": "kolan861129k@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000094",
"FullName": "ооо тк Телезон",
"Phone": "",
"INN": "2460087999",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000095",
"FullName": "ООО \"ДубльГис\"",
"Phone": "",
"INN": "5405276278",
"KPP": "997750001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000096",
"FullName": "ИП Ишунин Ю.Г.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000097",
"FullName": "ИП Абдулжелилова Секинат Гюльмагомедовна",
"Phone": "89080180558",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000098",
"FullName": "ХОЗКОМПЛЕКТ Демин Роман",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000099",
"FullName": "ИП Едигарев Павел Викторович",
"Email": "79029820352@yandex.ru",
"Phone": "89029820352",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000100",
"FullName": "ИП Евдокименко Анжелика Хачатуровна",
"Phone": "",
"INN": "245304131090",
"KPP": "245301001",
"OrganizationType": "Юр. лицо",
"ContractType": "Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000101",
"FullName": "ИП Никулин В.В.",
"Email": "val2806@mail.ru",
"Phone": "89135647095",
"INN": "246512240180",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000102",
"FullName": "ИП Попов Сергей Николаевич",
"Phone": "89029403332",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000102",
"FullName": "ИП Попов Сергей Николаевич",
"Phone": "89130438502",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000103",
"FullName": "Старые чехлы и зарядки",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "RS0000006",
"FullName": "Олеся Мясина",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000104",
"FullName": "ИП Полосин Юрий Викторович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000105",
"FullName": "ИП Кевбрина С.Б.",
"Email": "kevbrina_svetlana@mail.ru",
"Phone": "89504190144",
"INN": "241200007648",
"KPP": "241201001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000106",
"FullName": "ХОЗКОМПЛЕКТ Самовьюк И.А.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000107",
"FullName": "ИП Краюхина О.А.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000108",
"FullName": "ХОЗКОМПЛЕКТ Крылов Андрей Владимирович",
"Phone": "89029926470",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000109",
"FullName": "ИП Бердюгин А.С.",
"Phone": "9293204020",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000110",
"FullName": "ХОЗКОМПЛЕКТ Поленчик М.В.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000111",
"FullName": "ХОЗКОМПЛЕКТ Павленкович Леонид Александрович",
"Phone": "89293384392",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000112",
"FullName": "Глаас Ольга",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000113",
"FullName": "ИП Рыбкина Наталья Владимировна",
"Phone": "89059765494",
"INN": "246530199383",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000114",
"FullName": "ХОЗКОМПЛЕКТ Жарый И.М.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000117",
"FullName": "ХОЗКОМПЛЕКТ Шиферштейн Денис",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000115",
"FullName": "ООО СК \"Кристалл\" (Уборка в ТРЦ Июнь)",
"Phone": "",
"INN": "2465315529",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000116",
"FullName": "РАСХОДЫ ПО КАРТЕ",
"Phone": "",
"INN": "7707083893",
"KPP": "770701001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000118",
"FullName": "ИП Боровский С.О.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000122",
"FullName": "Заповедная вода",
"Phone": "",
"INN": "2464233440",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000128",
"FullName": "ООО Спектр Логистики",
"Phone": "",
"INN": "5404503489",
"KPP": "540401001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000129",
"FullName": "ООО НЦ Лидер",
"Phone": "",
"INN": "2465285024",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000130",
"FullName": "Комиссия в другие банки",
"Phone": "",
"INN": "7707083893",
"KPP": "770701001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000119",
"FullName": "ИП Довгулев Артем Владимирович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000120",
"FullName": "ИП Багрец",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000121",
"FullName": "ИП Лазарев Николай",
"Email": "smartfix124@gmail.com",
"Phone": "89535867949",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000121",
"FullName": "ИП Лазарев Николай",
"Email": "<smartfix124@gmail.com>",
"Phone": "89535867949",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000123",
"FullName": "ИП Юшкова Светлана Алексеевна",
"Email": "SVEtuj@mail.ru",
"Phone": "89232759320",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000124",
"FullName": "ИП Шаповалов Павел Александрович (сотамаркет)",
"Phone": "89535853298",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000125",
"FullName": "ИП Калмыков Владимир (АМПЕР)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000126",
"FullName": "ИП Скоробогатов Олег Анатольевич",
"Email": "mcd@inbox.ru",
"Phone": "9504158179",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000127",
"FullName": "ИП Ковалев Дмитрий Николаевич",
"Email": "k79105@mail.ru",
"Phone": "89832663763",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000133",
"FullName": "ИП Назаров Александр Григорьевич",
"Phone": "9233117186",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000134",
"FullName": "ИП Лях Александр Александрович",
"Email": "2144465@mail.ru",
"Phone": "89233544465",
"INN": "246007432234",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000131",
"FullName": "Прочие поступления",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000132",
"FullName": "ПОКУПАТЕЛЬ авто",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000135",
"FullName": "ИП Варенов Вячеслав Евгеньевич",
"Email": "gordon78@list.ru",
"Phone": "9135737318",
"INN": "246205417615",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000136",
"FullName": "ООО ЛД-Маркет",
"Email": "lankin.kras@gmail.com",
"Phone": "89135193830",
"INN": "2463113397",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000137",
"FullName": "ИП Асташова Юлия Олеговна",
"Email": "totmina3@mail.ru",
"Phone": "89138350907",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000138",
"FullName": "ИП Экардт Андрей",
"Email": "941494@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000139",
"FullName": "ИП Миленков Максим Валерьевич (KrasCase)",
"Email": "myappleskins@yandex.ru",
"Phone": "89029433443",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000140",
"FullName": "ИП Воронов Дмитрий Автовокзал",
"Email": "dima.voronov.1972@mail.ru",
"Phone": "89607596202",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000141",
"FullName": "ИП Тимофеев Юрий",
"Email": "89333234140tu@gmail.com",
"Phone": "89333234140",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000142",
"FullName": "ХОЗКОМПЛЕКТ Исмадилов Эдуард",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000143",
"FullName": "hoco case МОСКВА",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000144",
"FullName": "ИП Сердюков Олег",
"Email": "oleg_serdykov@gmail.com",
"Phone": "89130495735",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000145",
"FullName": "НАЛОГИ",
"Phone": "",
"INN": "2465087248",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000146",
"FullName": "ИП Сидоренко Александр Иванович",
"Phone": "89233594075",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000147",
"FullName": "ИП Марковцев Яков Анатольевич",
"Email": "mr.styf@mail.ru",
"Phone": "89233007888",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000148",
"FullName": "Phone`s Friends",
"Email": "phonesfriends24@gmail.com",
"Phone": "79658988877",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000149",
"FullName": "ООО Космофон",
"Email": "semnv@inbox.ru",
"Phone": "89135678888",
"INN": "2466185061",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000150",
"FullName": "ООО «СтР»",
"Phone": "",
"INN": "2452045882",
"KPP": "245201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000157",
"FullName": "ООО \"Импульс\"",
"Email": "yganson@mail.ru",
"Phone": "89029821199",
"INN": "2462226214",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000151",
"FullName": "ИП Зозуля Евгений Константинович",
"Phone": "",
"INN": "246523992369",
"KPP": "0",
"OrganizationType": "Физ. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000152",
"FullName": "ИП Брылев Андрей Владимирович",
"Phone": "",
"INN": "246501336571",
"KPP": "0",
"OrganizationType": "Физ. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000155",
"FullName": "ООО Новое утро",
"Phone": "",
"INN": "2460221066",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000153",
"FullName": "ИП Марченко Елена Сергеевна",
"Email": "anganzorova@yandex.ru",
"Phone": "89050869555",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000154",
"FullName": "ООО Planeta Group",
"Email": "price-zakaz@planetahk.com",
"Phone": "89130308488",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000161",
"FullName": "Управление Федерального казначейства по Красноярскому краю (ИФНС России по Центральному району г.Кра",
"Phone": "",
"INN": "2466124118",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000162",
"FullName": "ООО \"СофтСервис\"",
"Phone": "",
"INN": "2463240437",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000156",
"FullName": "ИП Кольцов Александр Юрьевич (старая карта)",
"Email": "moymagazinhoztovari@mail.ru",
"Phone": "89029593447",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000158",
"FullName": "ООО Велес",
"Email": "oksa_1990@mail.ru",
"Phone": "89233022011",
"INN": "2461039780",
"KPP": "246101001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000159",
"FullName": "ООО Виктория",
"Email": "dikrsk@inbox.ru",
"Phone": "73916024100",
"INN": "2434002149",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000160",
"FullName": "ИП Брутчиков Роман Павлович",
"Email": "r_brutchikov@mail.ru",
"Phone": "9135842099",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000163",
"FullName": "ИП Смирнов Антон Сергеевич",
"Email": "ksk2010@inbox.ru",
"Phone": "9676113043",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000164",
"FullName": "AppClinic",
"Email": "appclinic@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000165",
"FullName": "ИП Постников Артем",
"Email": "gektorm24@mail.ru",
"Phone": "89232721678",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000166",
"FullName": "ИП Чубатова Татьяна Владимировна",
"Email": "tchubatova@mail.ru",
"Phone": "89029251113",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000167",
"FullName": "ИП Гараев Илгар Новрузоглан",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000168",
"FullName": "ООО СибНовТорг",
"Phone": "89233490905",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000169",
"FullName": "ИП Коваленко Вадим Сергеевич",
"Email": "19890@mail.ru",
"Phone": "+79832944485",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000170",
"FullName": "ООО \"АРЬЯВАРТА-АудиТТ\"",
"Phone": "",
"INN": "2465281855",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000174",
"FullName": "ООО Техносити",
"Phone": "83912746052",
"INN": "2466241502",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000171",
"FullName": "ИП Рудиков Владимир Владимирович",
"Email": "rudv2003@mail.ru",
"Phone": "89131767114",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000172",
"FullName": "ИП Зозуля Евгений",
"Email": "hello@clockwork.one",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000173",
"FullName": "ООО «ФОРВАРД АВТО»",
"Email": "olga.dmitrieva@forvardavto.ru",
"Phone": "",
"INN": "2464125540",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000181",
"FullName": "Стороженко Маргарита Игоревна",
"Email": "mteh2@ukr.net",
"Phone": "+390994008777",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000181",
"FullName": "Стороженко Маргарита Игоревна",
"Email": "mteh2@ukr.net",
"Phone": "+390994008777",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000175",
"FullName": "ХОЗКОМПЛЕКТ Ромашкин",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000176",
"FullName": "ООО «ОЛИМПИНВЕСТ»",
"Email": "m.egina@olgr.ru",
"Phone": "",
"INN": "2320163664",
"KPP": "232001001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000177",
"FullName": "ИП Бакшеева Тамара Вениаминовна",
"Email": "planetabatareek@gmail.com",
"Phone": "89233383269",
"INN": "246601416573",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000178",
"FullName": "ИП Турчак Игорь Викторович",
"Email": "turchak@ixx.ru",
"Phone": "89235783969",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000179",
"FullName": "ИП Бахтиер",
"Email": "bahtier_1984@mail.ru",
"Phone": "89836176260",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000180",
"FullName": "ИП Денисов Виктор",
"Email": "vitek23081985@ya.ru",
"Phone": "89504279280",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000182",
"FullName": "ИП Горохов Роман Александрович",
"Email": "geekgadget24@gmail.com",
"Phone": "+79620661166",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000183",
"FullName": "ИП Иванова Мария Александровна",
"Email": "ivanovamaria.1992@mail.ru",
"Phone": "89233683605",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000185",
"FullName": "ИП Бурнаев Михаил Андреевич",
"Email": "burnaiev80@mail.ru",
"Phone": "89620775188",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000186",
"FullName": "ООО УК \"Парус\"",
"Email": "silena.ooo@mail.ru",
"Phone": "2930354",
"INN": "2464125444",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000184",
"FullName": "ООО \"Мегапласт плюс\"",
"Phone": "",
"INN": "2464102944",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000002",
"FullName": "ИП Шавкун Е.В.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000190",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000187",
"FullName": "ИП Дейкус Евгений Викторович",
"Email": "r_o0890@mail.ru",
"Phone": "89232996512",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000188",
"FullName": "ИП Смирнов Алексей Владимирович",
"Email": "sms_3s@mail.ru",
"Phone": "89235477778",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000189",
"FullName": "ИП Федоренко Иван Иванович",
"Email": "feclii84@mail.ru",
"Phone": "89029112230",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000191",
"FullName": "ИП Ермолин Алексей Игоревич",
"Email": "ivanov43580999@gmail.com",
"Phone": "89831476490",
"INN": "190206055500",
"KPP": "190201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000192",
"FullName": "ИП Киркоров В.Н.",
"Email": "kirkorov64@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000193",
"FullName": "ИП Тюпин Максим Александрович",
"Email": "windertj@mail.ru",
"Phone": "89607656706",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000195",
"FullName": "ИП Пахомов Евгений Валентинович",
"Phone": "",
"INN": "246400191129",
"KPP": "0",
"OrganizationType": "Физ. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000194",
"FullName": "ООО ТелеМакс (Михаил Жбанков)",
"Email": "telemax24@mail.ru",
"Phone": "+79135954135",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000196",
"FullName": "ООО \"Домострой\"",
"Email": "Pilomaterial124@mail.ru",
"Phone": "2940339",
"INN": "2466179910",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000197",
"FullName": "ИП World Class (Нина)",
"Phone": "+79135515906",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000198",
"FullName": "ИП Новичков К.С.",
"Email": "lleitnet@rambler.ru",
"Phone": "89233649123",
"INN": "246312708665",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000199",
"FullName": "ИП Орлова Надежда Рудольфовна",
"Email": "orlovanr2013@yandex.ru",
"Phone": "89059704602",
"INN": "24652720332",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000200",
"FullName": "ИП Штраушайн Эдуард Юрьевич",
"Email": "shraushayn@bk.ru",
"Phone": "89131733666",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000202",
"FullName": "ИП Титков Иван Иванович",
"Phone": "",
"INN": "400903385592",
"KPP": "0",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000201",
"FullName": "ИП Матола Рината Васильевна",
"Email": "matola_ip@mail.ru",
"Phone": "89509801319",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000203",
"FullName": "ИП Козлов Констанин Николаевич",
"Email": "azard24@yandex.ru",
"Phone": "89131916850",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000204",
"FullName": "ИП Квас С.А.",
"Email": "verner.lana@mail.ru",
"Phone": "83915720202",
"INN": "244400972016",
"KPP": "244401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000205",
"FullName": "НЕДОСТАЧА AOMALE",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000215",
"FullName": "ИП Чистополов Александр Николаевич",
"Email": "amvodoley@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000216",
"FullName": "ООО \"Весна\"",
"Email": "kat1262@yandex.ru",
"Phone": "89029596990",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000220",
"FullName": "ИП Сендецкий Вадим Александрович",
"Email": "vabimir04.@yandex.ru",
"Phone": "89082020111",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000217",
"FullName": "ИП Поданев Евгений Александрович",
"Email": "fosazh.avtomarket@mail.ru",
"Phone": "89232706518",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000218",
"FullName": "ИП Лебедева Анастасия Андреевна",
"Email": "willbest2812@mail.ru",
"Phone": "89135352153",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000219",
"FullName": "ООО \"СпецАзия\"",
"Email": "2155155@bk.ru",
"Phone": "89233555155",
"INN": "2411020085",
"KPP": "241101001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000221",
"FullName": "ИП Усков В.В.",
"Phone": "89135565989",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000222",
"FullName": "ООО \"ЭнВита\"",
"Phone": "",
"INN": "2466254798",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000223",
"FullName": "ИП Ильин Дмитрий Сергеевич",
"Email": "dima232@mail.ru",
"Phone": "89632602625",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000224",
"FullName": "ИП Михайлов Анатолий Егорович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000225",
"FullName": "ИП Голубев Юрий Васильевич",
"Phone": "89112149983",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000226",
"FullName": "ИП Филипова Екатерина Васильевна",
"Email": "magazin_fazenda@mail.ru",
"Phone": "89029117649",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000227",
"FullName": "ИП Степанов Степан Владимирович",
"Email": "fragmeht@gmail.com",
"Phone": "89676127192",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000228",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000229",
"FullName": "БРАК hoco",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000230",
"FullName": "БРАК Treqa",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000231",
"FullName": "ИП Абдулжелилов Марат",
"Phone": "89080180558",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000232",
"FullName": "ООО \"Квартал-Инвест\"",
"Phone": "",
"INN": "2460238895",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000233",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000234",
"FullName": "ИП Мальцев Александр Юрьевич",
"Email": "anastasiya-malceva-76@mail.ru",
"Phone": "89538538878",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000235",
"FullName": "ИП Хакимов Равиль Вакилевич",
"Email": "rafaelka8@icloud.com",
"Phone": "89234501368",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000236",
"FullName": "ИП Кулиш Галина Николаевна",
"Email": "galinakulisch@mail.ru",
"Phone": "89631875678",
"INN": "246100368978",
"KPP": "246101001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000238",
"FullName": "ООО \"АЛЬТУМ\"",
"Phone": "",
"INN": "2461043264",
"KPP": "246101001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000239",
"FullName": "ООО \"Фарт\"",
"Phone": "",
"INN": "2461202740",
"KPP": "246101001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000237",
"FullName": "ИП Кубельда Станислав Станиславович",
"Email": "kubeldal.a._69@mail.ri",
"Phone": "89086595660",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000240",
"FullName": "ИП Памечик Александр Васильевич",
"Phone": "80982085275",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000241",
"FullName": "Иванов Евгений",
"Email": "inbox@diforce.ru",
"Phone": "89994452460",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000242",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000243",
"FullName": "ИП Сокольская Т.И.",
"Phone": "89135785578",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000244",
"FullName": "ХОЗКОМПЛЕКТ Жицкий Егор Викторович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000246",
"FullName": "ООО \"Ситилинк\"",
"Phone": "",
"INN": "7718979307",
"KPP": "246645001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000245",
"FullName": "ИП Соловьева Тамара Анатольевна",
"Email": "zvezda555moi@mail.ru",
"Phone": "89509991100",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000247",
"FullName": "ИП Ходшиев Али Миртонович",
"Email": "diloromcik@gmail.com",
"Phone": "89994459994",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000248",
"FullName": "Аксессуары XO",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДиФорс Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000249",
"FullName": "ИП Шаторная Людмила Николаевна",
"Email": "shatornay2015@mail.ru",
"Phone": "89607651300",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000250",
"FullName": "ИП Смирнов Сергей Вячеславович",
"Email": "wariant-2011@mail.ru",
"Phone": "89233320030",
"INN": "245205753975",
"KPP": "245201001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000251",
"FullName": "ООО \"Север\"",
"Email": "trannzit@mail.ru",
"Phone": "89233257756",
"INN": "2437004352",
"KPP": "243701001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000252",
"FullName": "ИП Дубровский Евгений Владимирович",
"Email": "hazin013@bk.ru",
"Phone": "2141777",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000253",
"FullName": "ИП Тафий В.Н.",
"Phone": "89233652243",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000254",
"FullName": "ИП Горовая Марина Константиновна",
"Email": "gormarina90@gmail.com",
"Phone": "89029635555",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000004",
"FullName": "РАСЧЕТЫ С ТЕРМИНАЛОВ ВТБ",
"Phone": "",
"INN": "7702070139",
"KPP": "0",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000005",
"FullName": "Рыбкина Н.В. (не для реализации)",
"Phone": "",
"INN": "246530199383",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000006",
"FullName": "ПАО \"Вымпелком\"",
"Phone": "",
"INN": "7713076301",
"KPP": "997750001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000255",
"FullName": "ИП Франк Дмитрий Эдуардович",
"Email": "artemb147741@gmail.com",
"Phone": "89293069001",
"INN": "246511619466",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000256",
"FullName": "ИП Писарев Андрей Сергеевич",
"Email": "andrey1510@ro.ru",
"Phone": "89080201957",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000257",
"FullName": "ИП Лесников Антон Александрович",
"Email": "fenshion1991@gmail.com",
"Phone": "89080236351",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000258",
"FullName": "Перенос остатков",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000259",
"FullName": "ИП Сушилин Александр Борисович",
"Email": "belka124@inbox.ru",
"Phone": "89831446666",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000261",
"FullName": "ИП Митина Снежана Александровна",
"Phone": "89057555750",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000260",
"FullName": "ООО \"Кооперативно-эксплуатационная служба крайпотребсоюза\"",
"Phone": "",
"INN": "2466135984",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000262",
"FullName": "ИП Аршинов Максим Сергеевич",
"Email": "maxarshinov_77@mail.ru",
"Phone": "89029678888",
"INN": "246203645052",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000007",
"FullName": "ООО \"Байкал-Сервис Красноярск\"",
"Phone": "",
"INN": "2465304012",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000263",
"FullName": "Общество с ограниченной ответственностью «Ритейл-Юг»",
"Email": "a.krayushkin@olgr.ru",
"Phone": "",
"INN": "2320252106",
"KPP": "232001001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000264",
"FullName": "ИП Колпаков Андрей Владимирович",
"Email": "neopixel-shop@mail.ru",
"Phone": "+79994458009",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000008",
"FullName": "ооо тк Телезон-Сити",
"Phone": "",
"INN": "2463115115",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000265",
"FullName": "ИП Шашков П.Ю.",
"Email": "Spartak-krs@yandex.ru",
"Phone": "2405076",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000009",
"FullName": "ООО \"21 СОВА\"",
"Phone": "",
"INN": "2465177903",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000266",
"FullName": "ИП Салихов Б.Я.",
"Email": "seferkurbanow@mail.ru",
"Phone": "89233277577",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000267",
"FullName": "ИП Хмелевский Александр Владимирович",
"Email": "sam20093@mail.ru",
"Phone": "2805591",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000268",
"FullName": "ИП Бычков Павел Алексеевич",
"Email": "buulltx@gmail.com",
"Phone": "89509987272",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000269",
"FullName": "ИП Сабельникова Ирина Валерьевна",
"Email": "ira160493@yandex.ru",
"Phone": "89333227538",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000271",
"FullName": "ИП Федоров А.В.",
"Phone": "2154411",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000271",
"FullName": "ИП Федоров А.В.",
"Phone": "2154488",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000270",
"FullName": "ИП Харченко Иван Олегович",
"Email": "hariraol@mail.ru",
"Phone": "89509775702",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000010",
"FullName": "УФК по Красноярскому краю (ОСП по ВАШ по г. Красноярску и Емельяновскому району УФССП России по Крас",
"Phone": "",
"INN": "2466124527",
"KPP": "246445001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000273",
"FullName": "ИП Арбатская Анна Викторовна",
"Email": "hozlavka2016@gmail.com",
"Phone": "89131884503",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000272",
"FullName": "ООО «Автомаркет Навигатор»",
"Email": "tov2@navigator124.ru",
"Phone": "3912020200",
"INN": "2465155240",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000011",
"FullName": "ООО КрасИнсайт",
"Phone": "",
"INN": "2465092752",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000274",
"FullName": "ООО \"Маяк\"",
"Email": "insulinoff@gmail.com",
"Phone": "83912783112",
"INN": "2464149332",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000275",
"FullName": "ИП Письмеров Илья Викторович",
"Email": "pismerov87@mail.ru",
"Phone": "89833642979",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000276",
"FullName": "ИП Ибрагимов Сергей",
"Email": "mybuk@inbox.ru",
"Phone": "89135328888",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000277",
"FullName": "ИП Алпатов Николай",
"Phone": "89135346652",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000278",
"FullName": "ИП Казаков Егор Юрьевич",
"Email": "ipkazakovegor@yandex.ru",
"Phone": "89232725455",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000279",
"FullName": "ИП Воробьев Данил Петрович",
"Email": "vor.tatyana@list.ru",
"Phone": "89224832797",
"INN": "720305854111",
"KPP": "720301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000280",
"FullName": "ИП Галкин Андрей Григорьевич",
"Email": "rig24@mail.ru",
"Phone": "89029277312",
"INN": "246301839000",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000281",
"FullName": "ИП Чебанов Никита Александрович",
"Email": "m.egina@olgr.ru",
"Phone": "89384639678",
"INN": "263111611639",
"KPP": "263101001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000012",
"FullName": "ИП Кузьмин В.И.",
"Email": "homs@mail.ru",
"Phone": "",
"INN": "246300183678",
"KPP": "246602001",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000282",
"FullName": "ИП Цысь Анна Дмитриевна",
"Email": "tsis92@mail.ru",
"Phone": "89232708627",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000283",
"FullName": "ИП Незамутдинов Андрей",
"Phone": "89082125931",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000284",
"FullName": "ИП Мустафаев Вугар",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000285",
"FullName": "ИП Пичугин Михаил Максимович",
"Email": "mihail.pichu@yandex.ru",
"Phone": "89509950301",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000286",
"FullName": "ИП Кейлин Евгений Андреевич",
"Phone": "89504297319",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000287",
"FullName": "ИП Тарков Виталий Викторович",
"Email": "vikultvv@yandex.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000013",
"FullName": "ООО ГРАНД ХОЛЛ",
"Phone": "",
"INN": "2465121636",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000014",
"FullName": "ГУ-КРАСНОЯРСКОЕ РО ФОНДА СОЦИАЛЬНОГО СТРАХОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
"Phone": "",
"INN": "2466039624",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000288",
"FullName": "1РОЗНИЧНЫЙ ПОКУПАТЕЛЬ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000290",
"FullName": "ИП Широв Михаил Викторович",
"Email": "krasman61@mail.ru",
"Phone": "89029225739",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000289",
"FullName": "ИП Горбунов Олег Витальевич",
"Email": "variantles@gmail.com",
"Phone": "2588369",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000291",
"FullName": "БОНУСЫ ОПТОВИКАМ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000292",
"FullName": "ООО Успех",
"Email": "semnv@inbox.ru",
"Phone": "",
"INN": "2466194450",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000293",
"FullName": "ИП Ромбульт Сергей",
"Email": "rombultsergei@yandex.ru",
"Phone": "+79632555883",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000294",
"FullName": "ИП Дроздов Владимир Иванович",
"Email": "emaildrozdov@yandex.ru",
"Phone": "89130325665",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000295",
"FullName": "ИП Ховалыг Урана Очур-ооловна",
"Email": "khovalyg.urana@mail.ru",
"Phone": "89235458991",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000296",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000297",
"FullName": "Недостача XO",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000016",
"FullName": "ООО \"Альма\"",
"Phone": "",
"INN": "3255044948",
"KPP": "325701001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000298",
"FullName": "ИП Василенко Юрий Николаевич",
"Email": "mountantiger@yandex.ru",
"Phone": "89232776999",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000299",
"FullName": "ИП Каргопольцева Ирина Александровна",
"Email": "imba13-1@rambler.u",
"Phone": "89607551929",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000300",
"FullName": "ИП Кирилов Кирилл Александрович (Стружка)",
"Email": "kirilov_91@inbox.ru",
"Phone": "89235772396",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000301",
"FullName": "ИП Колпакова Наталья Алексеевна",
"Phone": "89048910849",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000302",
"FullName": "ИП Бойко Клара Раисовна",
"Email": "klara646@mail.ru",
"Phone": "89676126229",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000302",
"FullName": "ИП Бойко Клара Раисовна",
"Email": "tatarovinstrument@mail.ru",
"Phone": "89676126229",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000017",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "ЦБ0000018",
"FullName": "ПОДАРКИ  В ТРЦ ИЮНЬ",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000019",
"FullName": "ПОДАРКИ В ТРЦ РЭД СЕЙЛ",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000303",
"FullName": "ИП Яковлев Александр Валерьевич",
"Email": "Jonycoach@mail.ru",
"Phone": "89012400104",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000303",
"FullName": "ИП Яковлев Александр Валерьевич",
"Email": "901rus@gmail.com",
"Phone": "89012400104",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000304",
"FullName": "ИП Клоцбах Александр Иванович",
"Email": "klocbah78@gmail.com",
"Phone": "89236687535",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000305",
"FullName": "ИП Горячева Светлана Владимировна",
"Email": "irish1404@mail.ru",
"Phone": "89233000522",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "RS0000007",
"FullName": "Пробный с сайта SNP",
"Phone": "89995556644",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000020",
"FullName": "УФПС Красноярского края",
"Phone": "",
"INN": "7724490000",
"KPP": "246643001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000306",
"FullName": "ИП Воронова Лилия Вениаминовна",
"Email": "liliya.voronova.69@mail.ru",
"Phone": "89020128031",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000021",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "ЦБ0000022",
"FullName": "РЭД СЕЙЛ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000023",
"FullName": "ИЮНЬ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000024",
"FullName": "ДИФОРС",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000307",
"FullName": "ИП Груздев Илья Петрович",
"Email": "ily.gruzdev99@gmail.com",
"Phone": "89233170843",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000308",
"FullName": "ИП Гук Анастасия Игоревна",
"Email": "guk-ai@mail.ru",
"Phone": "89658968639",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000309",
"FullName": "ИП Казаков Дмитрий Георгиевич",
"Email": "dmitii82@bk.ru",
"Phone": "89138340333",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000310",
"FullName": "ИП Мареев Юрий Васильевич",
"Email": "vitalyamaree@mail.ru",
"Phone": "89293219588",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000311",
"FullName": "ИП Вертипрахов Дмитрий Александрович",
"Email": "vertiprakhov@inbox.ru",
"Phone": "89059769111",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000312",
"FullName": "ИП Постников (не проводить)",
"Email": "gektorm24@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "RS0000008",
"FullName": "Елена АКБ iPhone 8 plus",
"Phone": "89029807997",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000314",
"FullName": "ИП Федлов Владислав Сергеевич",
"Email": "tk.atlant@mail.ru",
"Phone": "89029409322",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000313",
"FullName": "ИП Черкашин Сергей Валерьевич (МЕГАОПТ)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000316",
"FullName": "ИП Федореева Оксана Александровна",
"Email": "ok-feda@rambler.ru",
"Phone": "89130332926",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000324",
"FullName": "ИП Мальчугова Евгения Владимировна",
"Email": "Evg-yushkova@yandex.ru",
"Phone": "89233187337",
"INN": "245803045464",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000025",
"FullName": "ИП Ващенко Андрей Александрович",
"Phone": "",
"INN": "246310676880",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000026",
"FullName": "АО АМК-фарма",
"Phone": "",
"INN": "7704260495",
"KPP": "770801001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000027",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "ЦБ0000028",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "ЦБ0000029",
"FullName": "ИП КУЛАКОВ ВИТАЛИЙ АЛЕКСАНДРОВИЧ (СДЭК)",
"Phone": "",
"INN": "246513266907",
"KPP": "0",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000030",
"FullName": "ООО \"КРАСУПАКСЕРВИС\"",
"Phone": "",
"INN": "2464258758",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000031",
"FullName": "Общество с Ограниченной Ответственностью ПЭЙКИПЕР-КАССА",
"Phone": "",
"INN": "5008055466",
"KPP": "500801001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000032",
"FullName": "ООО Совкомкард",
"Phone": "",
"INN": "9717049581",
"KPP": "440101001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000334",
"FullName": "ИП Антонов Олег Вячеславович",
"Email": "aovs@list.ru",
"Phone": "89232860625",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000334",
"FullName": "ИП Антонов Олег Вячеславович",
"Email": "aovs@list.ru",
"Phone": "89232860635",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000335",
"FullName": "ИП Куулар Буян Комиявич",
"Email": "buyanvip@mail.ru",
"Phone": "89232638181",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000336",
"FullName": "ИП Смородников Илья Викторович",
"Email": "mr.atlant007@mail.ru",
"Phone": "89233731727",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000337",
"FullName": "ИП Шаров Сергей Николаевич",
"Email": "sharov.73@inbox.ru",
"Phone": "89134426101",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000338",
"FullName": "ИП Долзат Ч.Д.",
"Phone": "89232150035",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000339",
"FullName": "ИП Арыскин Сергей Александрович",
"Email": "natalya.nxt@mail.ru",
"Phone": "89082110407",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000340",
"FullName": "ИП Сердюкова Тамара Владимировна",
"Phone": "89232875123",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000341",
"FullName": "ХОЗКОМПЛЕКТ Бекмирзаева Холида",
"Phone": "89059735948",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000342",
"FullName": "ИП ДевайсМаркет",
"Email": "zakaz@device.market",
"Phone": "89052407102",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000343",
"FullName": "Лазаренко Кирилл Максимович",
"Phone": "89647426248",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000344",
"FullName": "ИП Анисимов Андрей Александрович",
"Email": "andrey.anisimov.86@list.ru",
"Phone": "89233386306",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000345",
"FullName": "ИП Выходцева Анастасия Олеговна",
"Email": "killprice24@yandex.ru",
"Phone": "",
"INN": "245689699853",
"KPP": "245601001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000034",
"FullName": "ИП Кильдияров Чингиз Айдарович",
"Phone": "",
"INN": "027817047883",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000346",
"FullName": "ИП Васильева Анна Викторовна",
"Email": "vadimka.vasilev.8383@mail.ru",
"Phone": "89233352939",
"INN": "242900518150",
"KPP": "242901001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000347",
"FullName": "ИП Боженков Александр Александрович",
"Email": "enolry39@gmail.com",
"Phone": "89234544488",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000348",
"FullName": "ИП Наумчик Елена Юрьевна",
"Email": "Feyou@inbox.ru",
"Phone": "89233604417",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000349",
"FullName": "ИП Карпович Александр Сергеевич",
"Email": "quickly23@yandex.ru",
"Phone": "89233074440",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000351",
"FullName": "ИП Ахметзянов Вагиз Давлятович",
"Phone": "89504219007",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000350",
"FullName": "ИП Кузьмин Мирослав Владимирович",
"Email": "2716898@mail.ru",
"Phone": "",
"INN": "246522407992",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000350",
"FullName": "ИП Кузьмин Мирослав Владимирович",
"Email": "9835055355@mail.ru",
"Phone": "",
"INN": "246522407992",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000352",
"FullName": "ИП Каверзина Зинаида Николаевна",
"Email": "kaverzina.z@yandex.ru",
"Phone": "89080135224",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000353",
"FullName": "ИП Голубев Андрей Михайлович",
"Email": "tsmarket24@yandex.ru",
"Phone": "",
"INN": "246400004964",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000354",
"FullName": "ИП Филипова Татьяна Михайловна (СЦ БЕЛКА)",
"Phone": "89535851215",
"INN": "243700103495",
"KPP": "243701001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000355",
"FullName": "ИП Ефендиев Ягуб",
"Email": "efendievagub@gmail.com",
"Phone": "89631912899",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000356",
"FullName": "ИП Усков Вячеслав Анатольевич (GSM Service)",
"Phone": "83912067236",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000357",
"FullName": "ИП Парилов Владимир Дмитриевич",
"Email": "ipparilov@yandex.ru",
"Phone": "89138349455",
"INN": "246211084481",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000358",
"FullName": "ИП Мыськив Игорь Ярославович",
"Email": "muskivirina@mail.ru",
"Phone": "89130370944",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000360",
"FullName": "ИП Тимохович Сергей Анатольевич",
"Phone": "89232894449",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000362",
"FullName": "ООО \"Софт - 33\"",
"Email": "33@xxxiii.ru",
"Phone": "+79069148833",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000369",
"FullName": "ИП Жуков Вячеслав Борисович (U-Store)",
"Email": "zhukovvyacheslav92@mail.ru",
"Phone": "89607599176",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000370",
"FullName": "ИП Егоров Алексей Валерьевич",
"Phone": "89082234887",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000371",
"FullName": "ИП Мустафаев Шабан Мурад Оглы",
"Email": "shaban.6969@bk.ru",
"Phone": "+79029422726",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000372",
"FullName": "ООО «СК-МИТРА»",
"Email": "nda@ck-mitra.ru",
"Phone": "+73912699920",
"INN": "2465178520\n2",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000373",
"FullName": "ООО \"ТС КОМАНДОР\"",
"Phone": "",
"INN": "2465008567",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000374",
"FullName": "ИП Бухтуева Анастасия Анатольевна",
"Phone": "89631865610",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000375",
"FullName": "Павел Хохлов програмист",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000376",
"FullName": "ИП Калиенко Алексей Павлович",
"Email": "kalienko1984@mail.ru",
"Phone": "89993131661",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000377",
"FullName": "ИП Белоколодов Сергей Иванович",
"Email": "midass72@mail.ru",
"Phone": "89232750567",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000378",
"FullName": "ИП Камышников Сергей Дмитриевич",
"Email": "sergokam95@icloud.com",
"Phone": "79371868298",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000379",
"FullName": "ИП Гайнутдинов Равиль",
"Email": "pav0077@gmail.com",
"Phone": "89831410770",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000037",
"FullName": "ПАО \"Совкомбанк\"",
"Phone": "",
"INN": "4401116480",
"KPP": "440101001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000380",
"FullName": "ООО «АвтоСтройМаркет»",
"Email": "volodya__92@mail.ru",
"Phone": "89029189684",
"INN": "2411014892",
"KPP": "241101001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000038",
"FullName": "ИП Фролов Алексей Николаевич (айфоника)",
"Phone": "89831273205",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000381",
"FullName": "ИП Чернозубов Валентин Владиславович",
"Email": "d797cf@yandex.ru",
"Phone": "89135322286",
"INN": "880100026830",
"KPP": "880101001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000039",
"FullName": "Олег магазин АНТИСТОР (AntiStore)",
"Phone": "89130308488",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000382",
"FullName": "ИП Галеева Н.Д.",
"Email": "ipGaleeva@mail.ru",
"Phone": "89233102214",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000383",
"FullName": "ИП Полехин Игорь Анатольевич",
"Email": "polehinigor@mail.ru",
"Phone": "89233551797",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000040",
"FullName": "Индивидуальный предприниматель Филаткин Андрей Николаевич",
"Phone": "",
"INN": "246500589851",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000384",
"FullName": "ООО \"Торговый дом \"Валесин\"",
"Email": "tdvalesin@mail.ru",
"Phone": "89235850525",
"INN": "2466278929",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000385",
"FullName": "Хозкомплект Лынов Вячеслав",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000386",
"FullName": "ООО ОПХ Ояхтинское",
"Phone": "89620712056",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000387",
"FullName": "ИП Напесочный Николай Сергеевич",
"Email": "nmv-00@mail.ru",
"Phone": "89131732774",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000388",
"FullName": "ООО «Торгмонтаж»",
"Email": "Abakan-torgmontazh@yandex.ru",
"Phone": "83902343948",
"INN": "1901075596",
"KPP": "190101001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000389",
"FullName": "ООО «АМК-ЕНИСЕЙ»",
"Email": "vsolovieva@regionsgroup.ru",
"Phone": "2568551",
"INN": "2465221253",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000390",
"FullName": "МАУ \"ПГДК\"",
"Email": "pbgdk@mail.ru",
"Phone": "2643027",
"INN": "2462002260",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000391",
"FullName": "000 НК «НАФТА-СИБИРЬ»",
"Email": "nafta-sibir@bk.ru",
"Phone": "89233559020",
"INN": "2465144908",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000392",
"FullName": "ИП Таракин Александр Дмитриевич",
"Email": "arakin158@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000393",
"FullName": "ИП Соломин И.С.",
"Email": "trade@snpmarket.com",
"Phone": "83902261336",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000394",
"FullName": "ИП Латыпов Рафаил Мингареевич",
"Email": "Latypov1304@mail.ru",
"Phone": "89029451911",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000395",
"FullName": "ИП Ларин Владимир Александрович",
"Phone": "89233344807",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000396",
"FullName": "ФКУ ЖКУ ГУФСИН России по Красноярскому краю",
"Phone": "",
"INN": "2464030792",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000397",
"FullName": "ИП Семенов Максим Сергеевич",
"Email": "glaider@bk.ru",
"Phone": "89504031415",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000398",
"FullName": "ИП Винникова Ольга Петровна",
"Email": "dom8.70@mail.ru",
"Phone": "89135347212",
"INN": "244600068200",
"KPP": "244601001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000399",
"FullName": "ХОЗКОМПЛЕКТ сервис Боря",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000400",
"FullName": "ИП Винковская Яна Владимировна",
"Email": "telemart@yandex.ru",
"Phone": "89059037742",
"INN": "421712714723",
"KPP": "421701001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000401",
"FullName": "ООО \"Радар\"",
"Phone": "2790736",
"INN": "2466185431",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000402",
"FullName": "ООО \"Сфера Плюс\"",
"Email": "sferaplus24@yandex.ru",
"Phone": "+79080152211",
"INN": "2443051336",
"KPP": "244301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000403",
"FullName": "ООО \"ДС+\"",
"Phone": "89832658000",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000405",
"FullName": "АО «Газпром газораспределение Север»",
"Email": "grukalo_da@sever04.ru",
"Phone": "83452289097",
"INN": "7203058440",
"KPP": "720301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000041",
"FullName": "Червякова Екатерина Васильевна",
"Phone": "89994439564",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000042",
"FullName": "Мыськов Иван Сергеевич (МТС)",
"Phone": "89232753030",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000043",
"FullName": "ИП Ольков Александр Борисович",
"Phone": "89831458940",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000044",
"FullName": "КГКУ по ОИПОО",
"Email": "e2882531@mail.ru",
"Phone": "89913741013",
"INN": "2466137212",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000404",
"FullName": "ИП Тычинский Александр Анатольевич",
"Email": "aleksandr-kapran@yandex.ru",
"Phone": "89628484912",
"INN": "190200623362",
"KPP": "190201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000406",
"FullName": "ИП Лапицкий Олег Владимирович",
"Phone": "89831685308",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000045",
"FullName": "КРАСНОЯРСКИЙ ФИЛИАЛ ПАО \"РОСТЕЛЕКОМ\"",
"Phone": "",
"INN": "7707049388",
"KPP": "246643001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000407",
"FullName": "АО «Декор-Лайн»",
"Phone": "7954307",
"INN": "5075370914",
"KPP": "507501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000408",
"FullName": "ООО «Хёгель Шу Фэшн»",
"Phone": "84956463540",
"INN": "7702600001",
"KPP": "770201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000409",
"FullName": "ИП Паначева Татьяна Алексеевна",
"Email": "zamretail2@profi-center.ru",
"Phone": "3912529595",
"INN": "246406991548",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000410",
"FullName": "ООО «ДНС Ритейл»",
"Email": "Matekanistov.K@dns-shop.ru",
"Phone": "",
"INN": "2540167061",
"KPP": "246545013",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000046",
"FullName": "ИП Шадрин Александр Владимирович",
"Email": "joyash@mail.ru",
"Phone": "+79233004546",
"INN": "246401238683",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000047",
"FullName": "ООО «Радуга»",
"Email": "Viktoriya.Yuhnevich@lemurrr.com",
"Phone": "",
"INN": "7805401216",
"KPP": "780501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000048",
"FullName": "ЗАО \"ОДЕОН-СТИЛЬ\"",
"Email": "lora15-2006@yandex.ru",
"Phone": "+79059714464",
"INN": "5034038347",
"KPP": "503401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000411",
"FullName": "ООО «Спортмастер»",
"Phone": "",
"INN": "7728551528",
"KPP": "540543002",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000412",
"FullName": "ИП Костиков Павел Николаевич",
"Email": "viper777_84@mail.ru",
"Phone": "89504211711",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000413",
"FullName": "ИП Волков Андрей Александрович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000414",
"FullName": "Закрытое акционерное общество «Космик»",
"Phone": "",
"INN": "7705912697",
"KPP": "770501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000415",
"FullName": "Общество с ограниченной ответственностью «АЛЬФА ТРЕЙД»",
"Email": "mercury24@bk.ru",
"Phone": "+73912096868",
"INN": "2465138485",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000416",
"FullName": "ООО «Респект-Ост»",
"Email": "respect_krsk@mail.ru",
"Phone": "2768455",
"INN": "2466148870",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000049",
"FullName": "Индивидуальный предприниматель Орлов Илья Андреевич",
"Phone": "",
"INN": "660605020110",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000417",
"FullName": "ИП Овечкин Сергей  Геннадьевич",
"Email": "irn@afra.su",
"Phone": "3432637953",
"INN": "667330637236",
"KPP": "667301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000419",
"FullName": "Акционерное общество «ПанКлуб»",
"Phone": "",
"INN": "7743765161",
"KPP": "772501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000418",
"FullName": "ООО «Агроник»",
"Phone": "",
"INN": "2411028447",
"KPP": "241101001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000421",
"FullName": "Индивидуальный предприниматель Чивчян Георгий Тумасович",
"Email": "olga.dmitrieva@forvardavto.ru",
"Phone": "",
"INN": "246313528619",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000422",
"FullName": "ООО Интернет Решения",
"Email": "tovaroved@forvardavto.ru",
"Phone": "",
"INN": "7704217370",
"KPP": "770401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000420",
"FullName": "ИП Рублевский Александр Иванович",
"Email": "yueya.ru.79@mail.ru",
"Phone": "89659111588",
"INN": "240900072168",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000050",
"FullName": "БАНК ВТБ Филиал ЦЕНТРАЛЬНЫЙ",
"Phone": "",
"INN": "9717049581",
"KPP": "440101001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000423",
"FullName": "ИП Шеховцева Татьяна Александровна",
"Email": "shehovtseva@mail.ru",
"Phone": "89235718237",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000424",
"FullName": "ИП Зорина Снежана Вячеславовна",
"Phone": "89509811854",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000051",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "ЦБ0000052",
"FullName": "Рыбкина Наталья",
"Phone": "+79059765494",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000053",
"FullName": "Романенко Вадим",
"Phone": "+79994479138",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000054",
"FullName": "Петров Иван",
"Phone": "+79155308434",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000425",
"FullName": "ИП Рудаков Валентин Николаевич",
"Email": "zoomych@mail.ru",
"Phone": "+79233333323",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000426",
"FullName": "ИП Московкин Сергей Викторович",
"Email": "partphone24@yandex.ru",
"Phone": "89029191366",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000426",
"FullName": "ИП Московкин Сергей Викторович",
"Email": "mschitova@yandex.ru",
"Phone": "89029191366",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000427",
"FullName": "Индивидуальный предприниматель Савченко Алексей Георгиевич",
"Email": "logist@4ip.info",
"Phone": "89501279413",
"INN": "381600451550",
"KPP": "381601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000428",
"FullName": "ИП Рустамов Абдусаид",
"Email": "rustamovap@mail.ru",
"Phone": "89029257723",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000429",
"FullName": "ИП Соломин И.С (для заказов с сайта)",
"Email": "zakaz@snpmarket.com",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "КРУПНЫЙ ОПТ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000055",
"FullName": "Комардина Евгения",
"Phone": "+79235779231",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000056",
"FullName": "Антон Антон",
"Phone": "+79130397785",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000057",
"FullName": "Богданов Олег",
"Phone": "+79676126449",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000058",
"FullName": "Кузнецова Наталья",
"Phone": "+79233644024",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000059",
"FullName": "Кузьмина Елена",
"Phone": "+79029248186",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000060",
"FullName": "Паршутин Вячеслав",
"Phone": "+79135913254",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000061",
"FullName": "Миронова Светлана",
"Phone": "+79956625365",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000062",
"FullName": "Буслаев Иван",
"Phone": "+79130499777",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000063",
"FullName": "Подрезенко Анастасия",
"Phone": "+79293552322",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000064",
"FullName": "Лазовский Артем",
"Phone": "+79135653104",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000065",
"FullName": "Мочалова Ольга",
"Phone": "+79135187688",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000066",
"FullName": "Исаева Татьяна",
"Phone": "+79135837960",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000067",
"FullName": "Тимофеенко Наталья",
"Phone": "+79135373848",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000068",
"FullName": "Зимина Валерия",
"Phone": "+79831538113",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000069",
"FullName": "Балахонова Екатерина",
"Phone": "+79029418682",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000070",
"FullName": "Белозеров Кирилл",
"Phone": "+79232944692",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000071",
"FullName": "Варыгина Валентина",
"Phone": "+79233311432",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000072",
"FullName": "Анастасия Стрижелковская",
"Phone": "+79509996399",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000073",
"FullName": "Назаров Иван",
"Phone": "+79233522555",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000074",
"FullName": "Ирт Анастасия",
"Phone": "+79233596905",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000076",
"FullName": "Во Тата",
"Phone": "+79224832797",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000077",
"FullName": "Уточкин Дмитрий",
"Phone": "+79994458955",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000078",
"FullName": "Крис Кристина",
"Phone": "+79233208789",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000079",
"FullName": "Юдина Анастасия",
"Phone": "+79029211136",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000080",
"FullName": "Ермолаева Кристина",
"Phone": "+79029460513",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000081",
"FullName": "Ваймер Денис",
"Phone": "+79135884694",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000082",
"FullName": "Майер Елена",
"Phone": "+79029575667",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000083",
"FullName": "Соломина Надежда",
"Phone": "+79233225507",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000084",
"FullName": "Рыбкин Иван",
"Phone": "+79631912570",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000085",
"FullName": "Гуляйкина Марина",
"Phone": "+79029436752",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000086",
"FullName": "Клементенок Павел",
"Phone": "+79832975589",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000087",
"FullName": "Бархатова Женя",
"Phone": "+79533701748",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000088",
"FullName": "Митрякова Мария",
"Phone": "+79233315302",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000089",
"FullName": "Абдинасиров Зарлык",
"Phone": "+79832823867",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000090",
"FullName": "Свечникова Дарья",
"Phone": "+79994412061",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000091",
"FullName": "Пилипенко Сергей",
"Phone": "+79131922569",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000092",
"FullName": "ИП Смирнов Михаил юрьевич (хокорус)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000093",
"FullName": "Шулбаева Александра",
"Phone": "+79080138615",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000094",
"FullName": "Мел Ольга",
"Phone": "+79535880338",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000095",
"FullName": "Вика Вика",
"Phone": "+79029650009",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000096",
"FullName": "Власова Арина",
"Phone": "+79230163464",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000097",
"FullName": "Орлова Алёна",
"Phone": "+79135098758",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000098",
"FullName": "Афоничев Михаил",
"Phone": "+79135589090",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000099",
"FullName": "Трубникова Ирина",
"Phone": "+79232864505",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000100",
"FullName": "Яковлева Марина",
"Phone": "+79131763445",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000101",
"FullName": "Рыськова Анна",
"Phone": "+79232921641",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000102",
"FullName": "Михаль Лариса",
"Phone": "+79293393997",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000103",
"FullName": "Балышева Елена",
"Phone": "+79082202886",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000104",
"FullName": "Кузнецов Илья",
"Phone": "+79659094590",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000105",
"FullName": "Власова Анна",
"Phone": "+79233104541",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000106",
"FullName": "Диченко Юлия",
"Phone": "+79339999655",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000107",
"FullName": "Кузнецова Алика",
"Phone": "+79964295114",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000120",
"FullName": "Внутрибанковские требования по хозяйственным /внутрибанковским операциям. Миграция филиал 5440 г. Но",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000108",
"FullName": "Шаройко Елена",
"Phone": "+79029477349",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000109",
"FullName": "Муравьева Софья",
"Phone": "+79535829993",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000110",
"FullName": "Михайлова Евгения",
"Phone": "+79185242906",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000111",
"FullName": "Казаренко Ирина",
"Phone": "+79233153010",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000112",
"FullName": "Нестерова Елизавета",
"Phone": "+79964282305",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000113",
"FullName": "Л Екатерина",
"Phone": "+79233224104",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000114",
"FullName": "Мельникова Татьяна",
"Phone": "+79131774747",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000115",
"FullName": "Липнягова Екатерина",
"Phone": "+79632636642",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000116",
"FullName": "Ухова Яна",
"Phone": "+79832941046",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000117",
"FullName": "Яковлева Яна",
"Phone": "+79607531122",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000118",
"FullName": "Заева Алена",
"Phone": "+79233399913",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000119",
"FullName": "Пятанова Александра",
"Phone": "+79135753016",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000121",
"FullName": "М Олег",
"Phone": "+79233257784",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000430",
"FullName": "ИП Финк Игорь Евгеньевич",
"Email": "finichik@gmail.com",
"Phone": "9131902234",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000122",
"FullName": "Васильева Ирина",
"Phone": "+79131921957",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000123",
"FullName": "Князев Глеб",
"Phone": "+79832940056",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000431",
"FullName": "ООО «КО-Монтаж»",
"Email": "aanyav@mail.ru",
"Phone": "",
"INN": "2460089379",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000124",
"FullName": "Карелина Софья",
"Phone": "+79607695290",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000125",
"FullName": "Бабаян Тарон",
"Phone": "+79994401214",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000126",
"FullName": "Богданова Яна",
"Phone": "+79293399965",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000127",
"FullName": "Попова Настя",
"Phone": "+79832003226",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000128",
"FullName": "Рицберг Надежда",
"Phone": "+79135373248",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000129",
"FullName": "Максим Малков",
"Phone": "+79339990646",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000130",
"FullName": "Будникова Ольга",
"Phone": "+79138317328",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000131",
"FullName": "Скрипка Кристина",
"Phone": "+79048923257",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000143",
"FullName": "ИП Баюшкин Александр",
"Email": "aleksandrbs@mail.ru",
"Phone": "89232860625",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000143",
"FullName": "ИП Баюшкин Александр",
"Email": "aleksandrbs@mail.ru",
"Phone": "89293346444",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000132",
"FullName": "Шварцкопф Кристина",
"Phone": "+79994421677",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000133",
"FullName": "Олишевская Кристина",
"Phone": "+79538064086",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000134",
"FullName": "Сади Сайхана",
"Phone": "+79235424221",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000135",
"FullName": "Черепанова Александра",
"Phone": "+79130391575",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000136",
"FullName": "Студзинская Елена",
"Phone": "+79293374407",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000137",
"FullName": "Карелина Алина",
"Phone": "+79135071603",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000138",
"FullName": "Калачикова Виктория",
"Phone": "+79607635630",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000139",
"FullName": "Осипенко Анастасия",
"Phone": "+79676141607",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000140",
"FullName": "Лобышева Екатерина",
"Phone": "+79915007790",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000141",
"FullName": "Будник Алия",
"Phone": "+79131903399",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000142",
"FullName": "Тужилкина Дарья",
"Phone": "+79029701734",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000144",
"FullName": "Логинов Александр",
"Phone": "+79232703952",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000145",
"FullName": "Микаелян Карен",
"Phone": "+79831596536",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000146",
"FullName": "Вы Я",
"Phone": "+79135592771",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000147",
"FullName": "Мокрецова Александра",
"Phone": "+79607702064",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000148",
"FullName": "Привалов Роман",
"Phone": "+79994460045",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000149",
"FullName": "Замкина Татьяна",
"Phone": "+79235794020",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000675",
"FullName": "Жестовский Максим",
"Phone": "89233142101",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000676",
"FullName": "Алексей Аболемов",
"Phone": "89509865148",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000677",
"FullName": "Наталья Коршунова",
"Phone": "89237838408",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000678",
"FullName": "ИП Круглов Михаил Иванович",
"Phone": "",
"INN": "100104935202",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000679",
"FullName": "ООО \"Ворлд Класс Красноярск\"",
"Phone": "",
"INN": "2465288970",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000680",
"FullName": "ИП Демешко Алексей Александрович",
"Phone": "",
"INN": "245304071691",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000681",
"FullName": "Опарина Карина Сергеевна",
"Phone": "89233133404",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000682",
"FullName": "ООО \"ЯНДЕКС\"",
"Phone": "",
"INN": "7736207543",
"KPP": "997750001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000683",
"FullName": "ооо \"Вконтакте\"",
"Phone": "",
"INN": "7842349892",
"KPP": "997750001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000684",
"FullName": "Гегечкори Сандро",
"Phone": "89131712474",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000033",
"FullName": "ООО Комтет",
"Phone": "",
"INN": "5834041042",
"KPP": "583401001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000325",
"FullName": "ИП Новичков Константин Серегевич",
"Phone": "89233649123",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000326",
"FullName": "ИП Алиева Алеся Сохраб-Кызы",
"Email": "igadget24@bk.ru",
"Phone": "89333317868",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000327",
"FullName": "ИП Радченко Ольга Николаевна",
"Email": "1976ronvv@mail.ru",
"Phone": "89135205725",
"INN": "243800002204",
"KPP": "243801001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000328",
"FullName": "ИП Черных Анна Олеговна",
"Email": "ann_ch91@mail.ru",
"Phone": "89233711112",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000330",
"FullName": "ИП Кользин Алексей Игоревич",
"Phone": "89029911234",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000331",
"FullName": "ИП Дмитриев Сергей Анатольевич",
"Email": "tron_85@bk.ru",
"Phone": "89509766669",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000329",
"FullName": "ИП Малышенко  Людмила Владимировна",
"Email": "fon,kotta.luda@mail.ru",
"Phone": "89059969954",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000332",
"FullName": "ИП Герасимов Алексей Юрьевич",
"Email": "krastennis@mail.ru",
"Phone": "+79135320522",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000333",
"FullName": "Телевизорная 1ст4  (Изумрудный город)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "MV0000004",
"FullName": "Семенов Виктор Валерьевич",
"Phone": "89232871148",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DB0000001",
"FullName": "Панфилов Андрей",
"Phone": "89232850565",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000682",
"FullName": "ИП Бронников Олег Валерьевич",
"Email": "home-interest@mail.ru",
"Phone": "89233140654",
"INN": "241104351006",
"KPP": "241101001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000684",
"FullName": "ИП Смолин Александр Сергеевич (Назарово)",
"Email": "first6957@gmail.com",
"Phone": "89059746406",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000685",
"FullName": "ИП Большакова Анна Алексеевна",
"Phone": "",
"INN": "381403380589",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000686",
"FullName": "ИП Еговцева Любовь Ильинична",
"Email": "egovceva56@mail.ru",
"Phone": "89504143115",
"INN": "242300281847",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000687",
"FullName": "Ганцов Равиль Ибрагимович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000688",
"FullName": "ИП Асафов Иван Александрович",
"Email": "asafov.store@yandex.ru",
"Phone": "+79069587022",
"INN": "701754947250",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000689",
"FullName": "ХОЗКОМПЛЕКТ Юдина Татьяна",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000690",
"FullName": "ИП Слобода Олег Владимирович",
"Email": "39151@mail.ru",
"Phone": "+79293342299",
"INN": "244300070159",
"KPP": "244301001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000691",
"FullName": "Ниндзя Шоп",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000673",
"FullName": "Каменев Кирилл Викторович",
"Phone": "89025625662",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000674",
"FullName": "ООО «КрасИнтегра»",
"Email": "zep001@krasintegra.ru",
"Phone": "",
"INN": "2466168845",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000675",
"FullName": "ООО «АкваСтандарт»",
"Phone": "89135245744",
"INN": "2462055978",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000676",
"FullName": "ООО «Спикатрэйд»",
"Email": "spikatrade@yandex.ru",
"Phone": "+73912746150",
"INN": "2460221620",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000677",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000683",
"FullName": "ООО \"ТЕХНОСТРОЙ\"",
"Phone": "+79135344063",
"INN": "2462063545",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000678",
"FullName": "Исаев Муслим Исаевич",
"Email": "isaev_mus@mail.ru",
"Phone": "+79659111113",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000679",
"FullName": "ХОЗКОМПЛЕКТ Конищева Виктория Владимировна",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000680",
"FullName": "ИП Наталья Сочнева (Ачинск)",
"Phone": "89632658686",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000681",
"FullName": "Владимир (Iprotect) ачинск",
"Phone": "89535977776",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000721",
"FullName": "Лавдаренко Анна Анатольевна",
"Email": "anna.lavdarenko@mail.ru",
"Phone": "+79607535599",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000722",
"FullName": "Хмелева Дарья Александровна",
"Email": "khmeleva-d@mail.ru",
"Phone": "+79607544350",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000723",
"FullName": "Конарев Максим Владимирович",
"Email": "mkonarev502@gmail.com",
"Phone": "+79832987525",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000724",
"FullName": "Герменчук Елена Владимировна",
"Email": "lenc93bb@mail.ru",
"Phone": "+79607662402",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000725",
"FullName": "Хмурин Александр Михайлович",
"Email": "alek19@mail.ru",
"Phone": "+79029291562",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000726",
"FullName": "Скаморина Мария Кирилловна",
"Email": "muceniece.maria2008@yandex.ru",
"Phone": "+79509839093",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000727",
"FullName": "Халецкая Мария",
"Phone": "+79039882211",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000728",
"FullName": "Гаврилова Анжелика Евгеньевна",
"Email": "angelika32@bk.ru",
"Phone": "+79535941989",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000729",
"FullName": "Гантимурова Яна Олеговна",
"Email": "missis-guzenko88@mail.ru",
"Phone": "+79130434133",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000730",
"FullName": "Архип Виктор",
"Phone": "+79607682068",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000731",
"FullName": "Явонова Наталья Геннадьевна",
"Email": "Natamail10@rambler.ru",
"Phone": "+79025523790",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000732",
"FullName": "Гарькавенко Виктор Валерьевич",
"Phone": "+79039233000",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000733",
"FullName": "Китаев Игорь Юрьевич",
"Email": "igoKit@mail.ru",
"Phone": "+79834200109",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000734",
"FullName": "Паничевская Екатерина",
"Email": "katya_kr@inbox.ru",
"Phone": "+79048919838",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000735",
"FullName": "Кожина Наталья Григорьевна",
"Email": "natali19ko@yandex.ru",
"Phone": "+79509925044",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000736",
"FullName": "Тучина Наталья Анатольевна",
"Email": "h11091979@mail.ru",
"Phone": "+79135920102",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000737",
"FullName": "Шумейко Павел Гельмутович",
"Phone": "+79135387421",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000738",
"FullName": "Чикишев Кирилл Игоревич",
"Email": "kirillchikishev2005@gmail.com",
"Phone": "+79029180373",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000739",
"FullName": "Хурамшин Вадим Данилович",
"Email": "drvaskas@mail.ru",
"Phone": "+79173833869",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000740",
"FullName": "Куволдан Михаил Васильевич",
"Email": "harleguik.zeko93@gmail.com",
"Phone": "+79131799321",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000741",
"FullName": "Суворова Анастасия Олеговна",
"Email": "nanka90210@gmail.com",
"Phone": "+79994430375",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000742",
"FullName": "Ермолаева Ирина Георгиевна",
"Email": "pobedairinailove198825@mail.ru",
"Phone": "+79509968472",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000743",
"FullName": "Тобышев Константин Валерьевич",
"Email": "2946545@mail.ru",
"Phone": "+79029246545",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000744",
"FullName": "Волков Виктор Викторович",
"Phone": "+79029247696",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000745",
"FullName": "Глисков Александр Александрович",
"Email": "gliskov@yandex.ru",
"Phone": "+79835081370",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000746",
"FullName": "Коровец Артём Евгеньевич",
"Phone": "+79130361385",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000747",
"FullName": "Тимонин Александр Сергеевич",
"Email": "virusss911@rambler.ru",
"Phone": "+79036256437",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000748",
"FullName": "Живаев Артем Геннадьевич",
"Email": "zhivaev_artem@mail.ru",
"Phone": "+79504074141",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000749",
"FullName": "Петров Кирилл Александрович",
"Email": "laki.ruru@mail.ru",
"Phone": "+79082062322",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000750",
"FullName": "Сапрошина Татьяна Борисовна",
"Email": "t.saproshina@yandex.ru",
"Phone": "+79048946686",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000751",
"FullName": "Ахмедзянов Рамиль Махмутович",
"Email": "Ram.575@yahoo.com",
"Phone": "+79233033765",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000752",
"FullName": "Шушаков Алексей Олегович",
"Phone": "+79504287821",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000753",
"FullName": "Гольченко Анастасия Евгеньевна",
"Phone": "+79509957184",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000754",
"FullName": "Бондарева Дарья Владиславовна",
"Email": "cherkashina.dasha2016@yandex.ru",
"Phone": "+79233213682",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000755",
"FullName": "Филиппов Виталий Викторович",
"Phone": "+79080182851",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000756",
"FullName": "Чуриорв Станислав Юрьевич",
"Phone": "+79235999228",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000150",
"FullName": "Серова Юлия",
"Phone": "+79232932327",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000151",
"FullName": "Оскар Екатерина",
"Phone": "+79832864525",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000152",
"FullName": "Зауэр Ольга",
"Phone": "+79069118731",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000432",
"FullName": "ИП Мухачев Михаил Михайлович",
"Email": "mihail@truegeek.ru",
"Phone": "",
"INN": "880300288590",
"KPP": "880301001",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000433",
"FullName": "ИП Юдин Владимир Викторович",
"Email": "welcome@dotstore.ru",
"Phone": "",
"INN": "246512755736",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000153",
"FullName": "Абдуллаева Эльмира",
"Phone": "+79964278396",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000154",
"FullName": "Ершова Дарья",
"Phone": "+79234548657",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000155",
"FullName": "Рубина Юлия",
"Phone": "+79082013871",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000434",
"FullName": "ИП Беляева Ольга Анатольевна",
"Email": "olga79olga2018@mail.ru",
"Phone": "89029247792",
"INN": "246311292460",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000156",
"FullName": "Смирнова Лира",
"Phone": "+79029785371",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000157",
"FullName": "Павлович Данила",
"Phone": "+79233777710",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000158",
"FullName": "Мусиенко Михаил",
"Phone": "+79029777171",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000159",
"FullName": "Стомер Николай",
"Phone": "+79233410799",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000160",
"FullName": "Venediktova Anna",
"Phone": "+79131990023",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000435",
"FullName": "ИП Топалян Григорий Арменович",
"Email": "gregoryarm@mail.ru",
"Phone": "89509719802",
"INN": "246011182293",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000161",
"FullName": "Смирнов Анатолий",
"Phone": "+79535995245",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000162",
"FullName": "Романова Екатерина",
"Phone": "+79832089828",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000163",
"FullName": "Дмитриева Виктория",
"Phone": "+79082215561",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000164",
"FullName": "Шумилов Алексей",
"Phone": "+79135637345",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000165",
"FullName": "Пушкарев Сергей",
"Phone": "+79027634470",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000166",
"FullName": "Губарев Андрей",
"Phone": "+79994481461",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000167",
"FullName": "Мишина Екатерина",
"Phone": "+79135936121",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000168",
"FullName": "Туктарова Эльвира",
"Phone": "+79293558515",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000169",
"FullName": "Сапожникова Анна",
"Phone": "+79504097057",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000170",
"FullName": "Филимонова Евгения",
"Phone": "+79130300320",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000171",
"FullName": "Лужникова Оксана",
"Phone": "+79639585788",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000172",
"FullName": "Титов Артем",
"Phone": "+79504243308",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000173",
"FullName": "Ковальчук Владимир",
"Phone": "+79029275000",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000174",
"FullName": "Баглай Григорий",
"Phone": "+79135883220",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000175",
"FullName": "Березюк Николай",
"Phone": "+79607632088",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000176",
"FullName": "Анатольевич Данил",
"Phone": "+79833750255",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000177",
"FullName": "Топоев Андрей",
"Phone": "+79232974416",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000178",
"FullName": "Баженова Мария",
"Phone": "+79131980202",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000179",
"FullName": "Буяк Марта",
"Phone": "+79232766795",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000180",
"FullName": "Гаврилец Анастасия",
"Phone": "+79607599990",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000181",
"FullName": "Ли Сергей",
"Phone": "+79992290484",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000182",
"FullName": "Трунова Дарья",
"Phone": "+79504249728",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000183",
"FullName": "Таракин Александр",
"Phone": "+79293557552",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000436",
"FullName": "ИП Оганесян Александр Арамаисович",
"Email": "anna.oganesyan.86@bk.ru",
"Phone": "89832943640",
"INN": "610301835609",
"KPP": "610301001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000184",
"FullName": "Королева Дарья",
"Phone": "+79039597627",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000185",
"FullName": "Горбатко Анастасия",
"Phone": "+79233062265",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000186",
"FullName": "Гайдабуро Евгений",
"Phone": "+79135287014",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000187",
"FullName": "Высоцкая Анастасия",
"Phone": "+79504291888",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000437",
"FullName": "ИП Акопян Ваге",
"Email": "akopyan_vage@mail.ru",
"Phone": "89233679662",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000188",
"FullName": "Зоненберг Мария",
"Phone": "+79293559070",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000189",
"FullName": "Orlova Elena",
"Phone": "+79659147858",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000438",
"FullName": "Хозкомплект Белых С.О.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000190",
"FullName": "Шубакова Ангелина",
"Phone": "+79233324521",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000191",
"FullName": "Баранникова Мария",
"Phone": "+79135535428",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000192",
"FullName": "Павлова Юлия",
"Phone": "+79535994169",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000439",
"FullName": "ЗАО ИКФ «Энергопроминвест»",
"Email": "epi1993@krasmail.ru",
"Phone": "2121596,2123049",
"INN": "2463019690",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000439",
"FullName": "ЗАО ИКФ «Энергопроминвест»",
"Email": "michael@epi-kr.ru",
"Phone": "2121596,2123049",
"INN": "2463019690",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000193",
"FullName": "Иванова Ирина",
"Phone": "+79676125492",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000194",
"FullName": "Артюхова Ангелина",
"Phone": "+79235781203",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000195",
"FullName": "Маликова Мария",
"Phone": "+79135343482",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000440",
"FullName": "ИП Ниазян Азат",
"Email": "kfh_karelina005@mail.ru",
"Phone": "89082235337",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000196",
"FullName": "Борисова Ангелина",
"Phone": "+79233189372",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000197",
"FullName": "Мачусская Дарья",
"Phone": "+79509938102",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000441",
"FullName": "ИП Жданов ХК",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000442",
"FullName": "Индивидуальный предприниматель Шуляк Ирина Юрьевна",
"Email": "olga.dmitrieva@forvardavto.ru",
"Phone": "3912777725",
"INN": "246005877118",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000198",
"FullName": "Воробьева Вероника",
"Phone": "+79130360049",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000199",
"FullName": "Линяев Сергей",
"Phone": "+79833612533",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000200",
"FullName": "Тарасова Дарья",
"Phone": "+79632587577",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000201",
"FullName": "В Анастасия",
"Phone": "+79131815022",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000202",
"FullName": "Семёнов Алексей",
"Phone": "+79029133847",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000203",
"FullName": "Титова Анна",
"Phone": "+79504185013",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000204",
"FullName": "Железняк Яна",
"Phone": "+79138353734",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000443",
"FullName": "ИП Скоков Михаил",
"Email": "rusocenka@list.ru",
"Phone": "89831595403",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000205",
"FullName": "Редькина Катя",
"Phone": "+79835739007",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000444",
"FullName": "ИП Кондрашова Ольга Петровна",
"Email": "osik.82@mail.ru",
"Phone": "89138327562",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000445",
"FullName": "ИП Корнейчук Виктор",
"Email": "nika-1516@ya.ru",
"Phone": "89029824118",
"INN": "246406870215",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000217",
"FullName": "Анна Федотова",
"Phone": "89082022879",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000206",
"FullName": "Миронова Софья",
"Phone": "+79504282045",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000207",
"FullName": "Зотова Татьяна",
"Phone": "+79029255345",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000208",
"FullName": "Ivanov Ivanov",
"Phone": "+79778787729",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000209",
"FullName": "Васильева Ольга",
"Phone": "+79535851451",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000446",
"FullName": "ИП Бедрицкий Василий Васильевич",
"Phone": "89234539499",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000447",
"FullName": "ИП Овсянников Дмитрий Константинович",
"Phone": "89607636818",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000210",
"FullName": "Кондрашов Евгений",
"Phone": "+79181661552",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000211",
"FullName": "Агибалова Юлия",
"Phone": "+79135711801",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000212",
"FullName": "Хеирхабарова Кристина",
"Phone": "+79778086628",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000213",
"FullName": "С Наталья",
"Phone": "+79029825921",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000214",
"FullName": "Нячко Елена",
"Phone": "+79233545776",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000215",
"FullName": "Т М",
"Phone": "+79233510777",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000216",
"FullName": "Щугорева Ирина",
"Phone": "+79029691154",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000218",
"FullName": "Ф Александр",
"Phone": "+79603693465",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000219",
"FullName": "Рябова Кристина",
"Phone": "+79233751441",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000220",
"FullName": "Лавренюк Мария",
"Phone": "+79994404061",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000221",
"FullName": "Лепеша Юрий",
"Phone": "+79135320103",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000222",
"FullName": "Токмачева Мария",
"Phone": "+79233177166",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000223",
"FullName": "Быков Андрей",
"Phone": "+79293082882",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000224",
"FullName": "Богданова Екатерина",
"Phone": "+79131776358",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000225",
"FullName": "Владимир Степанов",
"Phone": "+79029227768",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000226",
"FullName": "Мария Жилинская",
"Phone": "+79504025999",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000227",
"FullName": "Крылов Алексей",
"Phone": "+79994412617",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000228",
"FullName": "Новикова Еквтерина",
"Phone": "+79832075375",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000229",
"FullName": "Житникова Лариса",
"Phone": "+79833634585",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000230",
"FullName": "Остапчук Кирилл",
"Phone": "+79233139800",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000231",
"FullName": "Ерлыков Дмитрий",
"Phone": "+79527487555",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000232",
"FullName": "Мальцева Наталья",
"Phone": "+79639558866",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000233",
"FullName": "Неупокоева Диана",
"Phone": "+79135885498",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000234",
"FullName": "Коваленко Анастасия",
"Phone": "+79135686572",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000235",
"FullName": "Соколова Софья",
"Phone": "+79233034676",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000236",
"FullName": "Гончарова Анастасия",
"Phone": "+79832720524",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000237",
"FullName": "Волкова Полина",
"Phone": "+79236686972",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000238",
"FullName": "Никитина Анастасия",
"Phone": "+79832870619",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000239",
"FullName": "Попов Никита",
"Phone": "+79029476839",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000448",
"FullName": "ИП Дубовой Александр Владимирович",
"Phone": "89509941713",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000240",
"FullName": "Антонович Екатерина",
"Phone": "+79135892259",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000241",
"FullName": "Orozbay Amanbek",
"Phone": "+79964285385",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000242",
"FullName": "Джусоев Алан",
"Phone": "+79994402914",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000243",
"FullName": "Pilipko Ирина",
"Phone": "+79232061009",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000244",
"FullName": "Лушкин Сергей",
"Phone": "+79504319433",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000245",
"FullName": "Кормина Татьяна",
"Phone": "+79232936901",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000246",
"FullName": "Барских Наталья",
"Phone": "+79232831661",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000247",
"FullName": "Ложкина Екатерина",
"Phone": "+79136772330",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000248",
"FullName": "Загирова Яна",
"Phone": "+79833630220",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000249",
"FullName": "Кудимова Виктория",
"Phone": "+79029188809",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000250",
"FullName": "Настя Сердюкова",
"Phone": "+79610949492",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000251",
"FullName": "Лукьянова Яна",
"Phone": "+79029204305",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000252",
"FullName": "Дорогова Алёна",
"Phone": "+79135696572",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000253",
"FullName": "Османова Эсмира",
"Phone": "+79135507619",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000254",
"FullName": "Шумкина Галина",
"Phone": "+79135825164",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000255",
"FullName": "Гурина Кристина",
"Phone": "+79130392398",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000256",
"FullName": "Яценко Анастасия",
"Phone": "+79293315931",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000257",
"FullName": "Величко Дарья",
"Phone": "+79504174428",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000258",
"FullName": "Тыщенко Надежда",
"Phone": "+79135894919",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000449",
"FullName": "ИП Соколов Игорь Валерьевич",
"Phone": "89082150014",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000259",
"FullName": "Солдатова Инна",
"Phone": "+79504251706",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000260",
"FullName": "Марченко Елена",
"Phone": "+79509991660",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000261",
"FullName": "Смирнова Дарья",
"Phone": "+79131814244",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000262",
"FullName": "Курасова Анна",
"Phone": "+79029504074",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000263",
"FullName": "Штейн Анастасия",
"Phone": "+79232853703",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000264",
"FullName": "Литвиненко Андрей",
"Phone": "+79994425746",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000265",
"FullName": "Игуменова Алёна",
"Phone": "+79029210384",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000266",
"FullName": "Глазунов Дмитрий Викторович",
"Phone": "89504241650",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000267",
"FullName": "Герасимова Елена",
"Phone": "+79659171464",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000268",
"FullName": "Катрич Олег",
"Phone": "+79135298614",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000269",
"FullName": "Морозова Екатерина",
"Phone": "+79082125611",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000270",
"FullName": "Баутина Татьяна",
"Phone": "+79048950837",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000271",
"FullName": "K Gleb",
"Phone": "+79135321310",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000450",
"FullName": "ИП Дидур Андрей Олегович",
"Phone": "89135563901",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000272",
"FullName": "Новикова Лариса",
"Phone": "+79059764275",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000273",
"FullName": "Цибик Илья",
"Phone": "+79135606307",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000274",
"FullName": "Зыкин Николай",
"Phone": "+79960535838",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000275",
"FullName": "Камалдинов Арсений",
"Phone": "+79293071931",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000276",
"FullName": "Макаренко Дана",
"Phone": "+79029742306",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000277",
"FullName": "Алиева Рамила",
"Phone": "+79676017112",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000278",
"FullName": "Панфилов Андрей",
"Phone": "+79607627302",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000451",
"FullName": "ООО «Честная игра»",
"Email": "buh@fair-play24.ru",
"Phone": "89131898363",
"INN": "2465127606",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000279",
"FullName": "Бредихина Александра",
"Phone": "+79994430353",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000280",
"FullName": "Артякова Кристина",
"Phone": "+79833603686",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000281",
"FullName": "Дресвянских Ольга",
"Phone": "+79135914056",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000282",
"FullName": "Жданова Алина",
"Phone": "+79135916490",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000452",
"FullName": "ИП Пузынин Андрей Константинович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000283",
"FullName": "Галушко Виктор",
"Phone": "+79232816757",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000284",
"FullName": "котовщикова кристина",
"Phone": "+79130376003",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000285",
"FullName": "Ermolovich Tatiana",
"Phone": "+79039212999",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000286",
"FullName": "Романова Елизавета",
"Phone": "+79994422418",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000287",
"FullName": "Чарина Юлия",
"Phone": "+79029400593",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000288",
"FullName": "Герасимова Василина",
"Phone": "+79831497164",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000289",
"FullName": "Зубахина Дарья",
"Phone": "+79246098835",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000290",
"FullName": "Ляшева Елизавета",
"Phone": "+79831670879",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000291",
"FullName": "Васильева Ирина",
"Phone": "+79511634424",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000453",
"FullName": "ИП Кандин Евгений Анатольевич",
"Email": "ea663170@mail.ru",
"Phone": "89029124990",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000292",
"FullName": "Ермаков Константин Олегович",
"Phone": "89676140690",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000295",
"FullName": "Моисеева Светлана Анатольевна",
"Phone": "89964301123",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000293",
"FullName": "Козлова Полина",
"Phone": "+79833400454",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000294",
"FullName": "Беликова Анастасия",
"Phone": "+79535806761",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000454",
"FullName": "ИП Вишнякова Жанна Анатольевна",
"Email": "apanasenkoand@yandex.ru",
"Phone": "89504066313",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000456",
"FullName": "Кукушкин Дмитрий",
"Email": "tron_85@bk.ru",
"Phone": "89509766669",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000457",
"FullName": "Гордеев Артем Романович (курьер)",
"Phone": "89029754228",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000458",
"FullName": "Хозкомплект Шкурко Вадим",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000296",
"FullName": "Кудлацкий Анатолий Сергеевич",
"Phone": "89131800128",
"INN": "7707083893",
"KPP": "770701001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000297",
"FullName": "Николай Зыкин",
"Phone": "89960535838",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000311",
"FullName": "Индивидуальный предприниматель Глебова Татьяна Андреевна",
"Phone": "",
"INN": "744719462888",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000455",
"FullName": "ИП Кольцов Александр Юрьевич",
"Email": "rolcoyalex@mail.ru",
"Phone": "89232942098",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000298",
"FullName": "Водолазская Надежда",
"Phone": "+79029747533",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000299",
"FullName": "Ведмечук Вячеслав",
"Phone": "+79658991264",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000300",
"FullName": "Бабенко Анастасия",
"Phone": "+79994460173",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000301",
"FullName": "Федунов Максим",
"Phone": "+79607653080",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000302",
"FullName": "Белова Ульяна",
"Phone": "+79235085444",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000303",
"FullName": "Орлова Олеся",
"Phone": "+79235573607",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000304",
"FullName": "Досумбетова Вероника",
"Phone": "+79964287379",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000305",
"FullName": "Черкасова Екатерина",
"Phone": "+79333331569",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000306",
"FullName": "Мартынова Татьяна",
"Phone": "+79504051016",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000307",
"FullName": "Нагаев Максим",
"Phone": "+79835030729",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000308",
"FullName": "Gaytaeva Malena",
"Phone": "+79131987534",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000309",
"FullName": "Бочаров Никита",
"Phone": "+79135563000",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000310",
"FullName": "Туранова Юлия",
"Phone": "+79607736420",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000312",
"FullName": "ИП Чолоян Роман Карапетович",
"Email": "humaeyan.karine@mail.ru",
"Phone": "89135563858",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000317",
"FullName": "Турчина Кристина",
"Phone": "89832091593",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000459",
"FullName": "ООО \"АГАТ\"",
"Email": "sibpromkas@mail.ru",
"Phone": "",
"INN": "2452044455",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000313",
"FullName": "Хабенский Константин",
"Phone": "+79233145150",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000314",
"FullName": "Иванов Василий",
"Phone": "+79833632057",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000315",
"FullName": "Циберман Юлия",
"Phone": "+79130443056",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000316",
"FullName": "Сычева Оксана",
"Phone": "+79135952002",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000318",
"FullName": "Струкова Виктория",
"Phone": "+79130443734",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000319",
"FullName": "Любин Олег",
"Phone": "+79131949247",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000320",
"FullName": "Сокур Ирина",
"Phone": "+79131832760",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000321",
"FullName": "Кузнецова Наталья",
"Phone": "+79135945946",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000322",
"FullName": "Юдкина Элина",
"Phone": "+79048951477",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000323",
"FullName": "Павлюк Александр",
"Phone": "+79829864139",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000324",
"FullName": "Королева Екатерина",
"Phone": "+79509981948",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000325",
"FullName": "Полякова Анна",
"Phone": "+79233755200",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000326",
"FullName": "EgorovB24 Aleksandr",
"Phone": "+79607639797",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000327",
"FullName": "Петрова Марина",
"Phone": "+79994426487",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000460",
"FullName": "ИП Егоров Александр",
"Email": "drew444124@mail.ru",
"Phone": "+79607639797",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000461",
"FullName": "ИП Бельков Станислав Валерьевич",
"Email": "larix24@mail.ru",
"Phone": "+79293366836",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000328",
"FullName": "Степанова Юлия",
"Phone": "+79969329326",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000329",
"FullName": "Брюханова Анна",
"Phone": "+79994431223",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000330",
"FullName": "Гришан Арина",
"Phone": "+79535832923",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000462",
"FullName": "ИП Богданов Дмитрий",
"Email": "2080802\"ьфшдюкг",
"Phone": "89835080802",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000331",
"FullName": "Милова Ия",
"Phone": "+79994692510",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000463",
"FullName": "ИП Пшонко Виталий Владимирович",
"Phone": "89237725777",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000332",
"FullName": "Васильцов Виктор",
"Phone": "89607622225",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000334",
"FullName": "Якутенок Константин Эдуардович",
"Phone": "89994405252",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000335",
"FullName": "ПК \"АРТЕЛЬ \"СТАТСКИЙ СОВЕТНИК\"",
"Phone": "",
"INN": "2466189429",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000333",
"FullName": "Рыжов Андрей",
"Phone": "+79504012838",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000336",
"FullName": "Чаленко Павел",
"Phone": "+79509793279",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000337",
"FullName": "Filatov Vladimir",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000338",
"FullName": "Filatov Vladimir",
"Phone": "+79234722086",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000464",
"FullName": "ИП Терентьев Николай Андреевич",
"Email": "ternik888@yandex.ru",
"Phone": "89131914524",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000339",
"FullName": "Русакова Екатерина",
"Phone": "+79992009149",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000340",
"FullName": "Моисеева Светлана",
"Phone": "+79964301123",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000341",
"FullName": "Зулкайдарова Александра",
"Phone": "+79832802070",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000342",
"FullName": "Фролова Елена",
"Phone": "+79232883288",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000343",
"FullName": "Азингареева Кристина",
"Phone": "+79232818196",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000465",
"FullName": "ИП Тархнишвили Дмитрий",
"Email": "trendvideo@mail.ru",
"Phone": "89233255530",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000344",
"FullName": "Куренкова Мария",
"Phone": "+79135747113",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000345",
"FullName": "Семенив Ксения",
"Phone": "+79676122132",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000466",
"FullName": "ХОЗКОМПЛЕКТ Беляк Евгений Петрович",
"Phone": "89080139661",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000346",
"FullName": "Крылова Ирина",
"Phone": "+79232867686",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000347",
"FullName": "Мулеванова Софья",
"Phone": "+79082071296",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000348",
"FullName": "Полещук Анастасия",
"Phone": "+79994453615",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000349",
"FullName": "Титов Герман",
"Phone": "+79538485665",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000350",
"FullName": "Назаров Александр",
"Phone": "+79232828444",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000352",
"FullName": "Рыбалко Николай Сергеевич",
"Phone": "89233260500",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000353",
"FullName": "ИП Васильев Максим Игоревич",
"Phone": "89233333233",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000356",
"FullName": "ООО Торговая компания АлСтрой",
"Phone": "",
"INN": "2465320960",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000351",
"FullName": "Скребцова Влада",
"Phone": "+79029662388",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000354",
"FullName": "Андреева Олеся",
"Phone": "+79135912157",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000355",
"FullName": "Павловская Анастасия",
"Phone": "+79620824614",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000357",
"FullName": "Муллагалеева Анна",
"Phone": "+79232762021",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000358",
"FullName": "Андрияс Ольга",
"Phone": "+79232806977",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000359",
"FullName": "Зайцева Екатерина",
"Phone": "+79130446912",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000360",
"FullName": "Калимулина Вероника",
"Phone": "+79509804432",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000467",
"FullName": "Пузырев Владислав Дмитриевич",
"Phone": "89135540095",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000361",
"FullName": "Кузьмин Владимир Иванович (личная)",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000362",
"FullName": "Легачёва Анастасия",
"Phone": "+79082218641",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000468",
"FullName": "ООО Зевс",
"Email": "dkrsn@mail.ru",
"Phone": "89272714272",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000469",
"FullName": "Дорохов Ярослав Игоревич",
"Phone": "+79535977410",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000470",
"FullName": "Сулайманов Зак",
"Phone": "89659099900",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000363",
"FullName": "Терская Валентина",
"Phone": "+79509730360",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000364",
"FullName": "Бутакова Настя",
"Phone": "+79631805696",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000365",
"FullName": "Фоминых Елизавета",
"Phone": "+79132969776",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000366",
"FullName": "Попова Юля",
"Phone": "+79535813254",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000367",
"FullName": "Золотых Ксения",
"Phone": "+79333300776",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000368",
"FullName": "Чесных Александр",
"Phone": "+79232917600",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000369",
"FullName": "Пономаренко Игорь",
"Phone": "+79659169080",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000370",
"FullName": "Семенов Юрий",
"Phone": "+79135340006",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000371",
"FullName": "Гордеева Ю.Н. (внесение наличных)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000372",
"FullName": "Сокирка Дмитрий Дмитриевич",
"Phone": "89994459422",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000373",
"FullName": "Мельникова Татьяна",
"Phone": "+79131891790",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000374",
"FullName": "Емельяненко Ирина",
"Phone": "+79048905404",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000375",
"FullName": "Бледных Елена",
"Phone": "+79233763889",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000376",
"FullName": "Прилепских Алина",
"Phone": "+79233747097",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000377",
"FullName": "Иванова Ксения",
"Phone": "+79130453639",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000378",
"FullName": "Белоруков Роман",
"Phone": "+79504029699",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000379",
"FullName": "Перетолчина Екатерина",
"Phone": "+79632559933",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000380",
"FullName": "Сосновский Андрей",
"Phone": "+79964304241",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000381",
"FullName": "Стефанькина Валерия",
"Phone": "+79332005242",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000382",
"FullName": "Свешникова Валерия",
"Phone": "+79504053635",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000383",
"FullName": "Kuzmina Alexandra",
"Phone": "+79232766722",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000384",
"FullName": "Алексеева Виктория",
"Phone": "+79135382476",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000385",
"FullName": "Ковалева Анастасия",
"Phone": "+79233124416",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000471",
"FullName": "ИП Кузьменко Дмитрий Алексеевич",
"Email": "neobyt@mail.ru",
"Phone": "89029408886",
"INN": "246200321613",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000386",
"FullName": "Алиев Сеймур",
"Phone": "+79994457801",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000387",
"FullName": "Бровченко Ангелина",
"Phone": "+79135878131",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000391",
"FullName": "Гаряминский Дмитрий Игоревич",
"Email": "thewinningteam967@gmail.ru",
"Phone": "89131988533",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000472",
"FullName": "ИП Кузнецов Николай Германович",
"Phone": "89029183558",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000388",
"FullName": "Быков Тимофей",
"Phone": "+79509971220",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000389",
"FullName": "Ефимов Антон",
"Phone": "+79996566533",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000390",
"FullName": "Плеханов Андрей",
"Phone": "+79293098586",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000392",
"FullName": "Лысенко Татьяна",
"Phone": "+79133258004",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000473",
"FullName": "ИП Сергей Лейниш",
"Email": "serg.leinish@yandex.ru",
"Phone": "9082048666",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000393",
"FullName": "И Марина",
"Phone": "+79532579811",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000394",
"FullName": "Ландышев Вячеслав",
"Phone": "89535906810",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000395",
"FullName": "Лаврентьева Елена",
"Phone": "+79029279820",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000396",
"FullName": "Шепотило Иван",
"Phone": "+79832898407",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000397",
"FullName": "Пушкова Наталья",
"Phone": "+79130333385",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000398",
"FullName": "Азизова Александра",
"Phone": "+79658977028",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000399",
"FullName": "Власов Артём",
"Phone": "+79233394808",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000474",
"FullName": "Сахиб Гасымов",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000400",
"FullName": "Бони Юлия",
"Phone": "+79232853371",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000401",
"FullName": "Шутеева Марина",
"Phone": "+79632582129",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000402",
"FullName": "Гусак Галина",
"Phone": "+79082120664",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000403",
"FullName": "Чемиренко Игорь",
"Phone": "+79233250847",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000404",
"FullName": "Чемиренко Оксана",
"Phone": "+79659004202",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000405",
"FullName": "Сухотина Сильва",
"Phone": "+79620699200",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000406",
"FullName": "Рыбакова Мира",
"Phone": "+79233430102",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000407",
"FullName": "Арсланов Максим",
"Phone": "+79333231226",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000408",
"FullName": "Агуреев Павел",
"Phone": "+79080103833",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000409",
"FullName": "Синькевич Илья",
"Phone": "+79080134151",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000410",
"FullName": "Нечепуренко Илья",
"Phone": "+79080194654",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000411",
"FullName": "Кононов Константин",
"Phone": "+79232787744",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000412",
"FullName": "Попов Алексей",
"Phone": "+79233130805",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000421",
"FullName": "ИП Крупин Алексей Олегович",
"Email": "mobiziprus@gmail.com",
"Phone": "+79219403161",
"INN": "471401831200",
"KPP": "471401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000413",
"FullName": "Крыш Екатерина",
"Phone": "+79994402359",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000414",
"FullName": "Орлова Мария",
"Phone": "+79135964969",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000415",
"FullName": "Огиенко Маргарита",
"Phone": "+79833621921",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000416",
"FullName": "Гельвер Александр",
"Phone": "+79509970863",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000417",
"FullName": "Рудольф Антон",
"Phone": "+79535987826",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000475",
"FullName": "ИП Лущик Роман Валерьевич",
"Email": "lrv24@mail.ru",
"Phone": "89333319600",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000418",
"FullName": "Елеонович Ирина",
"Phone": "+79029911061",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000419",
"FullName": "Седельникова Юля",
"Phone": "+79130488675",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000420",
"FullName": "Орлова Анастасия",
"Phone": "+79831602126",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000422",
"FullName": "Мариноха Олеся",
"Phone": "+79535857979",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000423",
"FullName": "Иванова Татьяна",
"Phone": "+79135823633",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000424",
"FullName": "Крафт Вероника",
"Phone": "+79632691912",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000425",
"FullName": "Гурина Регина",
"Phone": "+79039218779",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000426",
"FullName": "Петровская Ольга",
"Phone": "+79029403125",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000427",
"FullName": "Алукаев Наиль",
"Phone": "+79135277068",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000428",
"FullName": "Файзулина Татьяна",
"Phone": "+79029248300",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000429",
"FullName": "Михалева Гульназ",
"Phone": "+79069114335",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000430",
"FullName": "Бехтерева Екатерина",
"Phone": "+79994464926",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000476",
"FullName": "ИП Сугурбаева Ольга Владимировна",
"Email": "osugutbaeva@mail.ru",
"Phone": "89631880808",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000431",
"FullName": "Попович Анастасия",
"Phone": "+79607652591",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000432",
"FullName": "Мушавец Любовь",
"Phone": "+79620839505",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000433",
"FullName": "Голубь Ольга",
"Phone": "+79631911127",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000434",
"FullName": "Панченко Екатерина",
"Phone": "+79293080452",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000477",
"FullName": "ООО «СПЕЦКТК»",
"Email": "2155155@bk.ru",
"Phone": "",
"INN": "2460250564",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000478",
"FullName": "ООО Онлайн-Медика",
"Email": "boldina081@mail.ru",
"Phone": "83912582773",
"INN": "2452043652",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000435",
"FullName": "Artem Artem",
"Phone": "+79231262397",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000436",
"FullName": "Саворенко Анастасия",
"Phone": "+79135867082",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000437",
"FullName": "Кораблева Татьяна",
"Phone": "+79135220366",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000438",
"FullName": "Дайнеко Ксения",
"Phone": "+79235755854",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000439",
"FullName": "Медведева Алина",
"Phone": "+79384480500",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000440",
"FullName": "Кушников Сергей",
"Phone": "+79135771011",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000441",
"FullName": "Волчек Вилена",
"Phone": "+79233128545",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000479",
"FullName": "ИП Сафина Алена Александровна",
"Email": "safina-alena@list.ru",
"Phone": "89080249933",
"INN": "4081781013",
"KPP": "408101001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000442",
"FullName": "Алексеева Анастасия",
"Phone": "+79632621811",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000443",
"FullName": "Королева Дарья",
"Phone": "+79029922698",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000444",
"FullName": "Пархацкая Евгения",
"Phone": "+79029249668",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000445",
"FullName": "Братчун Елена",
"Phone": "+79029191029",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000446",
"FullName": "Турабов Митал",
"Phone": "+79059752626",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000447",
"FullName": "Ренкс Мария",
"Phone": "+79069166989",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000480",
"FullName": "ИП",
"Email": "nosov@autodevice.info",
"Phone": "+79135567373",
"INN": "245012262709",
"KPP": "245001001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000481",
"FullName": "ИП Речкина Лариса Антоновна",
"Email": "lariska.rechkina@mail.ru",
"Phone": "89500656659",
"INN": "381603686920",
"KPP": "381601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000482",
"FullName": "ИП Жидких Дарья Андреевна",
"Email": "dsh.tmn@gmail.ru",
"Phone": "89339990799",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000483",
"FullName": "Прокопишко Иван (дифорс)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000448",
"FullName": "Кузнецова Анастасия",
"Phone": "+79135136684",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000449",
"FullName": "Карачун Кристина",
"Phone": "+79994454787",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000450",
"FullName": "З Наталья",
"Phone": "+79233226039",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000451",
"FullName": "Турусов Артём",
"Phone": "+79994485525",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000484",
"FullName": "ИП Стержанов Станислав Юрьевич",
"Email": "ctac_ur@mail.ru",
"Phone": "89059703766",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000452",
"FullName": "ООО\"УНИКАР\"",
"Phone": "",
"INN": "5507043265",
"KPP": "550701001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000456",
"FullName": "ЧАСТНОЕ ЛИЦО",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000457",
"FullName": "Лахов Константин Алексеевич",
"Phone": "89509617038",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000453",
"FullName": "Скирточенко Ирина",
"Phone": "+79232879777",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000454",
"FullName": "Uyrei Redozubov",
"Phone": "+79951344238",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000455",
"FullName": "Бородина Ангелина",
"Phone": "+79504179951",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000467",
"FullName": "АНО «ЦВВС»",
"Phone": "89048988890",
"INN": "2460249135",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000458",
"FullName": "Гаврилов Григорий",
"Phone": "+79535887708",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000459",
"FullName": "Секурцев Андрей",
"Phone": "+79029515992",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000460",
"FullName": "Огородова Юлия",
"Phone": "+79029139207",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000461",
"FullName": "Пантелеев Дмитрий",
"Phone": "+79135945497",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000485",
"FullName": "ИП Филатов А.А.",
"Email": "filatalex@mail.ru",
"Phone": "89835070000",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000486",
"FullName": "ИП Котвицкая Светлана Сергеевна",
"Email": "kotvitskayas@mail.ru",
"Phone": "89234882884",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000462",
"FullName": "Шваргонова Надежда",
"Phone": "+79080217444",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000463",
"FullName": "Панюшкина Кристина",
"Phone": "+79293319040",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000464",
"FullName": "Заболотникова Наталья",
"Phone": "+79135564628",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000487",
"FullName": "ООО «Диверсификация»",
"Email": "kireev@autodevice.info",
"Phone": "89232719800",
"INN": "2466163460",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000465",
"FullName": "Максимова Екатерина",
"Phone": "+79293574968",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000466",
"FullName": "Грызлова Валерия",
"Phone": "+79130384956",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000488",
"FullName": "Красноярское региональное отделение Общероссийской общественной организации «Ассоциация юристов России»",
"Email": "kovrigina07@mail.ru",
"Phone": "",
"INN": "2460085952",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000468",
"FullName": "Евельсон Роман",
"Phone": "+79080130003",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000489",
"FullName": "Брюханова Ирина Викторовна",
"Email": "ir.rod@bk.ru",
"Phone": "89535888858",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000469",
"FullName": "Афанасьева Алена",
"Phone": "+79607603701",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000490",
"FullName": "Индивидуальный предприниматель Мириджанян Андрей",
"Email": "a.krayushkin@olgr.ru",
"Phone": "",
"INN": "263114926482",
"KPP": "263101001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000470",
"FullName": "Алиева Виктория",
"Phone": "+79130333337",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000491",
"FullName": "Олег ФорвардАвто",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000471",
"FullName": "Заказы с сайта SNP",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000472",
"FullName": "Высокова Елена",
"Phone": "+79131763688",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000473",
"FullName": "Графодацкая Елена",
"Phone": "+79233620687",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000474",
"FullName": "Воронько Анастасия",
"Phone": "+79659157983",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000475",
"FullName": "Ященко Алина",
"Phone": "+79501032406",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000476",
"FullName": "Лакомых Наталья",
"Phone": "+79230165040",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000477",
"FullName": "Исокович Иброхим",
"Phone": "+79659110009",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000478",
"FullName": "Алескеров Наиль",
"Phone": "89835016818",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000479",
"FullName": "ИП Плаутина Полина Евгеньевна",
"Email": "zhirnova.81@mail.ru",
"Phone": "89639550080",
"INN": "246520094470",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000492",
"FullName": "ИП Сафонова Ольга Валерьевна",
"Email": "dikrsk@inbox.ru",
"Phone": "",
"INN": "246105742146",
"KPP": "246101001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000480",
"FullName": "Федотов Виктор",
"Phone": "+79676137217",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000493",
"FullName": "ИП Дороганич Александр Валерьевич",
"Email": "gvardeisk0108@yandex.ru",
"Phone": "89504304760",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000494",
"FullName": "Маргарита Навигатор",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000481",
"FullName": "Косарикова Дарья",
"Phone": "+79833608445",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000482",
"FullName": "Кукарцева Екатерина",
"Phone": "+79232708024",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000495",
"FullName": "ИП Миськов Андрей Юрьевич",
"Phone": "89836166775",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000496",
"FullName": "ИП Ковилкина Ольга Валерьевна",
"Phone": "89039206439",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000483",
"FullName": "Усс Никита",
"Phone": "+79831400555",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000497",
"FullName": "ИП Лазарев Виталий Николаевич",
"Phone": "89233066607",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000498",
"FullName": "ИП Шишкус Марина Николаевна",
"Phone": "89659106157",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000499",
"FullName": "Электроэнергия ДИФОРС",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000484",
"FullName": "Лапыгина Кристина",
"Phone": "+79333351591",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000485",
"FullName": "Ермаков Виктор",
"Phone": "+79994460919",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000486",
"FullName": "Шишкина Дарья",
"Phone": "+79233356699",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000487",
"FullName": "Сулейманова Юлия",
"Phone": "+79080243075",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000488",
"FullName": "Степаненко Мария",
"Phone": "+79831547483",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000489",
"FullName": "Ульяна Зима",
"Phone": "+79631897755",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000490",
"FullName": "Филимонова Екатерина",
"Phone": "+79233629686",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000491",
"FullName": "Хабаров Сергей",
"Phone": "+79029568090",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000492",
"FullName": "Тыченко Владислав",
"Phone": "+79835017311",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000493",
"FullName": "Яшникова Диана",
"Phone": "+79535942616",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000494",
"FullName": "Долгова Яна",
"Phone": "+79080104311",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000495",
"FullName": "Ушакова Ирина",
"Phone": "+79659101227",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000496",
"FullName": "Осокина Александра",
"Phone": "+79135197720",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000497",
"FullName": "Нижниченко Анна",
"Phone": "+79632663852",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000498",
"FullName": "Клейменова Алина",
"Phone": "+79232791877",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000499",
"FullName": "Журавлёва Наталья",
"Phone": "+79135330781",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000500",
"FullName": "К Юлия",
"Phone": "+79138320071",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000501",
"FullName": "Русанюк Кристина",
"Phone": "+79029417384",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000502",
"FullName": "Шалыгина Наталья",
"Phone": "+79832904555",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000503",
"FullName": "Никотина Юлия",
"Phone": "+79131890048",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000504",
"FullName": "Сердюк Светлана",
"Phone": "+79135196581",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000505",
"FullName": "Гогусева Анастасия",
"Phone": "+79135990620",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000506",
"FullName": "Кондратьева Ольга",
"Phone": "+79232770947",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000507",
"FullName": "Быкова Алина",
"Phone": "+79994425403",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000508",
"FullName": "Дубицкий Олег",
"Phone": "+79135954211",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000509",
"FullName": "Филимонов Илья",
"Phone": "+79676008060",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000510",
"FullName": "Вернитская Анастасия",
"Phone": "+79994464683",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000500",
"FullName": "ИП Черноусов Евгений Михайлович",
"Phone": "89029904846",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000501",
"FullName": "ИП Теперев Василий Викторович",
"Phone": "89831554470",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000502",
"FullName": "ХОЗКОМПЛЕКТ Рзаев Мрах Илгарович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000511",
"FullName": "Малаева Юлия",
"Phone": "+79135363136",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000512",
"FullName": "Паничевская Екатерина",
"Phone": "+79048919838",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000513",
"FullName": "Амосов Вячеслав",
"Phone": "+79138336649",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000514",
"FullName": "Шевцова Кристина",
"Phone": "+79233241107",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000515",
"FullName": "Филиппова Екатерина",
"Phone": "+79138369629",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000516",
"FullName": "Зябкина Алина",
"Phone": "+79835741081",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000517",
"FullName": "Кожуховский Александр",
"Phone": "+79233348996",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000518",
"FullName": "Халезова Наталья",
"Phone": "+79509909496",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000519",
"FullName": "Андрей Мельниченко",
"Phone": "+79233137608",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000520",
"FullName": "Попелюк Полина",
"Phone": "+79233177374",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000503",
"FullName": "ИП Батюшов Олег Федорович",
"Email": "info@bofik.ru",
"Phone": "+79088566705",
"INN": "890408524183",
"KPP": "890401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000521",
"FullName": "Карпенко Александр",
"Phone": "+79131717070",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000522",
"FullName": "Мисюркеева Татьяна",
"Phone": "+79135346422",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000523",
"FullName": "Соколова Кристина",
"Phone": "+79232936806",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000524",
"FullName": "Шаркунова Анастасия",
"Phone": "+79232805888",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000525",
"FullName": "Трофименко Анжелика",
"Phone": "+79538547016",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000526",
"FullName": "Кузняк Ангелина",
"Phone": "+79994480568",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000504",
"FullName": "Дзун-Хемчинский потребительский кооператив",
"Email": "chadangorpo@yandex.ru",
"Phone": "89233867361",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000527",
"FullName": "Ковригин Алексей Сергеевич",
"Phone": "89233540581",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000528",
"FullName": "Комаров Семен Александрович",
"Phone": "89233265566",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000529",
"FullName": "Писаренко Игорь",
"Phone": "+79029239292",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000530",
"FullName": "Мозгунова Анастасия",
"Phone": "+79632638963",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000531",
"FullName": "Андреева Екатерина",
"Phone": "+79676158537",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000532",
"FullName": "Фомина Мария",
"Phone": "+79233532180",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000533",
"FullName": "Лапо Елена",
"Phone": "+79233510477",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000505",
"FullName": "ИП Канаева Кристина Сергеевна",
"Phone": "89659135960",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000534",
"FullName": "Морозова Татьяна",
"Phone": "+79233055925",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000535",
"FullName": "Вячеславович Артем",
"Phone": "+79080249098",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000536",
"FullName": "Кротова Татьяна",
"Phone": "+79535970192",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000537",
"FullName": "Кошечкина Евгения",
"Phone": "+79232743431",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000507",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000508",
"FullName": "Сучков Герман Владимирович (займ)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000538",
"FullName": "Кабанова Ксения",
"Phone": "+79964304954",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000506",
"FullName": "ИП Павлиди Виктор Алексеевич",
"Email": "2152959@mail.ru",
"Phone": "89233552959",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000539",
"FullName": "Прокопишко Иван Викторович",
"Phone": "",
"INN": "7728168971",
"KPP": "770801001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000540",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "ЦБ0000541",
"FullName": "1",
"Phone": "89999999",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000542",
"FullName": "Монич Лидия",
"Phone": "+79994475361",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000549",
"FullName": "ИП Рыбкин Иван Анатольевич (займ ХК)",
"Phone": "",
"INN": "246527922605",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000550",
"FullName": "1",
"Phone": "+79293015241",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000509",
"FullName": "ИП Лаврова Ирина Владимировна",
"Email": "mschitowa@yandex.ru",
"Phone": "89676063032",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000543",
"FullName": "Лазаренко Андрей",
"Phone": "+79509715973",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000544",
"FullName": "Бородина Галина",
"Phone": "+79130451335",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000545",
"FullName": "Щукина Мария",
"Phone": "+79069102286",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000546",
"FullName": "Лобастова Елизавета",
"Phone": "+79832956848",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000547",
"FullName": "Русских Максим",
"Phone": "+79232811900",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000548",
"FullName": "Федорова Алена",
"Phone": "+79059705211",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000551",
"FullName": "Голубина Ксения",
"Phone": "+79831690264",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000552",
"FullName": "Коноваллв Владимир",
"Phone": "+79082215222",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000510",
"FullName": "ИП Потехин Илья Вадимович",
"Email": "zakup.sv@hozmag24.su",
"Phone": "+79293211681",
"INN": "246514963570",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000553",
"FullName": "Максимова Светлана",
"Phone": "+79235794103",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000554",
"FullName": "Дубовицкий Степан",
"Phone": "+79803738861",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000555",
"FullName": "Васимов Дмитрий",
"Phone": "+79029747748",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000511",
"FullName": "ИП Голубев Вячеслав Александрович",
"Email": "zakup2@hozmag24.su",
"Phone": "+79831412168",
"INN": "241901013329",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000561",
"FullName": "Соколов Владимир Викторович",
"Phone": "89039886100",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000556",
"FullName": "Степанова Елизавета",
"Phone": "+79130355338",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000557",
"FullName": "Бобровская Екатерина",
"Phone": "+79233746441",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000512",
"FullName": "ИП Гук Игорь Николаевич",
"Email": "guk-ai@mail.ru",
"Phone": "89658968639",
"INN": "241101432271",
"KPP": "241101001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000558",
"FullName": "Бартуш Наталья",
"Phone": "+79233131842",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000559",
"FullName": "Чернокозинский Александр",
"Phone": "+79607631080",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000513",
"FullName": "ИП Курчатов Николай Васильевич",
"Phone": "89607573504",
"INN": "243901593088",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000560",
"FullName": "Поликарпов Даниил",
"Phone": "+79135832851",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000514",
"FullName": "ИП Таразеев Юрий Михайлович",
"Email": "204025@mail.ru",
"Phone": "89631917940",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000562",
"FullName": "Зуева Татьяна",
"Phone": "+79994407600",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000515",
"FullName": "ИП Фаркова Лариса Михайловна",
"Email": "potapovyury@mail.ru",
"Phone": "89029270271",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000570",
"FullName": "Кринке Ксения",
"Phone": "+79082000505",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000518",
"FullName": "ИП Рябов Антон Геннадьевич",
"Phone": "2939632",
"INN": "246508503976",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000522",
"FullName": "Общество с ограниченной ответственностью «ТПК АСТРУМ»",
"Email": "art@tpk-astrum.ru",
"Phone": "+73912722223",
"INN": "2465318505",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000571",
"FullName": "Корж Евгения",
"Phone": "+79130437238",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000572",
"FullName": "Ахтямова Светлана",
"Phone": "+79029472798",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000519",
"FullName": "ИП Матвеюк Анатолий Вячеславович",
"Email": "teboom@bk.ru",
"Phone": "+79831444044",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000520",
"FullName": "ИП Гулев Андрей Сергеевич",
"Email": "syper005@inbox.ru",
"Phone": "89233282352",
"INN": "244314790502",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000521",
"FullName": "ХОЗКОМПЛЕКТ Егор 3 склад",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000573",
"FullName": "Кучерявина Арина",
"Phone": "+79832665289",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000574",
"FullName": "Рузанкина Екатерина",
"Phone": "+79233101527",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000575",
"FullName": "Добрякова Прлина",
"Phone": "+79631917948",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000576",
"FullName": "Саенко Константин",
"Phone": "+79039592242",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000577",
"FullName": "Захарова Вероника",
"Phone": "+79232964457",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000578",
"FullName": "Чурикова Кристина",
"Phone": "+79676086923",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000579",
"FullName": "Карелина Валерия",
"Phone": "+79994451598",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000580",
"FullName": "Май Катерина",
"Phone": "+79069119496",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000581",
"FullName": "Мартюхов Михаил",
"Phone": "+79233402043",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000582",
"FullName": "Коротченко Светлана",
"Phone": "+79832857165",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000583",
"FullName": "Дегтерева Виктория",
"Phone": "+79059763351",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000584",
"FullName": "Зарубин Константин",
"Phone": "+79131910268",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000585",
"FullName": "Заболотская Алена",
"Phone": "+79233293376",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000586",
"FullName": "Писарева Юлия",
"Phone": "+79130505936",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000587",
"FullName": "Речкина Наталья",
"Phone": "+79832977167",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000588",
"FullName": "Трофимова Лариса",
"Phone": "+79029918461",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000524",
"FullName": "ООО \"СКИТ\" (сотовик-м)",
"Phone": "",
"INN": "7733324680",
"KPP": "773301001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000525",
"FullName": "Варенов Вячеслав (аренда Говорова)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000527",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000523",
"FullName": "Хозкомплект Вячеслав 8 склад",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000589",
"FullName": "Салех Афанди (м.опт)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000526",
"FullName": "ИП Машуков Николай Николаевич",
"Email": "walkman-k@mail.ru",
"Phone": "89234510070",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000528",
"FullName": "ООО «ШТИЛЬ»",
"Email": "a.krayushkin@olgr.ru",
"Phone": "",
"INN": "2320248082",
"KPP": "232001001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000529",
"FullName": "ООО « ВПМ»",
"Email": "alexandrtema@gmail.com",
"Phone": "+79230176118",
"INN": "2463123162",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000530",
"FullName": "ООО «АБВ+»",
"Phone": "",
"INN": "2465176508",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000531",
"FullName": "Евгений Вайзгор (DiForce)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000590",
"FullName": "Комаров Роман",
"Phone": "89635779988",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000532",
"FullName": "ИП Галат Даниил Алексееевич",
"Email": "galaxydan@yandex.ru",
"Phone": "+79046552590",
"INN": "332712551023",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000533",
"FullName": "ИП Шулыма Кирилл Викторович",
"Email": "iprokrsk@gmail.com",
"Phone": "+79607651229",
"INN": "246317944112",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000534",
"FullName": "ИП Рукосуев Владимир Владимирович",
"Email": "admin@rukas.ru",
"Phone": "",
"INN": "246522418105",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000535",
"FullName": "ЛОКТИОНОВ ВАДИМ ЮРЬЕВИЧ",
"Phone": "",
"INN": "241104722853",
"KPP": "241101001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000536",
"FullName": "ИП Шкода Вячеслав Дмитриевич",
"Phone": "89233451015",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000537",
"FullName": "ООО \"Корреджо\"",
"Email": "pr_maxmara@mail.ru",
"Phone": "89138392930",
"INN": "2466191611",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000591",
"FullName": "Спириденко Сергей",
"Phone": "89247036947",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000538",
"FullName": "ИП Чайка Роман Игоревич",
"Email": "rich11.404@gmail.com",
"Phone": "89994432559",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000539",
"FullName": "ИП Морозов Андрей Викторович",
"Phone": "89235569240",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000540",
"FullName": "ИП Габибов Вусал",
"Email": "rayskiy.dvorik@mail.ru",
"Phone": "89135500741",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000592",
"FullName": "ООО \"СКАТ\"",
"Phone": "",
"INN": "2463123860",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000541",
"FullName": "ИП Лопатенко Иван Иванович",
"Email": "ivan.ivan.lopatenko369@gmail.com",
"Phone": "89230189031",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000593",
"FullName": "НО «Благотворительный фонд им. В.П. Астафьева»",
"Email": "ggrom1970@yandex.ru",
"Phone": "",
"INN": "2464040938",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000594",
"FullName": "ИП Осипов Анатолий Владиславович",
"Phone": "",
"INN": "241901421381",
"KPP": "241901001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000595",
"FullName": "ООО \"ГРИН\"",
"Phone": "",
"INN": "4217195144",
"KPP": "421701001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000596",
"FullName": "ООО \"Байкал-Сервис ТК\"",
"Phone": "",
"INN": "5001038736",
"KPP": "504001001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000597",
"FullName": "ООО \"Крас.МАГНИТ\"",
"Phone": "",
"INN": "2463068546",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000543",
"FullName": "ООО ГК «Климат Строй»",
"Phone": "3432768347,2133519",
"INN": "6679044048",
"KPP": "667901001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000542",
"FullName": "ИП Дорофеева Дарья Викторовна",
"Email": "darya-bakaikina@mail.ru",
"Phone": "89315175081",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000545",
"FullName": "ИП Обиднык Вадим Юрьевич",
"Phone": "89029400816",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000546",
"FullName": "Никулин Ярослав Андреевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000547",
"FullName": "Кудряшов Владимир Сереегевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000544",
"FullName": "ИП Арепьев Владислав Викторович",
"Email": "deathpunch@bk.ru",
"Phone": "89082086609",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000548",
"FullName": "Кузьмина Ольга Афонасьевна",
"Phone": "89234513453",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000549",
"FullName": "ИП Ларин Андрей Иванович",
"Email": "Andrey-akadem@mail.ru",
"Phone": "89048909211",
"INN": "246311271439",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000550",
"FullName": "ИП Азанов Максим Юрьевич",
"Email": "msk008@mail.ru",
"Phone": "89048906561",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000551",
"FullName": "Довбаш Валентина Дмитриевна",
"Email": "valya-79@inbox.ru",
"Phone": "89029278229",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000552",
"FullName": "ИП Иванов Дмитрий Владимирович",
"Email": "m1@bic24.ru",
"Phone": "89535908672",
"INN": "246208384598",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000553",
"FullName": "Ольга ФорвардАвто",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000554",
"FullName": "Касрадзе Давид Александрович",
"Email": "2418686@mail.ru",
"Phone": "89029918686",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000555",
"FullName": "ИП Жихарев Василий Юрьевич",
"Email": "vasilij_zh@icloud.com",
"Phone": "89831440458",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000556",
"FullName": "ИП Цуканов Андрей Сергеевич",
"Email": "tsukanov@diversification.ltd",
"Phone": "89232719800",
"INN": "245012262709",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "КРУПНЫЙ ОПТ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000559",
"FullName": "ХОЗКОМПЛЕКТ (кредит)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000560",
"FullName": "ИП Сладкевич Артем Александрович",
"Phone": "89082229459",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000557",
"FullName": "ИП Лоренц Сергей Викторович",
"Phone": "89832069443",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000558",
"FullName": "ХОЗКОМПЛЕКТ Евгений плотник",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000561",
"FullName": "Дресвянников Андрей Александрович",
"Email": "dResv.andRey@gmail.com",
"Phone": "+79631910869",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000562",
"FullName": "ИП Мякинин К.В.",
"Email": "miakinin@rambler.ru",
"Phone": "89135589917",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000563",
"FullName": "ИП Сладкевич Артем Александрович",
"Phone": "89082229459",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000564",
"FullName": "ИП Мироненко Денис Викторович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000565",
"FullName": "ИП Богатов Александр Владимирович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000566",
"FullName": "Хозкомплект Лагвиненко Никита",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000567",
"FullName": "Самохвалова Наталья Николаевна",
"Phone": "89509899119",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000568",
"FullName": "Кротова Алина Федоровна",
"Email": "alina-5757@mail.ru",
"Phone": "89135389142",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000570",
"FullName": "Хозкомплект Ксюша Витрина",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000569",
"FullName": "ООО \"Деловой торгово-промышленный союз \"Сибирь\"",
"Phone": "89214443256",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000571",
"FullName": "ИП Николаев Николай Владимирович",
"Email": "nvniknik@yandex.ru",
"Phone": "+79676110777",
"INN": "031803995636",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000572",
"FullName": "Хозкомплект Луцкин Андрей Олегович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000573",
"FullName": "ИП Паршин Владимир Васильевич",
"Email": "autobest_24@mail.ru",
"Phone": "89535936024",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000598",
"FullName": "шмыголь полина",
"Phone": "+79029732273",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000599",
"FullName": "Понамарчук Виктория",
"Phone": "+79235705057",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000574",
"FullName": "Щаулов Евгений Валентинович",
"Email": "keha13082003@mail.ru",
"Phone": "89135155850",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000600",
"FullName": "Коновалова Мария",
"Phone": "+79131762633",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000601",
"FullName": "Беляева Екатерина",
"Phone": "+79135228083",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000602",
"FullName": "Швечков Даниил",
"Phone": "+79836137975",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000603",
"FullName": "Мишенин Матвей",
"Phone": "89138349697",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000604",
"FullName": "Саранина Кристина",
"Phone": "+79130367186",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000605",
"FullName": "Андреева Софья",
"Phone": "+79011115025",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000606",
"FullName": "Тимошенко Анастасия",
"Phone": "+79135213710",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000607",
"FullName": "Бурашова Евгения",
"Phone": "+79131793266",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000575",
"FullName": "ИП Лесык Мария Владимировна",
"Email": "a.krayushkin@olgr.ru",
"Phone": "",
"INN": "744607975497",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000608",
"FullName": "Смирнова Катя",
"Phone": "+79135641789",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000609",
"FullName": "Карасева Ангелина",
"Phone": "+79232916979",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000610",
"FullName": "Дикий Василий",
"Phone": "+79964282996",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000576",
"FullName": "ИП Брюхов Андрей Владимирович",
"Email": "autostyle24@mail.ru",
"Phone": "89029268182",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000611",
"FullName": "Исаева Нина",
"Phone": "+79131851547",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000577",
"FullName": "ИП Афонасьева Анастасия Андреевна",
"Email": "nastya.sumbulova@mail.ru",
"Phone": "89504299207",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000612",
"FullName": "Степанов Кирилл",
"Phone": "+79509995551",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000613",
"FullName": "Кривич Елизавета",
"Phone": "+79994425980",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000578",
"FullName": "Владимир Ванагас",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000614",
"FullName": "Скорнякова Елизавета",
"Phone": "+79509938167",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000615",
"FullName": "Артамонова Яна",
"Phone": "+79232951989",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000579",
"FullName": "Хозкомплект менеджер Альбина",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000580",
"FullName": "ИП Глухота Елизавета Витальевна",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000616",
"FullName": "Алиева Сабина",
"Phone": "+79832932696",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000581",
"FullName": "ИП Михеева Наталья Сергеевна",
"Phone": "",
"INN": "240400432729",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000617",
"FullName": "Касацкая Алëна",
"Phone": "+79639583163",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000582",
"FullName": "ИП Хлыстова Рита Анатольевна",
"Email": "rita-khlystova@mail.ru",
"Phone": "89233709468",
"INN": "243500222400",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000618",
"FullName": "Гуляева Марианна",
"Phone": "+79080108180",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000619",
"FullName": "ИП Кулаков Е.В.",
"Phone": "",
"INN": "246210316500",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000583",
"FullName": "Анастасия ФорвардАвто сев-енис",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000584",
"FullName": "абв",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000585",
"FullName": "Литвяков Александр Васильевич",
"Email": "adidasoutlet1986@gmail.com",
"Phone": "89535948671",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000586",
"FullName": "ИП Казенная Инна Сергеевна",
"Phone": "89504278989",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000587",
"FullName": "ООО « ГРИН»",
"Email": "filatalex@mail.ru",
"Phone": "89835070000",
"INN": "2453021676",
"KPP": "245301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000588",
"FullName": "ИП Журавель Николай Васильевич",
"Email": "gyravel@inbox.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000589",
"FullName": "Дом Быта (Мира 60)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000590",
"FullName": "ИП Турков Артем Юрьевич",
"Phone": "89504165949",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000591",
"FullName": "ИП Болтрик Дмитрий Александрович",
"Email": "2880873@bk.ru",
"Phone": "89535880874",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000620",
"FullName": "Общество с ограниченной ответственностью \"Орион телеком\"",
"Phone": "",
"INN": "2466220319",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000592",
"FullName": "ИП Полковников В.Е.",
"Email": "RepairLabNorilsk@gmail.com",
"Phone": "89029157333",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000621",
"FullName": "Неудахин Евгений",
"Phone": "89538548681",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000622",
"FullName": "Бузыкин Александр",
"Phone": "89339955950",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000593",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000594",
"FullName": "Контейнер №1 ООО Алегро-Хозком Токарь",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000595",
"FullName": "ИП Попов Евгений Викторович",
"Email": "pev252@yandex.ru",
"Phone": "89080152211",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000596",
"FullName": "ИП Долгих Вадим Алексеевич",
"Phone": "89135960464",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000597",
"FullName": "ИП Воронцов В.Н",
"Email": "voroncov75vah@gmail.com",
"Phone": "89504336856",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000623",
"FullName": "ЗАО \"Универсальный Дом Быта\"",
"Phone": "",
"INN": "2466071547",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000598",
"FullName": "Официальный представитель HQD \"Nicotine\"",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000599",
"FullName": "ИП Медведев Владимир Евгеньевич",
"Email": "vova.m.e@mail.ru",
"Phone": "",
"INN": "246528359720",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000626",
"FullName": "ИП Ушаков Константин Александрович",
"Phone": "",
"INN": "246315234290",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000600",
"FullName": "ИП Берстенев Александр Анатольевич",
"Email": "mobilaiter@gmail.com",
"Phone": "+73843609001",
"INN": "910708455479",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000624",
"FullName": "Белохонова Кристина",
"Phone": "+79954409791",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000625",
"FullName": "Васильева Татьяна",
"Phone": "+79832678553",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000601",
"FullName": "Шамелова Алина Андреевна",
"Phone": "89535886643",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000627",
"FullName": "Раченко Юлия",
"Phone": "+79131806760",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000628",
"FullName": "Коновалова Диана",
"Phone": "+79232805257",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000602",
"FullName": "ИП Сунейкина Светлана Игоревна",
"Phone": "89659099970",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000629",
"FullName": "ХАЛЕЦКАЯ Мария",
"Phone": "+79039882211",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000630",
"FullName": "Гензе Татьяна",
"Phone": "+79135577120",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000631",
"FullName": "Кириллова Екатерина",
"Phone": "+79233356357",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000632",
"FullName": "Семенов Владимир",
"Phone": "+79135746719",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000633",
"FullName": "Шафир Кристина",
"Phone": "+79994478715",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000634",
"FullName": "Шаталова Ирина",
"Phone": "+79233540130",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000635",
"FullName": "Сафина Татьяна",
"Phone": "+79293386055",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000636",
"FullName": "Кооль Кристина",
"Phone": "+79080137778",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000637",
"FullName": "Должецкая Кристина",
"Phone": "+79233649157",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000604",
"FullName": "ИП Попов В.Н.",
"Email": "vnz1970@gmail.ru",
"Phone": "89059762117",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000603",
"FullName": "Гречман Константин Константинович",
"Email": "goluckaya@bk.ru",
"Phone": "89029820688",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000638",
"FullName": "Ковалькова Анастасия",
"Phone": "+79232921911",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000639",
"FullName": "Mos Irina",
"Phone": "+79235775163",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000640",
"FullName": "Норный Максим",
"Phone": "+79832687700",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000641",
"FullName": "Зыкова Светлана",
"Phone": "+79135093677",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000642",
"FullName": "Арканов Дмитрий",
"Phone": "+79235563325",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000605",
"FullName": "Максимова Ольга Викторовна",
"Phone": "89504332500",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000643",
"FullName": "Горошенко Анастасия",
"Phone": "+79232751205",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000644",
"FullName": "Вычужанина Юлия",
"Phone": "+79029193712",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000645",
"FullName": "Шумова Людмила",
"Phone": "+79082078777",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000646",
"FullName": "Маркова Виктория",
"Phone": "+79831678500",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000606",
"FullName": "ИП Пискун Денис Андреевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000647",
"FullName": "Лебедева Анна",
"Phone": "+79131765147",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000648",
"FullName": "Воронова Авелина",
"Phone": "+79080142846",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000607",
"FullName": "ИП Божко Алла Михайловна",
"Email": "bozhkobalahta@ya.ru",
"Phone": "89135551033",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000649",
"FullName": "Vasilevski Alexandr",
"Phone": "+79233522244",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000650",
"FullName": "Пикулева Ирина",
"Phone": "+79535990361",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000651",
"FullName": "Попов Игорь  Сергеевич",
"Phone": "89990849772",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000652",
"FullName": "Даценко Ярослав Вячеславович",
"Phone": "89233030102",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000653",
"FullName": "Козырев Максим",
"Phone": "+79233142101",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000654",
"FullName": "Прокофьев Сергей",
"Phone": "+79219569599",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000655",
"FullName": "ООО \"ВИТЭКА\"",
"Phone": "",
"INN": "5403051423",
"KPP": "540301001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000656",
"FullName": "Каназакова Эльвира",
"Phone": "+79011113013",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000608",
"FullName": "ИП Гуркаев Андрей Анатольевич",
"Email": "8Gurkaev@gmail.com",
"Phone": "89832817191",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000657",
"FullName": "Мазина Алёна",
"Phone": "+79235731338",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000658",
"FullName": "Зайков Иван",
"Phone": "89835004890",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000659",
"FullName": "Силантьева Елена",
"Phone": "+79131941600",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000660",
"FullName": "Шиворда Роман",
"Phone": "+79111242430",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000609",
"FullName": "ИП Миллер Олег Анатольевич",
"Email": "omiller@millerstore.ru",
"Phone": "+79607701020",
"INN": "246513853503",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000661",
"FullName": "Сметанина Екатерина",
"Phone": "+79029904061",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000610",
"FullName": "ИП Ланцова Вера Михайловна",
"Email": "lvm24@mail.ru",
"Phone": "89029420930",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000611",
"FullName": "ИП Алешина Лидия Владимировна",
"Phone": "89831660365",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000612",
"FullName": "ИП Артемьева Светлана Александрова",
"Email": "lana04101991@mail.ru",
"Phone": "89135517610",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000613",
"FullName": "Jomo tech Quality",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000614",
"FullName": "Евгения Крастец",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ИН0000003",
"FullName": "Сафин Юрий",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ИН0000004",
"FullName": "ВЫЧЕТЫ ИЗ ЗП ПРОДАВЦОВ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ИН0000005",
"FullName": "Бобко Анна",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ИН0000006",
"FullName": "БРАК X.O.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ИН0000007",
"FullName": "Грошев Кирилл",
"Phone": "89964599424",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ИН0000008",
"FullName": "Руслан Алиев",
"Phone": "89994426592",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ИН0000009",
"FullName": "Антон Извеков",
"Phone": "89504241650",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ИН0000010",
"FullName": "Цой Алина",
"Phone": "89953120785",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ИН0000011",
"FullName": "гришин",
"Phone": "888888888",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ГВ0000001",
"FullName": "Клементенок Павел",
"Phone": "89832975589",
"OrganizationType": "Физ. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ГВ0000002",
"FullName": "ПОДАРКИ ИЗУМРУДНЫЙ ГОР",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "MV0000001",
"FullName": "Татарников Денис",
"Phone": "89135884694",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "MV0000002",
"FullName": "Щербина Кристина",
"Phone": "89233208789",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "MV0000003",
"FullName": "ПОДАРКИ ПОЛТАВСКИЙ",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000662",
"FullName": "ООО \"Деловые линии\"",
"Phone": "",
"INN": "7826156685",
"KPP": "997650001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000663",
"FullName": "ИП Зырьянов Александр Сергеевич (изумр.город)",
"Phone": "",
"INN": "241101874576",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "аренда Изумрудный город",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000664",
"FullName": "Курьерская доставка",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000665",
"FullName": "ИП Леонов Василий Николаевич",
"Phone": "",
"INN": "321800780458",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000757",
"FullName": "Садко Александр Юрьевич",
"Phone": "+79535910017",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000758",
"FullName": "Литвина Елена Игорьевна",
"Email": "lenfreedom@yandex.ru",
"Phone": "+79232918828",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000759",
"FullName": "Данилова Алена Васильевна",
"Email": "sdanilov_82@mail.ru",
"Phone": "+79029927599",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000760",
"FullName": "Павлова Татьяна Михайловна",
"Phone": "+79831533052",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000761",
"FullName": "Просененков Александр Викторович",
"Phone": "+79082125040",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000762",
"FullName": "Мирхалдам Бахтиер",
"Phone": "+79233461002",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000763",
"FullName": "Климова Мария Игорьевна",
"Email": "masha.klimova-2002@mail.ru",
"Phone": "+79994431976",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000764",
"FullName": "Самохина Ирина",
"Email": "farenkovairina@mail.ru",
"Phone": "+79233561510",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000765",
"FullName": "Андреева Юлия Рафаиловна",
"Phone": "+79538512632",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000766",
"FullName": "Ковалев Илья Владимирович",
"Email": "flashick@mail.ru",
"Phone": "+79293573922",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000767",
"FullName": "Павлова Наталья Викторовна",
"Email": "79039213218@ya.ru",
"Phone": "+79039213218",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000768",
"FullName": "Ковалев Сергей Сергеевич",
"Email": "tmnt@icloud.com",
"Phone": "+79029123430",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000769",
"FullName": "Мурзаев Мирлан Маматжанович",
"Email": "murzaev77@gmail.com",
"Phone": "+79131780939",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000770",
"FullName": "Мацковская Ирина Александровна",
"Email": "ira.matskovskaya.86@mail.ru",
"Phone": "+79233125574",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000771",
"FullName": "Денк Оксана Сергеевна",
"Email": "muha_ksu@bk.ru",
"Phone": "+79029270590",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000772",
"FullName": "Костенок Анастасия Александровна",
"Email": "anastaciakostenok@yandex.ru",
"Phone": "+79641266622",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000773",
"FullName": "Тюхай Елизавета Ивановна",
"Email": "rendals242@mail.ru",
"Phone": "+79233291728",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000774",
"FullName": "Масленко Сергей Сергеевич",
"Phone": "+79676020693",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000811",
"FullName": "Идт Ольга Владимировна",
"Phone": "+79237574888",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000812",
"FullName": "Олег",
"Phone": "+79131711718",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000813",
"FullName": "Березов Евгений Викторович",
"Phone": "+79048951884",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000814",
"FullName": "Шевцова Софья Олеговна",
"Phone": "+79048979981",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000815",
"FullName": "Боймирзаева Хулкар Рустамовна",
"Phone": "+79135390440",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000816",
"FullName": "Кокохов Александр Олегович",
"Phone": "+79830554032",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000817",
"FullName": "Радченко Олеся Юрьевна",
"Phone": "+79029908883",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000818",
"FullName": "Белянина Инна Петровна",
"Phone": "+79232859925",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000819",
"FullName": "Щекалева Наталья Алексеевна",
"Phone": "+79835735597",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000820",
"FullName": "Атаманова Татьяна Юрьевна",
"Phone": "+79135343215",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000821",
"FullName": "Фельдман Евгений Валерьевич",
"Phone": "+79135717070",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000822",
"FullName": "Матусевич Елена Николаевна",
"Phone": "+79832894103",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000823",
"FullName": "Пидасов Александр",
"Phone": "89233565504",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000824",
"FullName": "Матюшкина Татьяна",
"Phone": "+79293380079",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000825",
"FullName": "Лекаторчук Константин Юрьевич",
"Phone": "+79029402837",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000826",
"FullName": "Пелых Александр Николаевич",
"Phone": "+79235995520",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000827",
"FullName": "Филипова Инна",
"Phone": "+79082128468",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000828",
"FullName": "Дайдов Максим Андреевич",
"Phone": "+79827545122",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000829",
"FullName": "Блюм Нонна Анатольевна",
"Phone": "+79233005080",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000830",
"FullName": "Лозенко Андрей Александрович",
"Phone": "+79135006363",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000831",
"FullName": "Федорова Оксана Петровна",
"Phone": "+79832605426",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000832",
"FullName": "Иванов Алексей Владимирович",
"Phone": "+79233184717",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000833",
"FullName": "Хеирхабарова Кристина Викторовна",
"Phone": "+79016235666",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000834",
"FullName": "Агеева Кристина Александровна",
"Phone": "+79232941196",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000835",
"FullName": "Эллн Валерия Витальевна",
"Phone": "+79237826090",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000836",
"FullName": "ИНДИВИДУАЛЬНЫЙ ПРЕДПРИНИМАТЕЛЬ ГАСАНОВ ЭЛЧИН БАЛДАДАШ ОГЛЫ",
"Phone": "",
"INN": "245728073847",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000837",
"FullName": "ИП Гергердт Григорий Владимирович",
"Email": "enclaves777@mail.ru",
"Phone": "89082087203",
"INN": "245306455407",
"KPP": "245301001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000838",
"FullName": "Самойлик Павел",
"Phone": "893320010000",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000839",
"FullName": "Индивидуальный предприниматель Куприянов Павел Васильевич",
"Phone": "",
"INN": "243700554385",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000840",
"FullName": "Валерия Александровна",
"Phone": "+79994410806",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000841",
"FullName": "Рассказова Дарья Викторовна",
"Email": "darusha_5@mail.ru",
"Phone": "+79233713832",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000842",
"FullName": "Сафина Алена Александровна",
"Email": "safina@usf.ru",
"Phone": "+79080249933",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000843",
"FullName": "Войцехович Ирина Кудратовна",
"Email": "942075_kair@mail.ru",
"Phone": "+79631913100",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000844",
"FullName": "Хамзина Карина Гумеровна",
"Email": "karinika566@mail.ru",
"Phone": "+79832663508",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000845",
"FullName": "Михайлов Семен Вячеславович",
"Phone": "+79131950913",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000846",
"FullName": "Бояхчян Аревик Меружановна",
"Email": "Boyakchyan94@mail.ru",
"Phone": "+79232879998",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000748",
"FullName": "ХОЗКОМПЛЕКТ Виноградская Татьяна Викторовна",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000752",
"FullName": "пустая",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000753",
"FullName": "ИП Леонтьева Юлия Ивановна",
"Email": "delonkr@bk.ru",
"Phone": "89082069715",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000754",
"FullName": "ИП Миняева Анастасия Николаевна",
"Phone": "",
"INN": "632134220254",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "КРУПНЫЙ ОПТ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000756",
"FullName": "ООО \"Электрика\"",
"Phone": "",
"INN": "5403058362",
"KPP": "540301001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000755",
"FullName": "ИП Ермолович Лариса Тимофеевна",
"Email": "ermolovich031@gmail.com",
"Phone": "89029596162",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000761",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000762",
"FullName": "Партия DI-0008 и DI-0007 от 01.03.2023",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000757",
"FullName": "ООО \"МираМед\"",
"Phone": "",
"INN": "2465333567",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000758",
"FullName": "ИП Пендер Богдана Андреевна",
"Phone": "89497031408",
"INN": "614013900834",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "000000004",
"FullName": "ИП Ермашенко Павел Андреевич",
"Email": "emptyapostol@mail.ru",
"Phone": "89138396908",
"INN": "246504718258",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "000000005",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "000000006",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "000000007",
"FullName": "TREQA",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "000000008",
"FullName": "HOCO поставщик Китай",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "000000009",
"FullName": "Кузьмин Владимир Иванович (не для реализации)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "000000010",
"FullName": "Рыбкин Иван Анатольевич",
"Email": "diforce1@mail.ru",
"Phone": "89676083888",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "000000011",
"FullName": "Торговое оборудавание для ДиФорс",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "000000012",
"FullName": "ООО ПКФ \"Хозкомплект\"",
"Phone": "",
"INN": "2466172200",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "000000013",
"FullName": "ИП Ермашенко Алексей",
"Email": "pred_ros@mail.ru",
"Phone": "89135626666",
"INN": "246504718184",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ИН0000002",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "ЦБ0000685",
"FullName": "Коробкин Георгий Иософович",
"Phone": "89835025743",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000686",
"FullName": "Фронкин Богдан Игоревич",
"Phone": "89994409420",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000687",
"FullName": "Иванов Иван Иванович",
"Phone": "+799999999",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000688",
"FullName": "Новиков Артем",
"Phone": "89233666668",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000689",
"FullName": "Пупкин Вася Васьевич",
"Phone": "+79139139999",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000690",
"FullName": "(ЗП) МОИСЕЕВА СВЕТЛАНА АНАТОЛЬЕВНА",
"Phone": "",
"INN": "246214829358",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000691",
"FullName": "(ЗП) ИВАНОВ ЕВГЕНИЙ АЛЕКСАНДРОВИЧ",
"Phone": "",
"INN": "245304253765",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000692",
"FullName": "(ЗП) Уточкин Дмитрий Викторович",
"Phone": "",
"INN": "246414837684",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000693",
"FullName": "(ЗП) СПИРИДЕНКО СЕРГЕЙ АЛЕКСАНДРОВИЧ",
"Phone": "",
"INN": "381506145259",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000694",
"FullName": "Михайлов Валерий Алексеевич",
"Email": "9238707@gmail.com",
"Phone": "+79039238707",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000695",
"FullName": "Митракова Яна Александровна",
"Email": "yana.mit@me.com",
"Phone": "+79232711327",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000696",
"FullName": "Южаков Руслан Валерьевич",
"Email": "ruslanyuzhakov99@gmail.com",
"Phone": "+79631809361",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000697",
"FullName": "Усова Алена Николаевна",
"Email": "stsv24@bk.ru",
"Phone": "+79082128563",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000698",
"FullName": "Финашкина Анастасия Николаевна",
"Email": "malyga-n@ya.ru",
"Phone": "+79131971116",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000699",
"FullName": "Болбат Светлана Александровна",
"Email": "bosonozkina@mail.ru",
"Phone": "+79832833803",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000700",
"FullName": "Дольников Александр Михайлович",
"Email": "natashalatesheva12@icloud.com",
"Phone": "+79504096600",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000701",
"FullName": "Хендогин Максим Валерьевич",
"Email": "maksimhendogin961@gmail.com",
"Phone": "+79232869645",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000702",
"FullName": "Левый Кирилл Витальевич",
"Email": "liyvo@mail.ru",
"Phone": "+79069521111",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000703",
"FullName": "Лалетина Екатерина Александровна",
"Email": "laletinmatvei@yandex.ru",
"Phone": "+79509900022",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000704",
"FullName": "Амосова Елена Сергеевна",
"Phone": "+79138336643",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000705",
"FullName": "Климова Мария Юрьевна",
"Email": "polyubina@yandex.ru",
"Phone": "+79235312040",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000706",
"FullName": "Субботина Наталья Владимировна",
"Email": "angel55582@mail.ru",
"Phone": "+79131734482",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000707",
"FullName": "Черняков Роман Николаевич",
"Phone": "+79082212711",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000708",
"FullName": "Казимова Айша Валех кызы",
"Email": "kazimov.valekh@bk.ru",
"Phone": "+79607659309",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000709",
"FullName": "Костикова Ирина Васильевна",
"Email": "irenn84@mail.ru",
"Phone": "+79676122406",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000710",
"FullName": "Неверова Виктория Олеговна",
"Email": "vika.neverova14@mail.ru",
"Phone": "+79628122540",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000711",
"FullName": "Пилипчук Александр Николаевич",
"Email": "a.pilipchuk@mail.ru",
"Phone": "+79535824723",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000712",
"FullName": "Натюшкина Александра Сергеевна",
"Email": "matuyshkina.89@bk.ru",
"Phone": "+79293556787",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000713",
"FullName": "Титова Мария Андреевна",
"Email": "mashay2@mail.ru",
"Phone": "+79232924462",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000714",
"FullName": "Васекина Виктория Игоревна",
"Phone": "+79131724207",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000715",
"FullName": "Агаркова Светлана Алексеевна",
"Email": "svagarkova@mail.ru",
"Phone": "+79050884644",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000716",
"FullName": "Сизина Валерия Евгеньевна",
"Email": "lera.sizina@bk.ru",
"Phone": "+79029282600",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000717",
"FullName": "Арапова Виктория Николаевна",
"Email": "svv1868@gmail.com",
"Phone": "+79236696499",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000718",
"FullName": "Максимов Василий Валерьевич",
"Phone": "+79082111014",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000719",
"FullName": "Кузнецова Елена Александровна",
"Email": "kuznecova.96@mail.com",
"Phone": "+79082232346",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000720",
"FullName": "Жегалина Ирина Олеговна",
"Email": "qashqai-24@mail.ru",
"Phone": "+79029242399",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000775",
"FullName": "Дрозд Сергей Павлович",
"Phone": "+79535820879",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000776",
"FullName": "Понкратова Елизавета Александровна",
"Email": "elizaveta.ski@yandex.ru",
"Phone": "+79831627959",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000777",
"FullName": "Сизова Анастасия Вадимовна",
"Email": "polakanastasia48@gmail.com",
"Phone": "+79233577064",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000778",
"FullName": "Бурков Андрей Иванович",
"Email": "Buran77@ya.ru",
"Phone": "+79994407705",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000779",
"FullName": "Уткина Людмила Петровна",
"Email": "utkinaludmila50@gmail.com",
"Phone": "+79620765145",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000780",
"FullName": "Иванова-Карабутина Дарья Владимировна",
"Email": "karaby@inbox.ru",
"Phone": "+79029473177",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000781",
"FullName": "Фролов Константин Сергеевич",
"Email": "fst161415@gmail.com",
"Phone": "+79130499478",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000782",
"FullName": "Паврова Альбина Владиславовна",
"Email": "defff.soulll1999@gmail.com",
"Phone": "+79836108906",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000783",
"FullName": "Васин Александр Юрьевич",
"Email": "sasha02vasin@gmail.com",
"Phone": "+79642760344",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000784",
"FullName": "Трусова Екатерина Валерьевна",
"Email": "hamster1297@mail.ru",
"Phone": "+79504369505",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000785",
"FullName": "Носков Илья Сергеевич",
"Email": "pitbull-1452@mail.ru",
"Phone": "+79965220960",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000786",
"FullName": "Сабо Ирина Владимировна",
"Email": "marusy_911@mail.ru",
"Phone": "+79504283588",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000787",
"FullName": "Деккер Екатерина Юрьевна",
"Email": "dekker0505@gmail.com",
"Phone": "+79131747556",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000788",
"FullName": "Гольских Андрей Павлович",
"Email": "galskikh@bk.ru",
"Phone": "+79509735260",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000789",
"FullName": "Натчук Андрей Дмитриевич",
"Email": "natchuk24@mail.ru",
"Phone": "+79994401488",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000790",
"FullName": "Карнаухов Павел Михайлович",
"Email": "paveL.25.03@mail.ru",
"Phone": "+79131816365",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000791",
"FullName": "Трухина Ольга Юрьевна",
"Email": "olya.trukhina@bk.ru",
"Phone": "+79835029296",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000792",
"FullName": "Бирюков Алексей Валентинович",
"Email": "al.biriukov2018@gmail.com",
"Phone": "+79293326446",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000702",
"FullName": "ИП Ясковец Иванна Васильевна",
"Email": "ioanna3991@gmail.com",
"Phone": "+79013833725",
"INN": "860805457463",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000703",
"FullName": "Поняев Сергей Константинович",
"Email": "sergeyka333@yandex.ru",
"Phone": "+79202579303",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000705",
"FullName": "Кочанов Николай Николаевич",
"Phone": "89082121606",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000706",
"FullName": "Приходько Даниил",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000708",
"FullName": "ИП МАМЕДОВ ЭЛЬВИН АРЗУ ОГЛЫ",
"Phone": "",
"INN": "245731297100",
"KPP": "245701001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000707",
"FullName": "ООО \"Ирада\"",
"Phone": "89676112777",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000709",
"FullName": "Биснек Дмитрий Алексеевич",
"Phone": "89526148777",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000712",
"FullName": "(1) Расходы магазин hoco ИЮНЬ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000713",
"FullName": "(2) Расходы магазин hoco RED SAIL",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000714",
"FullName": "(3) Расходы магазин hoco ПОЛТАВСКИЙ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000715",
"FullName": "(4) Расходы магазин hoco ДОМ БЫТА",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000716",
"FullName": "(0) Расходы магазин ДИФОРС",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000710",
"FullName": "Горбунов Никита Евгеньевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000711",
"FullName": "ИП Терещенко Лариса Анатольевна",
"Email": "uyt77@mail.ru",
"Phone": "89509994415",
"INN": "246606342822",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000719",
"FullName": "Прокопенко Илья",
"Phone": "89531546394",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000717",
"FullName": "ИП Иванова Александра Ильинична",
"Email": "zveropolice24@yandex.ru",
"Phone": "89135235303",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000718",
"FullName": "ИП Гулуев Аяз Гусейн Оглы",
"Phone": "89086495202",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000720",
"FullName": "ИП Бугаева Ирина Алексеевна",
"Email": "Safon_s@mail.ru",
"Phone": "",
"INN": "246521415260",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "КРУПНЫЙ ОПТ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000721",
"FullName": "Общество с ограниченной ответственностью «Гурман»",
"Email": "gyrman24@mail.ru",
"Phone": "89048920933",
"INN": "2407062861",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000692",
"FullName": "Perfeo",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000694",
"FullName": "MI KRSK ксиоми Сергей",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000693",
"FullName": "Акабаева Мадина",
"Phone": "89135216035",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000695",
"FullName": "ИП Розовел Дмитрий Георгиевич",
"Email": "dgrozovel@mail.ru",
"Phone": "+79998112516",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000698",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000696",
"FullName": "ИП Поздняк Виктор Викторович",
"Email": "zakup2@hozmag24.su",
"Phone": "",
"INN": "246602077700",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000697",
"FullName": "ООО ЮСТ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000699",
"FullName": "ИП Горобец Иван Петрович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000704",
"FullName": "Заказы AliExpress",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000700",
"FullName": "ИП Марьясова Л.С.",
"Email": "vhd1980@mail.ru",
"Phone": "89135347697",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000701",
"FullName": "ООО \"СК АКРОНИМ\"",
"Phone": "+79631912472",
"INN": "2465169028",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000793",
"FullName": "Зельберг Евгения Валентиновна",
"Email": "Karpevgen81@gmail.com",
"Phone": "+79082017637",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000794",
"FullName": "Медведева Екатерина",
"Email": "med.ek@yandex.ru",
"Phone": "+79233555411",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000795",
"FullName": "Стешанова Кристина Викторовна",
"Email": "kvzasemkova@yandex.ru",
"Phone": "+79232712481",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000796",
"FullName": "Налькин Иван Николаевич",
"Phone": "+79135887351",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000797",
"FullName": "Хорошкина Мария Владимировна",
"Phone": "+79833646457",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000798",
"FullName": "Кошемякин Иван Васильевич",
"Phone": "+79082222121",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000799",
"FullName": "Шуманов Алексей олегович",
"Phone": "+79504287821",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000800",
"FullName": "Кутиенко Алина",
"Phone": "+79504014800",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000801",
"FullName": "Назаров Дмитрий Владимирович",
"Phone": "+79835747847",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000802",
"FullName": "Шкикунова Алевтинав Александровна",
"Email": "33flaia@maij.ru",
"Phone": "+79095230792",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000803",
"FullName": "Гайдоров Фамил А Оглы",
"Phone": "+79535857778",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000804",
"FullName": "Энгель Евгения Леонидовна",
"Phone": "+79029742571",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000805",
"FullName": "Дингес Кристина Олеговна",
"Phone": "+79232860077",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000806",
"FullName": "Фисенко Вероника Робертиновна",
"Phone": "+79509791940",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000807",
"FullName": "Шепотило Иван Романович",
"Phone": "+79832898407",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000808",
"FullName": "Балобанова Анастасия Павловна",
"Phone": "+79509997379",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000809",
"FullName": "Кремзуков Роман Сергеевич",
"Phone": "+79237599955",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000810",
"FullName": "Ирт Анастасия",
"Phone": "+79011116557",
"OrganizationType": "Физ. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000722",
"FullName": "ИП Ноак Сергей Иванович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000723",
"FullName": "ИП Сабельфельд Вячеслав Владимирович",
"Phone": "89994419081",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000724",
"FullName": "ИП Бережная Анна Сергеевна",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000725",
"FullName": "ИП Еремкина Елена Михайловна",
"Email": "elenaem2018@yandex.ru",
"Phone": "",
"INN": "241800028304",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000726",
"FullName": "ИП Потехин Александр Васильевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000727",
"FullName": "Wildberries",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000728",
"FullName": "ИП Мочалов Евгений Олегович",
"Phone": "",
"INN": "246517393529",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000730",
"FullName": "AntiStore заказ товара",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000729",
"FullName": "ООО Целлер",
"Phone": "89676153888",
"INN": "2464130821",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000731",
"FullName": "ООО Норматив-Инфо",
"Phone": "89607677777",
"INN": "2465276990",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000847",
"FullName": "Сазанович Анна Викторовна",
"Email": "alyonasazanovich@gmail.com",
"Phone": "+79293354307",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000848",
"FullName": "Лобанов Алексей Александрович",
"Email": "lobanadis@ay.ru",
"Phone": "+79504344242",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000849",
"FullName": "Барбуца Мария Борисовна",
"Email": "marichusik_88@mail.ru",
"Phone": "+79135986409",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000850",
"FullName": "Кушнарев Станислав Владимирович",
"Email": "clkstas@ya.ru",
"Phone": "+79080126161",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000851",
"FullName": "Савинов Глеб Викторович",
"Email": "Gleba-s@mail.ru",
"Phone": "+79233212666",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000852",
"FullName": "Симпликевич Денис Владимирович",
"Email": "simplik-91@mail.ru",
"Phone": "+79233696501",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000853",
"FullName": "Маликова Мария Георгиевна",
"Phone": "+79135343482",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000854",
"FullName": "Корякин Данил Арьемович",
"Email": "danil89659003@mail.ru",
"Phone": "+79607668324",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000855",
"FullName": "Даутханов Никита Ренатович",
"Email": "nikitadautkhanov@icloud.com",
"Phone": "+79333343105",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000856",
"FullName": "Терентьева Наталья",
"Phone": "+79135336769",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000857",
"FullName": "КоролеваМаксим Васильевич",
"Phone": "+79676123538",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000858",
"FullName": "Лукянчук Денис Валерьевич",
"Email": "denis.azot8888@gmail.com",
"Phone": "+79509859094",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000859",
"FullName": "Корниенко Анжелика Владимировна",
"Email": "0169899@bk.ru",
"Phone": "+79080169899",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000860",
"FullName": "Жигальцова Светлана Владимировна",
"Phone": "+79082160759",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000861",
"FullName": "Шалаева Светлана Игоревна",
"Phone": "+79131843491",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000862",
"FullName": "Гравдан Ксения Александровна",
"Phone": "+79029414248",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000863",
"FullName": "Исаева Татьяна Викторовна",
"Email": "tvisa326@gmail.com",
"Phone": "+79135837960",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000864",
"FullName": "Нечай Павел Владимирович",
"Email": "magazincomfort@mail.ru",
"Phone": "+79233553404",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000865",
"FullName": "Рзазага Саид Ислам Оглы",
"Phone": "+79994470691",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000866",
"FullName": "Опарян Вячеслав Александрович",
"Phone": "+79538536668",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000867",
"FullName": "Черныш Светлана Анатольевна",
"Email": "tolic1989@list.ru",
"Phone": "+79131991635",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000868",
"FullName": "Оганджанян Шаво",
"Phone": "+79135287766",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000869",
"FullName": "Артамонова Анна Леонидовна",
"Email": "molovit@inbox.ru",
"Phone": "+79233095282",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000870",
"FullName": "ООО \"КРАСГОРСВЯЗЬ\"",
"Email": "odecolon@gmail.com",
"Phone": "",
"INN": "2460117989",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000871",
"FullName": "ООО \"Академия Семьи\"",
"Phone": "",
"INN": "2466160934",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000872",
"FullName": "Индивидуальный предприниматель Колегова Екатерина Валерьевна",
"Phone": "",
"INN": "246512177806",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000873",
"FullName": "ИП ТКАЧЕВ СТАНИСЛАВ ВАЛЕРЬЕВИЧ",
"Phone": "",
"INN": "241502533460",
"KPP": "241501001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000874",
"FullName": "УФК по Красноярскому краю (ОСФР по Красноярскому краю, л/сч 04194Ф19010)",
"Phone": "",
"INN": "2466001885",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000875",
"FullName": "УФК по Тульской области (Межрегиональная инспекция Федеральной налоговой службы по управлению долгом",
"Phone": "",
"INN": "7727406020",
"KPP": "770801001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000876",
"FullName": "(ЗП) ОПАРИНА КАРИНА СЕРГЕЕВНА",
"Phone": "",
"INN": "7707083893",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000877",
"FullName": "Наумов Сергей Игоревич",
"Phone": "89676156704",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000878",
"FullName": "Общество с ограниченной ответственностью \"Академи Принт\"",
"Phone": "",
"INN": "2460238856",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000879",
"FullName": "УФК по Красноярскому краю",
"Phone": "",
"INN": "2466124510",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000880",
"FullName": "(ЗП) КОРШУНОВА НАТАЛЬЯ СЕРГЕЕВНА",
"Phone": "",
"INN": "7707083893",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000881",
"FullName": "ООО \"Игра-сервис\"",
"Phone": "",
"INN": "2466092240",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000563",
"FullName": "Астафьева Татьяна",
"Phone": "+79029917743",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000516",
"FullName": "ИП Синкин Николай Александрович",
"Phone": "89083271188",
"INN": "246308297814",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000564",
"FullName": "Барковская Полина",
"Phone": "+79029160128",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000565",
"FullName": "Егорова Настя",
"Phone": "+79831269847",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000566",
"FullName": "Михайлова Аля",
"Phone": "+79135236491",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000517",
"FullName": "ООО «ОПТИМА»",
"Email": "optima.kras@mail.ru",
"Phone": "",
"INN": "2462032360",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000567",
"FullName": "Екатерина Маркова",
"Phone": "+79538505505",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "RS0000012",
"FullName": "ИП Ковригина Анна Рамильевна",
"Phone": "89233540581",
"INN": "246213678120",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000568",
"FullName": "ООО Санаторий \"Родник Алтая\"",
"Phone": "",
"INN": "2203010657",
"KPP": "220301001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000569",
"FullName": "Стрижевский Давид Борисович",
"Phone": "89082043311",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000732",
"FullName": "ИП Юновидов Андрей",
"Email": "andrey.yu75@mail.ru",
"Phone": "89029420931",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000733",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000734",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000735",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000736",
"FullName": "Глаас Антон Александрович",
"Phone": "89130382682",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000742",
"FullName": "ИП Васильева Светлана Александровна",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000743",
"FullName": "ИП Кононов Никколай Алексеевич",
"Phone": "",
"INN": "880200063025",
"KPP": "880201001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000737",
"FullName": "ХОЗКОМПЛЕКТ Черных Илья",
"Phone": "89535921922",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000738",
"FullName": "Савченко Александр Александрович",
"Phone": "89082185519",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000740",
"FullName": "ООО IPROMARKET24",
"Phone": "89080254333",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000739",
"FullName": "Смирнов Евгений Васильевич",
"Phone": "89535884450",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000741",
"FullName": "ИП Васильева Светлана Александровна",
"Phone": "",
"INN": "541019954570",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000744",
"FullName": "Аксессуары ориг/копии peipei zpx112300",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000745",
"FullName": "ООО \"ПЭК\"",
"Phone": "",
"INN": "7721823853",
"KPP": "77505001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000746",
"FullName": "Симонов Сергей Николаевич",
"Phone": "89831450272",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000747",
"FullName": "ИП Кублицкий Игорь Сергеевич",
"Phone": "+79130441941",
"INN": "245209686303",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000749",
"FullName": "Контейнер DI-0008",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000750",
"FullName": "ООО \"Мегабит\" Б/Н",
"Phone": "",
"INN": "5406714397",
"KPP": "540601001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000751",
"FullName": "Терентьев Николай Андреевич (поставщик усл)",
"Phone": "",
"INN": "246314598150",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000625",
"FullName": "ИП Гурьянов Андрей Александрович (FanBike)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000626",
"FullName": "ИП Боякова Светлана Сергеевна",
"Phone": "89535801919",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000627",
"FullName": "ИП Дианова Наталья Владимировна",
"Email": "tanya.titorenko00@mail.ru",
"Phone": "89029403530",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000628",
"FullName": "ИП Денисов Юрий Алексеевич",
"Phone": "89233040582",
"INN": "241104548250",
"KPP": "241101001",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000629",
"FullName": "ИП Деркач Дмитрий Олегович",
"Phone": "89029207750",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000630",
"FullName": "ООО «Скайфлай»",
"Email": "Myskyfly2014@gmail.com",
"Phone": "89232955155",
"INN": "2465275570",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000631",
"FullName": "Юрий Строитель",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000632",
"FullName": "Главное управление молодежной политики и туризма администрации города Красноярска",
"Phone": "",
"INN": "2466042634",
"KPP": "246601001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000633",
"FullName": "ИП Рябинкин Роман Владимирович",
"Email": "green999999@mail.ru",
"Phone": "89135627019",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000634",
"FullName": "FixMe",
"Phone": "89143108512",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000637",
"FullName": "Бакулина Анастасия",
"Phone": "89607730336",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000635",
"FullName": "Дывдык Жанна Олеговна",
"Phone": "",
"INN": "7707083893",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000636",
"FullName": "Общество с ограниченной ответственностью «М Плюс»",
"Email": "vor.tatyana@list.ru",
"Phone": "89224832797",
"INN": "7204195569",
"KPP": "720301001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000638",
"FullName": "ИП Шухрат Шарафи",
"Email": "sharaf.shukhrat@bk.ru",
"Phone": "+79631860909",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000639",
"FullName": "Ашрафов Руслан Азизага Оглы",
"Email": "89059751994@mai.ru",
"Phone": "89059751994",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000640",
"FullName": "ИП Полынцев Николай Анатольевич",
"Email": "polintsev_2017@mail.ru",
"Phone": "89233022543",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000641",
"FullName": "ИП Эфендиев Ягуб Гасан Оглы",
"Email": "efendievagub@gmail.com",
"Phone": "89631912899",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000642",
"FullName": "ИП Гончаров Анатолий Сергеевич",
"Email": "grandavvto1971@mail.ru",
"Phone": "89233440141",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000643",
"FullName": "Ирина Курчатова Хозкомплект",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000644",
"FullName": "ООО Технология звука",
"Phone": "+73912149964",
"INN": "2465275731",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000645",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000646",
"FullName": "hoco",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000647",
"FullName": "borofone",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000648",
"FullName": "no name",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000649",
"FullName": "Earldom",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000650",
"FullName": "ИП Путилин Андрей Алексеевич",
"Phone": "89131766872",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000651",
"FullName": "ИП Титов Максим Андреевич",
"Email": "maxim.andreevich98@mail.ru",
"Phone": "89041564388",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000652",
"FullName": "Общество с ограниченной ответственностью Производственно-строительная фирма «Краевая Строительная Компания»",
"Phone": "",
"INN": "2460241866",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000653",
"FullName": "Альбина Хозкомплект витрина",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000654",
"FullName": "Миронов Евгений",
"Phone": "89235703003",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000655",
"FullName": "Мурсахматов Бакыт (хоко Абакан)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000656",
"FullName": "ООО \"Интернет магазин Либерти\"",
"Phone": "84959880734",
"INN": "7715457077",
"KPP": "771701001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000657",
"FullName": "LOVE IS",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000658",
"FullName": "CONTEX",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000659",
"FullName": "ИП Полуэктов Роман Васильевич",
"Phone": "89131857321",
"INN": "246012129949",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС закуп поставщ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000660",
"FullName": "ИП Карасев Олег Михайлович",
"Email": "kmo10@inbox.ru",
"Phone": "",
"INN": "190300151667",
"KPP": "190101001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000661",
"FullName": "ИП Заболотникова Наталья Семеновна",
"Email": "lady.kutkina@gmail.com",
"Phone": "",
"INN": "246408275042",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000662",
"FullName": "Общество с ограниченной ответственностью \"Проф-ИТ\"",
"Email": "rimv@omegafuture.ru",
"Phone": "",
"INN": "7801553786",
"KPP": "781001001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000615",
"FullName": "Вастистов Дмитрий (дифорс)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000621",
"FullName": "ИП Мунтаева Гульнар Набатовна",
"Phone": "Телефонфакс\u00093919334391,89135261239",
"INN": "560505058420",
"KPP": "560501001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000616",
"FullName": "ХОЗКОМПЛЕКТ Белоусов Владимир Олегович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000617",
"FullName": "ИП Арутюнян Вреж",
"Phone": "89233339420",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000618",
"FullName": "ИП Ситкевич Ю.Л.",
"Email": "tiro-market@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000620",
"FullName": "ИП Дындарь Александр Викторович",
"Email": "Fedotorsay@mail.ru",
"Phone": "89021781567",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000619",
"FullName": "ИП Оюн Алдынай Владимировна",
"Email": "oyunalbyai80@mail.ru",
"Phone": "89232642156",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000622",
"FullName": "ООО СибЮнион",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000623",
"FullName": "ИП Сергеев Иван Николаевич",
"Phone": "89994404100",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000624",
"FullName": "ООО \"ДОТСТОРЕ\"",
"Email": "odecolon@gmail.com",
"Phone": "",
"INN": "2460239296",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000666",
"FullName": "ООО ФСК \"ЯНСН-КАПИТАЛ\"",
"Phone": "",
"INN": "2464016773",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000667",
"FullName": "ИП Андреев Василий Григорьевич",
"Phone": "",
"INN": "246522807912",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000668",
"FullName": "Тютрин Данил",
"Phone": "89177399749",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000669",
"FullName": "Индивидуальный предприниматель Иванов Алексей Владимирович",
"Phone": "",
"INN": "781699714453",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000670",
"FullName": "ООО \"КрасПромСтрой\"",
"Phone": "",
"INN": "2464236955",
"KPP": "502701001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000671",
"FullName": "Гордеева Юлия Николаевна",
"Phone": "89059767749",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000672",
"FullName": "ПОДАРКИ В ТЦ ДОМ БЫТА",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000673",
"FullName": "ООО «Спутниковая связь»",
"Phone": "",
"INN": "5404091235",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000674",
"FullName": "Терентьев Николай Андреевич (поставщик)",
"Phone": "",
"INN": "246314598150",
"KPP": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000359",
"FullName": "ООО \"ЛМ Компани\" Новосибирск Ибрагим",
"Phone": "89831273205",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000366",
"FullName": "ТЦ Полтавский (полтавская 38/22)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Себестоимость",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000361",
"FullName": "Аксессуары ПРЕСТИЖ Москва",
"Phone": "89690674747",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000363",
"FullName": "ИП Мельников Сергей Николаевич",
"Email": "disk.msn@mail.ru",
"Phone": "89130303026",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000035",
"FullName": "ООО НКО \"Яндекс.Деньги\"",
"Phone": "",
"INN": "7750005725",
"KPP": "770501001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000036",
"FullName": "ПAO СК Росгосстрах",
"Phone": "",
"INN": "7707067683",
"KPP": "997950001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000364",
"FullName": "ИП Бакулин Никита Павлович",
"Phone": "89131970775",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000365",
"FullName": "ИП Кролевецкий Николай",
"Email": "x-servis@mail.ru",
"Phone": "+79831675244",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000367",
"FullName": "ИП Гольм Ирина Анатольевна",
"Email": "gda_78.78@mail.ru",
"Phone": "89135391820",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000368",
"FullName": "ИП Мирзоалиев Алишер Меликбоевич",
"Phone": "89835093903",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000315",
"FullName": "ИП Неймашева Елена Михайловна",
"Email": "elena25biznes@mail.ru",
"Phone": "89832009057",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000318",
"FullName": "ИП Тимошенко Евгений Алексеевич",
"Phone": "89080107145",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000317",
"FullName": "ООО \"Мегабит\" (нал)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000319",
"FullName": "ИП Чивчян ВладимирТумасович",
"Email": "olga.dmitrieva@forvardavto.ru",
"Phone": "",
"INN": "246001172580",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000320",
"FullName": "ИП Астафьев Максим Владимирович",
"Email": "max999.07@mail.ru",
"Phone": "89082157625",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000321",
"FullName": "ООО \"Ко-ТОРГ (торговое оборудование)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000322",
"FullName": "ООО \"БониВент\"",
"Email": "marika_fruit@mail.ru",
"Phone": "89233005183",
"INN": "2463256797",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "RS0000009",
"FullName": "Индивидуальный  Предприниматель Мансурова Наталья Макаровна",
"Email": "mn2405145@mail.ru",
"Phone": "",
"INN": "246300475832",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000323",
"FullName": "ИП Левченко Наталья Сергеевна",
"Phone": "89029578704",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "RS0000010",
"FullName": "Елена Стекло 12 Pro Max матовое",
"Phone": "89836160717",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "RS0000011",
"FullName": "Анастасия чехол-книжка Samsung A50",
"Phone": "89080207673",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "000000001",
"FullName": "ИП Скроботова Е.В.",
"Email": "9835055355@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "000000001",
"FullName": "ИП Скроботова Е.В.",
"Email": "9082119303@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "000000002",
"FullName": "ООО \"ЗАВХОЗ\"",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "000000003",
"FullName": "ООО ТЕХНОМАГ",
"Email": "optomag@yandex.ru",
"Phone": "89029918970",
"OrganizationType": "Юр. лицо",
"ContractType": "КРУПНЫЙ ОПТ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000663",
"FullName": "ИП Богдан Дмитрий",
"Email": "2942216@gmail.com",
"Phone": "89504113852",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000664",
"FullName": "Быкова Виктория Георгиевна",
"Email": "gein_08@mail.ru",
"Phone": "89135290777",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000665",
"FullName": "ИП Темникова Марина Романовна",
"Email": "marina.temnikovh.2016@mail.ru",
"Phone": "89029216062",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000666",
"FullName": "ИП Епишкина Мария Михайловна",
"Email": "logist@4ip.info",
"Phone": "+79246032451",
"INN": "382708794508",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000667",
"FullName": "Даша Витрина ХК",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000668",
"FullName": "ИП Локтионов Вадим Юрьевич",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000669",
"FullName": "Чехлы Москва incase",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000670",
"FullName": "ХОЗКОМПЛЕКТ Швайдюк Лира",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000671",
"FullName": "Сендецкий Вадим Александрович",
"Email": "vabimir04.@yandex.ru",
"Phone": "89082020111",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000672",
"FullName": "Сергиенко Александр Сергеевич",
"Phone": "89029276725",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000882",
"FullName": "",
"Phone": "2536",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000883",
"FullName": "",
"Phone": "+79235762536",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000884",
"FullName": "",
"Email": "krasdevice24@gmail.com",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000885",
"FullName": "",
"Email": "i.vareldzhyan@olgr.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000886",
"FullName": "",
"Email": "e.ganzha@olgr.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000887",
"FullName": "",
"Email": "burnout2022@mail.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000888",
"FullName": "",
"Email": "9082146991@mail.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000889",
"FullName": "",
"Email": "m.bezrodnova@olgr.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000890",
"FullName": "",
"Email": "9135591923@mail.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000891",
"FullName": "Наталья",
"Email": "79059765494@mail.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000892",
"FullName": "",
"Email": "2infotab@gmail.com",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000893",
"FullName": "",
"Email": "dulism@yandex.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000894",
"FullName": "",
"Email": "s-en74@mail.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000895",
"FullName": "Евгений",
"Email": "good_doctor@mail.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000896",
"FullName": "",
"Email": "diforce18@inbox.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000897",
"FullName": "",
"Email": "ssov2424@yandex.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000898",
"FullName": "",
"Email": "2500877marketing@inbox.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000899",
"FullName": "",
"Email": "an.wileyfox1212@gmail.com",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000900",
"FullName": "",
"Email": "tsopt@yandex.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000901",
"FullName": "",
"Email": "haystv123@gmail.com",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000075",
"FullName": "ПРОЦЕНТЫ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000076",
"FullName": "ИП Белошапкин А. В.",
"Email": "2145153@mail.ru",
"Phone": "89535853529",
"INN": "2465133215",
"KPP": "246501001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000077",
"FullName": "Низамов А.П.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000079",
"FullName": "БОНУСЫ К ЗП РАБОТНИКАМ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000078",
"FullName": "ИП Черных Юрий Игоревич",
"Email": "svetolyuks24@mail.ru",
"Phone": "9233030530",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000080",
"FullName": "ИП Толомеева С.Г.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000081",
"FullName": "ИП Брылева Ж.В.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000082",
"FullName": "ХОЗКОМПЛЕКТ Адамович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000083",
"FullName": "ИП Бугаев Е.К.",
"Email": "9135155125@mail.ru",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000084",
"FullName": "ИП Владимир Радиотовары",
"Phone": "+79130420777",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000085",
"FullName": "ИП Никульшин Дмитрий Леонидович",
"Email": "ndl-r24@mail.ru",
"Phone": "9135329970",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000759",
"FullName": "ИП Григорьева Татьяна Николаевна",
"Email": "zaika19.04@mail.ru",
"Phone": "89232886780",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000760",
"FullName": "Васильев Евгений Владимирович",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000763",
"FullName": "ООО \"Хозкомплект\" ПОСТАВЩИК копия чека",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000764",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000770",
"FullName": "Партия DI-0009",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000766",
"FullName": "ООО ПКФ\" ВОЕВОДА\"",
"Email": "24voevoda@bk.ru",
"Phone": "+79831624006",
"INN": "2463124247",
"KPP": "246301001",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000768",
"FullName": "ИП Чумакова Евгения Олеговна",
"Email": "chymeo@mail.ru",
"Phone": "89233086647",
"INN": "245305955541",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000765",
"FullName": "ИП Лукичев Николай Валентинович",
"Email": "TAKTIKA35@BK.RU",
"Phone": "89218227020",
"INN": "352525083762",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000767",
"FullName": "ИП Романов Григорий Владимирович",
"Phone": "",
"INN": "781428375302",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "СПЕЦ ЦЕНА ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000769",
"FullName": "Мутовин С.В.",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000771",
"FullName": "ИП Мазманова Бела Артюшовна",
"Phone": "",
"INN": "540210021038",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000772",
"FullName": "ИП Аль-Кхалаф Кхалил",
"Phone": "89833630110",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000773",
"FullName": "ИП Перепилица Владислав Викторович",
"Phone": "",
"INN": "241102354788",
"KPP": "241101001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000774",
"FullName": "ИП Краснова Кристина Алексеевна",
"Phone": "+79620832619",
"INN": "246215338698",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "КРУПНЫЙ ОПТ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000775",
"FullName": "ИП Мисишина Елена Германовна",
"Email": "misishina.ip@gmail.com",
"Phone": "79232830096",
"INN": "246206837348",
"KPP": "246201001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000776",
"FullName": "ООО Красноярская торговая компания",
"Phone": "",
"INN": "2460250564",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000777",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000778",
"FullName": "",
"Phone": "",
"OrganizationType": "",
"ContractType": "",
"IsVendor": "",
"IsBuyer": ""
},
{
"ID": "DI0000779",
"FullName": "ИП Гребнев Станислав Евгеньевич",
"Email": "rich-ct@mail.ru",
"Phone": "+79233048215",
"INN": "245903442803",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000902",
"FullName": "",
"Email": "misishina.ip@gmail.com",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000903",
"FullName": "",
"Email": "hozkom@list.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000904",
"FullName": "",
"Email": "kosinov_da@hozkom.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000905",
"FullName": "",
"Phone": "+79235762536",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000906",
"FullName": "",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000907",
"FullName": "",
"Email": "lilja@casseta.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000908",
"FullName": "",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000909",
"FullName": "Ковалев Егор Сергеевич (поставщик услуги)",
"Phone": "",
"INN": "7710140679",
"KPP": "771001001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "ЦБ0000910",
"FullName": "",
"Phone": "+79659169188",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000911",
"FullName": "",
"Email": "o.razorionov@gmail.com",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000912",
"FullName": "Общество с ограниченной ответственностью \"Инженер Стеклов\"",
"Phone": "",
"INN": "2464215560",
"KPP": "246401001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000913",
"FullName": "",
"Phone": "+79236777753",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000914",
"FullName": "",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000915",
"FullName": "",
"Email": "abakanov2017@mail.ru",
"Phone": "",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000916",
"FullName": "ООО \"Бегет\"",
"Phone": "",
"INN": "7801451618",
"KPP": "780101001",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000206",
"FullName": "ИП Морозова Наталья Николаевна",
"Email": "nats24rus@mail.ru",
"Phone": "89029243584",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000207",
"FullName": "ИП Ованенко Елена Эдуардовна",
"Email": "ovanenkoelena@yandex.ru",
"Phone": "89135651919",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000208",
"FullName": "ИП Шапошников Илья Олегович",
"Phone": "",
"INN": "543307840950",
"KPP": "408028108",
"OrganizationType": "Физ. лицо",
"ContractType": "",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "ЦБ0000003",
"FullName": "ОПТОВЫЙ ПОКУПАТЕЛЬ В РОЗНИЦЕ",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000209",
"FullName": "1ЧАСТНОЕ ЛИЦО DiForce",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Да",
"IsBuyer": "Да"
},
{
"ID": "DI0000210",
"FullName": "ИП Цих Александр Леович",
"Email": "cixsany@mail.ru",
"Phone": "89293060707",
"INN": "243000628190",
"KPP": "243001001",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000211",
"FullName": "ИП Бабкина Валентина Алексеевна",
"Email": "babkinava@yandex.ru",
"Phone": "89131989390",
"OrganizationType": "Юр. лицо",
"ContractType": "РОЗНИЧНАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000212",
"FullName": "ИП Ярков Константин Владимирович",
"Email": "applekrsk124@mail.ru",
"Phone": "89293344788",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000213",
"FullName": "ИП Шалыгина Юлия Александровна",
"Email": "slinkova.n@yandex.ru",
"Phone": "89029902615",
"INN": "246007697689",
"KPP": "246001001",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000214",
"FullName": "ИП Ооржак Долаана Очур-ооловна",
"Phone": "",
"INN": "170800007186",
"KPP": "170801001",
"OrganizationType": "Юр. лицо",
"ContractType": "МЕЛКООПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000780",
"FullName": "Гурман (для собственного пользования)",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000781",
"FullName": "ИП Акпашев Сергей Владимирович",
"Email": "tubalarkin@gmail.com",
"Phone": "89294710908",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000782",
"FullName": "ИП Молитиков Владислав Юрьевич",
"Email": "mol.v@internet.ru",
"Phone": "89956201005",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000783",
"FullName": "Тараскыров Сергей Леонидович",
"Phone": "89029455872",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000784",
"FullName": "ИП Арынбаев Мухтар Орынханович",
"Email": "shakarim.orynkhan@bk.ru",
"Phone": "+77026977671",
"INN": "720118301812",
"KPP": "",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000786",
"FullName": "ИП Карелин Алексей Игоревич",
"Email": "leha.karelin.1990@mail.ru",
"Phone": "89235734898",
"OrganizationType": "Юр. лицо",
"ContractType": "ОПТОВАЯ",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000785",
"FullName": "Гайфулин Руслан",
"Phone": "89135345432",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
},
{
"ID": "DI0000788",
"FullName": "Партия DI-0010/DI-0011",
"Phone": "",
"OrganizationType": "Юр. лицо",
"ContractType": "ДИФОРС Закупочная",
"IsVendor": "Да",
"IsBuyer": "Нет"
},
{
"ID": "DI0000787",
"FullName": "Беляев Александр Игоревич",
"Phone": "8-913-197-59-52",
"OrganizationType": "Юр. лицо",
"ContractType": "",
"IsVendor": "Нет",
"IsBuyer": "Да"
}
]
s = set([x['ContractType'] for x in a])
print(s)
#auth.generate_email_verification_link('coddeboy@gmail.com', action_code_settings, default_app)