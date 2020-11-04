from docxtpl import DocxTemplate
from datetime import datetime
import time 
import datetime
import pandas as pd
import os

zpath=os.getcwd()+'\\'
# zpath=r'D:\【批量工具_效率工作】\批量_使用Python根据excel中数据批量生成word文件(word文件填空)'+'\\'
current_file_path=zpath+r'\文档生成结果'+str(datetime.date.today())
try:
    os.mkdir(current_file_path)
except:
    pass
tpl = DocxTemplate(zpath+'建大附小家长通知书.docx')

#这些字段从csv中获取
grade = pd.read_excel(zpath+'成绩单.xlsx')

stid = grade['学号']
name = grade['姓名'].str.rstrip()  # str.rstrip()用于去掉换行符
chinese = grade['语文']
math = grade['数学']
english = grade['外语']

# 遍历成绩单，逐个生成通知书
num = grade.shape[0]
for i in range(num):
    context = {
       "name": name[i],
       "chinese": chinese[i],
       "math": math[i],
       "english": english[i],
       "date": time.strftime('%Y-%m-%d',time.localtime(time.time())),
#      "date": {0:%Y}年{0:%m}月{0:%d}日".format(datetime.now()),
#       "date":time.strftime('%Y-%m-%d',time.localtime(time.time()))
#       "date": datetime.now(),
    }
    tpl.render(context)
    tpl.save(current_file_path+r"\{}的建大附小家长通知书.docx".format(name[i]))