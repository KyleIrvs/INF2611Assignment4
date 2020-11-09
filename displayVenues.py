# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'displayVenues.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_displayVenues(object):
    def setupUi(self, displayVenues):
        displayVenues.setObjectName("displayVenues")
        displayVenues.resize(203, 300)
        self.tblVenues = QtWidgets.QTableWidget(displayVenues)
        self.tblVenues.setGeometry(QtCore.QRect(15, 55, 176, 231))
        self.tblVenues.setObjectName("tblVenues")
        self.tblVenues.setColumnCount(0)
        self.tblVenues.setRowCount(0)

        self.retranslateUi(displayVenues)
        QtCore.QMetaObject.connectSlotsByName(displayVenues)

    def retranslateUi(self, displayVenues):
        _translate = QtCore.QCoreApplication.translate
        displayVenues.setWindowTitle(_translate("displayVenues", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    displayVenues = QtWidgets.QDialog()
    ui = Ui_displayVenues()
    ui.setupUi(displayVenues)
    displayVenues.show()
    sys.exit(app.exec_())
