# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_2_pedidoIlLlCe.ui'
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

import os, sys
sys.path.insert(0, './')
import side.icons_rc

class Ui_Pedido(object):
    def setupUi(self, Pedido):
        if Pedido.objectName():
            Pedido.setObjectName(u"Pedido")
        Pedido.resize(623, 516)
        self.verticalLayout_2 = QVBoxLayout(Pedido)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.b_corpo = QFrame(Pedido)
        self.b_corpo.setObjectName(u"b_corpo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_corpo.sizePolicy().hasHeightForWidth())
        self.b_corpo.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Century Gothic")
        self.b_corpo.setFont(font)
        self.b_corpo.setFrameShape(QFrame.StyledPanel)
        self.b_corpo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.b_corpo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.a_header = QFrame(self.b_corpo)
        self.a_header.setObjectName(u"a_header")
        self.a_header.setFrameShape(QFrame.StyledPanel)
        self.a_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.a_header)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.a_header_label = QLabel(self.a_header)
        self.a_header_label.setObjectName(u"a_header_label")
        self.a_header_label.setFont(font)
        self.a_header_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.a_header_label)

        self.a_header_modelo = QFrame(self.a_header)
        self.a_header_modelo.setObjectName(u"a_header_modelo")
        self.a_header_modelo.setFrameShape(QFrame.StyledPanel)
        self.a_header_modelo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.a_header_modelo)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.a_header_modelo_label = QLabel(self.a_header_modelo)
        self.a_header_modelo_label.setObjectName(u"a_header_modelo_label")
        self.a_header_modelo_label.setFont(font)

        self.horizontalLayout_12.addWidget(self.a_header_modelo_label, 0, Qt.AlignRight)

        self.a_header_modelo_combo = QComboBox(self.a_header_modelo)
        self.a_header_modelo_combo.setObjectName(u"a_header_modelo_combo")
        self.a_header_modelo_combo.setMinimumSize(QSize(114, 22))
        self.a_header_modelo_combo.setStyleSheet(u"QComboBox#a_header_modelo_combo {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"QComboBox#a_header_modelo_combo::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" \n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox#a_header_modelo_combo::down-arrow {\n"
"    image: url(:/icons/icones/chevron-down.svg);\n"
"	height: 20px\n"
"}")

        self.horizontalLayout_12.addWidget(self.a_header_modelo_combo, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.a_header_modelo)


        self.verticalLayout.addWidget(self.a_header, 0, Qt.AlignTop)

        self.b_cliente = QFrame(self.b_corpo)
        self.b_cliente.setObjectName(u"b_cliente")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.b_cliente.sizePolicy().hasHeightForWidth())
        self.b_cliente.setSizePolicy(sizePolicy1)
        self.b_cliente.setFrameShape(QFrame.StyledPanel)
        self.b_cliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.b_cliente)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.b_cliente_layout = QFrame(self.b_cliente)
        self.b_cliente_layout.setObjectName(u"b_cliente_layout")
        self.b_cliente_layout.setFrameShape(QFrame.StyledPanel)
        self.b_cliente_layout.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.b_cliente_layout)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.b_cliente_label = QLabel(self.b_cliente_layout)
        self.b_cliente_label.setObjectName(u"b_cliente_label")
        self.b_cliente_label.setFont(font)

        self.horizontalLayout_10.addWidget(self.b_cliente_label, 0, Qt.AlignRight)

        self.b_cliente_campo = QLineEdit(self.b_cliente_layout)
        self.b_cliente_campo.setObjectName(u"b_cliente_campo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.b_cliente_campo.sizePolicy().hasHeightForWidth())
        self.b_cliente_campo.setSizePolicy(sizePolicy2)
        self.b_cliente_campo.setMinimumSize(QSize(0, 20))
        self.b_cliente_campo.setFont(font)
        self.b_cliente_campo.setStyleSheet(u"QLineEdit#b_cliente_campo {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.b_cliente_campo)

        self.b_cliente_botao = QPushButton(self.b_cliente_layout)
        self.b_cliente_botao.setObjectName(u"b_cliente_botao")
        self.b_cliente_botao.setMinimumSize(QSize(70, 20))
        self.b_cliente_botao.setFont(font)
        self.b_cliente_botao.setStyleSheet(u"QPushButton#b_cliente_botao {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton#b_cliente_botao:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icones/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_cliente_botao.setIcon(icon)
        self.b_cliente_botao.setIconSize(QSize(10, 16))
        self.b_cliente_botao.setFlat(False)

        self.horizontalLayout_10.addWidget(self.b_cliente_botao, 0, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.b_cliente_layout)


        self.verticalLayout.addWidget(self.b_cliente, 0, Qt.AlignTop)

        self.c_adicionar = QFrame(self.b_corpo)
        self.c_adicionar.setObjectName(u"c_adicionar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(9)
        sizePolicy3.setHeightForWidth(self.c_adicionar.sizePolicy().hasHeightForWidth())
        self.c_adicionar.setSizePolicy(sizePolicy3)
        self.c_adicionar.setFrameShape(QFrame.StyledPanel)
        self.c_adicionar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.c_adicionar)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.layout_esq = QFrame(self.c_adicionar)
        self.layout_esq.setObjectName(u"layout_esq")
        self.layout_esq.setMinimumSize(QSize(0, 0))
        self.layout_esq.setFrameShape(QFrame.StyledPanel)
        self.layout_esq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.layout_esq)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.esq_tab = QTabWidget(self.layout_esq)
        self.esq_tab.setObjectName(u"esq_tab")
        self.esq_tab.setMinimumSize(QSize(0, 0))
        self.esq_tab.setFont(font)
        self.tab_add = QWidget()
        self.tab_add.setObjectName(u"tab_add")
        self.verticalLayout_10 = QVBoxLayout(self.tab_add)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 5, 0, 0)
        self.tab_add_1_label = QLabel(self.tab_add)
        self.tab_add_1_label.setObjectName(u"tab_add_1_label")

        self.verticalLayout_10.addWidget(self.tab_add_1_label)

        self.tab_add_2 = QFrame(self.tab_add)
        self.tab_add_2.setObjectName(u"tab_add_2")
        self.tab_add_2.setFrameShape(QFrame.StyledPanel)
        self.tab_add_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.tab_add_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tab_add_2_combo = QComboBox(self.tab_add_2)
        self.tab_add_2_combo.setObjectName(u"tab_add_2_combo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tab_add_2_combo.sizePolicy().hasHeightForWidth())
        self.tab_add_2_combo.setSizePolicy(sizePolicy4)
        self.tab_add_2_combo.setMinimumSize(QSize(0, 22))
        self.tab_add_2_combo.setStyleSheet(u"QComboBox#tab_add_2_combo {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"QComboBox#tab_add_2_combo::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" \n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox#tab_add_2_combo::down-arrow {\n"
"    image: url(:/icons/icones/chevron-down.svg);\n"
"	height: 20px\n"
"}")

        self.horizontalLayout_15.addWidget(self.tab_add_2_combo)


        self.verticalLayout_10.addWidget(self.tab_add_2, 0, Qt.AlignTop)

        self.tab_add_3 = QFrame(self.tab_add)
        self.tab_add_3.setObjectName(u"tab_add_3")
        sizePolicy1.setHeightForWidth(self.tab_add_3.sizePolicy().hasHeightForWidth())
        self.tab_add_3.setSizePolicy(sizePolicy1)
        self.tab_add_3.setFrameShape(QFrame.StyledPanel)
        self.tab_add_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.tab_add_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.tab_add_3_label = QLabel(self.tab_add_3)
        self.tab_add_3_label.setObjectName(u"tab_add_3_label")

        self.horizontalLayout_16.addWidget(self.tab_add_3_label)

        self.tab_add_3_campo = QLineEdit(self.tab_add_3)
        self.tab_add_3_campo.setObjectName(u"tab_add_3_campo")
        self.tab_add_3_campo.setMinimumSize(QSize(0, 22))
        self.tab_add_3_campo.setFont(font)
        self.tab_add_3_campo.setStyleSheet(u"QLineEdit#tab_add_3_campo {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.tab_add_3_campo)


        self.verticalLayout_10.addWidget(self.tab_add_3, 0, Qt.AlignTop)

        self.tab_add_4 = QFrame(self.tab_add)
        self.tab_add_4.setObjectName(u"tab_add_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(4)
        sizePolicy5.setHeightForWidth(self.tab_add_4.sizePolicy().hasHeightForWidth())
        self.tab_add_4.setSizePolicy(sizePolicy5)
        self.tab_add_4.setFrameShape(QFrame.StyledPanel)
        self.tab_add_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.tab_add_4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.tab_add_4_botao = QPushButton(self.tab_add_4)
        self.tab_add_4_botao.setObjectName(u"tab_add_4_botao")
        sizePolicy4.setHeightForWidth(self.tab_add_4_botao.sizePolicy().hasHeightForWidth())
        self.tab_add_4_botao.setSizePolicy(sizePolicy4)
        self.tab_add_4_botao.setMinimumSize(QSize(0, 25))
        self.tab_add_4_botao.setFont(font)
        self.tab_add_4_botao.setStyleSheet(u"QPushButton#tab_add_4_botao {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton#tab_add_4_botao:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icones/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_add_4_botao.setIcon(icon1)

        self.horizontalLayout_17.addWidget(self.tab_add_4_botao)


        self.verticalLayout_10.addWidget(self.tab_add_4, 0, Qt.AlignTop)

        self.esq_tab.addTab(self.tab_add, "")
        self.tab_rem = QWidget()
        self.tab_rem.setObjectName(u"tab_rem")
        self.verticalLayout_11 = QVBoxLayout(self.tab_rem)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 5, 0, 0)
        self.tab_rem_1_label = QLabel(self.tab_rem)
        self.tab_rem_1_label.setObjectName(u"tab_rem_1_label")

        self.verticalLayout_11.addWidget(self.tab_rem_1_label)

        self.tab_rem_2 = QFrame(self.tab_rem)
        self.tab_rem_2.setObjectName(u"tab_rem_2")
        self.tab_rem_2.setFrameShape(QFrame.StyledPanel)
        self.tab_rem_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.tab_rem_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tab_rem_2_combo = QComboBox(self.tab_rem_2)
        self.tab_rem_2_combo.setObjectName(u"tab_rem_2_combo")
        sizePolicy4.setHeightForWidth(self.tab_rem_2_combo.sizePolicy().hasHeightForWidth())
        self.tab_rem_2_combo.setSizePolicy(sizePolicy4)
        self.tab_rem_2_combo.setMinimumSize(QSize(0, 22))
        self.tab_rem_2_combo.setStyleSheet(u"QComboBox#tab_rem_2_combo {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"QComboBox#tab_rem_2_combo::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" \n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox#tab_rem_2_combo::down-arrow {\n"
"    image: url(:/icons/icones/chevron-down.svg);\n"
"	height: 20px\n"
"}")

        self.horizontalLayout_18.addWidget(self.tab_rem_2_combo)


        self.verticalLayout_11.addWidget(self.tab_rem_2, 0, Qt.AlignTop)

        self.tab_rem_3 = QFrame(self.tab_rem)
        self.tab_rem_3.setObjectName(u"tab_rem_3")
        sizePolicy1.setHeightForWidth(self.tab_rem_3.sizePolicy().hasHeightForWidth())
        self.tab_rem_3.setSizePolicy(sizePolicy1)
        self.tab_rem_3.setFrameShape(QFrame.StyledPanel)
        self.tab_rem_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.tab_rem_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.tab_rem_3_label = QLabel(self.tab_rem_3)
        self.tab_rem_3_label.setObjectName(u"tab_rem_3_label")

        self.horizontalLayout_19.addWidget(self.tab_rem_3_label)

        self.tab_rem_3_campo = QLineEdit(self.tab_rem_3)
        self.tab_rem_3_campo.setObjectName(u"tab_rem_3_campo")
        self.tab_rem_3_campo.setMinimumSize(QSize(0, 22))
        self.tab_rem_3_campo.setFont(font)
        self.tab_rem_3_campo.setStyleSheet(u"QLineEdit#tab_rem_3_campo {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}")

        self.horizontalLayout_19.addWidget(self.tab_rem_3_campo)


        self.verticalLayout_11.addWidget(self.tab_rem_3, 0, Qt.AlignTop)

        self.tab_rem_4 = QFrame(self.tab_rem)
        self.tab_rem_4.setObjectName(u"tab_rem_4")
        sizePolicy5.setHeightForWidth(self.tab_rem_4.sizePolicy().hasHeightForWidth())
        self.tab_rem_4.setSizePolicy(sizePolicy5)
        self.tab_rem_4.setFrameShape(QFrame.StyledPanel)
        self.tab_rem_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.tab_rem_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.tab_rem_4_botao = QPushButton(self.tab_rem_4)
        self.tab_rem_4_botao.setObjectName(u"tab_rem_4_botao")
        sizePolicy4.setHeightForWidth(self.tab_rem_4_botao.sizePolicy().hasHeightForWidth())
        self.tab_rem_4_botao.setSizePolicy(sizePolicy4)
        self.tab_rem_4_botao.setMinimumSize(QSize(0, 25))
        self.tab_rem_4_botao.setFont(font)
        self.tab_rem_4_botao.setStyleSheet(u"QPushButton#tab_rem_4_botao {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton#tab_rem_4_botao:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icones/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_rem_4_botao.setIcon(icon2)

        self.horizontalLayout_20.addWidget(self.tab_rem_4_botao)


        self.verticalLayout_11.addWidget(self.tab_rem_4, 0, Qt.AlignTop)

        self.esq_tab.addTab(self.tab_rem, "")

        self.verticalLayout_5.addWidget(self.esq_tab)

        self.frame_10 = QFrame(self.layout_esq)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_10, 0, Qt.AlignTop)


        self.horizontalLayout_13.addWidget(self.layout_esq)

        self.layout_dir = QFrame(self.c_adicionar)
        self.layout_dir.setObjectName(u"layout_dir")
        self.layout_dir.setFrameShape(QFrame.StyledPanel)
        self.layout_dir.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.layout_dir)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.campo_exibicao = QTextBrowser(self.layout_dir)
        self.campo_exibicao.setObjectName(u"campo_exibicao")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.campo_exibicao.sizePolicy().hasHeightForWidth())
        self.campo_exibicao.setSizePolicy(sizePolicy6)
        self.campo_exibicao.setMinimumSize(QSize(255, 0))
        self.campo_exibicao.setFont(font)
        self.campo_exibicao.setStyleSheet(u"QTextBrowser#campo_exibicao {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.campo_exibicao)


        self.horizontalLayout_13.addWidget(self.layout_dir)


        self.verticalLayout.addWidget(self.c_adicionar, 0, Qt.AlignTop)

        self.d_obs = QFrame(self.b_corpo)
        self.d_obs.setObjectName(u"d_obs")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(3)
        sizePolicy7.setHeightForWidth(self.d_obs.sizePolicy().hasHeightForWidth())
        self.d_obs.setSizePolicy(sizePolicy7)
        self.d_obs.setFrameShape(QFrame.StyledPanel)
        self.d_obs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.d_obs)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.d_obs_label = QLabel(self.d_obs)
        self.d_obs_label.setObjectName(u"d_obs_label")

        self.verticalLayout_12.addWidget(self.d_obs_label)

        self.d_obs_obs = QTextEdit(self.d_obs)
        self.d_obs_obs.setObjectName(u"d_obs_obs")
        self.d_obs_obs.setFont(font)
        self.d_obs_obs.setStyleSheet(u"QTextEdit#d_obs_obs {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}")

        self.verticalLayout_12.addWidget(self.d_obs_obs)


        self.verticalLayout.addWidget(self.d_obs)

        self.e_adicionar = QFrame(self.b_corpo)
        self.e_adicionar.setObjectName(u"e_adicionar")
        self.e_adicionar.setFrameShape(QFrame.StyledPanel)
        self.e_adicionar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.e_adicionar)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.e_adicionar_botao = QPushButton(self.e_adicionar)
        self.e_adicionar_botao.setObjectName(u"e_adicionar_botao")
        self.e_adicionar_botao.setMinimumSize(QSize(280, 25))
        self.e_adicionar_botao.setMaximumSize(QSize(280, 16777215))
        self.e_adicionar_botao.setFont(font)
        self.e_adicionar_botao.setStyleSheet(u"QPushButton#e_adicionar_botao {\n"
"    background-color: rgb(250,250,250);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(200,200,200);\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton#e_adicionar_botao:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.e_adicionar_botao)


        self.verticalLayout.addWidget(self.e_adicionar)


        self.verticalLayout_2.addWidget(self.b_corpo)


        self.retranslateUi(Pedido)

        self.esq_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Pedido)
    # setupUi

    def retranslateUi(self, Pedido):
        Pedido.setWindowTitle(QCoreApplication.translate("Pedido", u"Form", None))
        self.a_header_label.setText(QCoreApplication.translate("Pedido", u"Atendimento n\u00ba 00000000000000", None))
        self.a_header_modelo_label.setText(QCoreApplication.translate("Pedido", u"Modelo de pedido:", None))
        self.b_cliente_label.setText(QCoreApplication.translate("Pedido", u"Cliente:", None))
        self.b_cliente_campo.setPlaceholderText(QCoreApplication.translate("Pedido", u"Nome do Cliente.", None))
        self.b_cliente_botao.setText(QCoreApplication.translate("Pedido", u"Buscar", None))
        self.tab_add_1_label.setText(QCoreApplication.translate("Pedido", u"Adicionar Produtos:", None))
        self.tab_add_3_label.setText(QCoreApplication.translate("Pedido", u"Quantidade:", None))
        self.tab_add_3_campo.setPlaceholderText(QCoreApplication.translate("Pedido", u"Quantidade.", None))
        self.tab_add_4_botao.setText(QCoreApplication.translate("Pedido", u"Adicionar", None))
        self.esq_tab.setTabText(self.esq_tab.indexOf(self.tab_add), QCoreApplication.translate("Pedido", u"Adicionar", None))
        self.tab_rem_1_label.setText(QCoreApplication.translate("Pedido", u"Remover Produtos:", None))
        self.tab_rem_3_label.setText(QCoreApplication.translate("Pedido", u"Quantidade:", None))
        self.tab_rem_3_campo.setPlaceholderText(QCoreApplication.translate("Pedido", u"Quantidade.", None))
        self.tab_rem_4_botao.setText(QCoreApplication.translate("Pedido", u"Remover", None))
        self.esq_tab.setTabText(self.esq_tab.indexOf(self.tab_rem), QCoreApplication.translate("Pedido", u"Remover", None))
        self.campo_exibicao.setPlaceholderText(QCoreApplication.translate("Pedido", u"Lista com itens do pedido", None))
        self.d_obs_label.setText(QCoreApplication.translate("Pedido", u"Observa\u00e7\u00f5es:", None))
        self.d_obs_obs.setPlaceholderText(QCoreApplication.translate("Pedido", u"Observa\u00e7\u00f5es gerais sobre o pedido.", None))
        self.e_adicionar_botao.setText(QCoreApplication.translate("Pedido", u"Adicionar Pedido.", None))
    # retranslateUi

