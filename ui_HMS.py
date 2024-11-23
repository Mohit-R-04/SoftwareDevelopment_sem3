# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HMS.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import HMS_resources_rc
import HMS_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(984, 730)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-color: rgb(233, 224, 162);\n"
"color:black")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.maintopholder = QHBoxLayout()
        self.maintopholder.setObjectName(u"maintopholder")
        self.expand_menu = QPushButton(self.main)
        self.expand_menu.setObjectName(u"expand_menu")
        self.expand_menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.expand_menu.setMouseTracking(True)
        self.expand_menu.setStyleSheet(u"QPushButton {\n"
"    background-color: light yellow;\n"
"    border: none;\n"
"    padding: 10px 15px; /* Padding for the button */\n"
"    text-align: center;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	    background-color: rgb(226, 190, 134);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/images/stock_png/icons8-menu-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.expand_menu.setIcon(icon)
        self.expand_menu.setIconSize(QSize(30, 30))
        self.expand_menu.setCheckable(True)
        self.expand_menu.setChecked(False)
        self.expand_menu.setAutoRepeat(False)
        self.expand_menu.setAutoExclusive(False)
        self.expand_menu.setAutoDefault(True)

        self.maintopholder.addWidget(self.expand_menu)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.maintopholder.addItem(self.horizontalSpacer_3)

        self.main_heading = QLabel(self.main)
        self.main_heading.setObjectName(u"main_heading")

        self.maintopholder.addWidget(self.main_heading)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.maintopholder.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.maintopholder)

        self.line = QFrame(self.main)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.managepatientsrecords = QStackedWidget(self.main)
        self.managepatientsrecords.setObjectName(u"managepatientsrecords")
        self.managepatientsrecords.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.managepatientsrecords.setLineWidth(0)
        self.pg1 = QWidget()
        self.pg1.setObjectName(u"pg1")
        self.verticalLayout_6 = QVBoxLayout(self.pg1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.doctorsavailablity_label = QLabel(self.pg1)
        self.doctorsavailablity_label.setObjectName(u"doctorsavailablity_label")
        self.doctorsavailablity_label.setStyleSheet(u"padding:5px;\n"
"background-color: rgb(227, 172, 233);\n"
"border-radius:15px\n"
"")

        self.verticalLayout_6.addWidget(self.doctorsavailablity_label)

        self.doctorsavailablity_tab = QTabWidget(self.pg1)
        self.doctorsavailablity_tab.setObjectName(u"doctorsavailablity_tab")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_8 = QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.binsearchholder_2 = QHBoxLayout()
        self.binsearchholder_2.setSpacing(0)
        self.binsearchholder_2.setObjectName(u"binsearchholder_2")
        self.doctorsavailablity_tabnotavailable_searchentry = QLineEdit(self.tab_5)
        self.doctorsavailablity_tabnotavailable_searchentry.setObjectName(u"doctorsavailablity_tabnotavailable_searchentry")
        self.doctorsavailablity_tabnotavailable_searchentry.setMinimumSize(QSize(450, 35))
        self.doctorsavailablity_tabnotavailable_searchentry.setStyleSheet(u"background-color: rgb(209, 241, 239);\n"
"border-radius: 7px")
        self.doctorsavailablity_tabnotavailable_searchentry.setClearButtonEnabled(True)

        self.binsearchholder_2.addWidget(self.doctorsavailablity_tabnotavailable_searchentry)

        self.doctorsavailablity_tabnotavailable_searchbutton = QPushButton(self.tab_5)
        self.doctorsavailablity_tabnotavailable_searchbutton.setObjectName(u"doctorsavailablity_tabnotavailable_searchbutton")
        self.doctorsavailablity_tabnotavailable_searchbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doctorsavailablity_tabnotavailable_searchbutton.setStyleSheet(u"QPushButton {\n"
"    background-color: lightblue; /* light blue background */\n"
"    color: black; /* black text */\n"
"    border: none;\n"
"    padding: 10px 20px; /* Padding for the button */\n"
"    font-size: 16px; /* Font size */\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the button appearance on hover */\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 173, 229); /* Darker light blue on hover */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(186, 235, 207):\n"
"}")
        self.doctorsavailablity_tabnotavailable_searchbutton.setCheckable(True)
        self.doctorsavailablity_tabnotavailable_searchbutton.setChecked(False)
        self.doctorsavailablity_tabnotavailable_searchbutton.setAutoExclusive(True)

        self.binsearchholder_2.addWidget(self.doctorsavailablity_tabnotavailable_searchbutton)


        self.verticalLayout_8.addLayout(self.binsearchholder_2)

        self.doctorsavailablity_tabnotavailable_view = QTableWidget(self.tab_5)
        self.doctorsavailablity_tabnotavailable_view.setObjectName(u"doctorsavailablity_tabnotavailable_view")
        self.doctorsavailablity_tabnotavailable_view.setStyleSheet(u"background-color: rgb(234, 199, 202);\n"
"border-radius: 10px;gg")

        self.verticalLayout_8.addWidget(self.doctorsavailablity_tabnotavailable_view)

        self.frame_3 = QFrame(self.tab_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_11 = QSpacerItem(183, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)

        self.doctorsavailablity_tabnotavailable_markavailablebutton = QPushButton(self.frame_3)
        self.doctorsavailablity_tabnotavailable_markavailablebutton.setObjectName(u"doctorsavailablity_tabnotavailable_markavailablebutton")
        self.doctorsavailablity_tabnotavailable_markavailablebutton.setMinimumSize(QSize(150, 50))
        self.doctorsavailablity_tabnotavailable_markavailablebutton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(155, 155, 229);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.doctorsavailablity_tabnotavailable_markavailablebutton.setCheckable(True)
        self.doctorsavailablity_tabnotavailable_markavailablebutton.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.doctorsavailablity_tabnotavailable_markavailablebutton)

        self.horizontalSpacer_12 = QSpacerItem(183, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.doctorsavailablity_tab.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_7 = QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.binsearchholder = QHBoxLayout()
        self.binsearchholder.setSpacing(0)
        self.binsearchholder.setObjectName(u"binsearchholder")
        self.doctorsavailablity_tabavailable_searchentry = QLineEdit(self.tab_4)
        self.doctorsavailablity_tabavailable_searchentry.setObjectName(u"doctorsavailablity_tabavailable_searchentry")
        self.doctorsavailablity_tabavailable_searchentry.setMinimumSize(QSize(450, 35))
        self.doctorsavailablity_tabavailable_searchentry.setStyleSheet(u"background-color: rgb(209, 241, 239);\n"
"border-radius: 7px")
        self.doctorsavailablity_tabavailable_searchentry.setClearButtonEnabled(True)

        self.binsearchholder.addWidget(self.doctorsavailablity_tabavailable_searchentry)

        self.doctorsavailablity_tabavailable_searchbutton = QPushButton(self.tab_4)
        self.doctorsavailablity_tabavailable_searchbutton.setObjectName(u"doctorsavailablity_tabavailable_searchbutton")
        self.doctorsavailablity_tabavailable_searchbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doctorsavailablity_tabavailable_searchbutton.setStyleSheet(u"QPushButton {\n"
"    background-color: skyblue; /* light blue background */\n"
"    color: black; /* black text */\n"
"    border: none;\n"
"    padding: 10px 20px; /* Padding for the button */\n"
"    font-size: 16px; /* Font size */\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the button appearance on hover */\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 168, 229); /* Darker light blue on hover */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(186, 235, 207):\n"
"}")
        self.doctorsavailablity_tabavailable_searchbutton.setCheckable(True)
        self.doctorsavailablity_tabavailable_searchbutton.setChecked(False)
        self.doctorsavailablity_tabavailable_searchbutton.setAutoExclusive(True)

        self.binsearchholder.addWidget(self.doctorsavailablity_tabavailable_searchbutton)


        self.verticalLayout_7.addLayout(self.binsearchholder)

        self.doctorsavailablity_tabavailable_view = QTableWidget(self.tab_4)
        self.doctorsavailablity_tabavailable_view.setObjectName(u"doctorsavailablity_tabavailable_view")
        self.doctorsavailablity_tabavailable_view.setStyleSheet(u"background-color: rgb(204, 199, 202);\n"
"border-radius: 10px;gg")

        self.verticalLayout_7.addWidget(self.doctorsavailablity_tabavailable_view)

        self.frame_2 = QFrame(self.tab_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_10 = QSpacerItem(143, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.doctorsavailablity_tabavailable_marknotavailablebutton = QPushButton(self.frame_2)
        self.doctorsavailablity_tabavailable_marknotavailablebutton.setObjectName(u"doctorsavailablity_tabavailable_marknotavailablebutton")
        self.doctorsavailablity_tabavailable_marknotavailablebutton.setMinimumSize(QSize(150, 50))
        self.doctorsavailablity_tabavailable_marknotavailablebutton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(155, 125, 229);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.doctorsavailablity_tabavailable_marknotavailablebutton.setCheckable(True)
        self.doctorsavailablity_tabavailable_marknotavailablebutton.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.doctorsavailablity_tabavailable_marknotavailablebutton)

        self.horizontalSpacer_9 = QSpacerItem(144, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.doctorsavailablity_tab.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.binsearchholder_4 = QHBoxLayout()
        self.binsearchholder_4.setSpacing(0)
        self.binsearchholder_4.setObjectName(u"binsearchholder_4")
        self.doctorsavailablity_tabworking_searchentry = QLineEdit(self.tab_2)
        self.doctorsavailablity_tabworking_searchentry.setObjectName(u"doctorsavailablity_tabworking_searchentry")
        self.doctorsavailablity_tabworking_searchentry.setMinimumSize(QSize(450, 35))
        self.doctorsavailablity_tabworking_searchentry.setStyleSheet(u"background-color: rgb(209, 241, 239);\n"
"border-radius: 7px")
        self.doctorsavailablity_tabworking_searchentry.setClearButtonEnabled(True)

        self.binsearchholder_4.addWidget(self.doctorsavailablity_tabworking_searchentry)

        self.doctorsavailablity_tabworking_searchbutton = QPushButton(self.tab_2)
        self.doctorsavailablity_tabworking_searchbutton.setObjectName(u"doctorsavailablity_tabworking_searchbutton")
        self.doctorsavailablity_tabworking_searchbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doctorsavailablity_tabworking_searchbutton.setStyleSheet(u"QPushButton {\n"
"    background-color: lightblue; /* light blue background */\n"
"    color: black; /* black text */\n"
"    border: none;\n"
"    padding: 10px 20px; /* Padding for the button */\n"
"    font-size: 16px; /* Font size */\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the button appearance on hover */\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 173, 229); /* Darker light blue on hover */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(186, 235, 207):\n"
"}")
        self.doctorsavailablity_tabworking_searchbutton.setCheckable(True)
        self.doctorsavailablity_tabworking_searchbutton.setChecked(False)
        self.doctorsavailablity_tabworking_searchbutton.setAutoExclusive(True)

        self.binsearchholder_4.addWidget(self.doctorsavailablity_tabworking_searchbutton)


        self.verticalLayout_3.addLayout(self.binsearchholder_4)

        self.doctorsavailablity_tabworking_searchview = QTableWidget(self.tab_2)
        self.doctorsavailablity_tabworking_searchview.setObjectName(u"doctorsavailablity_tabworking_searchview")
        self.doctorsavailablity_tabworking_searchview.setStyleSheet(u"background-color: rgb(230, 190, 196);\n"
"border-radius: 10px;gg")

        self.verticalLayout_3.addWidget(self.doctorsavailablity_tabworking_searchview)

        self.doctorsavailablity_tab.addTab(self.tab_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_11 = QVBoxLayout(self.tab_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_4 = QFrame(self.tab_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.doctorsavailablity_tabadddoc_contact = QLineEdit(self.frame_4)
        self.doctorsavailablity_tabadddoc_contact.setObjectName(u"doctorsavailablity_tabadddoc_contact")
        self.doctorsavailablity_tabadddoc_contact.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.doctorsavailablity_tabadddoc_contact.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.doctorsavailablity_tabadddoc_contact)

        self.doctorsavailablity_tabadddoc_name = QLineEdit(self.frame_4)
        self.doctorsavailablity_tabadddoc_name.setObjectName(u"doctorsavailablity_tabadddoc_name")
        self.doctorsavailablity_tabadddoc_name.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.doctorsavailablity_tabadddoc_name.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.doctorsavailablity_tabadddoc_name)

        self.doctorsavailablity_tabadddoc_dept = QLineEdit(self.frame_4)
        self.doctorsavailablity_tabadddoc_dept.setObjectName(u"doctorsavailablity_tabadddoc_dept")
        self.doctorsavailablity_tabadddoc_dept.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.doctorsavailablity_tabadddoc_dept.setDragEnabled(False)
        self.doctorsavailablity_tabadddoc_dept.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.doctorsavailablity_tabadddoc_dept)

        self.doctorsavailablity_tabadddoc_houseno = QLineEdit(self.frame_4)
        self.doctorsavailablity_tabadddoc_houseno.setObjectName(u"doctorsavailablity_tabadddoc_houseno")
        self.doctorsavailablity_tabadddoc_houseno.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.doctorsavailablity_tabadddoc_houseno.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.doctorsavailablity_tabadddoc_houseno)

        self.doctorsavailablity_tabadddoc_state = QLineEdit(self.frame_4)
        self.doctorsavailablity_tabadddoc_state.setObjectName(u"doctorsavailablity_tabadddoc_state")
        self.doctorsavailablity_tabadddoc_state.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.doctorsavailablity_tabadddoc_state.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.doctorsavailablity_tabadddoc_state)

        self.doctorsavailablity_tabadddoc_salary = QLineEdit(self.frame_4)
        self.doctorsavailablity_tabadddoc_salary.setObjectName(u"doctorsavailablity_tabadddoc_salary")
        self.doctorsavailablity_tabadddoc_salary.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.doctorsavailablity_tabadddoc_salary.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.doctorsavailablity_tabadddoc_salary)

        self.doctorsavailablity_tabadddoc_city = QLineEdit(self.frame_4)
        self.doctorsavailablity_tabadddoc_city.setObjectName(u"doctorsavailablity_tabadddoc_city")
        self.doctorsavailablity_tabadddoc_city.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.doctorsavailablity_tabadddoc_city.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.doctorsavailablity_tabadddoc_city)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.doctorsavailablity_tabadddoc_dispprob = QLineEdit(self.tab_6)
        self.doctorsavailablity_tabadddoc_dispprob.setObjectName(u"doctorsavailablity_tabadddoc_dispprob")
        self.doctorsavailablity_tabadddoc_dispprob.setMinimumSize(QSize(0, 36))

        self.verticalLayout_11.addWidget(self.doctorsavailablity_tabadddoc_dispprob)

        self.widget = QWidget(self.tab_6)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_8 = QSpacerItem(168, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.doctorsavailablity_tabadddoc_button = QPushButton(self.widget)
        self.doctorsavailablity_tabadddoc_button.setObjectName(u"doctorsavailablity_tabadddoc_button")
        self.doctorsavailablity_tabadddoc_button.setMinimumSize(QSize(150, 0))
        self.doctorsavailablity_tabadddoc_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doctorsavailablity_tabadddoc_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100, 155, 229);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.doctorsavailablity_tabadddoc_button.setCheckable(True)
        self.doctorsavailablity_tabadddoc_button.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.doctorsavailablity_tabadddoc_button)

        self.horizontalSpacer_7 = QSpacerItem(167, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout_11.addWidget(self.widget)

        self.doctorsavailablity_tab.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_10 = QVBoxLayout(self.tab_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.binsearchholder_3 = QHBoxLayout()
        self.binsearchholder_3.setSpacing(0)
        self.binsearchholder_3.setObjectName(u"binsearchholder_3")
        self.doctorsavailablity_tabdeletedoc_searchentry = QLineEdit(self.tab_7)
        self.doctorsavailablity_tabdeletedoc_searchentry.setObjectName(u"doctorsavailablity_tabdeletedoc_searchentry")
        self.doctorsavailablity_tabdeletedoc_searchentry.setMinimumSize(QSize(450, 35))
        self.doctorsavailablity_tabdeletedoc_searchentry.setStyleSheet(u"background-color: rgb(209, 241, 239);\n"
"border-radius: 7px")
        self.doctorsavailablity_tabdeletedoc_searchentry.setClearButtonEnabled(True)

        self.binsearchholder_3.addWidget(self.doctorsavailablity_tabdeletedoc_searchentry)

        self.doctorsavailablity_tabdeletedoc_searchbutton = QPushButton(self.tab_7)
        self.doctorsavailablity_tabdeletedoc_searchbutton.setObjectName(u"doctorsavailablity_tabdeletedoc_searchbutton")
        self.doctorsavailablity_tabdeletedoc_searchbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doctorsavailablity_tabdeletedoc_searchbutton.setStyleSheet(u"QPushButton {\n"
"    background-color: lightblue; /* light blue background */\n"
"    color: black; /* black text */\n"
"    border: none;\n"
"    padding: 10px 20px; /* Padding for the button */\n"
"    font-size: 16px; /* Font size */\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the button appearance on hover */\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 173, 229); /* Darker light blue on hover */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(186, 235, 207):\n"
"}")
        self.doctorsavailablity_tabdeletedoc_searchbutton.setCheckable(True)
        self.doctorsavailablity_tabdeletedoc_searchbutton.setChecked(False)
        self.doctorsavailablity_tabdeletedoc_searchbutton.setAutoExclusive(True)

        self.binsearchholder_3.addWidget(self.doctorsavailablity_tabdeletedoc_searchbutton)


        self.verticalLayout_10.addLayout(self.binsearchholder_3)

        self.doctorsavailablity_tabdeletedoc_view = QTableWidget(self.tab_7)
        self.doctorsavailablity_tabdeletedoc_view.setObjectName(u"doctorsavailablity_tabdeletedoc_view")
        self.doctorsavailablity_tabdeletedoc_view.setStyleSheet(u"background-color: rgb(224, 163, 165);\n"
"border-radius: 10px;gg")

        self.verticalLayout_10.addWidget(self.doctorsavailablity_tabdeletedoc_view)

        self.doctorsavailablity_tabdeletedoc_deletebutton = QPushButton(self.tab_7)
        self.doctorsavailablity_tabdeletedoc_deletebutton.setObjectName(u"doctorsavailablity_tabdeletedoc_deletebutton")
        self.doctorsavailablity_tabdeletedoc_deletebutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doctorsavailablity_tabdeletedoc_deletebutton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100, 155, 229);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.doctorsavailablity_tabdeletedoc_deletebutton.setCheckable(True)
        self.doctorsavailablity_tabdeletedoc_deletebutton.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.doctorsavailablity_tabdeletedoc_deletebutton)

        self.doctorsavailablity_tab.addTab(self.tab_7, "")

        self.verticalLayout_6.addWidget(self.doctorsavailablity_tab)

        self.managepatientsrecords.addWidget(self.pg1)
        self.pg2 = QWidget()
        self.pg2.setObjectName(u"pg2")
        self.gridLayout_5 = QGridLayout(self.pg2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.managepatientsrecords_label = QLabel(self.pg2)
        self.managepatientsrecords_label.setObjectName(u"managepatientsrecords_label")
        self.managepatientsrecords_label.setMinimumSize(QSize(0, 30))
        self.managepatientsrecords_label.setStyleSheet(u"padding:5px;\n"
"background-color: rgb(227, 172, 233);\n"
"border-radius:10px\n"
"")

        self.gridLayout_5.addWidget(self.managepatientsrecords_label, 0, 0, 1, 1)

        self.managepatientsrecords_tab = QTabWidget(self.pg2)
        self.managepatientsrecords_tab.setObjectName(u"managepatientsrecords_tab")
        self.managepatientsrecords_tab.setEnabled(True)
        self.managepatientsrecords_tab.setStyleSheet(u"")
        self.medstock = QWidget()
        self.medstock.setObjectName(u"medstock")
        self.gridLayout_7 = QGridLayout(self.medstock)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.managepatientsrecords_tabrecords_view = QTableWidget(self.medstock)
        self.managepatientsrecords_tabrecords_view.setObjectName(u"managepatientsrecords_tabrecords_view")
        self.managepatientsrecords_tabrecords_view.setStyleSheet(u"background-color: rgb(234, 199, 202);\n"
"border-radius: 10px;")

        self.gridLayout_7.addWidget(self.managepatientsrecords_tabrecords_view, 1, 0, 1, 1)

        self.stocklinebuttonholder = QWidget(self.medstock)
        self.stocklinebuttonholder.setObjectName(u"stocklinebuttonholder")
        self.stocklinebuttonholder.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(155, 155, 229);\n"
"	border:none;\n"
"	padding:10px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.stocklinebuttonholder)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, 5, -1)
        self.managepatientsrecords_tabrecords_search = QLineEdit(self.stocklinebuttonholder)
        self.managepatientsrecords_tabrecords_search.setObjectName(u"managepatientsrecords_tabrecords_search")
        self.managepatientsrecords_tabrecords_search.setStyleSheet(u"background-color: rgb(227, 174, 175);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.managepatientsrecords_tabrecords_search.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.managepatientsrecords_tabrecords_search, 0, 0, 1, 1)

        self.managepatientsrecords_tabrecords_searchbutton = QPushButton(self.stocklinebuttonholder)
        self.managepatientsrecords_tabrecords_searchbutton.setObjectName(u"managepatientsrecords_tabrecords_searchbutton")
        self.managepatientsrecords_tabrecords_searchbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.managepatientsrecords_tabrecords_searchbutton.setStyleSheet(u"")
        self.managepatientsrecords_tabrecords_searchbutton.setCheckable(True)
        self.managepatientsrecords_tabrecords_searchbutton.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.managepatientsrecords_tabrecords_searchbutton, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.stocklinebuttonholder, 0, 0, 1, 1)

        self.managepatientsrecords_tab.addTab(self.medstock, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_20 = QVBoxLayout(self.tab_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.stocklinebuttonholder_2 = QWidget(self.tab_8)
        self.stocklinebuttonholder_2.setObjectName(u"stocklinebuttonholder_2")
        self.stocklinebuttonholder_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(155, 155, 229);\n"
"	border:none;\n"
"	padding:10px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.stocklinebuttonholder_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, -1, 5, -1)
        self.managepatientsrecords_tabrecords_searchpast = QLineEdit(self.stocklinebuttonholder_2)
        self.managepatientsrecords_tabrecords_searchpast.setObjectName(u"managepatientsrecords_tabrecords_searchpast")
        self.managepatientsrecords_tabrecords_searchpast.setStyleSheet(u"background-color: rgb(234, 174, 100);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.managepatientsrecords_tabrecords_searchpast.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.managepatientsrecords_tabrecords_searchpast, 0, 0, 1, 1)

        self.managepatientsrecords_tabrecords_searchbutton_past = QPushButton(self.stocklinebuttonholder_2)
        self.managepatientsrecords_tabrecords_searchbutton_past.setObjectName(u"managepatientsrecords_tabrecords_searchbutton_past")
        self.managepatientsrecords_tabrecords_searchbutton_past.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.managepatientsrecords_tabrecords_searchbutton_past.setStyleSheet(u"")
        self.managepatientsrecords_tabrecords_searchbutton_past.setCheckable(True)
        self.managepatientsrecords_tabrecords_searchbutton_past.setAutoExclusive(True)

        self.gridLayout_4.addWidget(self.managepatientsrecords_tabrecords_searchbutton_past, 0, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.stocklinebuttonholder_2)

        self.managepatientsrecords_tabrecords_view_past = QTableWidget(self.tab_8)
        self.managepatientsrecords_tabrecords_view_past.setObjectName(u"managepatientsrecords_tabrecords_view_past")
        self.managepatientsrecords_tabrecords_view_past.setStyleSheet(u"background-color: rgb(220, 160, 190);\n"
"border-radius: 10px;")

        self.verticalLayout_20.addWidget(self.managepatientsrecords_tabrecords_view_past)

        self.managepatientsrecords_tab.addTab(self.tab_8, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.managepatientsrecords_tabdelete_view = QTableWidget(self.tab)
        self.managepatientsrecords_tabdelete_view.setObjectName(u"managepatientsrecords_tabdelete_view")
        self.managepatientsrecords_tabdelete_view.setStyleSheet(u"background-color: rgb(234, 199, 202);\n"
"border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.managepatientsrecords_tabdelete_view)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.managepatientsrecords_tabdelete_search = QLineEdit(self.frame)
        self.managepatientsrecords_tabdelete_search.setObjectName(u"managepatientsrecords_tabdelete_search")
        self.managepatientsrecords_tabdelete_search.setMinimumSize(QSize(280, 0))
        self.managepatientsrecords_tabdelete_search.setStyleSheet(u"background-color: rgb(227, 174, 175);\n"
"padding:10px;\n"
"border-radius:8px;")

        self.horizontalLayout_2.addWidget(self.managepatientsrecords_tabdelete_search)

        self.managepatientsrecords_tabdelete_searchbutton = QPushButton(self.frame)
        self.managepatientsrecords_tabdelete_searchbutton.setObjectName(u"managepatientsrecords_tabdelete_searchbutton")
        self.managepatientsrecords_tabdelete_searchbutton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(175, 135, 190);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.managepatientsrecords_tabdelete_searchbutton.setCheckable(True)
        self.managepatientsrecords_tabdelete_searchbutton.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.managepatientsrecords_tabdelete_searchbutton)

        self.managepatientsrecords_tabdelete_deletebutton = QPushButton(self.frame)
        self.managepatientsrecords_tabdelete_deletebutton.setObjectName(u"managepatientsrecords_tabdelete_deletebutton")
        self.managepatientsrecords_tabdelete_deletebutton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(155, 155, 229);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.managepatientsrecords_tabdelete_deletebutton.setCheckable(True)
        self.managepatientsrecords_tabdelete_deletebutton.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.managepatientsrecords_tabdelete_deletebutton)


        self.verticalLayout_2.addWidget(self.frame)

        self.managepatientsrecords_tab.addTab(self.tab, "")

        self.gridLayout_5.addWidget(self.managepatientsrecords_tab, 2, 0, 1, 1)

        self.managepatientsrecords.addWidget(self.pg2)
        self.pg3 = QWidget()
        self.pg3.setObjectName(u"pg3")
        self.verticalLayout_18 = QVBoxLayout(self.pg3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.book_appointment_label = QLabel(self.pg3)
        self.book_appointment_label.setObjectName(u"book_appointment_label")
        self.book_appointment_label.setStyleSheet(u"padding:5px;\n"
"background-color: rgb(227, 172, 233);\n"
"border-radius:15px\n"
"")

        self.verticalLayout_18.addWidget(self.book_appointment_label)

        self.bookappointment_tab = QTabWidget(self.pg3)
        self.bookappointment_tab.setObjectName(u"bookappointment_tab")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_13 = QVBoxLayout(self.tab_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea = QScrollArea(self.tab_10)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 119, 494))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.bookappointment_tabentry_name = QLineEdit(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_name.setObjectName(u"bookappointment_tabentry_name")
        self.bookappointment_tabentry_name.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.bookappointment_tabentry_name.setClearButtonEnabled(True)

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_name)

        self.bookappointment_tabentry_doblabel = QLabel(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_doblabel.setObjectName(u"bookappointment_tabentry_doblabel")

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_doblabel)

        self.bookappointment_tabentry_dob = QDateEdit(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_dob.setObjectName(u"bookappointment_tabentry_dob")
        self.bookappointment_tabentry_dob.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_dob)

        self.bookappointment_tabentry_gender = QLineEdit(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_gender.setObjectName(u"bookappointment_tabentry_gender")
        self.bookappointment_tabentry_gender.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.bookappointment_tabentry_gender.setClearButtonEnabled(True)

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_gender)

        self.bookappointment_tabentry_medicalcondition = QLineEdit(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_medicalcondition.setObjectName(u"bookappointment_tabentry_medicalcondition")
        self.bookappointment_tabentry_medicalcondition.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.bookappointment_tabentry_medicalcondition.setClearButtonEnabled(True)

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_medicalcondition)

        self.bookappointment_tabentry_contact = QLineEdit(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_contact.setObjectName(u"bookappointment_tabentry_contact")
        self.bookappointment_tabentry_contact.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.bookappointment_tabentry_contact.setClearButtonEnabled(True)

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_contact)

        self.bookappointment_tabentry_labelappointmentdate = QLabel(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_labelappointmentdate.setObjectName(u"bookappointment_tabentry_labelappointmentdate")

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_labelappointmentdate)

        self.bookappointment_tabentry_appointmentdate = QDateEdit(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_appointmentdate.setObjectName(u"bookappointment_tabentry_appointmentdate")
        self.bookappointment_tabentry_appointmentdate.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_appointmentdate)

        self.bookappointment_tabentry_houseno = QLineEdit(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_houseno.setObjectName(u"bookappointment_tabentry_houseno")
        self.bookappointment_tabentry_houseno.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.bookappointment_tabentry_houseno.setClearButtonEnabled(True)

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_houseno)

        self.bookappointment_tabentry_city = QLineEdit(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_city.setObjectName(u"bookappointment_tabentry_city")
        self.bookappointment_tabentry_city.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.bookappointment_tabentry_city.setClearButtonEnabled(True)

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_city)

        self.bookappointment_tabentry_state = QLineEdit(self.scrollAreaWidgetContents)
        self.bookappointment_tabentry_state.setObjectName(u"bookappointment_tabentry_state")
        self.bookappointment_tabentry_state.setStyleSheet(u"background-color: rgb(165, 231, 190);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.bookappointment_tabentry_state.setDragEnabled(False)
        self.bookappointment_tabentry_state.setClearButtonEnabled(True)

        self.verticalLayout_12.addWidget(self.bookappointment_tabentry_state)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.scrollArea)

        self.bookappointment_tabentry_dispprob = QLineEdit(self.tab_10)
        self.bookappointment_tabentry_dispprob.setObjectName(u"bookappointment_tabentry_dispprob")
        self.bookappointment_tabentry_dispprob.setMinimumSize(QSize(0, 35))
        self.bookappointment_tabentry_dispprob.setAutoFillBackground(False)
        self.bookappointment_tabentry_dispprob.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.bookappointment_tabentry_dispprob)

        self.widget_2 = QWidget(self.tab_10)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_17 = QSpacerItem(168, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)

        self.bookappointment_tabentry_button = QPushButton(self.widget_2)
        self.bookappointment_tabentry_button.setObjectName(u"bookappointment_tabentry_button")
        self.bookappointment_tabentry_button.setMinimumSize(QSize(150, 0))
        self.bookappointment_tabentry_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bookappointment_tabentry_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100, 155, 229);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.bookappointment_tabentry_button.setCheckable(True)
        self.bookappointment_tabentry_button.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.bookappointment_tabentry_button)

        self.horizontalSpacer_18 = QSpacerItem(167, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)


        self.verticalLayout_13.addWidget(self.widget_2)

        self.bookappointment_tab.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.verticalLayout_16 = QVBoxLayout(self.tab_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.binsearchholder_6 = QHBoxLayout()
        self.binsearchholder_6.setSpacing(0)
        self.binsearchholder_6.setObjectName(u"binsearchholder_6")
        self.bookappointment_tabcancel_search = QLineEdit(self.tab_11)
        self.bookappointment_tabcancel_search.setObjectName(u"bookappointment_tabcancel_search")
        self.bookappointment_tabcancel_search.setMinimumSize(QSize(450, 35))
        self.bookappointment_tabcancel_search.setStyleSheet(u"background-color: rgb(209, 241, 239);\n"
"border-radius: 7px")
        self.bookappointment_tabcancel_search.setClearButtonEnabled(True)

        self.binsearchholder_6.addWidget(self.bookappointment_tabcancel_search)

        self.bookappointment_tabcancel_searchbutton = QPushButton(self.tab_11)
        self.bookappointment_tabcancel_searchbutton.setObjectName(u"bookappointment_tabcancel_searchbutton")
        self.bookappointment_tabcancel_searchbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bookappointment_tabcancel_searchbutton.setStyleSheet(u"QPushButton {\n"
"    background-color: lightblue; /* light blue background */\n"
"    color: black; /* black text */\n"
"    border: none;\n"
"    padding: 10px 20px; /* Padding for the button */\n"
"    font-size: 16px; /* Font size */\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the button appearance on hover */\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 173, 229); /* Darker light blue on hover */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(186, 235, 207):\n"
"}")
        self.bookappointment_tabcancel_searchbutton.setCheckable(True)
        self.bookappointment_tabcancel_searchbutton.setChecked(False)
        self.bookappointment_tabcancel_searchbutton.setAutoExclusive(True)

        self.binsearchholder_6.addWidget(self.bookappointment_tabcancel_searchbutton)


        self.verticalLayout_16.addLayout(self.binsearchholder_6)

        self.bookappointment_tabcancel_view = QTableWidget(self.tab_11)
        self.bookappointment_tabcancel_view.setObjectName(u"bookappointment_tabcancel_view")
        self.bookappointment_tabcancel_view.setStyleSheet(u"background-color: rgb(224, 163, 165);\n"
"border-radius: 10px;gg")

        self.verticalLayout_16.addWidget(self.bookappointment_tabcancel_view)

        self.bookappointment_tabcancel_buttondelete = QPushButton(self.tab_11)
        self.bookappointment_tabcancel_buttondelete.setObjectName(u"bookappointment_tabcancel_buttondelete")
        self.bookappointment_tabcancel_buttondelete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bookappointment_tabcancel_buttondelete.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100, 155, 229);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.bookappointment_tabcancel_buttondelete.setCheckable(True)
        self.bookappointment_tabcancel_buttondelete.setAutoExclusive(True)

        self.verticalLayout_16.addWidget(self.bookappointment_tabcancel_buttondelete)

        self.bookappointment_tab.addTab(self.tab_11, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_14 = QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.binsearchholder_7 = QHBoxLayout()
        self.binsearchholder_7.setSpacing(0)
        self.binsearchholder_7.setObjectName(u"binsearchholder_7")
        self.bookappointment_tabcompleted_search = QLineEdit(self.tab_3)
        self.bookappointment_tabcompleted_search.setObjectName(u"bookappointment_tabcompleted_search")
        self.bookappointment_tabcompleted_search.setMinimumSize(QSize(450, 35))
        self.bookappointment_tabcompleted_search.setStyleSheet(u"background-color: rgb(209, 241, 239);\n"
"border-radius: 7px")
        self.bookappointment_tabcompleted_search.setClearButtonEnabled(True)

        self.binsearchholder_7.addWidget(self.bookappointment_tabcompleted_search)

        self.bookappointment_tabcompleted_searchbutton = QPushButton(self.tab_3)
        self.bookappointment_tabcompleted_searchbutton.setObjectName(u"bookappointment_tabcompleted_searchbutton")
        self.bookappointment_tabcompleted_searchbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bookappointment_tabcompleted_searchbutton.setStyleSheet(u"QPushButton {\n"
"    background-color: lightblue; /* light blue background */\n"
"    color: black; /* black text */\n"
"    border: none;\n"
"    padding: 10px 20px; /* Padding for the button */\n"
"    font-size: 16px; /* Font size */\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the button appearance on hover */\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 173, 229); /* Darker light blue on hover */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(186, 235, 207):\n"
"}")
        self.bookappointment_tabcompleted_searchbutton.setCheckable(True)
        self.bookappointment_tabcompleted_searchbutton.setChecked(False)
        self.bookappointment_tabcompleted_searchbutton.setAutoExclusive(True)

        self.binsearchholder_7.addWidget(self.bookappointment_tabcompleted_searchbutton)


        self.verticalLayout_14.addLayout(self.binsearchholder_7)

        self.bookappointment_tabcompleted_view = QTableWidget(self.tab_3)
        self.bookappointment_tabcompleted_view.setObjectName(u"bookappointment_tabcompleted_view")
        self.bookappointment_tabcompleted_view.setStyleSheet(u"background-color: rgb(224, 163, 165);\n"
"border-radius: 10px;gg")

        self.verticalLayout_14.addWidget(self.bookappointment_tabcompleted_view)

        self.bookappointment_tab.addTab(self.tab_3, "")

        self.verticalLayout_18.addWidget(self.bookappointment_tab)

        self.managepatientsrecords.addWidget(self.pg3)
        self.pg4 = QWidget()
        self.pg4.setObjectName(u"pg4")
        self.verticalLayout_15 = QVBoxLayout(self.pg4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.billing_label = QLabel(self.pg4)
        self.billing_label.setObjectName(u"billing_label")
        self.billing_label.setStyleSheet(u"padding:5px;\n"
"background-color: rgb(227, 172, 233);\n"
"border-radius:15px\n"
"")

        self.verticalLayout_15.addWidget(self.billing_label)

        self.scrollArea_2 = QScrollArea(self.pg4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 664, 577))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.binsearchholder_8 = QHBoxLayout()
        self.binsearchholder_8.setSpacing(0)
        self.binsearchholder_8.setObjectName(u"binsearchholder_8")
        self.billing_search = QLineEdit(self.scrollAreaWidgetContents_2)
        self.billing_search.setObjectName(u"billing_search")
        self.billing_search.setMinimumSize(QSize(450, 35))
        self.billing_search.setStyleSheet(u"background-color: rgb(209, 241, 239);\n"
"border-radius: 7px")
        self.billing_search.setClearButtonEnabled(True)

        self.binsearchholder_8.addWidget(self.billing_search)

        self.billing_search_button = QPushButton(self.scrollAreaWidgetContents_2)
        self.billing_search_button.setObjectName(u"billing_search_button")
        self.billing_search_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.billing_search_button.setStyleSheet(u"QPushButton {\n"
"    background-color: lightblue; /* light blue background */\n"
"    color: black; /* black text */\n"
"    border: none;\n"
"    padding: 10px 20px; /* Padding for the button */\n"
"    font-size: 16px; /* Font size */\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the button appearance on hover */\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 173, 229); /* Darker light blue on hover */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(186, 235, 207):\n"
"}")
        self.billing_search_button.setCheckable(True)
        self.billing_search_button.setChecked(False)
        self.billing_search_button.setAutoExclusive(True)

        self.binsearchholder_8.addWidget(self.billing_search_button)


        self.verticalLayout_17.addLayout(self.binsearchholder_8)

        self.billing_search_display = QTableWidget(self.scrollAreaWidgetContents_2)
        self.billing_search_display.setObjectName(u"billing_search_display")
        self.billing_search_display.setMaximumSize(QSize(16777215, 300))
        self.billing_search_display.setStyleSheet(u"background-color: rgb(224, 163, 165);\n"
"border-radius: 10px;gg")

        self.verticalLayout_17.addWidget(self.billing_search_display)

        self.billing_days = QLineEdit(self.scrollAreaWidgetContents_2)
        self.billing_days.setObjectName(u"billing_days")
        self.billing_days.setStyleSheet(u"background-color: rgb(220, 151, 124);\n"
"padding:10px;\n"
"border-radius:8px;")

        self.verticalLayout_17.addWidget(self.billing_days)

        self.billing_costperday = QLineEdit(self.scrollAreaWidgetContents_2)
        self.billing_costperday.setObjectName(u"billing_costperday")
        self.billing_costperday.setStyleSheet(u"background-color: rgb(220, 151, 124);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.billing_costperday.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.billing_costperday)

        self.billing_totalcost = QLineEdit(self.scrollAreaWidgetContents_2)
        self.billing_totalcost.setObjectName(u"billing_totalcost")
        self.billing_totalcost.setStyleSheet(u"background-color: rgb(220, 151, 124);\n"
"padding:10px;\n"
"border-radius:8px;")
        self.billing_totalcost.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.billing_totalcost)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(221, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.billing_data = QPushButton(self.widget_3)
        self.billing_data.setObjectName(u"billing_data")
        self.billing_data.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(175, 135, 190);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.billing_data)

        self.billing_pay = QPushButton(self.widget_3)
        self.billing_pay.setObjectName(u"billing_pay")
        self.billing_pay.setMinimumSize(QSize(300, 0))
        self.billing_pay.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100, 155, 229);\n"
"	border:none;\n"
"	padding:15px 20px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 54, 227);\n"
"	color: white\n"
"}\n"
"")
        self.billing_pay.setCheckable(True)
        self.billing_pay.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.billing_pay)

        self.horizontalSpacer = QSpacerItem(220, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_17.addWidget(self.widget_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_15.addWidget(self.scrollArea_2)

        self.managepatientsrecords.addWidget(self.pg4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_19 = QVBoxLayout(self.page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.graphicsView = QGraphicsView(self.page)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_19.addWidget(self.graphicsView)

        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 900 18pt \"Arial Black\";")

        self.horizontalLayout_6.addWidget(self.label)

        self.lcdNumber_patient_count = QLCDNumber(self.frame_5)
        self.lcdNumber_patient_count.setObjectName(u"lcdNumber_patient_count")
        self.lcdNumber_patient_count.setMinimumSize(QSize(0, 40))
        self.lcdNumber_patient_count.setAutoFillBackground(False)
        self.lcdNumber_patient_count.setSmallDecimalPoint(False)

        self.horizontalLayout_6.addWidget(self.lcdNumber_patient_count)


        self.verticalLayout_19.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 900 18pt \"Arial Black\";")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.lcdNumber_available_doctors = QLCDNumber(self.frame_8)
        self.lcdNumber_available_doctors.setObjectName(u"lcdNumber_available_doctors")
        self.lcdNumber_available_doctors.setMinimumSize(QSize(0, 40))
        self.lcdNumber_available_doctors.setAutoFillBackground(False)
        self.lcdNumber_available_doctors.setSmallDecimalPoint(False)

        self.horizontalLayout_10.addWidget(self.lcdNumber_available_doctors)


        self.verticalLayout_19.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 900 18pt \"Arial Black\";")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.lcdNumber_notavailable_doctors = QLCDNumber(self.frame_6)
        self.lcdNumber_notavailable_doctors.setObjectName(u"lcdNumber_notavailable_doctors")
        self.lcdNumber_notavailable_doctors.setMinimumSize(QSize(0, 40))
        self.lcdNumber_notavailable_doctors.setAutoFillBackground(False)
        self.lcdNumber_notavailable_doctors.setSmallDecimalPoint(False)

        self.horizontalLayout_7.addWidget(self.lcdNumber_notavailable_doctors)


        self.verticalLayout_19.addWidget(self.frame_6)

        self.managepatientsrecords.addWidget(self.page)

        self.verticalLayout.addWidget(self.managepatientsrecords)


        self.gridLayout.addWidget(self.main, 0, 2, 1, 1)

        self.only_icon = QWidget(self.centralwidget)
        self.only_icon.setObjectName(u"only_icon")
        self.only_icon.setStyleSheet(u"/* Background color for the entire form */\n"
"QWidget {\n"
"    background-color: rgb(127, 133, 226); /* blue background */\n"
"}\n"
"\n"
"/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: rgb(181, 233, 162); /* Green background */\n"
"    color: black; /* White text */\n"
"    border: none;\n"
"    padding: 10px 20px; /* Padding for the button */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px; /* Font size */\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the button appearance on hover */\n"
"QPushButton:hover {\n"
"    background-color: rgb(143, 229, 112); /* Darker green on hover */\n"
"}\n"
"\n"
" QPushButton:checked {\n"
"	background-color:rgb(143, 229, 112) ;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.only_icon)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.prof1Holder = QHBoxLayout()
        self.prof1Holder.setObjectName(u"prof1Holder")
        self.prof1Holder.setContentsMargins(-1, 3, -1, -1)
        self.profile = QLabel(self.only_icon)
        self.profile.setObjectName(u"profile")
        self.profile.setMinimumSize(QSize(50, 50))
        self.profile.setMaximumSize(QSize(50, 50))
        self.profile.setPixmap(QPixmap(u":/images/stock_png/owuT8U7P_400x400.jpg"))
        self.profile.setScaledContents(True)

        self.prof1Holder.addWidget(self.profile)


        self.verticalLayout_4.addLayout(self.prof1Holder)

        self.dashboard = QPushButton(self.only_icon)
        self.dashboard.setObjectName(u"dashboard")
        self.dashboard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/stock_png/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboard.setIcon(icon1)
        self.dashboard.setIconSize(QSize(40, 40))
        self.dashboard.setCheckable(True)
        self.dashboard.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.dashboard)

        self.onlyiconholder = QVBoxLayout()
        self.onlyiconholder.setObjectName(u"onlyiconholder")
        self.appointment = QPushButton(self.only_icon)
        self.appointment.setObjectName(u"appointment")
        self.appointment.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/stock_png/history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.appointment.setIcon(icon2)
        self.appointment.setIconSize(QSize(40, 40))
        self.appointment.setCheckable(True)
        self.appointment.setAutoExclusive(True)

        self.onlyiconholder.addWidget(self.appointment)

        self.doctorentry = QPushButton(self.only_icon)
        self.doctorentry.setObjectName(u"doctorentry")
        self.doctorentry.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/images/stock_png/survey.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.doctorentry.setIcon(icon3)
        self.doctorentry.setIconSize(QSize(40, 40))
        self.doctorentry.setCheckable(True)
        self.doctorentry.setAutoExclusive(True)

        self.onlyiconholder.addWidget(self.doctorentry)

        self.patientrecord = QPushButton(self.only_icon)
        self.patientrecord.setObjectName(u"patientrecord")
        self.patientrecord.setEnabled(True)
        self.patientrecord.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/images/stock_png/health-report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.patientrecord.setIcon(icon4)
        self.patientrecord.setIconSize(QSize(40, 40))
        self.patientrecord.setCheckable(True)
        self.patientrecord.setAutoExclusive(True)

        self.onlyiconholder.addWidget(self.patientrecord)

        self.billing = QPushButton(self.only_icon)
        self.billing.setObjectName(u"billing")
        self.billing.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/images/stock_png/bill.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.billing.setIcon(icon5)
        self.billing.setIconSize(QSize(40, 40))
        self.billing.setCheckable(True)
        self.billing.setAutoExclusive(True)

        self.onlyiconholder.addWidget(self.billing)


        self.verticalLayout_4.addLayout(self.onlyiconholder)

        self.onlyiconspacer = QSpacerItem(68, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.onlyiconspacer)

        self.exit = QPushButton(self.only_icon)
        self.exit.setObjectName(u"exit")
        self.exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/images/stock_png/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit.setIcon(icon6)
        self.exit.setIconSize(QSize(40, 40))
        self.exit.setCheckable(True)
        self.exit.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.exit)


        self.gridLayout.addWidget(self.only_icon, 0, 0, 1, 1)

        self.iconname = QWidget(self.centralwidget)
        self.iconname.setObjectName(u"iconname")
        self.iconname.setStyleSheet(u"/* Background color for the entire form */\n"
"QWidget {\n"
"    background-color: rgb(127, 133, 226); /* blue background */\n"
"}\n"
"\n"
"/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: rgb(181, 233, 162); /* Green background */\n"
"    color: black; /* black text */\n"
"    border: none;\n"
"    padding: 10px 20px; /* Padding for the button */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px; /* Font size */\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the button appearance on hover */\n"
"QPushButton:hover {\n"
"    background-color: rgb(143, 229, 112); /* Darker green on hover */\n"
"}\n"
"\n"
" QPushButton:checked {\n"
"	background-color:rgb(143, 229, 112) ;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.iconname)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.prof2holder = QHBoxLayout()
        self.prof2holder.setObjectName(u"prof2holder")
        self.prof2holder.setContentsMargins(-1, 3, -1, -1)
        self.profile_expand = QLabel(self.iconname)
        self.profile_expand.setObjectName(u"profile_expand")
        self.profile_expand.setMinimumSize(QSize(50, 50))
        self.profile_expand.setMaximumSize(QSize(50, 50))
        self.profile_expand.setStyleSheet(u"")
        self.profile_expand.setPixmap(QPixmap(u":/images/stock_png/owuT8U7P_400x400.jpg"))
        self.profile_expand.setScaledContents(True)

        self.prof2holder.addWidget(self.profile_expand)

        self.profile_expand_label = QLabel(self.iconname)
        self.profile_expand_label.setObjectName(u"profile_expand_label")
        self.profile_expand_label.setStyleSheet(u"color: white;\n"
"font-weight:bold;\n"
"font-size:15px")
        self.profile_expand_label.setMargin(10)

        self.prof2holder.addWidget(self.profile_expand_label)


        self.verticalLayout_5.addLayout(self.prof2holder)

        self.iconwithnameholder = QVBoxLayout()
        self.iconwithnameholder.setObjectName(u"iconwithnameholder")
        self.dashboard_expand = QPushButton(self.iconname)
        self.dashboard_expand.setObjectName(u"dashboard_expand")
        self.dashboard_expand.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_expand.setIcon(icon1)
        self.dashboard_expand.setIconSize(QSize(40, 40))
        self.dashboard_expand.setCheckable(True)
        self.dashboard_expand.setChecked(False)
        self.dashboard_expand.setAutoExclusive(True)

        self.iconwithnameholder.addWidget(self.dashboard_expand)

        self.appointment_expand = QPushButton(self.iconname)
        self.appointment_expand.setObjectName(u"appointment_expand")
        self.appointment_expand.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.appointment_expand.setIcon(icon2)
        self.appointment_expand.setIconSize(QSize(40, 40))
        self.appointment_expand.setCheckable(True)
        self.appointment_expand.setAutoExclusive(True)

        self.iconwithnameholder.addWidget(self.appointment_expand)

        self.doctorentry_expand = QPushButton(self.iconname)
        self.doctorentry_expand.setObjectName(u"doctorentry_expand")
        self.doctorentry_expand.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doctorentry_expand.setIcon(icon3)
        self.doctorentry_expand.setIconSize(QSize(40, 40))
        self.doctorentry_expand.setCheckable(True)
        self.doctorentry_expand.setAutoExclusive(True)

        self.iconwithnameholder.addWidget(self.doctorentry_expand)

        self.patientrecord_expand = QPushButton(self.iconname)
        self.patientrecord_expand.setObjectName(u"patientrecord_expand")
        self.patientrecord_expand.setMinimumSize(QSize(0, 0))
        self.patientrecord_expand.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.patientrecord_expand.setMouseTracking(True)
        self.patientrecord_expand.setIcon(icon4)
        self.patientrecord_expand.setIconSize(QSize(40, 40))
        self.patientrecord_expand.setCheckable(True)
        self.patientrecord_expand.setAutoExclusive(True)

        self.iconwithnameholder.addWidget(self.patientrecord_expand)

        self.billing_expand = QPushButton(self.iconname)
        self.billing_expand.setObjectName(u"billing_expand")
        self.billing_expand.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.billing_expand.setIcon(icon5)
        self.billing_expand.setIconSize(QSize(40, 40))
        self.billing_expand.setCheckable(True)
        self.billing_expand.setAutoExclusive(True)

        self.iconwithnameholder.addWidget(self.billing_expand)


        self.verticalLayout_5.addLayout(self.iconwithnameholder)

        self.iconwithnamespacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.iconwithnamespacer)

        self.exit_expand = QPushButton(self.iconname)
        self.exit_expand.setObjectName(u"exit_expand")
        self.exit_expand.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exit_expand.setIcon(icon6)
        self.exit_expand.setIconSize(QSize(40, 40))
        self.exit_expand.setCheckable(True)
        self.exit_expand.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.exit_expand)


        self.gridLayout.addWidget(self.iconname, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.patientrecord_expand.toggled.connect(self.patientrecord.setChecked)
        self.doctorentry_expand.toggled.connect(self.doctorentry.setChecked)
        self.billing_expand.toggled.connect(self.billing.setChecked)
        self.dashboard_expand.toggled.connect(self.dashboard.setChecked)
        self.patientrecord.toggled.connect(self.patientrecord_expand.setChecked)
        self.doctorentry.toggled.connect(self.doctorentry_expand.setChecked)
        self.billing.toggled.connect(self.billing_expand.setChecked)
        self.dashboard.toggled.connect(self.dashboard_expand.setChecked)
        self.exit.toggled.connect(MainWindow.close)
        self.exit_expand.toggled.connect(MainWindow.close)
        self.expand_menu.toggled.connect(self.iconname.setVisible)
        self.expand_menu.toggled.connect(self.only_icon.setHidden)
        self.appointment.toggled.connect(self.appointment_expand.setChecked)
        self.appointment_expand.toggled.connect(self.appointment.setChecked)

        self.managepatientsrecords.setCurrentIndex(4)
        self.doctorsavailablity_tab.setCurrentIndex(1)
        self.managepatientsrecords_tab.setCurrentIndex(0)
        self.bookappointment_tab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.expand_menu.setText("")
        self.main_heading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">HOSPITAL MANAGEMENT SYSTEM</span></p></body></html>", None))
        self.doctorsavailablity_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Doctors Availablity</span></p></body></html>", None))
        self.doctorsavailablity_tabnotavailable_searchentry.setText("")
        self.doctorsavailablity_tabnotavailable_searchentry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.doctorsavailablity_tabnotavailable_searchbutton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.doctorsavailablity_tabnotavailable_markavailablebutton.setText(QCoreApplication.translate("MainWindow", u"mark available", None))
        self.doctorsavailablity_tab.setTabText(self.doctorsavailablity_tab.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"not available", None))
        self.doctorsavailablity_tabavailable_searchentry.setText("")
        self.doctorsavailablity_tabavailable_searchentry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.doctorsavailablity_tabavailable_searchbutton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.doctorsavailablity_tabavailable_marknotavailablebutton.setText(QCoreApplication.translate("MainWindow", u"mark not available", None))
        self.doctorsavailablity_tab.setTabText(self.doctorsavailablity_tab.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Available", None))
        self.doctorsavailablity_tabworking_searchentry.setText("")
        self.doctorsavailablity_tabworking_searchentry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.doctorsavailablity_tabworking_searchbutton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.doctorsavailablity_tab.setTabText(self.doctorsavailablity_tab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"working", None))
        self.doctorsavailablity_tabadddoc_contact.setText("")
        self.doctorsavailablity_tabadddoc_contact.setPlaceholderText(QCoreApplication.translate("MainWindow", u"contact info", None))
        self.doctorsavailablity_tabadddoc_name.setText("")
        self.doctorsavailablity_tabadddoc_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Doctor name", None))
        self.doctorsavailablity_tabadddoc_dept.setText("")
        self.doctorsavailablity_tabadddoc_dept.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.doctorsavailablity_tabadddoc_houseno.setText("")
        self.doctorsavailablity_tabadddoc_houseno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"House no", None))
        self.doctorsavailablity_tabadddoc_state.setText("")
        self.doctorsavailablity_tabadddoc_state.setPlaceholderText(QCoreApplication.translate("MainWindow", u"state", None))
        self.doctorsavailablity_tabadddoc_salary.setText("")
        self.doctorsavailablity_tabadddoc_salary.setPlaceholderText(QCoreApplication.translate("MainWindow", u"salary", None))
        self.doctorsavailablity_tabadddoc_city.setText("")
        self.doctorsavailablity_tabadddoc_city.setPlaceholderText(QCoreApplication.translate("MainWindow", u" city", None))
        self.doctorsavailablity_tabadddoc_button.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.doctorsavailablity_tab.setTabText(self.doctorsavailablity_tab.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"add doctor", None))
        self.doctorsavailablity_tabdeletedoc_searchentry.setText("")
        self.doctorsavailablity_tabdeletedoc_searchentry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.doctorsavailablity_tabdeletedoc_searchbutton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.doctorsavailablity_tabdeletedoc_deletebutton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.doctorsavailablity_tab.setTabText(self.doctorsavailablity_tab.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"delete doctor", None))
        self.managepatientsrecords_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Manage Patients Records</span></p></body></html>", None))
        self.managepatientsrecords_tabrecords_search.setText("")
        self.managepatientsrecords_tabrecords_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.managepatientsrecords_tabrecords_searchbutton.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.managepatientsrecords_tab.setTabText(self.managepatientsrecords_tab.indexOf(self.medstock), QCoreApplication.translate("MainWindow", u"Current Records", None))
        self.managepatientsrecords_tabrecords_searchpast.setText("")
        self.managepatientsrecords_tabrecords_searchpast.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.managepatientsrecords_tabrecords_searchbutton_past.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.managepatientsrecords_tab.setTabText(self.managepatientsrecords_tab.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Past Records", None))
        self.managepatientsrecords_tabdelete_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.managepatientsrecords_tabdelete_searchbutton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.managepatientsrecords_tabdelete_deletebutton.setText(QCoreApplication.translate("MainWindow", u"Delete Record", None))
        self.managepatientsrecords_tab.setTabText(self.managepatientsrecords_tab.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Delete record", None))
        self.book_appointment_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Book Appointment</span></p></body></html>", None))
        self.bookappointment_tabentry_name.setText("")
        self.bookappointment_tabentry_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"name", None))
        self.bookappointment_tabentry_doblabel.setText(QCoreApplication.translate("MainWindow", u"DOB", None))
        self.bookappointment_tabentry_gender.setText("")
        self.bookappointment_tabentry_gender.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gender", None))
        self.bookappointment_tabentry_medicalcondition.setText("")
        self.bookappointment_tabentry_medicalcondition.setPlaceholderText(QCoreApplication.translate("MainWindow", u"medical condition", None))
        self.bookappointment_tabentry_contact.setText("")
        self.bookappointment_tabentry_contact.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email", None))
        self.bookappointment_tabentry_labelappointmentdate.setText(QCoreApplication.translate("MainWindow", u"Appointed Date", None))
        self.bookappointment_tabentry_houseno.setText("")
        self.bookappointment_tabentry_houseno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"House no", None))
        self.bookappointment_tabentry_city.setText("")
        self.bookappointment_tabentry_city.setPlaceholderText(QCoreApplication.translate("MainWindow", u"city", None))
        self.bookappointment_tabentry_state.setText("")
        self.bookappointment_tabentry_state.setPlaceholderText(QCoreApplication.translate("MainWindow", u"state", None))
        self.bookappointment_tabentry_button.setText(QCoreApplication.translate("MainWindow", u"Book", None))
        self.bookappointment_tab.setTabText(self.bookappointment_tab.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Entry", None))
        self.bookappointment_tabcancel_search.setText("")
        self.bookappointment_tabcancel_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.bookappointment_tabcancel_searchbutton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.bookappointment_tabcancel_buttondelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bookappointment_tab.setTabText(self.bookappointment_tab.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"cancel appointment", None))
        self.bookappointment_tabcompleted_search.setText("")
        self.bookappointment_tabcompleted_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.bookappointment_tabcompleted_searchbutton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.bookappointment_tab.setTabText(self.bookappointment_tab.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"completed", None))
        self.billing_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Billing</span></p></body></html>", None))
        self.billing_search.setText("")
        self.billing_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.billing_search_button.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.billing_days.setPlaceholderText(QCoreApplication.translate("MainWindow", u"days admitted", None))
        self.billing_costperday.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cost per day", None))
        self.billing_totalcost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"total cost", None))
        self.billing_data.setText(QCoreApplication.translate("MainWindow", u"GET DATA", None))
        self.billing_pay.setText(QCoreApplication.translate("MainWindow", u"PAY", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PATIENT COUNT :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DOCTORS AVAILABLE:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NOT AVAILABLE DOCTORS :", None))
        self.profile.setText("")
        self.dashboard.setText("")
        self.appointment.setText("")
        self.doctorentry.setText("")
        self.patientrecord.setText("")
        self.billing.setText("")
        self.exit.setText("")
        self.profile_expand.setText("")
        self.profile_expand_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">APOLLO</span></p></body></html>", None))
        self.dashboard_expand.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.appointment_expand.setText(QCoreApplication.translate("MainWindow", u"Appointment", None))
        self.doctorentry_expand.setText(QCoreApplication.translate("MainWindow", u"Doctors entry", None))
        self.patientrecord_expand.setText(QCoreApplication.translate("MainWindow", u"Patient Records", None))
        self.billing_expand.setText(QCoreApplication.translate("MainWindow", u"Billing", None))
        self.exit_expand.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

