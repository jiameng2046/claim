import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyExcelerator import *
# import random

w = Workbook() #创建一个工作簿
ws = w.add_sheet('1') #创建一个工作表
for j in range(0,5):     #控制列

    for i in range(0, 50000):   #控制行

        if(j == 0):         #第一列
            ws.write(i, j, '13001454722')
        if(j == 1):
            ws.write(i,j,'6')
        if(j == 2):
            ws.write(i, j, 'KQ_201801_20WANONE')
        if(j == 3):
            ws.write(i,j,'1')
        if(j == 4):
            ws.write(i,j,u'否')





w.save('xqtest.xls')