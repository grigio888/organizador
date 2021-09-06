from PySide2 import QtCore, QtGui
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QPropertyAnimation)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import os, sys
sys.path.insert(0, './')
import side.icons_rc

class Ui_Organizador(object):
    def setupUi(self, Organizador):
        if Organizador.objectName():
            Organizador.setObjectName(u"Organizador")
        Organizador.resize(500, 411)
        Organizador.setMinimumSize(QSize(500, 410))
        Organizador.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.widget_central = QWidget(Organizador)
        self.widget_central.setObjectName(u"widget_central")
        self.horizontalLayout = QHBoxLayout(self.widget_central)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.a_menu_esquerda = QFrame(self.widget_central)
        self.a_menu_esquerda.setObjectName(u"a_menu_esquerda")
        self.a_menu_esquerda.setMaximumSize(QSize(60, 16777215))
        self.a_menu_esquerda.setStyleSheet(u"background-color: rgb(200,220,220);")
        self.a_menu_esquerda.setFrameShape(QFrame.StyledPanel)
        self.a_menu_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.a_menu_esquerda)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.a_menu_superior = QFrame(self.a_menu_esquerda)
        self.a_menu_superior.setObjectName(u"a_menu_superior")
        self.a_menu_superior.setMaximumSize(QSize(16777215, 292))
        self.a_menu_superior.setFrameShape(QFrame.StyledPanel)
        self.a_menu_superior.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.a_menu_superior)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.a_slot_1 = QFrame(self.a_menu_superior)
        self.a_slot_1.setObjectName(u"a_slot_1")
        self.a_slot_1.setFrameShape(QFrame.StyledPanel)
        self.a_slot_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.a_slot_1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.a_botao_home = QPushButton(self.a_slot_1)
        self.a_botao_home.setObjectName(u"a_botao_home")
        icon = QIcon()
        icon.addFile(u":/icons/icones/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.a_botao_home.setIcon(icon)
        self.a_botao_home.setIconSize(QSize(22, 22))
        self.a_botao_home.setCheckable(False)
        self.a_botao_home.setFlat(True)

        self.horizontalLayout_5.addWidget(self.a_botao_home)


        self.verticalLayout_9.addWidget(self.a_slot_1)

        self.b_slot_2 = QFrame(self.a_menu_superior)
        self.b_slot_2.setObjectName(u"b_slot_2")
        self.b_slot_2.setFrameShape(QFrame.StyledPanel)
        self.b_slot_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.b_slot_2)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 7, 0, 15)
        self.b_botao_pedido = QPushButton(self.b_slot_2)
        self.b_botao_pedido.setObjectName(u"b_botao_pedido")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icones/document-edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_botao_pedido.setIcon(icon1)
        self.b_botao_pedido.setIconSize(QSize(25, 25))
        self.b_botao_pedido.setFlat(True)

        self.verticalLayout_3.addWidget(self.b_botao_pedido)

        self.c_botao_cliente = QPushButton(self.b_slot_2)
        self.c_botao_cliente.setObjectName(u"c_botao_cliente")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icones/user-id.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.c_botao_cliente.setIcon(icon2)
        self.c_botao_cliente.setIconSize(QSize(25, 25))
        self.c_botao_cliente.setFlat(True)

        self.verticalLayout_3.addWidget(self.c_botao_cliente)

        self.d_botao_item = QPushButton(self.b_slot_2)
        self.d_botao_item.setObjectName(u"d_botao_item")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icones/to-do.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.d_botao_item.setIcon(icon3)
        self.d_botao_item.setIconSize(QSize(25, 25))
        self.d_botao_item.setFlat(True)

        self.verticalLayout_3.addWidget(self.d_botao_item, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.e_botao_relatorio = QPushButton(self.b_slot_2)
        self.e_botao_relatorio.setObjectName(u"e_botao_relatorio")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icones/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.e_botao_relatorio.setIcon(icon4)
        self.e_botao_relatorio.setIconSize(QSize(25, 25))
        self.e_botao_relatorio.setFlat(True)

        self.verticalLayout_3.addWidget(self.e_botao_relatorio, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.b_slot_2)


        self.verticalLayout_2.addWidget(self.a_menu_superior, 0, Qt.AlignTop)

        self.b_menu_inferior = QFrame(self.a_menu_esquerda)
        self.b_menu_inferior.setObjectName(u"b_menu_inferior")
        self.b_menu_inferior.setFrameShape(QFrame.StyledPanel)
        self.b_menu_inferior.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.b_menu_inferior)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.a_botao_opcao = QPushButton(self.b_menu_inferior)
        self.a_botao_opcao.setObjectName(u"a_botao_opcao")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icones/gear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.a_botao_opcao.setIcon(icon5)
        self.a_botao_opcao.setIconSize(QSize(20, 20))
        self.a_botao_opcao.setFlat(True)

        self.verticalLayout_4.addWidget(self.a_botao_opcao)

        self.b_botao_logout = QPushButton(self.b_menu_inferior)
        self.b_botao_logout.setObjectName(u"b_botao_logout")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icones/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_botao_logout.setIcon(icon6)
        self.b_botao_logout.setIconSize(QSize(20, 20))
        self.b_botao_logout.setFlat(True)

        self.verticalLayout_4.addWidget(self.b_botao_logout, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.b_menu_inferior, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.a_menu_esquerda)

        self.c_corpo = QFrame(self.widget_central)
        self.c_corpo.setObjectName(u"c_corpo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_corpo.sizePolicy().hasHeightForWidth())
        self.c_corpo.setSizePolicy(sizePolicy)
        self.c_corpo.setFrameShape(QFrame.StyledPanel)
        self.c_corpo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.c_corpo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.a_cabecalho = QFrame(self.c_corpo)
        self.a_cabecalho.setObjectName(u"a_cabecalho")
        self.a_cabecalho.setFrameShape(QFrame.StyledPanel)
        self.a_cabecalho.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.a_cabecalho)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.a_container = QFrame(self.a_cabecalho)
        self.a_container.setObjectName(u"a_container")
        self.a_container.setFrameShape(QFrame.StyledPanel)
        self.a_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.a_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.a_nome = QFrame(self.a_container)
        self.a_nome.setObjectName(u"a_nome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.a_nome.sizePolicy().hasHeightForWidth())
        self.a_nome.setSizePolicy(sizePolicy1)
        self.a_nome.setFrameShape(QFrame.StyledPanel)
        self.a_nome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.a_nome)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.nome_prog = QLabel(self.a_nome)
        self.nome_prog.setObjectName(u"nome_prog")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.nome_prog.sizePolicy().hasHeightForWidth())
        self.nome_prog.setSizePolicy(sizePolicy2)
        self.nome_prog.setMinimumSize(QSize(0, 24))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(8)
        self.nome_prog.setFont(font)

        self.horizontalLayout_4.addWidget(self.nome_prog, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.a_nome, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.b_botoes = QFrame(self.a_container)
        self.b_botoes.setObjectName(u"b_botoes")
        self.b_botoes.setFrameShape(QFrame.StyledPanel)
        self.b_botoes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.b_botoes)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.a_minimizar = QPushButton(self.b_botoes)
        self.a_minimizar.setObjectName(u"a_minimizar")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icones/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.a_minimizar.setIcon(icon7)
        self.a_minimizar.setFlat(True)

        self.horizontalLayout_3.addWidget(self.a_minimizar)

        self.b_maximizar = QPushButton(self.b_botoes)
        self.b_maximizar.setObjectName(u"b_maximizar")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icones/expand.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_maximizar.setIcon(icon8)
        self.b_maximizar.setIconSize(QSize(13, 13))
        self.b_maximizar.setFlat(True)

        self.horizontalLayout_3.addWidget(self.b_maximizar)

        self.c_fechar = QPushButton(self.b_botoes)
        self.c_fechar.setObjectName(u"c_fechar")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icones/cross.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.c_fechar.setIcon(icon9)
        self.c_fechar.setFlat(True)

        self.horizontalLayout_3.addWidget(self.c_fechar)


        self.horizontalLayout_2.addWidget(self.b_botoes, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.a_container, 0, Qt.AlignTop)

        self.b_divisor = QFrame(self.a_cabecalho)
        self.b_divisor.setObjectName(u"b_divisor")
        sizePolicy.setHeightForWidth(self.b_divisor.sizePolicy().hasHeightForWidth())
        self.b_divisor.setSizePolicy(sizePolicy)
        self.b_divisor.setMinimumSize(QSize(0, 5))
        self.b_divisor.setFrameShape(QFrame.StyledPanel)
        self.b_divisor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.b_divisor)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.divisor = QFrame(self.b_divisor)
        self.divisor.setObjectName(u"divisor")
        self.divisor.setFrameShape(QFrame.HLine)
        self.divisor.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.divisor)


        self.verticalLayout_6.addWidget(self.b_divisor, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.a_cabecalho, 0, Qt.AlignTop)

        self.b_corpo = QFrame(self.c_corpo)
        self.b_corpo.setObjectName(u"b_corpo")
        sizePolicy2.setHeightForWidth(self.b_corpo.sizePolicy().hasHeightForWidth())
        self.b_corpo.setSizePolicy(sizePolicy2)
        self.b_corpo.setFrameShape(QFrame.StyledPanel)
        self.b_corpo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.b_corpo)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout.addWidget(self.b_corpo)

        self.c_rodape = QFrame(self.c_corpo)
        self.c_rodape.setObjectName(u"c_rodape")
        self.c_rodape.setFrameShape(QFrame.StyledPanel)
        self.c_rodape.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.c_rodape)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.espacador = QFrame(self.c_rodape)
        self.espacador.setObjectName(u"espacador")
        self.espacador.setFrameShape(QFrame.StyledPanel)
        self.espacador.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.espacador)

        self.espacador_2 = QFrame(self.c_rodape)
        self.espacador_2.setObjectName(u"espacador_2")
        self.espacador_2.setMinimumSize(QSize(10, 10))
        self.espacador_2.setMaximumSize(QSize(10, 10))
        self.espacador_2.setFrameShape(QFrame.StyledPanel)
        self.espacador_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.espacador_2, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.c_rodape, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.c_corpo)

        Organizador.setCentralWidget(self.widget_central)

        self.retranslateUi(Organizador)

        QMetaObject.connectSlotsByName(Organizador)
    # setupUi

    def home_page(self, Organizador):
        self.frame = QFrame(self.b_corpo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame)

        self.frame_3 = QFrame(self.b_corpo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.imagem = QLabel(self.frame_3)
        self.imagem.setObjectName(u"imagem")
        self.imagem.setPixmap(QPixmap(u"../side/logo.png"))
        self.imagem.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.imagem)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.b_corpo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_2)

    def retranslateUi(self, Organizador):
        Organizador.setWindowTitle(QCoreApplication.translate("Organizador", u"MainWindow", None))
        self.a_botao_home.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Home</p></body></html>", None))
        self.a_botao_home.setText("")
        self.b_botao_pedido.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Pedidos</p></body></html>", None))
        self.b_botao_pedido.setText("")
        self.c_botao_cliente.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Clientes</p></body></html>", None))
        self.c_botao_cliente.setText("")
        self.d_botao_item.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Itens</p></body></html>", None))
        self.d_botao_item.setText("")
        self.e_botao_relatorio.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Relat\u00f3rio</p></body></html>", None))
        self.e_botao_relatorio.setText("")
        self.a_botao_opcao.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Op\u00e7\u00f5es</p></body></html>", None))
        self.a_botao_opcao.setText("")
        self.b_botao_logout.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>LogOut</p></body></html>", None))
        self.b_botao_logout.setText("")
        self.nome_prog.setText(QCoreApplication.translate("Organizador", u"Organizador", None))
        self.a_minimizar.setText("")
        self.b_maximizar.setText("")
        self.c_fechar.setText("")
    # retranslateUi

if __name__ == '__main__':
    import sys

    class Tela(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Organizador()
            self.ui.setupUi(self)

            #self.landing_page = [
            #    self.ui.frame,
            #    self.ui.frame_2,
            #    self.ui.frame_3,
            #    self.imagem,
            #]

            #  Comportamento
            self.estilo = "QPushButton:pressed{background-color: none; color: none; border: none;}"
            estilo_a_trocar = [self.ui.a_minimizar, self.ui.b_maximizar, self.ui.c_fechar,
                               self.ui.a_botao_home, self.ui.b_botao_pedido, self.ui.c_botao_cliente,
                               self.ui.d_botao_item, self.ui.e_botao_relatorio, self.ui.a_botao_opcao,
                               self.ui.b_botao_logout]
            for item in estilo_a_trocar: item.setStyleSheet(self.estilo)

            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            self.sombra = QGraphicsDropShadowEffect(self)
            self.sombra.setBlurRadius(50)
            self.sombra.setXOffset(0)
            self.sombra.setYOffset(0)
            self.sombra.setColor(QColor(0,92,157,550))
            
            self.ui.widget_central.setGraphicsEffect(self.sombra)

            self.setWindowIcon(QtGui.QIcon(':/icons/icones/basket.svg'))
            self.setWindowTitle('Organizador')

            # Eventos
            self.ui.a_container.mouseMoveEvent = self.movendo_janela
            
            self.ui.a_minimizar.clicked.connect(lambda: self.showMinimized())
            self.ui.b_maximizar.clicked.connect(self.aplicando_e_retornando_maximizar)
            self.ui.c_fechar.clicked.connect(lambda: self.close())

            self.ui.b_slot_2.setMaximumHeight(0)
            self.ui.a_botao_home.clicked.connect(self.exibindo_ocultando_menu)

            QSizeGrip(self.ui.espacador_2)

        def aplicando_e_retornando_maximizar(self):
            if self.isMaximized():
                self.showNormal()
                self.ui.b_maximizar.setIcon(QtGui.QIcon(':/icons/icones/expand.svg'))
            else:
                self.showMaximized()
                self.ui.b_maximizar.setIcon(QtGui.QIcon(':/icons/icones/contract.svg'))

        def movendo_janela(self, mouse):
            if not self.isMaximized():
                if mouse.buttons() == Qt.LeftButton:
                    self.move(self.pos() + mouse.globalPos() - self.posicao_mouse)
                    self.posicao_mouse = mouse.globalPos()
                    mouse.accept()
        
        def mousePressEvent(self, event):
            self.posicao_mouse = event.globalPos()

        def exibindo_ocultando_menu(self): #282
            altura = self.ui.b_slot_2.height()

            if altura == 0:
                nova_altura = 200
            else:
                nova_altura = 0

            self.animacao = QPropertyAnimation(self.ui.b_slot_2, b'maximumHeight')
            self.animacao.setDuration(1000)
            self.animacao.setStartValue(altura)
            self.animacao.setEndValue(nova_altura)
            self.animacao.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacao.start()

        def iniciando_aplicacao(self):
            pass

    app = QApplication(sys.argv)
    janela = Tela()
    janela.show()
    sys.exit(app.exec_())