# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_1_landingpageJUtmEk.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_LandingPage(object):
    def setupUi(self, LandingPage):
        if LandingPage.objectName():
            LandingPage.setObjectName(u"LandingPage")
        LandingPage.resize(400, 300)
        self.verticalLayout = QVBoxLayout(LandingPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(LandingPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.imagem = QLabel(self.frame_3)
        self.imagem.setObjectName(u"imagem")
        font = QFont()
        font.setFamily(u"Century Gothic")
        self.imagem.setFont(font)
        self.imagem.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.imagem)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(LandingPage)

        QMetaObject.connectSlotsByName(LandingPage)
    # setupUi

    def retranslateUi(self, LandingPage):
        LandingPage.setWindowTitle(QCoreApplication.translate("LandingPage", u"Form", None))
        self.imagem.setText(QCoreApplication.translate("LandingPage", u"Bem Vindo!", None))
    # retranslateUi

