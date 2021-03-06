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

class Ui_Organizador(object):
    def setupUi(self, Organizador):
        if Organizador.objectName():
            Organizador.setObjectName(u"Organizador")
        Organizador.resize(630, 550)
        Organizador.setMinimumSize(QSize(630, 550))
        Organizador.setStyleSheet(stylesheet)
        self.centralwidget = QWidget(Organizador)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255,255,255);\nborder-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.a_menu_esquerda = QFrame(self.frame)
        self.a_menu_esquerda.setObjectName(u"a_menu_esquerda")
        self.a_menu_esquerda.setMaximumSize(QSize(60, 16777215))
        self.a_menu_esquerda.setStyleSheet(u"background-color: rgb(200,220,220);")
        self.a_menu_esquerda.setFrameShape(QFrame.StyledPanel)
        self.a_menu_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.a_menu_esquerda)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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
        self.a_slot_1.setStyleSheet(u"background-color: rgb(180,200,200);")
        self.a_slot_1.setFrameShape(QFrame.StyledPanel)
        self.a_slot_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.a_slot_1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.a_botao_home = QPushButton(self.a_slot_1)
        self.a_botao_home.setObjectName(u"a_botao_home")
        icon = QIcon()
        icon.addFile(u":/icons/icones/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.a_botao_home.setIcon(icon)
        self.a_botao_home.setIconSize(QSize(25, 25))
        self.a_botao_home.setCheckable(False)
        self.a_botao_home.setFlat(True)

        self.horizontalLayout_5.addWidget(self.a_botao_home, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.a_slot_1)

        self.b_slot_2 = QFrame(self.a_menu_superior)
        self.b_slot_2.setObjectName(u"b_slot_2")
        self.b_slot_2.setMaximumSize(QSize(16777215, 200))
        self.b_slot_2.setFrameShape(QFrame.StyledPanel)
        self.b_slot_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.b_slot_2)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 7, 0, 15)
        self.b_botao_pedido = QPushButton(self.b_slot_2)
        self.b_botao_pedido.setObjectName(u"b_botao_pedido")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icones/document-edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_botao_pedido.setIcon(icon1)
        self.b_botao_pedido.setIconSize(QSize(20, 20))
        self.b_botao_pedido.setFlat(True)

        self.verticalLayout_4.addWidget(self.b_botao_pedido, 0, Qt.AlignHCenter)

        self.c_botao_cliente = QPushButton(self.b_slot_2)
        self.c_botao_cliente.setObjectName(u"c_botao_cliente")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icones/user-id.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.c_botao_cliente.setIcon(icon2)
        self.c_botao_cliente.setIconSize(QSize(20, 20))
        self.c_botao_cliente.setFlat(True)

        self.verticalLayout_4.addWidget(self.c_botao_cliente, 0, Qt.AlignHCenter)

        self.d_botao_item = QPushButton(self.b_slot_2)
        self.d_botao_item.setObjectName(u"d_botao_item")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icones/to-do.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.d_botao_item.setIcon(icon3)
        self.d_botao_item.setIconSize(QSize(20, 20))
        self.d_botao_item.setFlat(True)

        self.verticalLayout_4.addWidget(self.d_botao_item, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.e_botao_relatorio = QPushButton(self.b_slot_2)
        self.e_botao_relatorio.setObjectName(u"e_botao_relatorio")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icones/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.e_botao_relatorio.setIcon(icon4)
        self.e_botao_relatorio.setIconSize(QSize(20, 20))
        self.e_botao_relatorio.setFlat(True)

        self.verticalLayout_4.addWidget(self.e_botao_relatorio, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.b_slot_2)


        self.verticalLayout_3.addWidget(self.a_menu_superior, 0, Qt.AlignTop)

        self.b_menu_inferior = QFrame(self.a_menu_esquerda)
        self.b_menu_inferior.setObjectName(u"b_menu_inferior")
        self.b_menu_inferior.setMinimumSize(QSize(0, 67))
        self.b_menu_inferior.setFrameShape(QFrame.StyledPanel)
        self.b_menu_inferior.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.b_menu_inferior)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.a_botao_opcao = QPushButton(self.b_menu_inferior)
        self.a_botao_opcao.setObjectName(u"a_botao_opcao")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icones/gear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.a_botao_opcao.setIcon(icon5)
        self.a_botao_opcao.setIconSize(QSize(20, 20))
        self.a_botao_opcao.setFlat(True)

        self.verticalLayout_8.addWidget(self.a_botao_opcao)

        self.b_botao_logout = QPushButton(self.b_menu_inferior)
        self.b_botao_logout.setObjectName(u"b_botao_logout")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icones/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_botao_logout.setIcon(icon6)
        self.b_botao_logout.setIconSize(QSize(20, 20))
        self.b_botao_logout.setFlat(True)

        self.verticalLayout_8.addWidget(self.b_botao_logout)


        self.verticalLayout_3.addWidget(self.b_menu_inferior, 0, Qt.AlignBottom)


        self.horizontalLayout_8.addWidget(self.a_menu_esquerda)

        self.c_corpo = QFrame(self.frame)
        self.c_corpo.setObjectName(u"c_corpo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_corpo.sizePolicy().hasHeightForWidth())
        self.c_corpo.setSizePolicy(sizePolicy)
        self.c_corpo.setFrameShape(QFrame.StyledPanel)
        self.c_corpo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.c_corpo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_2.setContentsMargins(0, 5, 5, 5)
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
        self.nome_prog.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(8)
        self.nome_prog.setFont(font)
        self.nome_prog.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.nome_prog, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.a_nome, 0, Qt.AlignHCenter|Qt.AlignVCenter)

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


        self.verticalLayout_2.addWidget(self.a_cabecalho, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.c_corpo)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setMaximumSize(QSize(16777215, 2))
        self.frame_5.setStyleSheet(u"background-color: rgb(180,180,180);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.b_corpo = QFrame(self.c_corpo)
        self.b_corpo.setObjectName(u"b_corpo")
        sizePolicy2.setHeightForWidth(self.b_corpo.sizePolicy().hasHeightForWidth())
        self.b_corpo.setSizePolicy(sizePolicy2)
        self.b_corpo.setFrameShape(QFrame.StyledPanel)
        self.b_corpo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.b_corpo)

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
        self.espacador_2.setMinimumSize(QSize(12, 12))
        self.espacador_2.setMaximumSize(QSize(12, 12))
        self.espacador_2.setFrameShape(QFrame.StyledPanel)
        self.espacador_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.espacador_2, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.c_rodape, 0, Qt.AlignBottom)


        self.horizontalLayout_8.addWidget(self.c_corpo)


        self.horizontalLayout.addWidget(self.frame)

        Organizador.setCentralWidget(self.centralwidget)

        self.retranslateUi(Organizador)

        QMetaObject.connectSlotsByName(Organizador)
    # setupUi

    def retranslateUi(self, Organizador):
        Organizador.setWindowTitle(QCoreApplication.translate("Organizador", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.a_botao_home.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Home</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.a_botao_home.setText("")
#if QT_CONFIG(tooltip)
        self.b_botao_pedido.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Pedidos</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_botao_pedido.setText("")
#if QT_CONFIG(tooltip)
        self.c_botao_cliente.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Clientes</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.c_botao_cliente.setText("")
#if QT_CONFIG(tooltip)
        self.d_botao_item.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Itens</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.d_botao_item.setText("")
#if QT_CONFIG(tooltip)
        self.e_botao_relatorio.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Relat\u00f3rio</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.e_botao_relatorio.setText("")
#if QT_CONFIG(tooltip)
        self.a_botao_opcao.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>Op\u00e7\u00f5es</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.a_botao_opcao.setText("")
#if QT_CONFIG(tooltip)
        self.b_botao_logout.setToolTip(QCoreApplication.translate("Organizador", u"<html><head/><body><p>LogOut</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_botao_logout.setText("")
        self.nome_prog.setText(QCoreApplication.translate("Organizador", u"Organizador", None))
        self.a_minimizar.setText("")
        self.b_maximizar.setText("")
        self.c_fechar.setText("")
    # retranslateUi

if __name__ == '__main__':

    class Tela(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Organizador()
            self.ui.setupUi(self)

            # - Comportamento
            # -- retirada do frame padr??o do Windows.
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # -- adicionar sombra ?? janela principal.
            self.sombra = QGraphicsDropShadowEffect(self)
            self.sombra.setBlurRadius(50)
            self.sombra.setXOffset(0)
            self.sombra.setYOffset(0)
            self.sombra.setColor(QColor(0,92,157,550))
            self.ui.centralwidget.setGraphicsEffect(self.sombra)

            # -- adicionar icone e titulo ?? pagina.
            self.setWindowIcon(QIcon(':/icons/icones/basket.svg'))
            self.setWindowTitle('Organizador')


            # - Eventos
            # -- fun????o de arrastar a janela ao clicar no titulo.
            self.ui.a_nome.mouseMoveEvent = self.movendo_janela
            
            # -- fun????o basica de controle da janela.
            self.ui.c_fechar.clicked.connect(self.close)
        

        def movendo_janela(self, mouse): # fun????o prioridade global
            if not self.isMaximized():
                if mouse.buttons() == Qt.LeftButton:
                    self.move(self.pos() + mouse.globalPos() - self.posicao_mouse)
                    self.posicao_mouse = mouse.globalPos()
                    mouse.accept()
        
        def mousePressEvent(self, event): # fun????o prioridade global
            self.posicao_mouse = event.globalPos()

    app = QApplication(sys.argv)
    janela = Tela()
    janela.show()
    sys.exit(app.exec_())