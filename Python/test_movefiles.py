# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:18:26 2015

@author: justin.malinchak
"""

import os
import shutil

root_src_dir = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')
#root_dst_dir = 'C:\Batches\AutomationProjects\Investment Strategy\ETL\Uploads\Complete'.encode('string_escape')
root_dst_dir = 'E:\Batches\development\projects\Investment Strategy\ETL\Uploads\Ready'.encode('string_escape')

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir)
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.move(src_file, dst_dir)