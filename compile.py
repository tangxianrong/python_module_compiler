#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
AUTHOR: XIANRONG TANG

'''

import py_compile
from glob import glob
from shutil import copy
import os
"""
參考自：https://www.796t.com/article.php?id=61197
"""


for x in glob(os.path.join('input', '**\\*.*'), recursive = True):
    path_list = x.split('\\')
    path_list[0] = 'output' 
    if path_list[-2] == '__pycache__':
        continue
    if not os.path.exists('\\'.join(path_list[:-1])):
        os.makedirs('\\'.join(path_list[:-1]))
    
    if path_list[-1].split('.')[-1]=='py':
        name = path_list[-1].split('.')
        name[-1]='pyc'
        path_list[-1] = '.'.join(name)
        py_compile.compile(file=x, cfile='\\'.join(path_list), optimize=-1)
    else:
        copy(x, '\\'.join(path_list))
