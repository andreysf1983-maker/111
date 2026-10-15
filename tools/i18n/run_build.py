import importlib.util, sys
def load(p, n):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
a = load('tools/i18n/ru_world_a.py','a'); b = load('tools/i18n/ru_world_b.py','b'); c = load('tools/i18n/ru_world_c.py','c')
bn = load('tools/i18n/ru_bnet.py','bn')
merged = {}
for d in (a.WORLD_A, b.WORLD_B, c.WORLD_C): merged.update(d)
open('tools/i18n/ru_world_all.py','w',encoding='utf-8').write('# -*- coding: utf-8 -*-\nWORLD = ' + repr(merged) + '\n')
open('tools/i18n/ru_bnet_all.py','w',encoding='utf-8').write('# -*- coding: utf-8 -*-\nBNET = ' + repr(bn.BNET) + '\n')
print('world dict size', len(merged))
