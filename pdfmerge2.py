from PyPDF2 import PdfFileMerger, PdfFileReader
import os
import sys
from tkinter.filedialog import askopenfilename
import datetime
import openpyxl

#get_excel: 경로 + 파일명
get_excel = askopenfilename(title='엑셀 파일을 선택해주세요.',
                              initialdir=os.getcwd(),
                              filetypes=[("*.xlsx", "*xlsx"), ("*.xls", "*xls"), ("*.csv", "*csv")])


path = "C:/Users/User/Documents/실적/선익/단일/"

if get_excel != None and len(get_excel) != 0: #파일을 선택한게 맞는지 확인
    #파일 확장자 확인
    if get_excel[-4:] == 'xlsx' or get_excel[-3:] == 'xls' or get_excel[-3:] == 'csv':
        get_excel_path = get_excel.replace(os.path.basename(get_excel), '')  #엑셀파일 경로
        #print(get_excel_path)
        wb = openpyxl.load_workbook(get_excel) 
        ws = wb.active
        sheet_names = wb.sheetnames #엑셀 시트명 리스트 
        
        for name in sheet_names:       #시트명에 '실적' 이 없으면 리스트에서 제거
            if '실적' not in name:
                sheet_names.remove(name) 
        print(sheet_names)       


        for name in sheet_names:       
            globals()['{}'.format(name)] = [] #globals()[] 로 시트명 리스트에 있는 시트명으로 리스트 생성
            
            ws = wb[name]
            for row in ws.rows:
                if len(str(row[2].value)) > 4:
                    globals()[name].append(str(row[5].value).split(' ')[0] + '-' + str(row[2].value)+'.pdf')
            print(globals()[name])
            excel_path = get_excel_path + '실적/' + name  
            if not os.path.exists(excel_path): #폴더 있는지 확인 
                os.mkdir(excel_path)
            
            files = os.listdir(path)
            merger = PdfFileMerger()
            for file in files:
                if file in globals()[name]:
                    merger.append(PdfFileReader(open(path+file, 'rb'))) 
                    print(merger)            


            num = 1
            get_path = excel_path + '(' + str(num) + ').pdf'
            
            while os.path.exists(get_path): #파일이 존재하는지 확인 있으면 num+1을 해서 생성 
                num += 1
                get_path = excel_path + '(' + str(num) + ').pdf'
            merger.write(name + "(" + str(num) + ")" + ".pdf")
            merger.close()
    else:
        sys.exit()
        
else:
    sys.exit
