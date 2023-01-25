from loader import V83
from models.good import GoodModel


class V83Controller:
    @classmethod
    def getAllGoods(cls):
        goods = []
        if V83:
            q = "ВЫБРАТЬ * ИЗ Справочник.Номенклатура"
            query = V83.NewObject("Query", q)
            selection = query.Execute().Choose()
            while selection.Next():
                goods += [
                    GoodModel(name=selection.Наименование,
                              article_num=selection.Артикул,
                                base_measure_unit=selection.БазоваяЕдиницаИзмерения,
                                comment=selection.Комментарий,
                                good_set=selection.Набор,
                                description=selection.ДополнительноеОписаниеНоменклатуры,
                                general_image=selection.ОсновноеИзображение.ИмяФайла,
                                general_supplier=selection.ОсновнойПоставщик.ДокументУдостоверяющийЛичность + selection.ОсновнойПоставщик.НаименованиеПолное,
                                manufacturer=selection.ПроизводительТовара,
                                price_group=selection.ЦеноваяГруппа,
                                color=selection.Цвет)
                ]
        return goods