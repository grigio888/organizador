# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_3_cadastro_clientemfCBJx.ui'
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

from side.janelas.padrao import *

class Ui_CadastroCliente(object):
    def setupUi(self, CadastroCliente):
        if CadastroCliente.objectName():
            CadastroCliente.setObjectName(u"CadastroCliente")
        CadastroCliente.resize(336, 358)
        font = QFont()
        font.setFamily(u"Century Gothic")
        CadastroCliente.setFont(font)
        self.verticalLayout = QVBoxLayout(CadastroCliente)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.a_header = QFrame(CadastroCliente)
        self.a_header.setObjectName(u"a_header")
        self.a_header.setFrameShape(QFrame.StyledPanel)
        self.a_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.a_header)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.a_header_label = QLabel(self.a_header)
        self.a_header_label.setObjectName(u"a_header_label")

        self.verticalLayout_5.addWidget(self.a_header_label, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.a_header)

        self.b_corpo = QFrame(CadastroCliente)
        self.b_corpo.setObjectName(u"b_corpo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.b_corpo.sizePolicy().hasHeightForWidth())
        self.b_corpo.setSizePolicy(sizePolicy)
        self.b_corpo.setFrameShape(QFrame.StyledPanel)
        self.b_corpo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.b_corpo)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.guia = QTabWidget(self.b_corpo)
        self.guia.setObjectName(u"guia")
        self.guia_adicionar = QWidget()
        self.guia_adicionar.setObjectName(u"guia_adicionar")
        self.verticalLayout_7 = QVBoxLayout(self.guia_adicionar)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.a_frame_nome = QFrame(self.guia_adicionar)
        self.a_frame_nome.setObjectName(u"a_frame_nome")
        self.a_frame_nome.setFrameShape(QFrame.StyledPanel)
        self.a_frame_nome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.a_frame_nome)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.a_frame_nome_label = QLabel(self.a_frame_nome)
        self.a_frame_nome_label.setObjectName(u"a_frame_nome_label")
        self.a_frame_nome_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_10.addWidget(self.a_frame_nome_label)

        self.a_frame_nome_campo = QLineEdit(self.a_frame_nome)
        self.a_frame_nome_campo.setObjectName(u"a_frame_nome_campo")
        self.a_frame_nome_campo.setMinimumSize(QSize(0, 20))
        self.a_frame_nome_campo.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_10.addWidget(self.a_frame_nome_campo)


        self.verticalLayout_7.addWidget(self.a_frame_nome, 0, Qt.AlignTop)

        self.b_frame_id = QFrame(self.guia_adicionar)
        self.b_frame_id.setObjectName(u"b_frame_id")
        sizePolicy.setHeightForWidth(self.b_frame_id.sizePolicy().hasHeightForWidth())
        self.b_frame_id.setSizePolicy(sizePolicy)
        self.b_frame_id.setFrameShape(QFrame.StyledPanel)
        self.b_frame_id.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.b_frame_id)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.b_frame_id_label = QLabel(self.b_frame_id)
        self.b_frame_id_label.setObjectName(u"b_frame_id_label")
        self.b_frame_id_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_11.addWidget(self.b_frame_id_label)

        self.b_frame_id_campo = QLineEdit(self.b_frame_id)
        self.b_frame_id_campo.setObjectName(u"b_frame_id_campo")
        self.b_frame_id_campo.setMinimumSize(QSize(0, 20))
        self.b_frame_id_campo.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_11.addWidget(self.b_frame_id_campo)


        self.verticalLayout_7.addWidget(self.b_frame_id, 0, Qt.AlignTop)

        self.c_frame_endereco = QFrame(self.guia_adicionar)
        self.c_frame_endereco.setObjectName(u"c_frame_endereco")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(6)
        sizePolicy1.setHeightForWidth(self.c_frame_endereco.sizePolicy().hasHeightForWidth())
        self.c_frame_endereco.setSizePolicy(sizePolicy1)
        self.c_frame_endereco.setFrameShape(QFrame.StyledPanel)
        self.c_frame_endereco.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.c_frame_endereco)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.c_frame_endereco_label = QLabel(self.c_frame_endereco)
        self.c_frame_endereco_label.setObjectName(u"c_frame_endereco_label")
        self.c_frame_endereco_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_12.addWidget(self.c_frame_endereco_label)

        self.c_frame_endereco_campo = QLineEdit(self.c_frame_endereco)
        self.c_frame_endereco_campo.setObjectName(u"c_frame_endereco_campo")
        self.c_frame_endereco_campo.setMinimumSize(QSize(0, 20))
        self.c_frame_endereco_campo.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_12.addWidget(self.c_frame_endereco_campo)


        self.verticalLayout_7.addWidget(self.c_frame_endereco, 0, Qt.AlignTop)

        self.d_frame_tel_1 = QFrame(self.guia_adicionar)
        self.d_frame_tel_1.setObjectName(u"d_frame_tel_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(36)
        sizePolicy2.setHeightForWidth(self.d_frame_tel_1.sizePolicy().hasHeightForWidth())
        self.d_frame_tel_1.setSizePolicy(sizePolicy2)
        self.d_frame_tel_1.setFrameShape(QFrame.StyledPanel)
        self.d_frame_tel_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.d_frame_tel_1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.d_frame_tel_1_label = QLabel(self.d_frame_tel_1)
        self.d_frame_tel_1_label.setObjectName(u"d_frame_tel_1_label")
        self.d_frame_tel_1_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_13.addWidget(self.d_frame_tel_1_label)

        self.d_frame_tel_1_campo = QLineEdit(self.d_frame_tel_1)
        self.d_frame_tel_1_campo.setObjectName(u"d_frame_tel_1_campo")
        self.d_frame_tel_1_campo.setMinimumSize(QSize(0, 20))
        self.d_frame_tel_1_campo.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_13.addWidget(self.d_frame_tel_1_campo)


        self.verticalLayout_7.addWidget(self.d_frame_tel_1, 0, Qt.AlignTop)

        self.e_frame_tel_2 = QFrame(self.guia_adicionar)
        self.e_frame_tel_2.setObjectName(u"e_frame_tel_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(212)
        sizePolicy3.setHeightForWidth(self.e_frame_tel_2.sizePolicy().hasHeightForWidth())
        self.e_frame_tel_2.setSizePolicy(sizePolicy3)
        self.e_frame_tel_2.setFrameShape(QFrame.StyledPanel)
        self.e_frame_tel_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.e_frame_tel_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.e_frame_tel_2_label = QLabel(self.e_frame_tel_2)
        self.e_frame_tel_2_label.setObjectName(u"e_frame_tel_2_label")
        self.e_frame_tel_2_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_14.addWidget(self.e_frame_tel_2_label)

        self.e_frame_tel_2_campo = QLineEdit(self.e_frame_tel_2)
        self.e_frame_tel_2_campo.setObjectName(u"e_frame_tel_2_campo")
        self.e_frame_tel_2_campo.setMinimumSize(QSize(0, 20))
        self.e_frame_tel_2_campo.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_14.addWidget(self.e_frame_tel_2_campo)


        self.verticalLayout_7.addWidget(self.e_frame_tel_2, 0, Qt.AlignTop)

        self.f_frame_cadastrar = QFrame(self.guia_adicionar)
        self.f_frame_cadastrar.setObjectName(u"f_frame_cadastrar")
        self.f_frame_cadastrar.setFrameShape(QFrame.StyledPanel)
        self.f_frame_cadastrar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.f_frame_cadastrar)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.f_frame_cadastrar_botao = QPushButton(self.f_frame_cadastrar)
        self.f_frame_cadastrar_botao.setObjectName(u"f_frame_cadastrar_botao")
        self.f_frame_cadastrar_botao.setMinimumSize(QSize(0, 25))
        self.f_frame_cadastrar_botao.setFont(font)
        self.f_frame_cadastrar_botao.setStyleSheet(estilo_push_button())
        icon = QIcon()
        icon.addFile(u":/icons/icones/checkmark.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.f_frame_cadastrar_botao.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.f_frame_cadastrar_botao)


        self.verticalLayout_7.addWidget(self.f_frame_cadastrar)

        self.guia.addTab(self.guia_adicionar, "")
        self.guia_atualizar = QWidget()
        self.guia_atualizar.setObjectName(u"guia_atualizar")
        self.verticalLayout_10 = QVBoxLayout(self.guia_atualizar)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.guia_atualizar)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 35))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_26.addWidget(self.label_17)

        self.lineEdit_16 = QLineEdit(self.frame_17)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 20))
        self.lineEdit_16.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_26.addWidget(self.lineEdit_16)

        self.pushButton_2 = QPushButton(self.frame_17)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(70, 20))
        self.pushButton_2.setStyleSheet(estilo_push_button())
        icon1 = QIcon()
        icon1.addFile(u":/icons/icones/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(11, 16))

        self.horizontalLayout_26.addWidget(self.pushButton_2)


        self.verticalLayout_10.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.guia_atualizar)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer = QSpacerItem(501, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addWidget(self.frame_16)

        self.frame_14 = QFrame(self.guia_atualizar)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 35))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_24.addWidget(self.label_15)

        self.lineEdit_14 = QLineEdit(self.frame_14)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 20))
        self.lineEdit_14.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_24.addWidget(self.lineEdit_14)


        self.verticalLayout_10.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_15 = QFrame(self.guia_atualizar)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QSize(0, 35))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_25.addWidget(self.label_16)

        self.lineEdit_15 = QLineEdit(self.frame_15)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(0, 20))
        self.lineEdit_15.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_25.addWidget(self.lineEdit_15)


        self.verticalLayout_10.addWidget(self.frame_15)

        self.frame_12 = QFrame(self.guia_atualizar)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setMinimumSize(QSize(0, 35))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_22.addWidget(self.label_13)

        self.lineEdit_12 = QLineEdit(self.frame_12)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(0, 20))
        self.lineEdit_12.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_22.addWidget(self.lineEdit_12)


        self.verticalLayout_10.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.guia_atualizar)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy2.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy2)
        self.frame_13.setMinimumSize(QSize(0, 35))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_23.addWidget(self.label_14)

        self.lineEdit_13 = QLineEdit(self.frame_13)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(0, 20))
        self.lineEdit_13.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_23.addWidget(self.lineEdit_13)


        self.verticalLayout_10.addWidget(self.frame_13, 0, Qt.AlignTop)

        self.frame_11 = QFrame(self.guia_atualizar)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
        self.frame_11.setMinimumSize(QSize(0, 35))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_21.addWidget(self.label_12)

        self.lineEdit_11 = QLineEdit(self.frame_11)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 20))
        self.lineEdit_11.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_11.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_21.addWidget(self.lineEdit_11)


        self.verticalLayout_10.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.guia_atualizar)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 35))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_3 = QPushButton(self.frame_18)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 25))
        self.pushButton_3.setStyleSheet(estilo_push_button())
        icon2 = QIcon()
        icon2.addFile(u":/icons/icones/retweet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_28.addWidget(self.pushButton_3)


        self.verticalLayout_10.addWidget(self.frame_18, 0, Qt.AlignBottom)

        self.guia.addTab(self.guia_atualizar, "")
        self.guia_remover = QWidget()
        self.guia_remover.setObjectName(u"guia_remover")
        self.verticalLayout_11 = QVBoxLayout(self.guia_remover)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_21 = QFrame(self.guia_remover)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 35))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_31.addWidget(self.label_18)

        self.lineEdit_17 = QLineEdit(self.frame_21)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 20))
        self.lineEdit_17.setStyleSheet(estilo_line_edit())

        self.horizontalLayout_31.addWidget(self.lineEdit_17)

        self.pushButton_5 = QPushButton(self.frame_21)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(70, 20))
        self.pushButton_5.setStyleSheet(estilo_push_button())
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(11, 16))

        self.horizontalLayout_31.addWidget(self.pushButton_5)


        self.verticalLayout_11.addWidget(self.frame_21, 0, Qt.AlignTop)

        self.frame_20 = QFrame(self.guia_remover)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMinimumSize(QSize(0, 35))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.checkBox = QCheckBox(self.frame_20)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 20))
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet(u"")

        self.horizontalLayout_30.addWidget(self.checkBox)


        self.verticalLayout_11.addWidget(self.frame_20, 0, Qt.AlignBottom)

        self.frame_19 = QFrame(self.guia_remover)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 35))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pushButton_4 = QPushButton(self.frame_19)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 25))
        self.pushButton_4.setStyleSheet(estilo_push_button())
        icon3 = QIcon()
        icon3.addFile(u":/icons/icones/tag-delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.horizontalLayout_29.addWidget(self.pushButton_4)


        self.verticalLayout_11.addWidget(self.frame_19, 0, Qt.AlignBottom)

        self.guia.addTab(self.guia_remover, "")

        self.horizontalLayout_9.addWidget(self.guia)


        self.verticalLayout.addWidget(self.b_corpo)


        self.retranslateUi(CadastroCliente)

        self.guia.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CadastroCliente)
    # setupUi

    def retranslateUi(self, CadastroCliente):
        CadastroCliente.setWindowTitle(QCoreApplication.translate("CadastroCliente", u"CadastroCliente", None))
        self.a_header_label.setText(QCoreApplication.translate("CadastroCliente", u"Cadastro de Cliente", None))
        self.a_frame_nome_label.setText(QCoreApplication.translate("CadastroCliente", u"Nome:", None))
        self.a_frame_nome_campo.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"Nome Completo.", None))
        self.b_frame_id_label.setText(QCoreApplication.translate("CadastroCliente", u"ID:", None))
        self.b_frame_id_campo.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"000.000.000-00", None))
        self.c_frame_endereco_label.setText(QCoreApplication.translate("CadastroCliente", u"Endere\u00e7o:", None))
        self.c_frame_endereco_campo.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"Endere\u00e7o Completo.", None))
        self.d_frame_tel_1_label.setText(QCoreApplication.translate("CadastroCliente", u"Telefone 1:", None))
        self.d_frame_tel_1_campo.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"+55 27 99999-99999", None))
        self.e_frame_tel_2_label.setText(QCoreApplication.translate("CadastroCliente", u"Telefone 2:", None))
        self.e_frame_tel_2_campo.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"+55 27 99999-99999", None))
        self.f_frame_cadastrar_botao.setText(QCoreApplication.translate("CadastroCliente", u"Cadastrar", None))
        self.guia.setTabText(self.guia.indexOf(self.guia_adicionar), QCoreApplication.translate("CadastroCliente", u"Adicionar", None))
        self.label_17.setText(QCoreApplication.translate("CadastroCliente", u"Cliente:", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"Nome do Cliente", None))
        self.pushButton_2.setText(QCoreApplication.translate("CadastroCliente", u"Buscar", None))
        self.label_15.setText(QCoreApplication.translate("CadastroCliente", u"Nome:", None))
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"Nome Completo.", None))
        self.label_16.setText(QCoreApplication.translate("CadastroCliente", u"ID:", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"000.000.000-00", None))
        self.label_13.setText(QCoreApplication.translate("CadastroCliente", u"Endere\u00e7o:", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"Endere\u00e7o Completo.", None))
        self.label_14.setText(QCoreApplication.translate("CadastroCliente", u"Telefone 1:", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"+55 27 99999-99999", None))
        self.label_12.setText(QCoreApplication.translate("CadastroCliente", u"Telefone 2:", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"+55 27 99999-99999", None))
        self.pushButton_3.setText(QCoreApplication.translate("CadastroCliente", u"Atualizar", None))
        self.guia.setTabText(self.guia.indexOf(self.guia_atualizar), QCoreApplication.translate("CadastroCliente", u"Atualizar", None))
        self.label_18.setText(QCoreApplication.translate("CadastroCliente", u"Cliente:", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("CadastroCliente", u"Nome do Cliente", None))
        self.pushButton_5.setText(QCoreApplication.translate("CadastroCliente", u"Buscar", None))
        self.checkBox.setText(QCoreApplication.translate("CadastroCliente", u"Desejo remover o cliente do banco de dados.", None))
        self.pushButton_4.setText(QCoreApplication.translate("CadastroCliente", u"Remover", None))
        self.guia.setTabText(self.guia.indexOf(self.guia_remover), QCoreApplication.translate("CadastroCliente", u"Remover", None))
    # retranslateUi

