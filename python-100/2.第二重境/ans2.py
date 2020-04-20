# # 2. 读写文件 和excel

# '''
# https://www.liaoxuefeng.com/wiki/897692888725344/923030555456160
# '''
# # 读文件
# f = open('"文件路径"','r')  #如果文件不存在，open（）函数会抛出IOError的错误
# f.read()
# f.close()

# # 文件读写是可能产生IOError，一旦出错，后面的f.close()就不会调用
# try:
#     f = open('"文件路径"','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# # python引入with语句自动调用close()方法：
# with open('"文件路径"',r) as f:
#     print(f.read())

# # 1、read()会一次性读取文件的全部内容
# # 2、read(size)每次最多读取size个字节的内容
# # 3、readline()每次读取一行内容
# # 读取二进制文件用'rb'

# # 如果每次都这么手动转换编码嫌麻烦，Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：

# import codecs
# with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
#     f.read() # u'\u6d4b\u8bd5'


# # # 写文件
# # # 'w'或'wb'


# https://github.com/ShaShiDiZhuanLan/Demo_Excel_Python
# # # 读excel
# # #-*- coding=utf-8 -*-
# import xlrd
# from datetime import date,datetime

# arrayNum = 6
# #array = {'L1':'','L2':'','L3':'','L4':'','Question':'','Answer':''}
# tables = []
# newTables = []

# def read_excel():
#     # 打开文件
#     workbook = xlrd.open_workbook(r'C:\Users\zhang.xinyue\Desktop\工作簿1.xlsx')
#     # 获取所有sheet
#     sheet_name = workbook.sheet_names()[0]

#     # 根据sheet索引或者名称获取sheet内容
#     sheet = workbook.sheet_by_index(0) # sheet索引从0开始
#     # sheet = workbook.sheet_by_name('Sheet1')

#     #print (workboot.sheets()[0])
#     # sheet的名称，行数，列数
#     print (sheet.name,sheet.nrows,sheet.ncols)

#     # 获取整行和整列的值（数组）
#     rows = sheet.row_values(1) # 获取第2行内容
#     # cols = sheet.col_values(2) # 获取第3列内容
#     print (rows)
#     # print (cols)

#     for rown in range(sheet.nrows):
#        array = {'L1':'','L2':'','L3':'','L4':'','Question':'','Answer':''}
#        array['L1'] = sheet.cell_value(rown,0)
#        array['L2'] = sheet.cell_value(rown,1)
#        array['L3'] = sheet.cell_value(rown,2)
#        array['L4'] = sheet.cell_value(rown,3)
#        array['Question'] = sheet.cell_value(rown,4)
#        array['Answer'] = sheet.cell_value(rown,5)
#        tables.append(array)

#     print (len(tables))
#     #print (tables)
#     #print (tables[5])
# if __name__ == '__main__':
#     # 读取Excel
#     read_excel();
#     print ('读取成功')

# 在xlwt中生成的xls文件最多能支持65536行数据。

  # 1. 导入模块
# import xlwt
# def write_excel():
#   # 2. 创建Excel工作薄
#   myWorkbook = xlwt.Workbook()
#   # 3. 添加Excel工作表
#   mySheet = myWorkbook.add_sheet('A Test Sheet')
#   # 4. 写入数据
#   myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')   #数据格式
# #   mySheet.write(i, j, 1234.56, myStyle)
#   mySheet.write(2, 0, 1)                          #写入A3，数值等于1
#   mySheet.write(2, 1, 1)                          #写入B3，数值等于1
#   mySheet.write(2, 2, xlwt.Formula("A3+B3"))      #写入C3，数值等于2（A3+B3）
#   #5. 保存
#   myWorkbook.save('excelFile.xls')
# if __name__ == '__main__':
#     # 写入Excel
#     write_excel();
#     print ('写入成功')       