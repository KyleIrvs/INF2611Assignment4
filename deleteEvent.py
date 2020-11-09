# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteEvent.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deleteEvent(object):
    def setupUi(self, deleteEvent):
        deleteEvent.setObjectName("deleteEvent")
        deleteEvent.resize(323, 166)
        self.gridLayoutWidget = QtWidgets.QWidget(deleteEvent)
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
        self.btnDeleteEvent = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDeleteEvent.setObjectName("btnDeleteEvent")
        self.gridLayout.addWidget(self.btnDeleteEvent, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.lblMain = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblMain.setObjectName("lblMain")
        self.gridLayout.addWidget(self.lblMain, 0, 0, 1, 3)
        self.edtEventDelete = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtEventDelete.setObjectName("edtEventDelete")
        self.gridLayout.addWidget(self.edtEventDelete, 2, 0, 1, 3)

        self.retranslateUi(deleteEvent)
        QtCore.QMetaObject.connectSlotsByName(deleteEvent)

    def retranslateUi(self, deleteEvent):
        _translate = QtCore.QCoreApplication.translate
        deleteEvent.setWindowTitle(_translate("deleteEvent", "Dialog"))
        self.btnDeleteEvent.setText(_translate("deleteEvent", "Delete Event"))
        self.lblMain.setText(_translate("deleteEvent", "Enter the name of the Sport event you want to delete below"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteEvent = QtWidgets.QDialog()
    ui = Ui_deleteEvent()
    ui.setupUi(deleteEvent)
    deleteEvent.show()
    sys.exit(app.exec_())
