# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addVenue.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddVenue(object):
    def setupUi(self, AddVenue):
        AddVenue.setObjectName("AddVenue")
        AddVenue.resize(323, 165)
        self.gridLayoutWidget = QtWidgets.QWidget(AddVenue)
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
        self.btnAddVenue = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAddVenue.setObjectName("btnAddVenue")
        self.gridLayout.addWidget(self.btnAddVenue, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.lblMain = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblMain.setObjectName("lblMain")
        self.gridLayout.addWidget(self.lblMain, 0, 0, 1, 3)
        self.edtVenue = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtVenue.setObjectName("edtVenue")
        self.gridLayout.addWidget(self.edtVenue, 2, 0, 1, 3)

        self.retranslateUi(AddVenue)
        QtCore.QMetaObject.connectSlotsByName(AddVenue)

    def retranslateUi(self, AddVenue):
        _translate = QtCore.QCoreApplication.translate
        AddVenue.setWindowTitle(_translate("AddVenue", "Add Venue"))
        self.btnAddVenue.setText(_translate("AddVenue", "Add New Venue"))
        self.lblMain.setText(_translate("AddVenue", "Enter the New Olympic Venue Name Below"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddVenue = QtWidgets.QDialog()
    ui = Ui_AddVenue()
    ui.setupUi(AddVenue)
    AddVenue.show()
    sys.exit(app.exec_())
