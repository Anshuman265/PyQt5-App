from email.charset import QP
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from re import sub
import re
import sys
from tkinter import Button
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QMessageBox,
                             QWidget, QFileDialog, QGridLayout, QTextEdit, QComboBox, QCalendarWidget, QSizePolicy)

widgets = {
    "logo": [],
    "submit_button": [],
    "main_heading": [],
    "student_name": [],
    "student_name_label": [],
}

"""


# Student Name
student_name_label = QLabel(
    "Student's Name")
student_name = QTextEdit(
    lineWrapMode=QTextEdit.FixedColumnWidth,
    lineWrapColumnOrWidth=50,
    placeholderText="Enter Student's Name",
    readOnly=False,
)
# button widget
submit_button = QPushButton("Submit", clicked=lambda: press_it())
submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
submit_button.setStyleSheet("*{border-radius:15px;" +
                            "border:4px solid '#A51417';" +
                            "font-size:35px;" +
                            "color: '#A51417';" +
                            "padding: 25px 0;" +
                            "margin: 100px 200px;}" +
                            "*:hover{background: '#A51417';color: '#FFFFFF'; }"
                            )
widgets["logo"].append(logo)
widgets["submit_button"].append(submit_button)
widgets["student_name"].append(student_name)
widgets["main_heading"].append(heading)
widgets["student_name_label"].append(student_name_label)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle(
    "Financial Support For Attending International Conference")
window.setFixedWidth(1000)
window.setStyleSheet("background: #FFFFFF;")
window.setWindowIcon(QtGui.QIcon('IIT-Bombay.png'))

grid = QGridLayout()


def frame1():


    def press_it():
        print(student_name.toPlainText())
        student_name.setPlainText("")

    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["main_heading"][-1], 0, 1)
    grid.addWidget(widgets["student_name_label"][-1], 1, 0)
    grid.addWidget(widgets["student_name"][-1], 1, 1)
    grid.addWidget(widgets["submit_button"][-1], 2, 0, 1, 2)


frame1()
window.setLayout(grid)
window.show()

sys.exit(app.exec())
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "Financial Support For Attending International Conference")
        self.setWindowIcon(QtGui.QIcon('window_icon_iitb.png'))
        # Creating a grid layout instance
        layout = QGridLayout()
        # layout.setRowStretch(self)
        # display logo
        image = QPixmap("IIT-Bombay.png")
        pixmap2 = image.scaledToWidth(150)
        self.logo = QLabel()
        self.logo.setPixmap(pixmap2)
        self.logo.resize(200, 200)
        self.logo.setAlignment(QtCore.Qt.AlignLeft)
        self.logo.setStyleSheet(
            "margin-top: 0px;")
        # self.logo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Main heading
        self.heading = QLabel(
            "Financial Support For Attending International Conference")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setFont(QFont('Arial', 15))
        self.heading.setStyleSheet("margin-top: 0px;")
        # Student Name
        self.student_name_label = QLabel(
            "Student's Name")
        self.student_name_label.resize(200, 10)
        self.student_name = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Enter Student's Name",
            readOnly=False,
        )
        self.student_name.resize(200, 10)
        self.roll_number_label = QLabel(
            "Roll Number")
        self.roll_number = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Enter Student's Roll Number",
            readOnly=False,
        )
        self.category_dropdown_label = QLabel(
            "Category")
        self.category_dropdown = QComboBox()
        self.category_dropdown.addItems(
            ["TA", "TAP", "MONASH", "RA", "CT", "SW", "SF"])
        self.department_dropdown_label = QLabel(
            "Department")
        self.department_dropdown = QComboBox()
        self.department_dropdown.addItems(
            ["CHEMISTRY", "MATHEMATICS", "PHYSICS"])
        self.guides_number_label = QLabel(
            "Guide's Name")
        self.guides_number = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Enter Student's guide's Name",
            readOnly=False,
        )
        self.date_of_application_label = QLabel("Date Of Application")
        self.date_of_application = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Date Of Application",
            readOnly=False,
        )
        """
        self.date_of_application = QCalendarWidget()
        self.date_of_application.setGeometry(50, 50, 400, 250)
        # value = self.date_of_application.selectedDate().toPyDate()
        # print(f'The date selected from the calendar is {value}')
        """
        self.days_available_label = QLabel(
            "Days available for processing of Application for ITCommittee")
        self.days_available = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Days available for processing of Application for ITCommittee",
            readOnly=False,
        )
        self.name_of_conference_label = QLabel(
            "Name of Conference")
        self.name_of_conference = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Name of Conference",
            readOnly=False,
        )
        self.place_of_conference_label = QLabel(
            "Place of Conference")
        self.place_of_conference = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Place of Conference",
            readOnly=False,
        )
        self.region_dropdown_label = QLabel(
            "Region")
        self.region_dropdown = QComboBox()
        self.region_dropdown.addItems(
            ["Group A", "Group B", "Group C"])
        self.from_date_label = QLabel(
            "From Date")
        self.from_date = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="From Date",
            readOnly=False,
        )
        self.to_date_label = QLabel(
            "To Date")
        self.to_date = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="To Date",
            readOnly=False,
        )
        self.amount_eligible_label = QLabel(
            "Amount Eligible")
        self.amount_eligible = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Amount Eligible",
            readOnly=False,
        )
        self.request_for_label = QLabel(
            "Request For")
        self.request_for = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Request For",
            readOnly=False,
        )
        self.amount_requested_label = QLabel(
            "Amount Requested")
        self.amount_requested = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Amount Requested",
            readOnly=False,
        )
        self.km_clearance_label = QLabel(
            "KM Clearance")
        self.km_clearence = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="KM Clearance",
            readOnly=False,
        )
        self.ifc_clearance_label = QLabel(
            "IFC Clearance")
        self.ifc_clearence = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="IFC Clearance",
            readOnly=False,
        )
        self.reason_or_remark_label = QLabel(
            "Reason or Remark")
        self.reason_or_remark = QTextEdit(
            lineWrapMode=QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Reason or Remark",
            readOnly=False,
        )

        # Adding the submit button finally
        self.submit_button = QPushButton("Submit", clicked=lambda: press_it())
        self.submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_button.setStyleSheet("*{border-radius:10px;" +
                                         "border:2px solid '#32CD32';" +
                                         "font-size:35px;" +
                                         "padding: 5px;" +
                                         "color: '#32CD32';}" +
                                         "*:hover{background: '#32CD32';color: '#FFFFFF'; }"
                                         )
        self.qbtn = QPushButton(
            "Quit", clicked=lambda: closeEvent())
        self.qbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.qbtn.setStyleSheet("*{border-radius:10px;" +
                                "border:2px solid '#FF0000';" +
                                "font-size:35px;" +
                                "padding: 5px;" +
                                "width: 50%;" +
                                "padding: 50px;"
                                "color: '#FF0000';}" +
                                "*:hover{background: '#FF0000';color: '#FFFFFF'; }"
                                )

        def closeEvent():
            close = QMessageBox.question(self,
                                         "Quit?",
                                         "Are you sure want to quit?",
                                         QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                sys.exit()
            else:
                pass
        # Adding the widgets to the layout
        layout.addWidget(self.logo, 0, 0)
        layout.addWidget(self.heading, 0, 1)
        layout.addWidget(self.student_name_label, 1, 0)
        layout.addWidget(self.student_name, 1, 1)
        layout.addWidget(self.roll_number_label, 2, 0)
        layout.addWidget(self.roll_number, 2, 1)
        layout.addWidget(self.category_dropdown_label, 3, 0)
        layout.addWidget(self.category_dropdown, 3, 1)
        layout.addWidget(self.department_dropdown_label, 4, 0)
        layout.addWidget(self.department_dropdown, 4, 1)
        layout.addWidget(self.date_of_application_label, 5, 0)
        layout.addWidget(self.date_of_application, 5, 1)
        layout.addWidget(self.days_available_label, 6, 0)
        layout.addWidget(self.days_available, 6, 1)
        layout.addWidget(self.name_of_conference_label, 7, 0)
        layout.addWidget(self.name_of_conference, 7, 1)
        layout.addWidget(self.place_of_conference_label, 8, 0)
        layout.addWidget(self.place_of_conference, 8, 1)
        layout.addWidget(self.region_dropdown_label, 9, 0)
        layout.addWidget(self.region_dropdown, 9, 1)
        layout.addWidget(self.from_date_label, 10, 0)
        layout.addWidget(self.from_date, 10, 1)
        layout.addWidget(self.to_date_label, 11, 0)
        layout.addWidget(self.to_date, 11, 1)
        layout.addWidget(self.amount_eligible_label, 12, 0)
        layout.addWidget(self.amount_eligible, 12, 1)
        layout.addWidget(self.request_for_label, 13, 0)
        layout.addWidget(self.request_for, 13, 1)
        layout.addWidget(self.amount_requested_label, 14, 0)
        layout.addWidget(self.amount_requested, 14, 1)
        layout.addWidget(self.km_clearance_label, 15, 0)
        layout.addWidget(self.km_clearence, 15, 1)
        layout.addWidget(self.ifc_clearance_label, 16, 0)
        layout.addWidget(self.ifc_clearence, 16, 1)
        layout.addWidget(self.reason_or_remark_label, 17, 0)
        layout.addWidget(self.reason_or_remark, 17, 1)
        layout.addWidget(self.submit_button, 18, 0)
        layout.addWidget(self.qbtn, 18, 1)
        # Set the layout on the application's window
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
