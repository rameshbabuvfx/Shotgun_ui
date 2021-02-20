# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShotgunUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import shotgun_icons_rc

class UiMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(443, 693)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"background-color: rgb(42, 42, 42);")
        self.MainFrame.setFrameShape(QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CategoryFrame = QFrame(self.MainFrame)
        self.CategoryFrame.setObjectName(u"CategoryFrame")
        self.CategoryFrame.setMinimumSize(QSize(0, 46))
        self.CategoryFrame.setMaximumSize(QSize(16777215, 50))
        self.CategoryFrame.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.CategoryFrame.setFrameShape(QFrame.NoFrame)
        self.CategoryFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.CategoryFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 10, 0, 0)
        self.pushButton = QPushButton(self.CategoryFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(56, 32))
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(Qt.StrongFocus)
        self.pushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border : none;\n"
"	\n"
"	color: rgb(199, 199, 199);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.CategoryFrame)

        self.Projects = QFrame(self.MainFrame)
        self.Projects.setObjectName(u"Projects")
        self.Projects.setMinimumSize(QSize(0, 61))
        self.Projects.setMaximumSize(QSize(16777215, 65))
        self.Projects.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.Projects.setFrameShape(QFrame.Box)
        self.Projects.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.Projects)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 9, 0)
        self.ProjectsLabel = QLabel(self.Projects)
        self.ProjectsLabel.setObjectName(u"ProjectsLabel")
        self.ProjectsLabel.setMinimumSize(QSize(134, 0))
        font1 = QFont()
        font1.setFamily(u"Kievit Offc Pro")
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        self.ProjectsLabel.setFont(font1)
        self.ProjectsLabel.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.ProjectsLabel.setTextFormat(Qt.AutoText)
        self.ProjectsLabel.setScaledContents(False)
        self.ProjectsLabel.setAlignment(Qt.AlignCenter)
        self.ProjectsLabel.setWordWrap(False)
        self.ProjectsLabel.setMargin(0)

        self.horizontalLayout_2.addWidget(self.ProjectsLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.stackedWidget_2 = QStackedWidget(self.Projects)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(161, 16777211))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(86, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border : none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(84, 167, 255);\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/shotgun icons/search-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(23, 22))
        self.pushButton_2.setCheckable(False)

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setMinimumSize(QSize(59, 0))
        self.gridLayout_5 = QGridLayout(self.page_4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.page_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(76, 24))
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(195, 195, 195);\n"
"	border-radius: 6px;\n"
"	\n"
"	color: rgb(134, 134, 134);\n"
"}")
        self.lineEdit.setFrame(False)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.page_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon1 = QIcon()
        icon1.addFile(u":/icons/SP_DES_200914103021AacKD78q1600078206712/icons/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(17, 21))

        self.gridLayout_5.addWidget(self.pushButton_6, 0, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.page_4)

        self.horizontalLayout_2.addWidget(self.stackedWidget_2)


        self.verticalLayout.addWidget(self.Projects)

        self.ProjectsList = QFrame(self.MainFrame)
        self.ProjectsList.setObjectName(u"ProjectsList")
        self.ProjectsList.setMinimumSize(QSize(0, 0))
        self.ProjectsList.setMaximumSize(QSize(1600000, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        self.ProjectsList.setFont(font2)
        self.ProjectsList.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ProjectsList.setStyleSheet(u"background-color: rgb(42, 42, 42);")
        self.ProjectsList.setFrameShape(QFrame.NoFrame)
        self.ProjectsList.setFrameShadow(QFrame.Raised)
        self.ProjectsList.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.ProjectsList)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 5, 0)
        self.stackedWidget = QStackedWidget(self.ProjectsList)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Project1 = QToolButton(self.page)
        self.Project1.setObjectName(u"Project1")
        self.Project1.setStyleSheet(u"QToolButton{\n"
"	border:none;\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/project_thumbnails/thumbnails/aquama1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Project1.setIcon(icon2)
        self.Project1.setIconSize(QSize(100, 100))
        self.Project1.setPopupMode(QToolButton.DelayedPopup)
        self.Project1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.Project1, 0, 0, 1, 1)

        self.Project3 = QToolButton(self.page)
        self.Project3.setObjectName(u"Project3")
        self.Project3.setStyleSheet(u"QToolButton{\n"
"	border:none;\n"
"	\n"
"	\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/project_thumbnails/thumbnails/blackadam.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Project3.setIcon(icon3)
        self.Project3.setIconSize(QSize(100, 100))
        self.Project3.setPopupMode(QToolButton.DelayedPopup)
        self.Project3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.Project3, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.Project2 = QToolButton(self.page)
        self.Project2.setObjectName(u"Project2")
        self.Project2.setStyleSheet(u"QToolButton{\n"
"	border:none;\n"
"	\n"
"	\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/project_thumbnails/thumbnails/batman vs superman.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Project2.setIcon(icon4)
        self.Project2.setIconSize(QSize(100, 100))
        self.Project2.setPopupMode(QToolButton.DelayedPopup)
        self.Project2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.Project2, 0, 1, 1, 1)

        self.Project4 = QToolButton(self.page)
        self.Project4.setObjectName(u"Project4")
        self.Project4.setStyleSheet(u"QToolButton{\n"
"	border:none;\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/project_thumbnails/thumbnails/joke1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Project4.setIcon(icon5)
        self.Project4.setIconSize(QSize(100, 100))
        self.Project4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.Project4, 1, 0, 1, 1)

        self.Project5 = QToolButton(self.page)
        self.Project5.setObjectName(u"Project5")
        self.Project5.setStyleSheet(u"QToolButton{\n"
"	border:none;\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/project_thumbnails/thumbnails/justiec league.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Project5.setIcon(icon6)
        self.Project5.setIconSize(QSize(100, 100))
        self.Project5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.Project5.setAutoRaise(False)

        self.gridLayout_3.addWidget(self.Project5, 1, 1, 1, 1)

        self.Project6 = QToolButton(self.page)
        self.Project6.setObjectName(u"Project6")
        self.Project6.setStyleSheet(u"QToolButton{\n"
"	border:none;\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/project_thumbnails/thumbnails/the-flash1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Project6.setIcon(icon7)
        self.Project6.setIconSize(QSize(100, 100))
        self.Project6.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_3.addWidget(self.Project6, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 77))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(80, 16777215))
        self.pushButton_4.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"thumbnails/nukex.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setIconSize(QSize(100, 100))

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(80, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/software_thumbnails/thumbnails/maya_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon9)
        self.pushButton_7.setIconSize(QSize(65, 100))

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(80, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/software_thumbnails/thumbnails/Houdini3D_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon10)
        self.pushButton_5.setIconSize(QSize(65, 100))

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 51))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font3 = QFont()
        font3.setPointSize(13)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border : none;\n"
"	\n"
"	color: rgb(231, 243, 243);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/SP_DES_200914103021AacKD78q1600078206712/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon11)
        self.pushButton_3.setIconSize(QSize(31, 23))

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.horizontalSpacer_5 = QSpacerItem(337, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.ProjectsList)

        self.AccountFrame = QFrame(self.MainFrame)
        self.AccountFrame.setObjectName(u"AccountFrame")
        self.AccountFrame.setMinimumSize(QSize(0, 53))
        self.AccountFrame.setMaximumSize(QSize(16777215, 53))
        self.AccountFrame.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.AccountFrame.setFrameShape(QFrame.NoFrame)
        self.AccountFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.AccountFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(16, 0, 15, 2)
        self.ShotgunLabel = QLabel(self.AccountFrame)
        self.ShotgunLabel.setObjectName(u"ShotgunLabel")
        font4 = QFont()
        font4.setFamily(u"Arial Black")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.ShotgunLabel.setFont(font4)
        self.ShotgunLabel.setStyleSheet(u"color: rgb(199, 199, 199);")

        self.horizontalLayout_3.addWidget(self.ShotgunLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.AccountButton = QPushButton(self.AccountFrame)
        self.AccountButton.setObjectName(u"AccountButton")
        self.AccountButton.setStyleSheet(u"QPushButton{\n"
"	border : none;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/shotgun icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AccountButton.setIcon(icon12)
        self.AccountButton.setIconSize(QSize(28, 25))
        self.AccountButton.setAutoDefault(False)
        self.AccountButton.setFlat(False)

        self.horizontalLayout_3.addWidget(self.AccountButton)


        self.verticalLayout.addWidget(self.AccountFrame)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.AccountButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.ProjectsLabel.setText(QCoreApplication.translate("MainWindow", u"PROJECTS", None))
        self.pushButton_2.setText("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Projects", None))
        self.pushButton_6.setText("")
        self.Project1.setText(QCoreApplication.translate("MainWindow", u"Aquaman", None))
        self.Project3.setText(QCoreApplication.translate("MainWindow", u"Black Adam", None))
        self.Project2.setText(QCoreApplication.translate("MainWindow", u"Batman vs Superman", None))
        self.Project4.setText(QCoreApplication.translate("MainWindow", u"Joker", None))
        self.Project5.setText(QCoreApplication.translate("MainWindow", u"Justice League", None))
        self.Project6.setText(QCoreApplication.translate("MainWindow", u"The Flash", None))
        self.pushButton_4.setText("")
        self.pushButton_7.setText("")
        self.pushButton_5.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.ShotgunLabel.setText(QCoreApplication.translate("MainWindow", u"MACHINeGUN", None))
        self.AccountButton.setText("")
    # retranslateUi

