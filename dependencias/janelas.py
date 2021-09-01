from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Organizador(object):
    def setupUi(self, Organizador):
        if Organizador.objectName():
            Organizador.setObjectName(u"Organizador")
        Organizador.resize(210, 200)
        Organizador.setMinimumSize(QSize(210, 200))
        Organizador.setMaximumSize(QSize(210, 200))
        self.centralwidget = QWidget(Organizador)
        self.centralwidget.setObjectName(u"centralwidget")
        self.texto_login = QLabel(self.centralwidget)
        self.texto_login.setObjectName(u"texto_login")
        self.texto_login.setGeometry(QRect(20, 70, 47, 21))
        self.texto_senha = QLabel(self.centralwidget)
        self.texto_senha.setObjectName(u"texto_senha")
        self.texto_senha.setGeometry(QRect(20, 110, 47, 21))
        self.campo_login = QLineEdit(self.centralwidget)
        self.campo_login.setObjectName(u"campo_login")
        self.campo_login.setGeometry(QRect(60, 70, 131, 20))
        self.campo_senha = QLineEdit(self.centralwidget)
        self.campo_senha.setObjectName(u"campo_senha")
        self.campo_senha.setGeometry(QRect(60, 110, 131, 20))
        self.botao_login = QPushButton(self.centralwidget)
        self.botao_login.setObjectName(u"botao_login")
        self.botao_login.setGeometry(QRect(70, 150, 75, 23))
        self.botao_opcoes = QPushButton(self.centralwidget)
        self.botao_opcoes.setObjectName(u"botao_opcoes")
        self.botao_opcoes.setGeometry(QRect(180, 170, 21, 23))
        Organizador.setCentralWidget(self.centralwidget)
        self.retranslateUi(Organizador)
        QMetaObject.connectSlotsByName(Organizador)

    def retranslateUi(self, Organizador):
        Organizador.setWindowTitle(QCoreApplication.translate("Organizador", u"Organizador", None))
        self.texto_login.setText(QCoreApplication.translate("Organizador", u"Login:", None))
        self.texto_senha.setText(QCoreApplication.translate("Organizador", u"Senha:", None))
        self.botao_login.setText(QCoreApplication.translate("Organizador", u"Login", None))
        self.botao_opcoes.setToolTip(QCoreApplication.translate("Organizador", u"Op\u00e7\u00f5es", None))
        self.botao_opcoes.setText(QCoreApplication.translate("Organizador", u"...", None))