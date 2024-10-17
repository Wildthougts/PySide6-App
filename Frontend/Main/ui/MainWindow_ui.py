# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        font = QFont()
        font.setPointSize(12)
        self.actionQuit.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_stopstream = QPushButton(self.tab_3)
        self.pb_stopstream.setObjectName(u"pb_stopstream")

        self.gridLayout.addWidget(self.pb_stopstream, 1, 1, 1, 1)

        self.pb_startstream = QPushButton(self.tab_3)
        self.pb_startstream.setObjectName(u"pb_startstream")

        self.gridLayout.addWidget(self.pb_startstream, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.pb_uploadaccounts = QPushButton(self.groupBox)
        self.pb_uploadaccounts.setObjectName(u"pb_uploadaccounts")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pb_uploadaccounts)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.pb_uploadurl = QPushButton(self.groupBox)
        self.pb_uploadurl.setObjectName(u"pb_uploadurl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pb_uploadurl)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout = QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lw_devices = QListWidget(self.tab_4)
        self.lw_devices.setObjectName(u"lw_devices")

        self.verticalLayout.addWidget(self.lw_devices)

        self.pb_refreshdevices = QPushButton(self.tab_4)
        self.pb_refreshdevices.setObjectName(u"pb_refreshdevices")

        self.verticalLayout.addWidget(self.pb_refreshdevices)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.te_log = QTextEdit(self.tab_6)
        self.te_log.setObjectName(u"te_log")
        self.te_log.setEnabled(True)
        self.te_log.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.te_log)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"iHeart Streaming Bot", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.pb_stopstream.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pb_startstream.setText(QCoreApplication.translate("MainWindow", u"Start Stream", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pb_uploadaccounts.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.pb_uploadurl.setText(QCoreApplication.translate("MainWindow", u"Url", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Home", None))
        self.pb_refreshdevices.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Devices", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Accounts", None))
    # retranslateUi

