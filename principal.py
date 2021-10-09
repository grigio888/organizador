import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Signal
from dependencias.janelas import *
from dependencias.models_peewee import *
from dependencias.erros import *
from side.janelas.ui_janela_aviso import Ui_MainWindow

class WidgetLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # - Modulos a serem utilizados:
        self.db = PeeweeLogin()


        # - Transicao:
        self.proximo = Tela()
        self.proximo.hide()


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
        self.ui.login_botao.setStyleSheet(self.estilo)


        # - Eventos
        # -- função de arrastar a janela ao clicar no titulo.
        self.ui.para_arrastar.mouseMoveEvent = self.movendo_janela
        
        # -- função basica de controle da janela.
        self.ui.c_fechar.clicked.connect(lambda: self.close())

        # -- gatilho para transitar para o main
        self.ui.login_botao.clicked.connect(self.avancar)
    

    def avancar(self):
        try:
            validador = self.db.get(PeeweeLogin.login == self.ui.login_campo.text())
            if validador.senha == self.ui.senha_campo.text():
                self.proximo.show()
                self.hide()
            else: raise Exception
        except:
            print('ta errado')

    def movendo_janela(self, mouse): # função prioridade global
        if not self.isMaximized():
            if mouse.buttons() == Qt.LeftButton:
                self.move(self.pos() + mouse.globalPos() - self.posicao_mouse)
                self.posicao_mouse = mouse.globalPos()
                mouse.accept()
    
    def mousePressEvent(self, event): # função prioridade global
        self.posicao_mouse = event.globalPos()


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Organizador()
        self.ui.setupUi(self)


        # - Janelas a serem exibidas
        self.landing_page = WidgetLandingPage(self)
        self.pedido = WidgetPedido(self)
        self.cadastro_cliente = WidgetCadastroCliente(self)


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
        self.ui.verticalLayout.addWidget(self.cadastro_cliente, 0, Qt.AlignCenter)


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
        self.ui.c_botao_cliente.clicked.connect(self.exibir_cliente)

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
        self.animacao2.setDuration(500)
        self.animacao2.setStartValue(self.ui.b_menu_inferior.height())
        self.animacao2.setEndValue(nova_altura2)
        self.animacao2.setEasingCurve(QtCore.QEasingCurve.InOutQuint)

        self.animacao.start()
        self.animacao2.start()

    def exibir_landing_page(self):
        self.landing_page.show()
        self.pedido.hide()
        self.cadastro_cliente.hide()

    def exibir_pedido(self):
        self.landing_page.hide()
        self.pedido.show()
        self.cadastro_cliente.hide()
        self.exibindo_ocultando_menu()

    def exibir_cliente(self):
        self.landing_page.hide()
        self.pedido.hide()
        self.cadastro_cliente.show()
        self.exibindo_ocultando_menu()


class WidgetLandingPage(QWidget):
    def __init__(self, parent=None):
        super(WidgetLandingPage, self).__init__(parent)

        self.ui = Ui_LandingPage()
        self.ui.setupUi(self)

        # - Comportamento
        self.hide()

class WidgetPedido(QWidget):
    def __init__(self, parent=None):
        super(WidgetPedido, self).__init__(parent)

        self.ui = Ui_Pedido()
        self.ui.setupUi(self)

        # - Comportamento
        self.hide()


class WidgetCadastroCliente(QWidget):
    def __init__(self, parent=None):
        super(WidgetCadastroCliente, self).__init__(parent)

        self.ui = Ui_cadastro_cliente()
        self.ui.setupUi(self)

        self.cliente = PeeweeCliente()
        self.aviso = JanelaAviso()

        # - Comportamento:
        # -- zerando os campos dos formularios:
        self.zerando_cliente()
        self.ui.rem_c_remover_botao.setEnabled(False)
        
        # -- iniciando escondido:
        self.hide()


        # - Sinais:
        # -- disparando função de adicionar cadastro:
        self.ui.add_f_cadastrar_botao.clicked.connect(self.criando_cadastro)

        # -- disparando função de atualizar cadastro:
        self.ui.att_a_cliente_botao.clicked.connect(lambda: self.buscando_cadastro('att'))
        self.ui.att_h_atualizar_botao.clicked.connect(self.atualizando_cadastro)
        
        # -- disparando função de remover cadastro:
        self.ui.rem_a_cliente_botao.clicked.connect(lambda: self.excluindo_cadastro(1))
        self.ui.rem_c_remover_botao.clicked.connect(lambda: self.excluindo_cadastro(2))


    def zerando_cliente(self):
        itens = [
            self.ui.add_a_nome_campo,
            self.ui.add_b_id_campo,
            self.ui.add_c_end_campo,
            self.ui.add_d_tel_1_campo,
            self.ui.add_e_tel_2_campo
        ]

        for item in itens:
            item.setText('')

    def checando_campos_adicionar(self):
        if len(self.ui.add_a_nome_campo.text()) < 10:
            raise ClienteNomeNaoValido('Nome não válido.')
        elif len(self.ui.add_b_id_campo.text()) < 10 or not self.ui.add_b_id_campo.text().replace('-','').replace('.','').isdigit:
            raise ClienteIDNaoValido('ID não válido.')
        elif len(self.ui.add_c_end_campo.text()) < 10:
            raise ClienteEnderecoNaoValido('Endereço não válido.')
        elif len(self.ui.add_d_tel_1_campo.text()) < 9 or not self.ui.add_d_tel_1_campo.text().isdigit():
            raise ClienteEnderecoNaoValido('Telefone não válido.')

    def criando_cadastro(self):
        try:
            self.checando_campos_adicionar()
            self.cliente.create(
                nome = self.ui.add_a_nome_campo.text(),
                identidade = self.ui.add_b_id_campo.text().replace('-','').replace('.',''),
                endereco = self.ui.add_c_end_campo.text(),
                tel_1 = self.ui.add_d_tel_1_campo.text(),
                tel_2 = self.ui.add_e_tel_2_campo.text()
            )
            self.zerando_cliente()
            print('inserido')
        except Exception as e:
            print(e)

    def buscando_cadastro(self, campo):
        try:
            if campo == 'att':
                busca = self.ui.att_a_cliente_campo.text()
            elif campo == 'rem':
                busca = self.ui.rem_a_cliente_botao.text()

            try:
                comparativo = PeeweeCliente.get(PeeweeCliente.nome == busca)
            except:
                print('não é nome')
                try:
                    comparativo = PeeweeCliente.get(PeeweeCliente.identidade == busca)
                except:
                    print('nao é id')

            self.ui.att_c_nome_campo.setText(f'{comparativo.nome}')
            self.ui.att_d_id_campo.setText(f'{comparativo.identidade}')
            self.ui.att_e_end_campo.setText(f'{comparativo.endereco}')
            self.ui.att_f_tel_1_campo.setText(f'{comparativo.tel_1}')
            self.ui.att_g_tel_2_campo.setText(f'{comparativo.tel_2}')
        except:
            self.aviso.ui.label_2.setText('Cadastro não encontrado.')
            self.aviso.show()

    def atualizando_cadastro(self):
        try:
            comparativo = PeeweeCliente.get(PeeweeCliente.nome == self.ui.att_a_cliente_campo.text())

            comparativo.nome = self.ui.att_c_nome_campo.text()
            comparativo.identidade = int(self.ui.att_d_id_campo.text())
            comparativo.endereco = self.ui.att_e_end_campo.text()
            comparativo.tel_1 = self.ui.att_f_tel_1_campo.text()
            comparativo.tel_2 = self.ui.att_g_tel_2_campo.text()

            print(
                comparativo.nome,
                comparativo.identidade,
                comparativo.endereco,
                comparativo.tel_1,
                comparativo.tel_2,
            )

            comparativo.save()
            self.aviso.ui.label_2.setText('Cadastro Atualizado com Sucesso!')
            self.aviso.show()

        except Exception as erro:
            self.aviso.ui.label_2.setText(f'Não foi possivel atualizar.\nErro: {erro}.')
            self.aviso.show()

        finally:
            lista_de_checagem = [
                self.ui.att_a_cliente_campo.text(),
                self.ui.att_c_nome_campo.text(),
                self.ui.att_d_id_campo.text(),
                self.ui.att_e_end_campo.text(),
                self.ui.att_f_tel_1_campo.text(),
                self.ui.att_g_tel_2_campo.text()
            ]

    def excluindo_cadastro(self, etapa):
        comparativo = PeeweeCliente.get(PeeweeCliente.nome == self.ui.rem_a_cliente_campo.text())

        if etapa == 1:
            try:
                self.aviso.ui.label_2.setText(f'Cliente {comparativo.nome} foi escolhido')
                self.aviso.show()
                self.ui.rem_c_remover_botao.setEnabled(True)
            except:
                self.aviso.ui.label_2.setText('Cadastro não encontrado.')
                self.aviso.show()
                self.ui.rem_c_remover_botao.setEnabled(False)

        elif etapa == 2:
            try:
                nome = comparativo.nome
                if not self.ui.rem_b_ciente_checkbox.isChecked():
                    raise Exception
                comparativo.delete_instance()

                self.aviso.ui.label_2.setText(f'Cadastro {nome} excluido com sucesso.')
                self.aviso.show()
                self.ui.rem_a_cliente_campo.setText('')
                self.ui.rem_b_ciente_checkbox.setChecked(False)
                self.ui.rem_c_remover_botao.setEnabled(False)

            except Exception as erro:
                self.aviso.ui.label_2.setText('Cheque a caixa de ciente para confirmar a exclusão.')
                self.aviso.show()


class JanelaAviso(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        self.setWindowTitle('Aviso')

        # - Eventos
        # -- função de arrastar a janela ao clicar no titulo.
        self.ui.frame_8.mouseMoveEvent = self.movendo_janela

        # -- gatilho para transitar para o main
        self.ui.pushButton.clicked.connect(self.hide)
        self.hide()
    

    def movendo_janela(self, mouse): # função prioridade global
        if not self.isMaximized():
            if mouse.buttons() == Qt.LeftButton:
                self.move(self.pos() + mouse.globalPos() - self.posicao_mouse)
                self.posicao_mouse = mouse.globalPos()
                mouse.accept()
    
    def mousePressEvent(self, event): # função prioridade global
        self.posicao_mouse = event.globalPos()


app = QApplication(sys.argv)
janela = WidgetLogin()
janela.show()
sys.exit(app.exec_())