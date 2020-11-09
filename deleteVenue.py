# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteVenue.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteVenue(object):
    def setupUi(self, DeleteVenue):
        DeleteVenue.setObjectName("DeleteVenue")
        DeleteVenue.resize(323, 166)
        self.gridLayoutWidget = QtWidgets.QWidget(DeleteVenue)
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
        self.btnDeleteVenue = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDeleteVenue.setObjectName("btnDeleteVenue")
        self.gridLayout.addWidget(self.btnDeleteVenue, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.lblMain = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblMain.setObjectName("lblMain")
        self.gridLayout.addWidget(self.lblMain, 0, 0, 1, 3)
        self.edtVenueDelete = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtVenueDelete.setObjectName("edtVenueDelete")
        self.gridLayout.addWidget(self.edtVenueDelete, 2, 0, 1, 3)

        self.retranslateUi(DeleteVenue)
        QtCore.QMetaObject.connectSlotsByName(DeleteVenue)

    def retranslateUi(self, DeleteVenue):
        _translate = QtCore.QCoreApplication.translate
        DeleteVenue.setWindowTitle(_translate("DeleteVenue", "Dialog"))
        self.btnDeleteVenue.setText(_translate("DeleteVenue", "Delete Event"))
        self.lblMain.setText(_translate("DeleteVenue", "Enter the name of the Venue you want to delete below"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteVenue = QtWidgets.QDialog()
    ui = Ui_DeleteVenue()
    ui.setupUi(DeleteVenue)
    DeleteVenue.show()
    sys.exit(app.exec_())
