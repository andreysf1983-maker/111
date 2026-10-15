import re, sys
EXAMPLE_RU = """#    Имя_настройки = значение
#        Описание: Краткое описание того, что делает настройка.
#        Важно:    Важные замечания по настройке (если есть).
#        Пример:   Пример значения (для текстовых значений в кавычках).
#        По умолчанию: 10 - (Включено | Комментарий | Имя связанной настройки)
#                      0  - (Выключено | Комментарий | Имя связанной настройки)
#
# Примечания для разработчиков:
# - Копируйте этот пример, чтобы сохранить оформление.
# - Переносы строк делайте примерно на 100-м символе.
"""
HEADER = {
 'server/bnetserver.conf.dist': [
   ('LegionForge Core Auth Server configuration file', 'Файл настроек сервера авторизации Battle.net (bnetserver) — LegionForge'),
   ('AUTH SERVER SETTINGS', 'НАСТРОЙКИ СЕРВЕРА АВТОРИЗАЦИИ'),
   ('MYSQL SETTINGS', 'НАСТРОЙКИ БАЗ ДАННЫХ (MYSQL)'),
   ('ОГЛАВЛЕНИЕ', 'ОГЛАВЛЕНИЕ'),
 ],
 'server/worldserver.conf.dist': [
   ('LegionForge Core World Server configuration file', 'Файл настроек игрового сервера (worldserver) — LegionForge'),
 ],
}
SECTION_EXTRA = {
 'AUTH SERVER SETTINGS': 'НАСТРОЙКИ СЕРВЕРА АВТОРИЗАЦИИ',
 'MYSQL SETTINGS': 'НАСТРОЙКИ БАЗ ДАННЫХ (MYSQL)',
}
path = sys.argv[1]
s = open(path, encoding='utf-8').read()
for a, b in HEADER.get(path, []):
    s = s.replace(a, b)
for a, b in SECTION_EXTRA.items():
    s = re.sub(r'(#\s+)' + re.escape(a) + r'\b', lambda m: m.group(1) + b, s)
# Replace the English "EXAMPLE CONFIG" template block with the Russian one.
s = re.sub(r'(# ПРИМЕР НАСТРОЙКИ\n#\n)(.*?)(\n#{20,}\n)', lambda m: m.group(1) + EXAMPLE_RU + m.group(3), s, count=1, flags=re.S)
open(path, 'w', encoding='utf-8', newline='\n').write(s)
