from PyQt4.QtCore import *
import os
from PyQt4.QtGui import *
import sys
from My_First_Widget import Ui_Form

class MainFunction (QWidget, Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.Mitigate_Button.clicked.connect(self.run_command)
    def run_command(self):
        os.system('FOR /L %N IN () DO @arp -d')
app = QApplication(sys.argv)
window = MainFunction()
window.show()
app.exec_()
