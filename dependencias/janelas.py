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

from side.janelas.ui_a_login import Ui_Login
from side.janelas.ui_main import Ui_Organizador
from side.janelas.ui_widget_1_landingpage import Ui_LandingPage
from side.janelas.ui_widget_2_pedido import Ui_Pedido
from side.janelas.ui_widget_3_cadastro_cliente import Ui_cadastro_cliente
from side.janelas.ui_janela_aviso import Ui_MainWindow
from side.janelas.ui_widget_4_cadastro_item import Ui_cadastro_item

if __name__ == '__main__':
    pass