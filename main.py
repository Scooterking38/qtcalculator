
#imports
import sys
mode = 'gui'
if mode == 'gui':
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
    def __init__(self, window):
        # logical to python
        self.cli_map = {
            'n0':'0','n1':'1','n2':'2','n3':'3','n4':'4','n5':'5','n6':'6','n7':'7','n8':'8','n9':'9',
            'o0':'+','o1':'-','o2':'*','o3':'/','o4':'**','o5':'**2','o6':'**3',
            'dot':'.','pi':'pi','floor':'//','mod':'%'
        }
        
        self.window = window
        self.ans = '0'
        self.mem = 0
        self.new = 1
        self.currenttext = '0'
        self.ops = ['+', '-', '*', '/', '^', '^2', '^3']

        if mode == 'cli':
            # instructions for CLI
            print("=== CLI Calculator ===")
            print("Numbers: 0 1 2 3 4 5 6 7 8 9")
            print("Operators: + - * / ^ ^2 ^3")
            print("Special: . (dot), pi, // (floor), mod , powerten (10^x)")
            print("Memory: M+ (add), M- (subtract), MR (recall), MC (clear)")
            print("Other: AC (all clear), DEL (delete), = (calculate), Ans (last answer)")
            print("======================")

            # friendly to logical
            friendly_to_internal = {
                '0':'n0','1':'n1','2':'n2','3':'n3','4':'n4','5':'n5','6':'n6','7':'n7','8':'n8','9':'n9',
                '+':'o0','-':'o1','*':'o2','/':'o3','^':'o4','^2':'o5','^3':'o6',
                '.':'dot','pi':'pi','//':'floor','mod':'mod','powerten':'upten',
                'M+':'m0','M-':'m1','MR':'m2','MC':'m3',
                'AC':'AC','DEL':'DEL','=':'calc','Ans':'ans'
            }

            # input for CLI
            while True:
                inp = input(':').strip()
                if inp in friendly_to_internal:
                    self.button_clicked(friendly_to_internal[inp])
                else:
                    print("Unknown command:", inp)
        else:
            # connectors
            for btn in self.window.findChildren(QPushButton):
                btn.clicked.connect(lambda checked, b=btn: self.button_clicked(b))
    def setText(self, t):
        if mode == 'gui':
            self.window.display.setText(t)
        else:
            self.currenttext = t
            print(self.currenttext)
    def text(self):
        if mode == 'gui':
            return self.window.display.text()
        else:
            return self.currenttext
            
    #handler for redirecting button clicks
    def button_clicked(self, sender):

        if mode=='cli':
            name = sender
            text = self.cli_map.get(sender, sender)
        else:
            name, text = sender.objectName(), sender.text()
        if len(name) == 2 and name[1].isdigit():
            if name.startswith(('n', 'o')):
                self.append(text)
            elif name.startswith("m"):
                self.memory(text)
        else:
            match name:
                case "AC":
                    self.setText('0')
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
                    self.append('mod')
                case _:
                    pass

    #removing holder 0 and appending a string to the display
    def append(self, text):
        if self.new:
            self.setText('')
            self.new = 0
        self.setText(self.text() + text)

    #delete last char of displayed text unless its only 1 long in which case replace with 0
    def delete(self):
        self.new = 0
        current = self.text()[:-1]
        self.setText(current if current else '0')

    #prepare and standardize the input from the display
    def prepare(self):
        text = self.text()
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
            self.setText(result)
            self.ans = str(round(float(result), 6))
            
        except Exception as e:
            print("Error:", e)
            self.setText('Error!')
        self.new = 1

    #memory options: add to, subtract from, recall, and wipe
    def memory(self, option):
        if option.startswith('m'):
            option = option[1]
        try:
            val = float(self.text())
        except ValueError:
            val = 0
        match option:
            case '0':
                self.mem += val
            case '1':
                self.mem -= val
            case '2':
                self.setText(str(self.mem))
                self.new = 1
            case '3':
                self.mem = 0

#initialize the class, gui, and program
calc = Calculator(window if mode=='gui' else None)
if mode == 'gui':
    window.show()
    app.exec()
