# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'defaultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DefaultWindow(object):
    def setupUi(self, DefaultWindow):
        DefaultWindow.setObjectName("DefaultWindow")
        DefaultWindow.resize(368, 144)
        self.lblMainInfo = QtWidgets.QLabel(DefaultWindow)
        self.lblMainInfo.setGeometry(QtCore.QRect(25, 40, 311, 16))
        self.lblMainInfo.setObjectName("lblMainInfo")
        self.lblMenuUse = QtWidgets.QLabel(DefaultWindow)
        self.lblMenuUse.setGeometry(QtCore.QRect(26, 60, 276, 66))
        self.lblMenuUse.setTextFormat(QtCore.Qt.RichText)
        self.lblMenuUse.setScaledContents(False)
        self.lblMenuUse.setWordWrap(True)
        self.lblMenuUse.setObjectName("lblMenuUse")

        self.retranslateUi(DefaultWindow)
        QtCore.QMetaObject.connectSlotsByName(DefaultWindow)

    def retranslateUi(self, DefaultWindow):
        _translate = QtCore.QCoreApplication.translate
        DefaultWindow.setWindowTitle(_translate("DefaultWindow", "Dialog"))
        self.lblMainInfo.setText(_translate("DefaultWindow", "Welcome to my Assignment 4 for INF2611 in semester 1 of 2020"))
        self.lblMenuUse.setText(_translate("DefaultWindow", "Please use the menu above to navigate through the application. Please login to continue and view all table data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DefaultWindow = QtWidgets.QDialog()
    ui = Ui_DefaultWindow()
    ui.setupUi(DefaultWindow)
    DefaultWindow.show()
    sys.exit(app.exec_())
