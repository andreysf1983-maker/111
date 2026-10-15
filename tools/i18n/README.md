# Перевод конфигов (tools/i18n)

* `ru_bnet.py`, `ru_world_a.py`, `ru_world_b.py`, `ru_world_c.py` — словари русских описаний.
* `ru_bnet_all.py`, `ru_world_all.py` — объединённые словари (генерируются из частей через `run_build.py`).
* `build_conf_ru.py` — заменяет английские блоки комментариев над настройками на русские.
  Значения настроек не меняются.
* `post_ru.py` — заголовок файла и блок «ПРИМЕР НАСТРОЙКИ».

Пересборка:

```
python tools/i18n/run_build.py
python tools/i18n/build_conf_ru.py server/worldserver.conf.dist server/worldserver.conf.dist tools/i18n/ru_world_all.py WORLD
python tools/i18n/build_conf_ru.py server/bnetserver.conf.dist server/bnetserver.conf.dist tools/i18n/ru_bnet_all.py BNET
python tools/i18n/post_ru.py server/worldserver.conf.dist
python tools/i18n/post_ru.py server/bnetserver.conf.dist
```
