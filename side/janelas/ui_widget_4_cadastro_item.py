from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import os, sys
sys.path.insert(0, './')
import side.icons_rc

stylesheet = open('side/janelas/padrao.css', 'r').read()

class Ui_cadastro_item(object):
    def setupUi(self, cadastro_item):
        if cadastro_item.objectName():
            cadastro_item.setObjectName(u"cadastro_item")
        cadastro_item.resize(358, 358)
        cadastro_item.setStyleSheet(stylesheet)
        self.verticalLayout = QVBoxLayout(cadastro_item)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.a_header = QFrame(cadastro_item)
        self.a_header.setObjectName(u"a_header")
        self.a_header.setFrameShape(QFrame.StyledPanel)
        self.a_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.a_header)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.a_header_label = QLabel(self.a_header)
        self.a_header_label.setObjectName(u"a_header_label")

        self.verticalLayout_5.addWidget(self.a_header_label, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.a_header)

        self.b_corpo = QFrame(cadastro_item)
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
        self.add_a_nome = QFrame(self.guia_adicionar)
        self.add_a_nome.setObjectName(u"add_a_nome")
        self.add_a_nome.setFrameShape(QFrame.StyledPanel)
        self.add_a_nome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.add_a_nome)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.add_a_produto_label = QLabel(self.add_a_nome)
        self.add_a_produto_label.setObjectName(u"add_a_produto_label")
        self.add_a_produto_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_10.addWidget(self.add_a_produto_label)

        self.add_a_produto_campo = QLineEdit(self.add_a_nome)
        self.add_a_produto_campo.setObjectName(u"add_a_produto_campo")
        self.add_a_produto_campo.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_10.addWidget(self.add_a_produto_campo)


        self.verticalLayout_7.addWidget(self.add_a_nome, 0, Qt.AlignTop)

        self.add_c_end = QFrame(self.guia_adicionar)
        self.add_c_end.setObjectName(u"add_c_end")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(6)
        sizePolicy1.setHeightForWidth(self.add_c_end.sizePolicy().hasHeightForWidth())
        self.add_c_end.setSizePolicy(sizePolicy1)
        self.add_c_end.setFrameShape(QFrame.StyledPanel)
        self.add_c_end.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.add_c_end)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.add_b_tipo_label = QLabel(self.add_c_end)
        self.add_b_tipo_label.setObjectName(u"add_b_tipo_label")
        self.add_b_tipo_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_12.addWidget(self.add_b_tipo_label)

        self.add_b_tipo_lista = QComboBox(self.add_c_end)
        self.add_b_tipo_lista.setObjectName(u"add_b_tipo_lista")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add_b_tipo_lista.sizePolicy().hasHeightForWidth())
        self.add_b_tipo_lista.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.add_b_tipo_lista)


        self.verticalLayout_7.addWidget(self.add_c_end, 0, Qt.AlignTop)

        self.add_d_tel_1 = QFrame(self.guia_adicionar)
        self.add_d_tel_1.setObjectName(u"add_d_tel_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(36)
        sizePolicy3.setHeightForWidth(self.add_d_tel_1.sizePolicy().hasHeightForWidth())
        self.add_d_tel_1.setSizePolicy(sizePolicy3)
        self.add_d_tel_1.setFrameShape(QFrame.StyledPanel)
        self.add_d_tel_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.add_d_tel_1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.add_d_preco_label = QLabel(self.add_d_tel_1)
        self.add_d_preco_label.setObjectName(u"add_d_preco_label")
        self.add_d_preco_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_13.addWidget(self.add_d_preco_label)

        self.add_d_preco_campo = QLineEdit(self.add_d_tel_1)
        self.add_d_preco_campo.setObjectName(u"add_d_preco_campo")
        self.add_d_preco_campo.setMinimumSize(QSize(0, 20))
        self.add_d_preco_campo.setInputMethodHints(Qt.ImhExclusiveInputMask)
        self.add_d_preco_campo.setMaxLength(7)


        self.horizontalLayout_13.addWidget(self.add_d_preco_campo)


        self.verticalLayout_7.addWidget(self.add_d_tel_1, 0, Qt.AlignTop)

        self.add_f_cadastrar = QFrame(self.guia_adicionar)
        self.add_f_cadastrar.setObjectName(u"add_f_cadastrar")
        self.add_f_cadastrar.setFrameShape(QFrame.StyledPanel)
        self.add_f_cadastrar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.add_f_cadastrar)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.add_f_cadastrar_botao = QPushButton(self.add_f_cadastrar)
        self.add_f_cadastrar_botao.setObjectName(u"add_f_cadastrar_botao")
        self.add_f_cadastrar_botao.setMinimumSize(QSize(0, 25))
        icon = QIcon()
        icon.addFile(u":/icons/icones/checkmark.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_f_cadastrar_botao.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.add_f_cadastrar_botao)


        self.verticalLayout_7.addWidget(self.add_f_cadastrar)

        self.guia.addTab(self.guia_adicionar, "")
        self.guia_atualizar = QWidget()
        self.guia_atualizar.setObjectName(u"guia_atualizar")
        self.verticalLayout_10 = QVBoxLayout(self.guia_atualizar)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.att_a_cliente = QFrame(self.guia_atualizar)
        self.att_a_cliente.setObjectName(u"att_a_cliente")
        self.att_a_cliente.setMinimumSize(QSize(0, 35))
        self.att_a_cliente.setFrameShape(QFrame.StyledPanel)
        self.att_a_cliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.att_a_cliente)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.att_a_produto_label = QLabel(self.att_a_cliente)
        self.att_a_produto_label.setObjectName(u"att_a_produto_label")

        self.horizontalLayout_26.addWidget(self.att_a_produto_label)

        self.att_a_produto_campo = QLineEdit(self.att_a_cliente)
        self.att_a_produto_campo.setObjectName(u"att_a_produto_campo")
        self.att_a_produto_campo.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_26.addWidget(self.att_a_produto_campo)

        self.att_a_produto_botao = QPushButton(self.att_a_cliente)
        self.att_a_produto_botao.setObjectName(u"att_a_produto_botao")
        self.att_a_produto_botao.setMinimumSize(QSize(70, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icones/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.att_a_produto_botao.setIcon(icon1)
        self.att_a_produto_botao.setIconSize(QSize(11, 16))

        self.horizontalLayout_26.addWidget(self.att_a_produto_botao)


        self.verticalLayout_10.addWidget(self.att_a_cliente)

        self.att_b_espacador = QFrame(self.guia_atualizar)
        self.att_b_espacador.setObjectName(u"att_b_espacador")
        self.att_b_espacador.setFrameShape(QFrame.StyledPanel)
        self.att_b_espacador.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.att_b_espacador)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer = QSpacerItem(501, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addWidget(self.att_b_espacador)

        self.att_c_nome = QFrame(self.guia_atualizar)
        self.att_c_nome.setObjectName(u"att_c_nome")
        self.att_c_nome.setMinimumSize(QSize(0, 35))
        self.att_c_nome.setFrameShape(QFrame.StyledPanel)
        self.att_c_nome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.att_c_nome)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.att_c_nome_label = QLabel(self.att_c_nome)
        self.att_c_nome_label.setObjectName(u"att_c_nome_label")
        self.att_c_nome_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_24.addWidget(self.att_c_nome_label)

        self.att_c_nome_campo = QLineEdit(self.att_c_nome)
        self.att_c_nome_campo.setObjectName(u"att_c_nome_campo")
        self.att_c_nome_campo.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_24.addWidget(self.att_c_nome_campo)


        self.verticalLayout_10.addWidget(self.att_c_nome, 0, Qt.AlignTop)

        self.att_d_id = QFrame(self.guia_atualizar)
        self.att_d_id.setObjectName(u"att_d_id")
        sizePolicy.setHeightForWidth(self.att_d_id.sizePolicy().hasHeightForWidth())
        self.att_d_id.setSizePolicy(sizePolicy)
        self.att_d_id.setMinimumSize(QSize(0, 35))
        self.att_d_id.setFrameShape(QFrame.StyledPanel)
        self.att_d_id.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.att_d_id)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.att_d_id_label = QLabel(self.att_d_id)
        self.att_d_id_label.setObjectName(u"att_d_id_label")
        self.att_d_id_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_25.addWidget(self.att_d_id_label)

        self.att_d_id_campo = QTextBrowser(self.att_d_id)
        self.att_d_id_campo.setObjectName(u"att_d_id_campo")
        self.att_d_id_campo.setMinimumSize(QSize(0, 20))
        self.att_d_id_campo.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.att_d_id_campo.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_25.addWidget(self.att_d_id_campo)


        self.verticalLayout_10.addWidget(self.att_d_id)

        self.att_e_end = QFrame(self.guia_atualizar)
        self.att_e_end.setObjectName(u"att_e_end")
        sizePolicy1.setHeightForWidth(self.att_e_end.sizePolicy().hasHeightForWidth())
        self.att_e_end.setSizePolicy(sizePolicy1)
        self.att_e_end.setMinimumSize(QSize(0, 35))
        self.att_e_end.setFrameShape(QFrame.StyledPanel)
        self.att_e_end.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.att_e_end)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.att_e_tipo_label = QLabel(self.att_e_end)
        self.att_e_tipo_label.setObjectName(u"att_e_tipo_label")
        self.att_e_tipo_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_22.addWidget(self.att_e_tipo_label)

        self.att_e_tipo_lista = QComboBox(self.att_e_end)
        self.att_e_tipo_lista.setObjectName(u"att_e_tipo_lista")
        sizePolicy2.setHeightForWidth(self.att_e_tipo_lista.sizePolicy().hasHeightForWidth())
        self.att_e_tipo_lista.setSizePolicy(sizePolicy2)
        self.att_e_tipo_lista.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_22.addWidget(self.att_e_tipo_lista)


        self.verticalLayout_10.addWidget(self.att_e_end, 0, Qt.AlignTop)

        self.att_f_tel_1 = QFrame(self.guia_atualizar)
        self.att_f_tel_1.setObjectName(u"att_f_tel_1")
        sizePolicy3.setHeightForWidth(self.att_f_tel_1.sizePolicy().hasHeightForWidth())
        self.att_f_tel_1.setSizePolicy(sizePolicy3)
        self.att_f_tel_1.setMinimumSize(QSize(0, 35))
        self.att_f_tel_1.setFrameShape(QFrame.StyledPanel)
        self.att_f_tel_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.att_f_tel_1)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.att_f_preco_label = QLabel(self.att_f_tel_1)
        self.att_f_preco_label.setObjectName(u"att_f_preco_label")
        self.att_f_preco_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_23.addWidget(self.att_f_preco_label)

        self.att_f_preco_campo = QLineEdit(self.att_f_tel_1)
        self.att_f_preco_campo.setObjectName(u"att_f_preco_campo")
        self.att_f_preco_campo.setMinimumSize(QSize(0, 20))
        self.att_f_preco_campo.setInputMethodHints(Qt.ImhExclusiveInputMask)
        self.att_f_preco_campo.setMaxLength(7)

        self.horizontalLayout_23.addWidget(self.att_f_preco_campo)


        self.verticalLayout_10.addWidget(self.att_f_tel_1, 0, Qt.AlignTop)

        self.att_h_atualizar = QFrame(self.guia_atualizar)
        self.att_h_atualizar.setObjectName(u"att_h_atualizar")
        self.att_h_atualizar.setMinimumSize(QSize(0, 35))
        self.att_h_atualizar.setFrameShape(QFrame.StyledPanel)
        self.att_h_atualizar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.att_h_atualizar)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.att_h_atualizar_botao = QPushButton(self.att_h_atualizar)
        self.att_h_atualizar_botao.setObjectName(u"att_h_atualizar_botao")
        self.att_h_atualizar_botao.setMinimumSize(QSize(0, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icones/retweet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.att_h_atualizar_botao.setIcon(icon2)

        self.horizontalLayout_28.addWidget(self.att_h_atualizar_botao)


        self.verticalLayout_10.addWidget(self.att_h_atualizar, 0, Qt.AlignBottom)

        self.guia.addTab(self.guia_atualizar, "")
        self.guia_remover = QWidget()
        self.guia_remover.setObjectName(u"guia_remover")
        self.verticalLayout_11 = QVBoxLayout(self.guia_remover)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.rem_a_cliente = QFrame(self.guia_remover)
        self.rem_a_cliente.setObjectName(u"rem_a_cliente")
        self.rem_a_cliente.setMinimumSize(QSize(0, 35))
        self.rem_a_cliente.setFrameShape(QFrame.StyledPanel)
        self.rem_a_cliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.rem_a_cliente)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.rem_a_produto_label = QLabel(self.rem_a_cliente)
        self.rem_a_produto_label.setObjectName(u"rem_a_produto_label")
        self.rem_a_produto_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_31.addWidget(self.rem_a_produto_label)

        self.rem_a_produto_campo = QLineEdit(self.rem_a_cliente)
        self.rem_a_produto_campo.setObjectName(u"rem_a_produto_campo")
        self.rem_a_produto_campo.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_31.addWidget(self.rem_a_produto_campo)

        self.rem_a_produto_botao = QPushButton(self.rem_a_cliente)
        self.rem_a_produto_botao.setObjectName(u"rem_a_produto_botao")
        self.rem_a_produto_botao.setMinimumSize(QSize(70, 20))
        self.rem_a_produto_botao.setIcon(icon1)
        self.rem_a_produto_botao.setIconSize(QSize(11, 16))

        self.horizontalLayout_31.addWidget(self.rem_a_produto_botao)


        self.verticalLayout_11.addWidget(self.rem_a_cliente, 0, Qt.AlignTop)

        self.rem_b_ciente = QFrame(self.guia_remover)
        self.rem_b_ciente.setObjectName(u"rem_b_ciente")
        sizePolicy.setHeightForWidth(self.rem_b_ciente.sizePolicy().hasHeightForWidth())
        self.rem_b_ciente.setSizePolicy(sizePolicy)
        self.rem_b_ciente.setMinimumSize(QSize(0, 35))
        self.rem_b_ciente.setFrameShape(QFrame.StyledPanel)
        self.rem_b_ciente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.rem_b_ciente)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.rem_b_ciente_checkbox = QCheckBox(self.rem_b_ciente)
        self.rem_b_ciente_checkbox.setObjectName(u"rem_b_ciente_checkbox")
        self.rem_b_ciente_checkbox.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_30.addWidget(self.rem_b_ciente_checkbox)


        self.verticalLayout_11.addWidget(self.rem_b_ciente, 0, Qt.AlignBottom)

        self.rem_c_remover = QFrame(self.guia_remover)
        self.rem_c_remover.setObjectName(u"rem_c_remover")
        self.rem_c_remover.setMinimumSize(QSize(0, 35))
        self.rem_c_remover.setFrameShape(QFrame.StyledPanel)
        self.rem_c_remover.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.rem_c_remover)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.rem_c_remover_botao = QPushButton(self.rem_c_remover)
        self.rem_c_remover_botao.setObjectName(u"rem_c_remover_botao")
        self.rem_c_remover_botao.setMinimumSize(QSize(0, 25))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icones/tag-delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rem_c_remover_botao.setIcon(icon3)

        self.horizontalLayout_29.addWidget(self.rem_c_remover_botao)


        self.verticalLayout_11.addWidget(self.rem_c_remover, 0, Qt.AlignBottom)

        self.guia.addTab(self.guia_remover, "")

        self.horizontalLayout_9.addWidget(self.guia)


        self.verticalLayout.addWidget(self.b_corpo)


        self.retranslateUi(cadastro_item)

        self.guia.setCurrentIndex(0)
        self.add_b_tipo_lista.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(cadastro_item)
    # setupUi

    def retranslateUi(self, cadastro_item):
        cadastro_item.setWindowTitle(QCoreApplication.translate("cadastro_item", u"cadastro_item", None))
        self.a_header_label.setText(QCoreApplication.translate("cadastro_item", u"Cadastro de Itens", None))
        self.add_a_produto_label.setText(QCoreApplication.translate("cadastro_item", u"Produto:", None))
        self.add_a_produto_campo.setPlaceholderText(QCoreApplication.translate("cadastro_item", u"Nome do Item.", None))
        self.add_b_tipo_label.setText(QCoreApplication.translate("cadastro_item", u"Tipo:", None))
        self.add_d_preco_label.setText(QCoreApplication.translate("cadastro_item", u"Pre\u00e7o:", None))
        self.add_d_preco_campo.setInputMask(QCoreApplication.translate("cadastro_item", u"0000,00", None))
        self.add_d_preco_campo.setPlaceholderText(QCoreApplication.translate("cadastro_item", u"R$ 0000,00", None))
        self.add_f_cadastrar_botao.setText(QCoreApplication.translate("cadastro_item", u"Cadastrar", None))
        self.guia.setTabText(self.guia.indexOf(self.guia_adicionar), QCoreApplication.translate("cadastro_item", u"Adicionar", None))
        self.att_a_produto_label.setText(QCoreApplication.translate("cadastro_item", u"Produto / ID:", None))
        self.att_a_produto_campo.setPlaceholderText(QCoreApplication.translate("cadastro_item", u"Nome do Item.", None))
        self.att_a_produto_botao.setText(QCoreApplication.translate("cadastro_item", u"Buscar", None))
        self.att_c_nome_label.setText(QCoreApplication.translate("cadastro_item", u"Produto:", None))
        self.att_c_nome_campo.setPlaceholderText(QCoreApplication.translate("cadastro_item", u"Nome do Item.", None))
        self.att_d_id_label.setText(QCoreApplication.translate("cadastro_item", u"ID:", None))
        self.att_e_tipo_label.setText(QCoreApplication.translate("cadastro_item", u"Tipo:", None))
        self.att_f_preco_label.setText(QCoreApplication.translate("cadastro_item", u"Pre\u00e7o:", None))
        self.att_f_preco_campo.setInputMask(QCoreApplication.translate("cadastro_item", u"0000,00", None))
        self.att_f_preco_campo.setPlaceholderText(QCoreApplication.translate("cadastro_item", u"R$ 0000,00", None))
        self.att_h_atualizar_botao.setText(QCoreApplication.translate("cadastro_item", u"Atualizar", None))
        self.guia.setTabText(self.guia.indexOf(self.guia_atualizar), QCoreApplication.translate("cadastro_item", u"Atualizar", None))
        self.rem_a_produto_label.setText(QCoreApplication.translate("cadastro_item", u"Produto / ID:", None))
        self.rem_a_produto_campo.setPlaceholderText(QCoreApplication.translate("cadastro_item", u"Nome do Item.", None))
        self.rem_a_produto_botao.setText(QCoreApplication.translate("cadastro_item", u"Buscar", None))
        self.rem_b_ciente_checkbox.setText(QCoreApplication.translate("cadastro_item", u"Desejo remover o item do banco de dados.", None))
        self.rem_c_remover_botao.setText(QCoreApplication.translate("cadastro_item", u"Remover", None))
        self.guia.setTabText(self.guia.indexOf(self.guia_remover), QCoreApplication.translate("cadastro_item", u"Remover", None))
    # retranslateUi

