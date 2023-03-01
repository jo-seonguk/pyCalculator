import sqlite3
import os
import openpyxl



db_path = os.getenv('HOME')+'/mydb.db'
con = sqlite3.connect(db_path)

c = con.cursor()

path = "C:/Users/User/Documents/test/"
filename = "engineer career.xlsx"

# 엑셀파일 읽어옴 
wb = openpyxl.load_workbook(path + filename, data_only=True)

sheet_names = wb.sheetnames

def createTable():
    
    for i, name in enumerate(sheet_names):
        ws = wb[name]
        c.execute("DROP TABLE IF EXISTS " + name)
        c.execute("CREATE TABLE IF NOT EXISTS "+ name +" (_id INTEGER PRIMARY KEY, work TEXT, sdate TEXT, fdate TEXT, field TEXT, type1 TEXT, order1 TEXT, type2 TEXT, type3 TEXT, price INT, day INT, wday INT)")
        
        for row in ws.rows:
            data = []
            if row[0].row < 3:
                pass
            else:
                if (row[0].row - 2) != row[0].value:
                    pass
                else:
                    for i in range(0, 12):
                        if i == 2 or i == 3:
                            data.append(str(row[i].value)[0:10])
                        else:
                            if i == 8 and row[i].value == None:
                                data.append('기타')
                            elif i == 9 and row[i].value == None:
                                data.append(0)
                            else:
                                data.append(row[i].value)
            
                    c.execute('INSERT INTO ' + name + ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)
                        
    con.commit()
    
    con.close()




def main():
    createTable()
    
    print('finish')


if __name__ == "__main__":
    main()
    
#SELECT SUM(wday) AS wday FROM 손병락 where type1 like '교량';
#SELECT type1, type2, SUM(wday) AS wday FROM 손병락 GROUP BY type1, type2
#SELECT name FROM sqlite_master WHERE type IN ('table', 'view') AND name NOT LIKE 'sqlite_%' UNION ALL SELECT name FROM sqlite_temp_master WHERE type IN ('table', 'view') ORDER BY 1;
