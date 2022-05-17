# -*- coding: utf-8 -*-
# 输出文本文件的属性
# filename property.py

def printfp(filename):
    fh = open(filename)
    try:
        print('file name  :  %s' % fh.name)
        print('access mode:  %s' % fh.mode)
        print('encoding   :  %s' % fh.encoding)
        print('closed     :  %s' % fh.closed)
    finally:
        fh.close()
# end printfp

if __name__=='__main__':
    printfp('sample.txt')
# end if
