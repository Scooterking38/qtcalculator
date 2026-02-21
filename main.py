import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

app = QApplication(sys.argv)
file = QFile("calculator.ui")   # your .ui filename
file.open(QFile.ReadOnly)
loader = QUiLoader()
window = loader.load(file)
file.close()

class calculator:
    def __init__(self):
        self.new = 0
        self.ops = ['+','-','*','/','^','^2','^3']
        self.mem = 0
        self.ans = '0'
        window.AC.clicked.connect(lambda: window.display.setText('0'))
        window.DEL.clicked.connect(lambda: self.delete())
        window.calc.clicked.connect(lambda: self.prepare())
        window.ans.clicked.connect(lambda: self.append('Ans'))
        for i in range(10):
            getattr(window, f"n{i}").clicked.connect(lambda _,d=str(i): self.append(d))
        for i in range(4):
            getattr(window, f"m{i}").clicked.connect(lambda _,d=str(i): self.memory(d))
        for i, op in enumerate(self.ops):
            getattr(window, f"o{i+1}").clicked.connect(lambda _, o=op: self.append(o))

    def calc(self, text):
        try:
            result = eval(text)
            window.display.setText(result)
            self.new = 1
            self.ans = result
        except Exception as a:
            print(a)
            window.display.setText('Error, Check Terminal!')

    def prepare(self, ):
        text = window.display.text()
        while 'Ans' in text:
            i = text.index('Ans')
            if (i < 1) or (text[i-1] in self.ops) or ((i > 1) and (text[i-2:i] in self.ops)):
                #safe options for ans location= Ans at start. last char is an operator. there are two chars before and they are a dual char operator.
                text = text[:i]+self.ans+text[i+3:]
            else:
                text = text[:i]+'*'+self.ans+text[i+3:]
        text = text.replace('^','**')
        self.calc(text)

    def memory(self, option):
        current = window.display.text()
        match option:
            case '0'|'1':
                if not any(e in self.ops for e in current):
                    try:
                        if option == '1':
                            text = 0-current
                        self.mem += float(current)
                    except ValueError:
                        window.display.setText('0')
            case '2':
                window.display.setText(str(self.mem))
            case _:
                self.mem = 0

    def append(self,text):
        if self.new == 1 or window.display.text() == '0':
            window.display.setText('')
            self.new = 0
        window.display.setText(str(window.display.text())+str(text))

    def delete(self):
        self.new = 0
        window.display.setText(window.display.text()[:-1])
        if len(window.display.text()) <= 0:
            window.display.setText('0')




myproject = calculator()




#init
window.show()
app.exec()
