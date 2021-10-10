# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'a_loginteYcmx.ui'
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

stylesheet = open('side/janelas/padrao.css', 'r').read()

class Ui_Login(object):
    def setupUi(self, Login):
        if Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(290, 190)
        Login.setMinimumSize(QSize(290, 190))
        Login.setMaximumSize(QSize(290, 190))
        Login.setStyleSheet(stylesheet)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.fundo = QLabel(self.centralwidget)
        self.fundo.setObjectName(u"fundo")
        self.fundo.setGeometry(QRect(-1, 0, 290, 190))
        self.fundo.setPixmap(QPixmap("./side/fundo_login.png"))
        self.login_label = QLabel(self.centralwidget)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(10, 20, 271, 31))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(10)
        self.login_label.setFont(font)
        self.login_label.setAlignment(Qt.AlignCenter)
        self.login_campo = QLineEdit(self.centralwidget)
        self.login_campo.setObjectName(u"login_campo")
        self.login_campo.setGeometry(QRect(60, 70, 171, 20))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        self.login_campo.setFont(font1)
        self.login_campo.setAlignment(Qt.AlignCenter)
        self.senha_campo = QLineEdit(self.centralwidget)
        self.senha_campo.setObjectName(u"senha_campo")
        self.senha_campo.setGeometry(QRect(60, 110, 171, 20))
        self.senha_campo.setFont(font1)
        self.senha_campo.setEchoMode(QLineEdit.Password)
        self.senha_campo.setAlignment(Qt.AlignCenter)
        self.login_botao = QPushButton(self.centralwidget)
        self.login_botao.setObjectName(u"login_botao")
        self.login_botao.setGeometry(QRect(110, 150, 71, 23))
        self.login_botao.setFont(font1)
        self.c_fechar = QPushButton(self.centralwidget)
        self.c_fechar.setObjectName(u"c_fechar")
        self.c_fechar.setGeometry(QRect(260, 13, 20, 16))
        icon = QIcon()
        icon.addFile(u":/icons/icones/cross.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.c_fechar.setIcon(icon)
        self.c_fechar.setFlat(True)
        self.para_arrastar = QFrame(self.centralwidget)
        self.para_arrastar.setObjectName(u"para_arrastar")
        self.para_arrastar.setGeometry(QRect(10, 5, 271, 16))
        self.para_arrastar.setFrameShape(QFrame.StyledPanel)
        self.para_arrastar.setFrameShadow(QFrame.Raised)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.fundo.setText("")
        self.login_label.setText(QCoreApplication.translate("Login", u"Login", None))
        self.login_campo.setPlaceholderText(QCoreApplication.translate("Login", u"Login", None))
        self.senha_campo.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.login_botao.setText(QCoreApplication.translate("Login", u"Logar", None))
        self.c_fechar.setText("")
    # retranslateUi

if __name__ == '__main__':

    class Tela(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Login()
            self.ui.setupUi(self)

            # - Comportamento
            # -- retirada do frame padrão do Windows.
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # -- adicionar sombra à janela principal.
            self.sombra = QGraphicsDropShadowEffect(self)
            self.sombra.setBlurRadius(50)
            self.sombra.setXOffset(0)
            self.sombra.setYOffset(0)
            self.sombra.setColor(QColor(0,92,157,550))
            self.ui.centralwidget.setGraphicsEffect(self.sombra)

            # -- adicionar icone e titulo à pagina.
            self.setWindowIcon(QIcon(':/icons/icones/basket.svg'))
            self.setWindowTitle('Organizador')


            # - Eventos
            # -- função de arrastar a janela ao clicar no titulo.
            self.ui.para_arrastar.mouseMoveEvent = self.movendo_janela
            
            # -- função basica de controle da janela.
            self.ui.c_fechar.clicked.connect(self.close)

            # -- gatilho para transitar para o main
            self.ui.login_botao.clicked.connect(lambda: print('login'))
        

        def movendo_janela(self, mouse): # função prioridade global
            if not self.isMaximized():
                if mouse.buttons() == Qt.LeftButton:
                    self.move(self.pos() + mouse.globalPos() - self.posicao_mouse)
                    self.posicao_mouse = mouse.globalPos()
                    mouse.accept()
        
        def mousePressEvent(self, event): # função prioridade global
            self.posicao_mouse = event.globalPos()

    app = QApplication(sys.argv)
    janela = Tela()
    janela.show()
    sys.exit(app.exec_())