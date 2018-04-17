from PyQt4 import QtCore, QtGui
#############################################################################################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
#############################################################################################


class Ui_Form(object):
    def setupUi(self, form):
        form.setObjectName(_fromUtf8("form"))
        form.resize(262, 239)
        self.verticalLayout_4 = QtGui.QVBoxLayout(form)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Mitigate_Button = QtGui.QPushButton(form)
        self.Mitigate_Button.setObjectName(_fromUtf8("Mitigate_Button"))
        self.verticalLayout_3.addWidget(self.Mitigate_Button)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        form.setWindowTitle(_translate("form", "ANti SelfishNet", None))
        self.Mitigate_Button.setText(_translate("form", "Mitigate", None))
#############################################################################################

