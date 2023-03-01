from PyPDF2 import PdfFileMerger
import os
import sys
from tkinter.filedialog import askopenfilenames
import datetime
#pdf 파일 합치기 
get_pdf = askopenfilenames(title='pdf 파일을 선택해주세요.',
                              initialdir=os.getcwd(),
                              filetypes=[("Adobe PDF 파일", "*.pdf")])


if get_pdf != None and len(get_pdf) != 0: #파일을 선택한게 맞는지 확인
    filename = []
    for i in get_pdf:
        if i[-3:] == 'pdf': #확장자가 pdf인지 확인 후 맞으면 list에 추가
            filename.append(os.path.basename(i))
        else:
            pass

    if filename != None and len(filename) != 0: #리스트가 비어있는지 확인 
        merger = PdfFileMerger()
        
        for f in filename:
            merger.append(f)

        pdf_name = datetime.datetime.now().strftime("%Y%m%d")  #파일 명을 오늘 날짜로 
        num = 1 

        get_path = os.getcwd() + '\\' + pdf_name + '(' + str(num) + ').pdf' #파일 경로 + 파일 명 
        
        while os.path.exists(get_path): #getpath가 존재하는지 확인 해서 있으면 num+1을 해서 생성 
            num +=1
            get_path = os.getcwd() + '\\' + pdf_name + '(' + str(num) + ').pdf'
            
        merger.write(pdf_name + "(" + str(num) + ")" + ".pdf")
        merger.close()

    else:
        sys.exit()
        
else:
    sys.exit
