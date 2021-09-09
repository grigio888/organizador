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

from side.janelas.ui_main import *
from side.janelas.ui_widget_1_landingpage import *
from side.janelas.ui_widget_2_pedido import *
from side.janelas.ui_widget_3_cadastro_cliente import *

if __name__ == '__main__':
    pass