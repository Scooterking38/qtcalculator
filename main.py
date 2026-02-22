#imports
import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

#read + load the ui file
app = QApplication(sys.argv)
file = QFile("calculator.ui")
file.open(QFile.ReadOnly)
loader = QUiLoader()
window = loader.load(file)
file.close()

#make the calculator
class Calculator:
    #set some internal variables and detect every button
    def __init__(self, window):
        self.window = window
        self.ans = '0'
        self.mem = 0
        self.new = 1
        self.ops = ['+', '-', '*', '/', '^', '^2', '^3']
        for btn in self.window.findChildren(QPushButton):
            btn.clicked.connect(lambda checked, b=btn: self.button_clicked(b))

    #handler for redirecting button clicks
    def button_clicked(self, sender):
        name, text = sender.objectName(), sender.text()
        if len(name) == 2 and name[1].isdigit():
            if name.startswith(('n', 'o')):
                self.append(text)
            elif name.startswith("m"):
                self.memory(text)
        else:
            match name:
                case "AC":
                    self.window.display.setText('0')
                    self.new = 1
                case "DEL":
                    self.delete()
                case "calc":
                    self.prepare()
                case "ans":
                    self.append('Ans')
                case "dot":
                    self.append('.')
                case 'upten':
                    self.append('*10^')
                case 'pi':
                    self.append('pi')
                case 'floor':
                    self.append('//')
                case 'mod':
                    self.append('%')
                case _:
                    pass

    #removing holder 0 and appending a string to the display
    def append(self, text):
        if self.new:
            self.window.display.setText('')
            self.new = 0
        self.window.display.setText(self.window.display.text() + text)

    #delete last char of displayed text unless its only 1 long in which case replace with 0
    def delete(self):
        self.new = 0
        current = self.window.display.text()[:-1]
        self.window.display.setText(current if current else '0')

    #prepare and standardize the input from the display
    def prepare(self):
        text = self.window.display.text()
        while 'Ans' in text:
            i = text.index('Ans')
            if i == 0 or text[i-1] in self.ops:
                text = text[:i] + self.ans + text[i+3:]
            else:
                text = text[:i] + '*' + self.ans + text[i+3:]
        text = text.replace('^', '**')
        text = text.replace('pi', '3.14159265358979323846264338327950288419716939937510')
        self.calc(text)

    #perform the eval and tell the class that the user has finished creating the equation
    def calc(self, expr):
        try:
            result = str(eval(expr))
            self.window.display.setText(result)
            self.ans = str(round(float(result), 6))
            self.new = 1
        except Exception as e:
            print("Error:", e)
            self.window.display.setText('Error!')

    #memory options: add to, subtract from, recall, and wipe
    def memory(self, option):
        try:
            val = float(self.window.display.text())
        except ValueError:
            val = 0
        match option:
            case '0':
                self.mem += val
            case '1':
                self.mem -= val
            case '2':
                self.window.display.setText(str(self.mem))
                self.new = 1
            case '3':
                self.mem = 0

#initialize the class, gui, and program
calc = Calculator(window)
window.show()
app.exec()
