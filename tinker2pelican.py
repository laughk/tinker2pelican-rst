#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import glob
import re

rst_files = glob.glob('content/201*/*/*/*.rst')
image_files = glob.glob('content/201*/*/*/*.png') + glob.glob('content/201*/*/*/*.jpg')
p = re.compile('^\.\. (categories|tags|comments)::\s*(.*)$')

def conv_rstfile(rst_files):
    for rst_path in rst_files:
        move_line = []
        file_line = []
        rst_read = open(rst_path, 'r')
        img_direname = os.path.dirname(rst_path).replace('content/', '/images/')

        for r in rst_read.readlines():
            if p.match(r):
                move_line.append(p.sub(r':\1: \2', r))
            elif re.match('^\.\. author::\s*.+$', r):
                pass
            elif re.match('^\.\. tags::\s*none.*$', r):
                pass
            elif re.match('^\.\. more::', r):
                file_line.append(re.sub('^\.\. more::', '.. PELICAN_END_SUMMARY', r))
            elif re.match('^\.\. image:: ', r) and not re.match('^\.\. image::\s*/images/', r):
                file_line.append(re.sub('^(\.\. image::\s*)([^\s]+)', r'\1%s/\2' % img_direname, r ))
            else:
                file_line.append(r)
        move_line.append('\n')
        rst_read.close()


        rst_write = open(rst_path, 'w')

        for dummy in range(2):
            rst_write.write(file_line.pop(0))

        for line in move_line:
            rst_write.write(line)

        for line in file_line:
            rst_write.write(line)

        rst_write.close()

def move_imagefiles(image_files):
    for image in image_files:
        dest_dir = os.path.dirname(image).replace('content/', 'content/images/')
        if not os.path.isdir(dest_dir):
            os.makedirs(dest_dir, mode=0755)
        dest = dest_dir + '/' + os.path.basename(image)
        os.rename( image, dest )

if __name__ == '__main__':
    conv_rstfile(rst_files)
    move_imagefiles(image_files)

