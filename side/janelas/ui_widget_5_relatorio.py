# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_5_relatoriocSjCuX.ui'
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

import icons_rc

class Ui_relatorio(object):
    def setupUi(self, relatorio):
        if relatorio.objectName():
            relatorio.setObjectName(u"relatorio")
        relatorio.resize(516, 515)
        font = QFont()
        font.setFamily(u"Century Gothic")
        relatorio.setFont(font)
        self.verticalLayout = QVBoxLayout(relatorio)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.a_header = QFrame(relatorio)
        self.a_header.setObjectName(u"a_header")
        self.a_header.setFrameShape(QFrame.StyledPanel)
        self.a_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.a_header)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.a_header_label = QLabel(self.a_header)
        self.a_header_label.setObjectName(u"a_header_label")

        self.verticalLayout_5.addWidget(self.a_header_label, 0, Qt.AlignHCenter)

        self.b_corpo = QFrame(self.a_header)
        self.b_corpo.setObjectName(u"b_corpo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.b_corpo.sizePolicy().hasHeightForWidth())
        self.b_corpo.setSizePolicy(sizePolicy)
        self.b_corpo.setFrameShape(QFrame.StyledPanel)
        self.b_corpo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.b_corpo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.b_corpo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.att_a_produto_label_2 = QLabel(self.frame_3)
        self.att_a_produto_label_2.setObjectName(u"att_a_produto_label_2")
        self.att_a_produto_label_2.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.att_a_produto_label_2)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.att_a_produto_botao = QPushButton(self.frame_3)
        self.att_a_produto_botao.setObjectName(u"att_a_produto_botao")
        self.att_a_produto_botao.setMinimumSize(QSize(70, 20))
        self.att_a_produto_botao.setMaximumSize(QSize(70, 16777215))
        self.att_a_produto_botao.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icones/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.att_a_produto_botao.setIcon(icon)
        self.att_a_produto_botao.setIconSize(QSize(11, 16))

        self.horizontalLayout_3.addWidget(self.att_a_produto_botao)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame = QFrame(self.b_corpo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout.addWidget(self.dateEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.dateEdit_2 = QDateEdit(self.frame)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.horizontalLayout.addWidget(self.dateEdit_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.b_corpo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableView = QTableView(self.frame_2)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_2.addWidget(self.tableView)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_5.addWidget(self.b_corpo)


        self.verticalLayout.addWidget(self.a_header)


        self.retranslateUi(relatorio)

        QMetaObject.connectSlotsByName(relatorio)
    # setupUi

    def retranslateUi(self, relatorio):
        relatorio.setWindowTitle(QCoreApplication.translate("relatorio", u"relatorio", None))
        self.a_header_label.setText(QCoreApplication.translate("relatorio", u"Listagem", None))
        self.att_a_produto_label_2.setText(QCoreApplication.translate("relatorio", u"Item :", None))
        self.att_a_produto_botao.setText(QCoreApplication.translate("relatorio", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("relatorio", u"De:", None))
        self.label_2.setText(QCoreApplication.translate("relatorio", u"At\u00e9:", None))
    # retranslateUi

