#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
AUTHOR: XIANRONG TANG

'''

import py_compile
from glob import glob
from shutil import copy2
import os
"""
參考自：https://www.796t.com/article.php?id=61197
"""

output = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
print(output)
for x in glob(os.path.join(output, '**\\*.*'), recursive=True):
    print(x)
    # path_list = x.replace('input', 'output')
    path_list = x.split('\\')

    if path_list[-2] == '__pycache__':
        continue
    if not os.path.exists('\\'.join(path_list[:-1])):
        os.makedirs('\\'.join(path_list[:-1]))

    if path_list[-1].split('.')[-1] == 'py':
        name = path_list[-1].split('.')
        name[-1] = 'pyc'
        path_list[-1] = '.'.join(name)
        py_compile.compile(file=x, cfile='\\'.join(path_list), optimize=-1)
        os.remove(x)
    # elif path_list[-1].split('.')[-1] in ('c', 'js', 'h', 'cpp'):
    #     os.remove(x)
    else:
        continue
