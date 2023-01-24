from loader import V83


class V83Controller:
    @classmethod
    def getAllGoods(cls):
        goods = []
        q = "ВЫБРАТЬ Наименование КАК g_name ИЗ Справочник.Номенклатура"
        query = V83.NewObject("Query", q)
        selection = query.Execute().Choose()
        while selection.Next():
            goods += [
                dict(Name=selection['g_name'])
            ]
        return goods
