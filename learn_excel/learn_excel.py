import xlwt


workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheets')

for i in range(100):
    for n in range(10):
        worksheet.write(i, n, 'dsafsfas')  # 不带样式的写入

workbook.save('formattings.xls') # 保存文件
