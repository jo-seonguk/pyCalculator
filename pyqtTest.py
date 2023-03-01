import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    
    operator = ['+', '-', '×', '÷', '(', ')']
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.display2 = QLineEdit("0")
        self.display2.setReadOnly(True)
        self.display2.setAlignment(Qt.AlignRight)
        
        self.display = QLineEdit("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)

        layout = QVBoxLayout()
        gridLayout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.display2)
        layout.addWidget(self.display)
        layout.addLayout(gridLayout)

        self.digitBtn = []        

        self.clearBtn = QPushButton("CE", self)
        self.clearAllBtn = QPushButton("C", self)
        self.delBtn = QPushButton("←", self)
        self.divBtn = QPushButton("÷", self)
        self.mulBtn = QPushButton("×", self)
        self.minBtn = QPushButton("-", self)
        self.plusBtn = QPushButton("+", self)
        self.equalBtn = QPushButton("=", self)
        self.dotBtn = QPushButton(".", self)
        self.revBtn = QPushButton("+/-", self)

        for i in range(0, 10):
            row = int(((9 - i) / 3) + 2)
            col = ((i -  1) % 3)
            self.digitBtn.append(QPushButton(str(i)))
            
            if i == 0:
                gridLayout.addWidget(self.digitBtn[i], 5, 1)
            else:
                gridLayout.addWidget(self.digitBtn[i], row, col)

            self.digitBtn[i].clicked.connect(self.btn)
            
        
        gridLayout.addWidget(self.clearBtn, 1, 0)
        gridLayout.addWidget(self.clearAllBtn, 1, 1)
        gridLayout.addWidget(self.delBtn, 1, 2)
        gridLayout.addWidget(self.divBtn, 1, 3)
        gridLayout.addWidget(self.mulBtn, 2, 3)
        gridLayout.addWidget(self.minBtn, 3, 3)
        gridLayout.addWidget(self.plusBtn, 4, 3)
        gridLayout.addWidget(self.equalBtn, 5, 3)
        gridLayout.addWidget(self.dotBtn, 5, 2)
        gridLayout.addWidget(self.revBtn, 5, 0)

        self.delBtn.clicked.connect(self.delete)
        self.clearBtn.clicked.connect(self.clear)
        self.clearAllBtn.clicked.connect(self.clearAll)
        self.revBtn.clicked.connect(self.reverse)
        self.dotBtn.clicked.connect(self.dot)
        self.divBtn.clicked.connect(self.btn)
        self.mulBtn.clicked.connect(self.btn)
        self.minBtn.clicked.connect(self.btn)
        self.plusBtn.clicked.connect(self.btn)
        self.equalBtn.clicked.connect(self.calc)
        
        
        self.setWindowTitle("My Application")
        self.setGeometry(300, 300, 300, 200)    #move + resize
        self.show()

    def clear(self):
        self.display.setText("0")
            
    def clearAll(self):
        self.display.setText("0")
        self.display2.setText("0")

    def delete(self):
        if len(self.display.text) == 1:
            self.display.setText('0')
        else:
            if self.display.text == '':
                pass
            else:
                self.display.setText(self.display.text()[:-1])
        
        
    def reverse(self):
        if self.display.text()[0] == '-':
            self.display.setText(self.display.text()[1:])
        else:
            self.display.setText('-' + self.display.text())
            

    def dot(self):
        if self.display.text() == '':
            pass
        else:
            if self.display.text().find('.') == -1:
                self.display.setText(self.display.text() + '.')
            else:
                pass
            
    
    def btn(self):
        if self.sender() == '':
            pass
        else:
            sender = self.sender()
            str_sender = str(sender.text())

            if str_sender in self.operator:
                if self.display.text()[-1] == '.':
                    text = self.display.text()[:-1]
                else:
                    text = self.display.text()
                if self.display2.text() == '0':
                    self.display2.setText(text + str_sender)

                elif self.display2.text()[-1] in self.operator:
                    if self.display.text() == '0':
                        self.display2.setText(self.display2.text()[:-1] + str_sender)
                    else:
                        self.display2.setText(self.display2.text() + text + str_sender)
                else:
                    self.display2.setText(self.display2.text() + text + str_sender)
                self.display.setText('0')

            else:
                if self.display.text() == '0':
                    self.display.setText(str_sender)
                else:
                    self.display.setText(self.display.text()+str_sender)
                    
    def calc(self):
        self.display2.setText(self.display2.text() + self.display.text())
        calc_list = []
        i = 0

        for idx, s in enumerate(self.display2.text()):
            if s in self.operator:
                if self.display2.text()[i:idx].strip() != "":
                    calc_list.append(self.display2.text()[i:idx])
                    calc_list.append(s)
                    i = idx + 1
        calc_list.append(self.display.text())
        
        while True:
            for idx, s in enumerate(calc_list):
                if s in self.operator:
                    tmp=''
                    if s == '×':
                        tmp = calc_list[idx-1] + '*' + calc_list[idx+1]
                        del calc_list[idx-1:idx+2]
                        calc_list.insert(idx-1, str(eval(tmp)))
                        break
                    elif s == '÷':
                        tmp = calc_list[idx-1] + '/' + calc_list[idx+1]
                        del calc_list[idx-1:idx+2]
                        calc_list.insert(idx-1, str(eval(tmp)))
                        break
                    else:
                        if calc_list.count('×') == 0 and calc_list.count('÷') == 0:
                            tmp = calc_list[idx-1] + calc_list[idx] + calc_list[idx+1]
                            del calc_list[idx-1:idx+2]
                            calc_list.insert(idx-1, str(eval(tmp)))
                            break
                        else: pass
                    
            if len(calc_list) == 1:
                self.display.setText(calc_list[0])
                calc_list = []         
                break
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
