import datetime
from openpyxl import load_workbook
wb = load_workbook('my_xl.xlsx')

# блок Описание
wb.properties.title = "111" # Название
wb.properties.subject = "222" # Тема
wb.properties.keywords = "333" # Теги
wb.properties.category ="444" # Категории
wb.properties.description = "555" # Комментарии

# блок Источник
wb.properties.creator='www.gf8.ru' #Авторы
wb.properties.lastModifiedBy="Пантелеев А.С." # Кем сохранён
wb.properties.revision="66666" # Редакция
wb.properties.version="77777" # Номер версии

        # Дата создания содержимого
wb.properties.created=datetime.datetime(2019, 1, 31, 9, 0, 0) 
        # Дата последнего сохранения
wb.properties.modified=datetime.datetime(2019, 2, 28, 9, 0, 0)
        # Последний вывод на печать
wb.properties.lastPrinted=datetime.datetime(2019, 3, 30, 9, 0, 0)

# блок Содержание
wb.properties.contentStatus="Истинная правда" # Состояние содержимого
wb.properties.language="RUS" # Язык

# Визуально Никуда не идёт
wb.properties.identifier = "44444"


print(wb.properties)
wb.save('my_xl.xlsx')

