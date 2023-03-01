from pymongo import MongoClient
import traceback
import pymongo
import openpyxl

'''
    mongoDB에 저장 로컬db여서 사용할때 실행해줘야함
    기존 sql 문과 달라서 공부를 좀 더 해야함
'''

host = 'localhost'
port = 27017

def main():
    # 파일 경로 및 파일 이름(확장자)
    path = "C:/Users/User/Documents/test/"
    filename = "engineer career.xlsx"

    # 엑셀파일 읽어옴 
    wb = openpyxl.load_workbook(path + filename, data_only=True)
    ws = wb.active

    ws = wb['SHEETname']

    workList =[]
    
    for row in ws.rows:
        item = {}
        if row[0].row < 3:
            pass
        else:
            if (row[0].row - 2) != row[0].value:
                pass
            else:
                item['_id'] = str(row[0].value)
                item['work'] = str(row[1].value)
                item['sdate'] = str(row[2].value)
                item['fdate'] = str(row[3].value)
                item['field'] = str(row[4].value)
                item['type1'] = str(row[5].value)
                item['order'] = str(row[6].value)
                item['type2'] = str(row[7].value)
                item['type3'] = str(row[8].value)
                item['price'] = str(row[9].value)
                item['day'] = str(row[10].value)
                item['wday'] = str(row[11].value)
                
                workList.append(item)

        

    #print(workList)
        
    try:
        client = MongoClient(
            host=host,
            port=port)
        db = client['sheet']
        col = db["jdh"]
        x = col.insert_many(workList)
        print(x.inserted_ids)
        print('MongoDB Connected.')

        cursor = db.member.find({})
        print(list(cursor))
        
    except Exception as e:
        print(traceback.format_exc())
    finally:
        client.close()
        print('MongoDB Closed.')

if __name__ == "__main__":
    main()

