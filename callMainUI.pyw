from PyQt5 import QtWidgets, QtSql, QtGui
from PyQt5.QtWidgets import QMdiSubWindow, QMessageBox
from Assignment4Q2Ui import Ui_MainWindow
from defaultWindow import Ui_DefaultWindow
from addEvent import Ui_AddEvent
from addVenue import Ui_AddVenue
from UpdateVenue import Ui_UpdateVenue
from UpdateSport import Ui_UpdateSport
from deleteEvent import Ui_deleteEvent
from deleteVenue import Ui_DeleteVenue
from displayEvents import Ui_displayEvents
from displayVenues import Ui_displayVenues
import MySQLdb as mdb
import re
import sys


class mainForm(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(mainForm, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("INF 2611 Assignment 4 Kyle Irvine")
        self.defaultUi = Ui_DefaultWindow()
        self.defaultWindow = QMdiSubWindow()
        self.defaultUi.setupUi(self.defaultWindow)

        self.addEventUi = Ui_AddEvent()
        self.addEventWindow = QMdiSubWindow()
        self.addEventUi.setupUi(self.addEventWindow)
        self.addEventUi.btnAddEvent.clicked.connect(self.addEventToList)

        self.addVenueUi = Ui_AddVenue()
        self.addVenueWindow = QMdiSubWindow()
        self.addVenueUi.setupUi(self.addVenueWindow)
        self.addVenueUi.btnAddVenue.clicked.connect(self.addVenueToList)

        self.alterVenueUi = Ui_UpdateVenue()
        self.alterVenueWindow = QMdiSubWindow()
        self.alterVenueUi.setupUi(self.alterVenueWindow)
        self.alterVenueUi.btnUpdateVenue.clicked.connect(self.alterVenue)

        self.alterSportUi = Ui_UpdateSport()
        self.alterSportWindow = QMdiSubWindow()
        self.alterSportUi.setupUi(self.alterSportWindow)
        self.alterSportUi.btnUpdateSport.clicked.connect(self.alterEvent)

        self.deleteVenueUi = Ui_DeleteVenue()
        self.deleteVenueWindow = QMdiSubWindow()
        self.deleteVenueUi.setupUi(self.deleteVenueWindow)
        self.deleteVenueUi.btnDeleteVenue.clicked.connect(self.deleteVenueFromList)

        self.deleteEventUi = Ui_deleteEvent()
        self.deleteEventWindow = QMdiSubWindow()
        self.deleteEventUi.setupUi(self.deleteEventWindow)
        self.deleteEventUi.btnDeleteEvent.clicked.connect(self.deleteEventFromList)

        self.displayEventsUi = Ui_displayEvents()
        self.displayEventsWindow = QMdiSubWindow()
        self.displayEventsUi.setupUi(self.displayEventsWindow)

        self.displayVenuesUi = Ui_displayVenues()
        self.displayVenuesWindow = QMdiSubWindow()
        self.displayVenuesUi.setupUi(self.displayVenuesWindow)

        # Commented out code is the other menu items triggered events and
        # what their respective functions would be

        self.actionAdd_New_Event_Record.triggered.connect(self.addEvent)
        self.actionEdit_Existing_Event_Record.triggered.connect(self.editEvents)
        self.actionDelete_Existing_Event_Record.triggered.connect(self.deleteEvent)
        self.actionShow_File_Content.triggered.connect(self.showEvents)
        self.actionAdd_New_Venue_Record.triggered.connect(self.addVenue)
        self.actionEdit_Existing_Venue_Record.triggered.connect(self.editVenues)
        self.actionDelete_Existing_Venue_Record.triggered.connect(self.deleteVenue)
        self.actionShow_vFile_content.triggered.connect(self.showVenues)

        self.defaultWindow.setWindowTitle("Default Window")
        self.mdi.addSubWindow(self.defaultWindow)
        self.defaultWindow.show()

        self.connectToDB()

        self.errMessageCheck = re.compile("Duplicate entry")

        # Resizes all Ui to ensure that everything is fitting properly and my
        # student number  is always on the bottom right of the UI
        self.mdi.resize(self.defaultWindow.width(), self.defaultWindow.height())
        self.resize(self.defaultWindow.width() + 10, self.defaultWindow.height()+100)
        self.verticalLayoutWidget.move(self.width() - 225, self.height() - 80)

    def connectToDB(self):
        try:
            #connects to local DB using the following values
            self.dataB = mdb.connect('127.0.0.1', 'root', '', 'olympics')
            self.cur = self.dataB.cursor()
        except mdb.Error as e:
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            sys.exit(1)

    def addEvent(self):

        self.mdi.closeAllSubWindows()
        self.resize(330, 200)
        self.addEventWindow.setWindowTitle("Add New Event")
        self.mdi.addSubWindow(self.addEventWindow)
        self.addEventWindow.show()

        # Resizes all Ui to ensure that everything is fitting properly and my
        # student number  is always on the bottom right of the UI
        self.mdi.resize(self.addEventWindow.width(), self.addEventWindow.height())
        self.resize(self.addEventWindow.width() + 10, self.addEventWindow.height() + 100)
        self.verticalLayoutWidget.move(self.width() - 225, self.height() - 80)

        self.mdi.tileSubWindows()

    def addEventToList(self):

        # Retrieves the value from the lineEdit of the name of the new Event to be added
        newEventName = self.addEventUi.edtEvent.text()
        if newEventName == "":
            QMessageBox.warning(self, 'Missing Info', 'Please enter a Sport Name')
        else:
            self.addEventUi.edtEvent.clear()
            self.addEventUi.edtEvent.setFocus()
            #Will attempt to insert value, if it has any error it will return the Error
            # if the error is a duplicate entry, it will say so
            try:
                self.cur.execute("INSERT INTO `olympics`.`olympic sports` (`SportName`) VALUES (%s)",[newEventName])
                self.dataB.commit()
                QMessageBox.information(self, 'Entry Succesful', newEventName + ' succesfully added to table!')
            except mdb.Error as e:
                errMsg = str(e)
                #Searches to see if the words "DuplicateEntry" are in the error errMessageCheck
                #To say that is the error
                if self.errMessageCheck.search(errMsg):
                    QMessageBox.warning(self, 'Duplicate Entry', 'The Entered value already exists in that table')


    def addVenue(self):

        self.mdi.closeAllSubWindows()
        self.resize(330, 200)
        self.addVenueWindow.setWindowTitle("Add New Venue")
        self.mdi.addSubWindow(self.addVenueWindow)
        self.addVenueWindow.show()
        self.mdi.tileSubWindows()

        # Resizes all Ui to ensure that everything is fitting properly and my
        # student number  is always on the bottom right of the UI
        self.mdi.resize(self.addVenueWindow.width(), self.addVenueWindow.height())
        self.resize(self.addVenueWindow.width() + 10, self.addVenueWindow.height()+100)
        self.verticalLayoutWidget.move(self.width() - 225, self.height() - 80)

    def addVenueToList(self):

        # Retrieves the value from the lineEdit of the name of the new Venue to be added
        newVenueName = self.addVenueUi.edtVenue.text()
        if newVenueName == "":
            QMessageBox.warning(self, 'Missing Info', 'Please enter a Venue Name')
        else:
            self.addVenueUi.edtVenue.clear()
            self.addVenueUi.edtVenue.setFocus()
            #Will attempt to insert value, if it has any error it will return the Error
            # if the error is a duplicate entry, it will say so
            try:
                self.cur.execute("INSERT INTO `olympics`.`olympic venues` (`VenueName`) VALUES (%s)",[newVenueName])
                self.dataB.commit()
                QMessageBox.information(self, 'Entry Succesful', newVenueName + ' succesfully added to table!')
            except mdb.Error as e:
                errMsg = str(e)
                #Searches to see if the words "DuplicateEntry" are in the error errMessageCheck
                #To say that is the error
                if self.errMessageCheck.search(errMsg):
                    QMessageBox.warning(self, 'Duplicate Entry', 'The Entered value already exists in that table')

    def editVenues(self):
        self.mdi.closeAllSubWindows()
        self.alterVenueWindow.setWindowTitle("Update Venue Entry")
        self.mdi.addSubWindow(self.alterVenueWindow)
        self.alterVenueWindow.show()
        self.mdi.tileSubWindows()

        print("Hello")

        # Resizes all Ui to ensure that everything is fitting properly and my
        # student number  is always on the bottom right of the UI
        self.mdi.resize(self.alterVenueWindow.width() + 60, self.alterVenueWindow.height() + 100)
        self.resize(self.alterVenueWindow.width() + 10, self.alterVenueWindow.height()+100)
        self.verticalLayoutWidget.move(self.width() - 225, self.height() - 80)

    def alterVenue(self):
        #Gets the name of the venue to be changed as well as the new name from the respective line edits
        oldVenueName = self.alterVenueUi.edtOldVenueName.text()
        newVenueName = self.alterVenueUi.edtNewVenueName.text()

        if oldVenueName == "" or newVenueName == "":
            QMessageBox.warning(self, "Missing required information", "Please enter all information as it is all required")
        else:
            self.alterVenueUi.edtOldVenueName.clear()
            self.alterVenueUi.edtNewVenueName.clear()
            # Will attempt to change the name of the specified venue to the new name and will not if there is any sort of error
            try:
                self.cur.execute("UPDATE `olympics`.`olympic venues` SET `VenueName`= %s WHERE `VenueName`=%s ", ([newVenueName,oldVenueName]))
                self.dataB.commit()
            except mdb.Error as e:
                errMsg = str(e)
                print(errMsg)

    def editEvents(self):
        self.mdi.closeAllSubWindows()
        self.alterSportWindow.setWindowTitle("Update Sport Entry")
        self.mdi.addSubWindow(self.alterSportWindow)
        self.alterSportWindow.show()
        self.mdi.tileSubWindows()
        # Resizes all Ui to ensure that everything is fitting properly and my
        # student number  is always on the bottom right of the UI
        self.mdi.resize(self.alterSportWindow.width() + 60, self.alterSportWindow.height() + 100)
        self.resize(self.alterSportWindow.width() + 10, self.alterSportWindow.height()+100)
        self.verticalLayoutWidget.move(self.width() - 225, self.height() - 80)

    def alterEvent(self):
        #Gets the name of the venue to be changed as well as the new name from the respective line edits
        oldSportName = self.alterSportUi.edtOldSportName.text()
        newSportName = self.alterSportUi.edtNewSportName.text()

        if oldSportName == "" or newSportName == "":
            QMessageBox.warning(self, "Missing Required information", "Please enter all information as it is all required")
        else:
            self.alterSportUi.edtOldSportName.clear()
            self.alterSportUi.edtNewSportName.clear()
            # Will attempt to change the name of the specified event to the new name and will not if there is any sort of error
            try:
                self.cur.execute("UPDATE `olympics`.`olympic sports` SET `SportName`= %s WHERE `SportName`=%s ", ([newSportName, oldSportName]))
                self.dataB.commit()
            except mdb.Error as e:
                errMsg = str(e)
                print(errMsg)

    def deleteVenue(self):
        self.mdi.closeAllSubWindows()
        self.resize(330, 200)
        self.deleteVenueWindow.setWindowTitle("Delete Venue Entry")
        self.mdi.addSubWindow(self.deleteVenueWindow)
        self.deleteVenueWindow.show()

        # Resizes all Ui to ensure that everything is fitting properly and my
        # student number  is always on the bottom right of the UI
        self.mdi.resize(self.deleteVenueWindow.width() , self.deleteVenueWindow.height())
        self.resize(self.deleteVenueWindow.width() + 10, self.deleteVenueWindow.height()+100)
        self.verticalLayoutWidget.move(self.width() - 225, self.height() - 80)
        self.mdi.tileSubWindows()

    def deleteVenueFromList(self):

        venueToDelete = self.deleteVenueUi.edtVenueDelete.text()

        if venueToDelete == "":
            QMessageBox.warning(self, "Please enter Venue name" , "Please enter a Venue to delete")
        else:
            self.deleteVenueUi.edtVenueDelete.clear()
            try:
                self.cur.execute("DELETE FROM `olympics`.`olympic venues` WHERE `VenueName`= %s ", [venueToDelete])
                self.dataB.commit()
            except mdb.Error as e:
                errMsg = str(e)
                print(errMsg)

    def deleteEvent(self):
        self.mdi.closeAllSubWindows()
        self.resize(330, 200)
        self.deleteEventWindow.setWindowTitle("Delete Sport Entry")
        self.mdi.addSubWindow(self.deleteEventWindow)
        self.deleteEventWindow.show()

        # Resizes all Ui to ensure that everything is fitting properly and my
        # student number  is always on the bottom right of the UI
        self.mdi.resize(self.deleteEventWindow.width() , self.deleteEventWindow.height())
        self.resize(self.deleteEventWindow.width() + 10, self.deleteEventWindow.height()+100)
        self.verticalLayoutWidget.move(self.width() - 225, self.height() - 80)
        self.mdi.tileSubWindows()

    def deleteEventFromList(self):

        eventToDelete = self.deleteEventUi.edtEventDelete.text()

        if eventToDelete == "":
            QMessageBox.warning(self, "Please enter event name" , "Please enter an event name to delete")
        else:
            self.deleteEventUi.edtEventDelete.clear()
            try:
                self.cur.execute("DELETE FROM `olympics`.`olympic sports` WHERE `SportName`= %s ", [eventToDelete])
                self.dataB.commit()
            except mdb.Error as e:
                errMsg = str(e)
                print(errMsg)

    def showEvents(self):
        self.mdi.closeAllSubWindows()
        self.resize(330, 200)
        self.displayEventsWindow.setWindowTitle("All current Events")
        self.mdi.addSubWindow(self.displayEventsWindow)
        self.displayEventsWindow.show()

        # Resizes all Ui to ensure that everything is fitting properly and my
        # student number  is always on the bottom right of the UI
        self.mdi.resize(self.displayEventsWindow.width() , self.displayEventsWindow.height())
        self.resize(self.displayEventsWindow.width() + 10, self.displayEventsWindow.height()+100)
        self.verticalLayoutWidget.move(self.width() - 210, self.height() - 80)
        self.mdi.tileSubWindows()

        # Stores column count for table into variable to set the row count and
        # column count
        eventCounter = self.cur.execute("SELECT * FROM `olympics`.`olympic sports`")
        self.displayEventsUi.tblEvents.setRowCount(eventCounter)
        self.displayEventsUi.tblEvents.setColumnCount(1)
        self.displayEventsUi.tblEvents.setHorizontalHeaderLabels(['Events'])

        # adds each item from the events table in the database into the
        # table on the UI
        for i in range(eventCounter):
            itemFromEvents = self.convertToString(self.cur.fetchone())
            # sets the item at i,0  to whatever is retrieved from the DB
            self.displayEventsUi.tblEvents.setItem(i, 0, QtWidgets.QTableWidgetItem(itemFromEvents))

        eventsHeader = self.displayEventsUi.tblEvents.horizontalHeader()
        eventsHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

    def showVenues(self):

        self.mdi.closeAllSubWindows()
        self.resize(330, 200)
        self.displayVenuesWindow.setWindowTitle("All current Venues")
        self.mdi.addSubWindow(self.displayVenuesWindow)
        self.displayVenuesWindow.show()

        # Resizes all Ui to ensure that everything is fitting properly and my
        # student number  is always on the bottom right of the UI
        self.mdi.resize(self.displayVenuesWindow.width() , self.displayVenuesWindow.height())
        self.resize(self.displayVenuesWindow.width() + 10, self.displayVenuesWindow.height()+100)
        self.verticalLayoutWidget.move(self.width() - 210, self.height() - 80)
        self.mdi.tileSubWindows()

        # Stores column count for table into variable to set the row count and
        # column count
        venueCounter = self.cur.execute("SELECT * FROM `olympics`.`olympic venues`")
        self.displayVenuesUi.tblVenues.setRowCount(venueCounter)
        self.displayVenuesUi.tblVenues.setColumnCount(1)
        self.displayVenuesUi.tblVenues.setHorizontalHeaderLabels(['Venues'])

        # adds each item from the events table in the database into the
        # table on the UI
        for i in range(venueCounter):
            itemFromVenues = self.convertToString(self.cur.fetchone())
            # sets the item at i,0  to whatever is retrieved from the DB
            self.displayVenuesUi.tblVenues.setItem(i, 0, QtWidgets.QTableWidgetItem(itemFromVenues))

        venuesHeader = self.displayVenuesUi.tblVenues.horizontalHeader()
        venuesHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

    def convertToString(self,tup):
        # Converts the tuple recieved from the Db into a string for the table
        str = "".join(tup)
        return str

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = mainForm()
    application.show()
    sys.exit(app.exec_())
