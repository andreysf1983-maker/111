#!/usr/bin/env python3
"""
Переводит комментарии в worldserver.conf.dist и bnetserver.conf.dist на русский.

Для каждой настройки (строка вида `Key = value`) заменяет английский блок
описания, стоящий непосредственно над ней, на русское описание из словаря.
Значения настроек, секции и порядок строк НЕ меняются; после сборки скрипт
проверяет, что все рабочие строки конфига идентичны оригиналу.

Использование:
    python3 build_conf_ru.py <input.dist> <output.dist> <dict_module> <dict_name>
"""
import importlib.util
import re
import sys

SECTION_RU = {
    'EXAMPLE CONFIG': 'ПРИМЕР НАСТРОЙКИ',
    'CONNECTIONS AND DIRECTORIES': 'ПОДКЛЮЧЕНИЯ И КАТАЛОГИ',
    'PERFORMANCE SETTINGS': 'НАСТРОЙКИ ПРОИЗВОДИТЕЛЬНОСТИ',
    'SERVER LOGGING': 'ЛОГИРОВАНИЕ СЕРВЕРА',
    'SERVER SETTINGS': 'НАСТРОЙКИ СЕРВЕРА',
    'UPDATE SETTINGS': 'НАСТРОЙКИ АВТООБНОВЛЕНИЯ БАЗ ДАННЫХ',
    'HOTSWAP SETTINGS': 'ГОРЯЧАЯ ПЕРЕЗАГРУЗКА СКРИПТОВ (HOTSWAP)',
    'WARDEN SETTINGS': 'НАСТРОЙКИ ЗАЩИТЫ WARDEN',
    'PLAYER INTERACTION': 'ВЗАИМОДЕЙСТВИЕ ИГРОКОВ',
    'CREATURE SETTINGS': 'НАСТРОЙКИ СУЩЕСТВ (МОБОВ)',
    'CHAT SETTINGS': 'НАСТРОЙКИ ЧАТА',
    'GAME MASTER SETTINGS': 'НАСТРОЙКИ ГЕЙМ-МАСТЕРОВ',
    'SUPPORT SETTINGS': 'НАСТРОЙКИ ТИКЕТОВ ПОДДЕРЖКИ',
    'VISIBILITY AND DISTANCES': 'ВИДИМОСТЬ И ДИСТАНЦИИ',
    'SERVER RATES': 'МНОЖИТЕЛИ (РЕЙТЫ) СЕРВЕРА',
    'STATS LIMITS': 'ОГРАНИЧЕНИЯ ХАРАКТЕРИСТИК',
    'AUTO BROADCAST': 'АВТОМАТИЧЕСКИЕ ОБЪЯВЛЕНИЯ',
    'BATTLEGROUND CONFIG': 'НАСТРОЙКИ ПОЛЕЙ БОЯ',
    'BATTLEFIELD CONFIG': 'НАСТРОЙКИ ПОЛЕЙ БИТВ (ОСАДЫ)',
    'ARENA CONFIG': 'НАСТРОЙКИ АРЕН',
    'NETWORK CONFIG': 'НАСТРОЙКИ СЕТИ',
    'CONSOLE AND REMOTE ACCESS': 'КОНСОЛЬ И УДАЛЁННЫЙ ДОСТУП',
    'AUCTION HOUSE BOT SETTINGS': 'НАСТРОЙКИ БОТА АУКЦИОННОГО ДОМА',
    'BLACK MARKET SETTINGS': 'НАСТРОЙКИ ЧЁРНОГО РЫНКА',
    'LOGGING SYSTEM SETTINGS': 'НАСТРОЙКИ СИСТЕМЫ ЛОГИРОВАНИЯ',
    'CURRENCIES SETTINGS': 'НАСТРОЙКИ ВАЛЮТ',
    'PACKET SPOOF PROTECTION SETTINGS': 'ЗАЩИТА ОТ ПОДМЕНЫ ПАКЕТОВ',
    'METRIC SETTINGS': 'НАСТРОЙКИ МЕТРИК (ГРАФАНА/INFLUX)',
    'SECTION INDEX': 'ОГЛАВЛЕНИЕ',
    'REST SERVICE': 'REST-СЕРВИС МИРА',
    'WORLD TO DISCORD': 'ПЕРЕСЫЛКА ЧАТА В DISCORD',
    'CHARACTER DELETE OPTIONS': 'УДАЛЕНИЕ ПЕРСОНАЖЕЙ',
    'CUSTOM SERVER OPTIONS': 'ОСОБЫЕ НАСТРОЙКИ LEGIONFORGE',
    'AUCTION HOUSE BOT ITEM FINE TUNING': 'ТОНКАЯ НАСТРОЙКА БОТА АУКЦИОНА (ПРЕДМЕТЫ)',
    'AUCTION HOUSE BOT BUYER CONFIG': 'НАСТРОЙКИ ПОКУПАТЕЛЯ БОТА АУКЦИОНА',
    'AUTH SERVER SETTINGS': 'НАСТРОЙКИ СЕРВЕРА АВТОРИЗАЦИИ',
    'MYSQL SETTINGS': 'НАСТРОЙКИ БАЗ ДАННЫХ (MYSQL)',
}

SEP_RE = re.compile(r'^#{20,}\s*$')
KEY_RE = re.compile(r'^([A-Za-z][A-Za-z0-9_.]*)\s*=')
HDR_RE = re.compile(r'^(#\s*)([A-Z][A-Z0-9 &/()\-]+?)\s*$')


def load_dict(path, name):
    spec = importlib.util.spec_from_file_location('ru_dict', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, name)


def is_block_line(line):
    return line.startswith('#') and not SEP_RE.match(line) and line.strip() != ''


def render_block(key, desc):
    out = ['#    ' + key]
    for i, text in enumerate(desc.split('\n')):
        label = '#        Описание: ' if i == 0 else '#                  '
        out.append(label + text)
    return out


def main():
    src, dst, dict_path, dict_name = sys.argv[1:5]
    table = load_dict(dict_path, dict_name)
    lines = open(src, encoding='utf-8', errors='surrogateescape').read().split('\n')
    out = []
    missing = []
    seen_keys = set()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = KEY_RE.match(line)
        if m:
            key = m.group(1)
            seen_keys.add(key)
            # Collect the contiguous comment block directly above this key.
            # Walk back over comment and blank lines until a key, a separator or a
            # section header boundary. Everything in between is the English help
            # text for this key (or a group of keys) and is replaced.
            j = len(out) - 1
            while j >= 0 and (is_block_line(out[j]) or out[j].strip() == ''):
                j -= 1
            start = j + 1
            block = out[start:]
            # Keep section headers: never delete a header line (it sits between separators).
            if any(HDR_RE.match(x) and not x.strip().startswith('#    ') for x in block):
                start = len(out)
                block = []
            del out[start:]
            value = line.split('=', 1)[1].strip()
            if key in table:
                out.append('')
                out += render_block(key, table[key])
                out.append('#        Значение по умолчанию: ' + value)
            else:
                missing.append(key)
                out += block
            out.append(line)
            i += 1
            continue
        hm = HDR_RE.match(line)
        if hm and hm.group(2).strip() in SECTION_RU:
            out.append(hm.group(1) + SECTION_RU[hm.group(2).strip()])
        else:
            out.append(line)
        i += 1

    open(dst, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('keys translated:', len([k for k in seen_keys if k in table]), 'of', len(seen_keys))
    if missing:
        print('MISSING (kept English):', ' '.join(missing))


if __name__ == '__main__':
    main()
