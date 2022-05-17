# -*- coding: utf-8 -*-
# 输出文本文件的属性
# filename property.py

1) def printfp(filename):
2)     fh = open(filename)
3)     try:
4)         print('file name  :  %s' % fh.name)
5)         print('access mode:  %s' % fh.mode)
6)         print('encoding   :  %s' % fh.encoding)
7)         print('closed     :  %s' % fh.closed)
8)     finally:
9)         fh.close()
# end printfp

10) if __name__=='__main__':
11)     printfp('sample.txt')
# end if
