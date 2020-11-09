# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'displayEvents.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_displayEvents(object):
    def setupUi(self, displayEvents):
        displayEvents.setObjectName("displayEvents")
        displayEvents.resize(203, 300)
        self.tblEvents = QtWidgets.QTableWidget(displayEvents)
        self.tblEvents.setGeometry(QtCore.QRect(15, 55, 176, 231))
        self.tblEvents.setObjectName("tblEvents")
        self.tblEvents.setColumnCount(0)
        self.tblEvents.setRowCount(0)

        self.retranslateUi(displayEvents)
        QtCore.QMetaObject.connectSlotsByName(displayEvents)

    def retranslateUi(self, displayEvents):
        _translate = QtCore.QCoreApplication.translate
        displayEvents.setWindowTitle(_translate("displayEvents", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    displayEvents = QtWidgets.QDialog()
    ui = Ui_displayEvents()
    ui.setupUi(displayEvents)
    displayEvents.show()
    sys.exit(app.exec_())
