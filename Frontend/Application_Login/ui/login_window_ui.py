# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_w_loginform(object):
    def setupUi(self, w_loginform):
        if not w_loginform.objectName():
            w_loginform.setObjectName(u"w_loginform")
        w_loginform.resize(479, 339)
        font = QFont()
        font.setPointSize(12)
        w_loginform.setFont(font)
        self.gridLayout = QGridLayout(w_loginform)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(w_loginform)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_userid = QLineEdit(self.groupBox)
        self.le_userid.setObjectName(u"le_userid")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_userid)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_password = QLineEdit(self.groupBox)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_password)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.pb_okay = QPushButton(w_loginform)
        self.pb_okay.setObjectName(u"pb_okay")

        self.gridLayout.addWidget(self.pb_okay, 2, 0, 1, 1)

        self.lb_Message = QLabel(w_loginform)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout.addWidget(self.lb_Message, 3, 0, 1, 1)

        self.pb_cancel = QPushButton(w_loginform)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.gridLayout.addWidget(self.pb_cancel, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        QWidget.setTabOrder(self.le_userid, self.le_password)
        QWidget.setTabOrder(self.le_password, self.pb_okay)
        QWidget.setTabOrder(self.pb_okay, self.pb_cancel)

        self.retranslateUi(w_loginform)

        QMetaObject.connectSlotsByName(w_loginform)
    # setupUi

    def retranslateUi(self, w_loginform):
        w_loginform.setWindowTitle(QCoreApplication.translate("w_loginform", u"iHeart Streaming Bot", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_loginform", u"Welcome! Please Login", None))
        self.label.setText(QCoreApplication.translate("w_loginform", u"User ID:", None))
        self.label_2.setText(QCoreApplication.translate("w_loginform", u"Password:", None))
        self.pb_okay.setText(QCoreApplication.translate("w_loginform", u"Okay!", None))
        self.lb_Message.setText(QCoreApplication.translate("w_loginform", u"Message", None))
        self.pb_cancel.setText(QCoreApplication.translate("w_loginform", u"Cancel", None))
    # retranslateUi

