# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_1_landingpagewsbNAG.ui'
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
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.imagem = QLabel(self.frame_2)
        self.imagem.setObjectName(u"imagem")
        font = QFont()
        font.setFamily(u"Century Gothic")
        self.imagem.setFont(font)
        self.imagem.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.imagem)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"./side/logo.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.imagem_2 = QLabel(self.frame_4)
        self.imagem_2.setObjectName(u"imagem_2")
        self.imagem_2.setFont(font)
        self.imagem_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.imagem_2)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(LandingPage)

        QMetaObject.connectSlotsByName(LandingPage)
    # setupUi

    def retranslateUi(self, LandingPage):
        LandingPage.setWindowTitle(QCoreApplication.translate("LandingPage", u"Form", None))
        self.imagem.setText(QCoreApplication.translate("LandingPage", u"Bem Vindo!", None))
        self.label.setText("")
        self.imagem_2.setText("")
    # retranslateUi

