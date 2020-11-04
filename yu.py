import xlrd #引入excel读取模块
import xlwt #引入excel写入模块
from mailmerge import MailMerge #引用邮件处理模块
datafile_path = '22.xlsX'
data = xlrd.open_workbook(datafile_path)  #获取数据
table = data.sheet_by_name('Sheet1')
nrows = table.nrows
template = '22.docx'
document = MailMerge(template)
for i in range(nrows): #循环逐行打印
  if i > 0: #排除0项无用数据
    document.merge(
      name=table.row_values(i)[1]
    )
    wordname= table.row_values(i)[1]+'.docx'
    document.write(wordname) #创建新文件