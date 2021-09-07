from PySide2 import QtCore, QtGui
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QPropertyAnimation)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sys

class myApplication(QMainWindow):
    def __init__(self, parent=None):
        super(myApplication, self).__init__(parent)

        self.setWindowTitle('No Tool is Selected')

        #---- create instance of each tool widget ----

        self.tool1 = Tool1(self)
        self.tool2 = Tool2(self)

        #---- layout for central widget ----

        centralWidget = QWidget()
        centralLayout = QGridLayout()
        centralLayout.addWidget(self.tool1, 0, 0)
        centralLayout.addWidget(self.tool2, 1, 0)
        centralWidget.setLayout(centralLayout)

        self.setCentralWidget(centralWidget)  

        #---- set the menu bar ----

        contentMenu = self.menuBar().addMenu(("Tools"))
        contentMenu.addAction('show Tool 1', self.show_Tool1)
        contentMenu.addAction('show Tool 2', self.show_Tool2)
        contentMenu.addAction('show All', self.show_All)

    def show_Tool1(self):
        self.tool1.show()
        self.tool2.hide()
        self.setWindowTitle('Tool #1 is Selected')

    def show_Tool2(self):
        self.tool1.hide()
        self.tool2.show()
        self.setWindowTitle('Tool #2 is Selected')

    def show_All(self):
        self.tool1.show()
        self.tool2.show()
        self.setWindowTitle('All Tools are Selected')

class Tool1(QWidget):
    def __init__(self, parent=None):
        super(Tool1, self).__init__(parent)

        layout = QGridLayout()
        layout.addWidget(QPushButton('Tool #1'))
        self.setLayout(layout)
        self.hide()

class Tool2(QWidget):
    def __init__(self, parent=None):
        super(Tool2, self).__init__(parent)

        layout = QGridLayout()
        layout.addWidget(QTextEdit('Tool #2'))
        self.setLayout(layout)
        self.hide()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    instance = myApplication()  
    instance.show()    
    sys.exit(app.exec_())