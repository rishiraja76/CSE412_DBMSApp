import sys

from PyQt5 import QtCore

import backend

from PyQt5.QtWidgets import *

widgets = {"button1": [],
           "backbutton": [],
           "ticketbut": [],
           "flightbut": [],
           "airlinerbut": [],
           "userTable": []
           }

user_data = {'First Name': backend.firstname,
             'Last Name': backend.lastname,
             'User Name': backend.username,
             'Pass Word': backend.password,
             'Email': backend.email,
             'Address': backend.address,
             'Phone Number': backend.phonenumber,
             'Credit Card Number': backend.creditcardnumber_u}

ticket_data = {'Ticket Status': backend.ticketstatus,
               'Ticket ID': backend.ticketid_tr,
               'Price': backend.price,
               'Credit Card Number': backend.creditcardnumber_tr}

flight_data = {'Flight Status': backend.flightstatus,
               'Flight Number': backend.flightnumber_f,
               'Arrival Time': backend.arrivaltime,
               'Departure Time': backend.departuretime,
               'Departure Location': backend.departurelocation,
               'Destination': backend.destination,
               'Ticket ID': backend.ticketid_f}

airliner_data = {'Plane Type': backend.planetype,
                 'Airliner Name': backend.airlinername,
                 'Flight Number': backend.flightnumber_a}


class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)


def homepage():
    # user information button widget
    button1 = QPushButton("User Information")
    button1.setFixedSize(QtCore.QSize(120, 30))
    widgets["button1"].append(button1)
    button1.clicked.connect(user_info)
    grid.addWidget(widgets["button1"][-1], 0, 0)

    # ticket information button
    ticketbut = QPushButton("Ticket Information")
    ticketbut.setFixedSize(QtCore.QSize(120, 30))
    widgets["ticketbut"].append(ticketbut)
    ticketbut.clicked.connect(ticket_info)
    grid.addWidget(widgets["ticketbut"][-1], 1, 0)

    flightbut = QPushButton("Flight Information")
    flightbut.setFixedSize(QtCore.QSize(120, 30))
    widgets["flightbut"].append(flightbut)
    flightbut.clicked.connect(flight_info)
    grid.addWidget(widgets["flightbut"][-1], 2, 0)

    airlinerbut = QPushButton("Airliner Information")
    airlinerbut.setFixedSize(QtCore.QSize(120, 30))
    widgets["airlinerbut"].append(airlinerbut)
    airlinerbut.clicked.connect(airliner_info)
    grid.addWidget(widgets["airlinerbut"][-1], 3, 0)


def user_info():
    clear_widgets()

    userTable = TableView(user_data, len(backend.firstname), len(user_data))
    backbutton = QPushButton("Back")
    backbutton.setFixedSize(QtCore.QSize(120, 30))
    grid.addWidget(userTable, 0, 0)
    grid.addWidget(backbutton, 1, 0)

    widgets["backbutton"].append(backbutton)
    widgets["userTable"].append(userTable)
    userTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    backbutton.clicked.connect(show_homepage)


def ticket_info():
    clear_widgets()

    userTable = TableView(ticket_data, len(backend.ticketstatus), len(ticket_data))
    backbutton = QPushButton("Back")
    backbutton.setFixedSize(QtCore.QSize(120, 30))
    grid.addWidget(userTable, 0, 0)
    grid.addWidget(backbutton, 1, 0)

    widgets["backbutton"].append(backbutton)
    widgets["userTable"].append(userTable)
    userTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    backbutton.clicked.connect(show_homepage)


def flight_info():
    clear_widgets()

    userTable = TableView(flight_data, len(backend.flightstatus), len(flight_data))
    backbutton = QPushButton("Back")
    backbutton.setFixedSize(QtCore.QSize(120, 30))
    grid.addWidget(userTable, 0, 0)
    grid.addWidget(backbutton, 1, 0)

    widgets["backbutton"].append(backbutton)
    widgets["userTable"].append(userTable)
    userTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    backbutton.clicked.connect(show_homepage)


def airliner_info():
    clear_widgets()

    userTable = TableView(airliner_data, len(backend.planetype), len(airliner_data))
    backbutton = QPushButton("Back")
    backbutton.setFixedSize(QtCore.QSize(120, 30))

    grid.addWidget(userTable, 0, 0)
    grid.addWidget(backbutton, 1, 0)

    widgets["backbutton"].append(backbutton)
    widgets["userTable"].append(userTable)
    userTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    backbutton.clicked.connect(show_homepage)


def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def show_homepage():
    clear_widgets()
    homepage()


def next_tab():
    clear_widgets()
    user_info()


if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Flight Information")
    window.setFixedSize(1200, 200)

    grid = QGridLayout()
    homepage()

    window.setLayout(grid)

    window.show()

    sys.exit(app.exec_())
