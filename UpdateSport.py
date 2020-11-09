# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateSport.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateSport(object):
    def setupUi(self, UpdateSport):
        UpdateSport.setObjectName("UpdateSport")
        UpdateSport.resize(417, 195)
        self.gridLayoutWidget = QtWidgets.QWidget(UpdateSport)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 383, 127))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.lblMain = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblMain.setObjectName("lblMain")
        self.gridLayout.addWidget(self.lblMain, 0, 0, 1, 3)
        self.btnUpdateSport = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnUpdateSport.setObjectName("btnUpdateSport")
        self.gridLayout.addWidget(self.btnUpdateSport, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        self.edtOldSportName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtOldSportName.setObjectName("edtOldSportName")
        self.gridLayout.addWidget(self.edtOldSportName, 2, 0, 1, 3)
        self.edtNewSportName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtNewSportName.setObjectName("edtNewSportName")
        self.gridLayout.addWidget(self.edtNewSportName, 4, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 3)

        self.retranslateUi(UpdateSport)
        QtCore.QMetaObject.connectSlotsByName(UpdateSport)

    def retranslateUi(self, UpdateSport):
        _translate = QtCore.QCoreApplication.translate
        UpdateSport.setWindowTitle(_translate("UpdateSport", "Dialog"))
        self.lblMain.setText(_translate("UpdateSport", "Enter the name of the Sport you would like to alter below"))
        self.btnUpdateSport.setText(_translate("UpdateSport", "Update Sport"))
        self.label.setText(_translate("UpdateSport", "Enter the name that you would like it to now become below"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateSport = QtWidgets.QDialog()
    ui = Ui_UpdateSport()
    ui.setupUi(UpdateSport)
    UpdateSport.show()
    sys.exit(app.exec_())
