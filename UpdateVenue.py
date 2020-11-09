# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateVenue.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateVenue(object):
    def setupUi(self, UpdateVenue):
        UpdateVenue.setObjectName("UpdateVenue")
        UpdateVenue.resize(417, 195)
        self.gridLayoutWidget = QtWidgets.QWidget(UpdateVenue)
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
        self.btnUpdateVenue = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnUpdateVenue.setObjectName("btnUpdateVenue")
        self.gridLayout.addWidget(self.btnUpdateVenue, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        self.edtOldVenueName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtOldVenueName.setObjectName("edtOldVenueName")
        self.gridLayout.addWidget(self.edtOldVenueName, 2, 0, 1, 3)
        self.edtNewVenueName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtNewVenueName.setObjectName("edtNewVenueName")
        self.gridLayout.addWidget(self.edtNewVenueName, 4, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 3)

        self.retranslateUi(UpdateVenue)
        QtCore.QMetaObject.connectSlotsByName(UpdateVenue)

    def retranslateUi(self, UpdateVenue):
        _translate = QtCore.QCoreApplication.translate
        UpdateVenue.setWindowTitle(_translate("UpdateVenue", "Dialog"))
        self.lblMain.setText(_translate("UpdateVenue", "Enter the name of the Venue you would like to alter below"))
        self.btnUpdateVenue.setText(_translate("UpdateVenue", "Update Venue"))
        self.label.setText(_translate("UpdateVenue", "Enter the name that you would like it to now become below"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateVenue = QtWidgets.QDialog()
    ui = Ui_UpdateVenue()
    ui.setupUi(UpdateVenue)
    UpdateVenue.show()
    sys.exit(app.exec_())
