# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEvent.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEvent(object):
    def setupUi(self, AddEvent):
        AddEvent.setObjectName("AddEvent")
        AddEvent.resize(323, 166)
        self.gridLayoutWidget = QtWidgets.QWidget(AddEvent)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 301, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.btnAddEvent = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAddEvent.setObjectName("btnAddEvent")
        self.gridLayout.addWidget(self.btnAddEvent, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.lblMain = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblMain.setObjectName("lblMain")
        self.gridLayout.addWidget(self.lblMain, 0, 0, 1, 3)
        self.edtEvent = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtEvent.setObjectName("edtEvent")
        self.gridLayout.addWidget(self.edtEvent, 2, 0, 1, 3)

        self.retranslateUi(AddEvent)
        QtCore.QMetaObject.connectSlotsByName(AddEvent)

    def retranslateUi(self, AddEvent):
        _translate = QtCore.QCoreApplication.translate
        AddEvent.setWindowTitle(_translate("AddEvent", "Dialog"))
        self.btnAddEvent.setText(_translate("AddEvent", "Add New Event"))
        self.lblMain.setText(_translate("AddEvent", "Enter the New Olympic Event Name Below"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddEvent = QtWidgets.QDialog()
    ui = Ui_AddEvent()
    ui.setupUi(AddEvent)
    AddEvent.show()
    sys.exit(app.exec_())
