import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Signal
from dependencias.janelas import *

class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Organizador()
        self.ui.setupUi(self)


        # - Janelas a serem exibidas
        self.landing_page = LandingPage(self)
        self.pedido = Pedido(self)


        # - Comportamento
        # -- retirada do frame padrão do Windows.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # -- adicionar sombra à janela principal.
        self.sombra = QGraphicsDropShadowEffect(self)
        self.sombra.setBlurRadius(50)
        self.sombra.setXOffset(0)
        self.sombra.setYOffset(0)
        self.sombra.setColor(QColor(0,92,157,550))
        self.ui.centralwidget.setGraphicsEffect(self.sombra)

        # -- adicionar icone e titulo à pagina.
        self.setWindowIcon(QtGui.QIcon(':/icons/icones/basket.svg'))
        self.setWindowTitle('Organizador')

        # -- retirada de sombra dos botões.
        self.estilo = "QPushButton:pressed{background-color: none; color: none; border: none;}"
        estilo_a_trocar = [self.ui.a_minimizar, self.ui.b_maximizar, self.ui.c_fechar,
                            self.ui.a_botao_home, self.ui.b_botao_pedido, self.ui.c_botao_cliente,
                            self.ui.d_botao_item, self.ui.e_botao_relatorio, self.ui.a_botao_opcao,
                            self.ui.b_botao_logout]
        for item in estilo_a_trocar: item.setStyleSheet(self.estilo)

        # -- adicionando as janelas a serem exibidas no corpo
        self.ui.verticalLayout = QVBoxLayout(self.ui.b_corpo)
        self.ui.verticalLayout.setObjectName(u"verticalLayout")
        
        self.ui.verticalLayout.addWidget(self.landing_page, 0, Qt.AlignCenter)
        self.landing_page.show()
        self.ui.verticalLayout.addWidget(self.pedido, 0, Qt.AlignCenter)


        # - Eventos
        # -- função de arrastar a janela ao clicar no titulo.
        self.ui.a_container.mouseMoveEvent = self.movendo_janela
        
        # -- função basica de controle da janela.
        self.ui.a_minimizar.clicked.connect(lambda: self.showMinimized())
        self.ui.b_maximizar.clicked.connect(self.aplicando_e_retornando_maximizar)
        self.ui.c_fechar.clicked.connect(lambda: self.close())

        # -- animação de exibição do menu principal.
        self.ui.b_slot_2.setMaximumHeight(0)
        self.ui.b_menu_inferior.setMaximumHeight(0)
        self.ui.a_botao_home.clicked.connect(self.exibindo_ocultando_menu)

        # -- gatilhos para exibicao dos contextos no corpo
        self.ui.b_botao_pedido.clicked.connect(self.exibir_pedido)

        # -- função de controle do tamanho da janela.
        QSizeGrip(self.ui.espacador_2)


    def aplicando_e_retornando_maximizar(self):  # função prioridade global
        if self.isMaximized():
            self.showNormal()
            self.ui.b_maximizar.setIcon(QtGui.QIcon(':/icons/icones/expand.svg'))
        else:
            self.showMaximized()
            self.ui.b_maximizar.setIcon(QtGui.QIcon(':/icons/icones/contract.svg'))

    def movendo_janela(self, mouse): # função prioridade global
        if not self.isMaximized():
            if mouse.buttons() == Qt.LeftButton:
                self.move(self.pos() + mouse.globalPos() - self.posicao_mouse)
                self.posicao_mouse = mouse.globalPos()
                mouse.accept()
    
    def mousePressEvent(self, event): # função prioridade global
        self.posicao_mouse = event.globalPos()

    def exibindo_ocultando_menu(self): # função prioridade global
        # TODO: Enxugar esse código.

        if self.ui.b_slot_2.height() == 0: nova_altura = 147
        else: nova_altura = 0

        if self.ui.b_menu_inferior.height() == 0: nova_altura2 = 67
        else: nova_altura2 = 0

        self.animacao = QPropertyAnimation(self.ui.b_slot_2, b'maximumHeight')
        self.animacao.setDuration(500)
        self.animacao.setStartValue(self.ui.b_slot_2.height())
        self.animacao.setEndValue(nova_altura)
        self.animacao.setEasingCurve(QtCore.QEasingCurve.InOutQuint)

        self.animacao2 = QPropertyAnimation(self.ui.b_menu_inferior, b'maximumHeight')
        self.animacao2.setDuration(700)
        self.animacao2.setStartValue(self.ui.b_menu_inferior.height())
        self.animacao2.setEndValue(nova_altura2)
        #self.animacao2.setEasingCurve(QtCore.QEasingCurve.InOutQuint)

        self.animacao.start()
        self.animacao2.start()

    def exibir_landing_page(self):
        self.landing_page.show()
        self.pedido.hide()

    def exibir_pedido(self):
        self.pedido.show()
        self.landing_page.hide()
        self.exibindo_ocultando_menu()

class LandingPage(QWidget):
    def __init__(self, parent=None):
        super(LandingPage, self).__init__(parent)

        self.ui = Ui_LandingPage()
        self.ui.setupUi(self)

        # - Comportamento
        self.hide()

class Pedido(QWidget):
    def __init__(self, parent=None):
        super(Pedido, self).__init__(parent)

        self.ui = Ui_Pedido()
        self.ui.setupUi(self)

        # - Comportamento
        self.hide()

app = QApplication(sys.argv)
janela = Tela()
janela.show()
sys.exit(app.exec_())