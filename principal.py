import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from dependencias.janelas import *
from dependencias.models_peewee import *
from dependencias.erros import *
from side.janelas.ui_janela_aviso import Ui_MainWindow


# TODO: Retirar essa artimanha da engenharia
login = ''


class Suporte(QMainWindow):
    def retirar_frame_padrao(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    
    def adicionar_sombra(self):
        self.sombra = QGraphicsDropShadowEffect(self)
        self.sombra.setBlurRadius(50)
        self.sombra.setXOffset(0)
        self.sombra.setYOffset(0)
        self.sombra.setColor(QColor(0,92,157,550))
        self.ui.centralwidget.setGraphicsEffect(self.sombra)

    def adicionar_icone_titulo(self, titulo):
        self.setWindowIcon(QtGui.QIcon(':/icons/icones/basket.svg'))
        self.setWindowTitle(titulo)

    def movendo_janela(self, mouse): # função prioridade global
        if not self.isMaximized():
            if mouse.buttons() == Qt.LeftButton:
                self.move(self.pos() + mouse.globalPos() - self.posicao_mouse)
                self.posicao_mouse = mouse.globalPos()
                mouse.accept()
    
    def mousePressEvent(self, event): # função prioridade global
        self.posicao_mouse = event.globalPos()

    def aplicando_e_retornando_maximizar(self):  # função prioridade global
        if self.isMaximized():
            self.showNormal()
            self.ui.b_maximizar.setIcon(QtGui.QIcon(':/icons/icones/expand.svg'))
        else:
            self.showMaximized()
            self.ui.b_maximizar.setIcon(QtGui.QIcon(':/icons/icones/contract.svg'))
    
    def emitindo_aviso(self, texto):
        self.aviso.ui.label_2.setText(texto)
        self.aviso.show()


class WidgetLogin(Suporte, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # - Modulos a serem utilizados:
        self.db = PeeweeLogin()
        self.aviso = JanelaAviso()


        # - Transicao:
        self.proximo = Tela()
        self.proximo.hide()


        # - Comportamento
        self.retirar_frame_padrao()
        self.adicionar_sombra()
        self.adicionar_icone_titulo('Login')
        

        # - Eventos
        # -- função de arrastar a janela ao clicar no titulo.
        self.ui.para_arrastar.mouseMoveEvent = self.movendo_janela
        
        # -- função basica de controle da janela.
        self.ui.c_fechar.clicked.connect(self.close)

        # -- gatilho para transitar para o main
        self.ui.login_botao.clicked.connect(self.avancar)

        self.automatico()
    
    def automatico(self):
        self.ui.login_campo.setText('grigio888')
        self.ui.senha_campo.setText('kiju1475')

    def avancar(self):
        global login
        try:
            validador = self.db.get(PeeweeLogin.login == self.ui.login_campo.text())
            if validador.senha == self.ui.senha_campo.text():
                self.proximo.show()
                self.hide()
                login = validador.login
            else: raise Exception
        except:
            self.emitindo_aviso('Login / Senha incorretos.')


class Tela(Suporte, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Organizador()
        self.ui.setupUi(self)


        # - Janelas a serem exibidas
        self.landing_page = WidgetLandingPage(self)
        self.pedido = WidgetPedido(self)
        self.cadastro_cliente = WidgetCadastroCliente(self)
        self.cadastro_item = WidgetCadastroItem(self)


        # -- adicionando as janelas a serem exibidas no corpo
        self.ui.verticalLayout = QVBoxLayout(self.ui.b_corpo)
        self.ui.verticalLayout.setObjectName(u"verticalLayout")
        
        self.ui.verticalLayout.addWidget(self.landing_page, 0, Qt.AlignCenter)
        self.landing_page.show()
        self.ui.verticalLayout.addWidget(self.pedido, 0, Qt.AlignCenter)
        self.ui.verticalLayout.addWidget(self.cadastro_cliente, 0, Qt.AlignCenter)
        self.ui.verticalLayout.addWidget(self.cadastro_item, 0, Qt.AlignCenter)


        # - Comportamento
        self.retirar_frame_padrao()
        self.adicionar_sombra()
        self.adicionar_icone_titulo('Organizador')


        # - Eventos
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
        self.ui.d_botao_item.clicked.connect(self.exibir_item)

        # -- função de controle do tamanho da janela.
        QSizeGrip(self.ui.espacador_2)


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
        self.cadastro_item.hide()

    def exibir_pedido(self):
        self.landing_page.hide()
        self.pedido.show()
        self.cadastro_cliente.hide()
        self.cadastro_item.hide()
        self.exibindo_ocultando_menu()

    def exibir_cliente(self):
        self.landing_page.hide()
        self.pedido.hide()
        self.cadastro_cliente.show()
        self.cadastro_item.hide()
        self.exibindo_ocultando_menu()

    def exibir_item(self):
        self.landing_page.hide()
        self.pedido.hide()
        self.cadastro_cliente.hide()
        self.cadastro_item.show()
        self.exibindo_ocultando_menu()


class WidgetLandingPage(QWidget):
    def __init__(self, parent=None):
        super(WidgetLandingPage, self).__init__(parent)

        self.ui = Ui_LandingPage()
        self.ui.setupUi(self)

        # - Comportamento
        self.hide()




class SuporteWidget(QWidget):
    def emitindo_aviso(self, texto):
        self.aviso.ui.label_2.setText(texto)
        self.aviso.show()


class WidgetPedido(SuporteWidget, QWidget):
    def __init__(self, parent=None):
        super(WidgetPedido, self).__init__(parent)

        self.ui = Ui_Pedido()
        self.ui.setupUi(self)

        # - Modulos a serem utilizados:
        self.cliente = PeeweePedido()
        self.aviso = JanelaAviso()


        # - Variaveis:
        self.relacao_itens = {}
        self.pontos_de_checagem = 0


        # - Comportamento
        # -- inserindo modelos de pedido.
        self.ui.a_header_modelo_combo.insertItem(0, 'Pedido de Compra')
        self.ui.a_header_modelo_combo.insertItem(1, 'Orçamento')

        # -- zerando os campos dos formularios:
        self.zerando_campos()
        self.ui.e_adicionar_botao.setEnabled(False)

        # -- iniciando escondido.
        self.hide()


        # - Sinais:
        self.ui.b_cliente_botao.clicked.connect(self.buscando_cliente)
        self.ui.tab_add_4_botao.clicked.connect(self.adicionando_itens)
        self.ui.tab_rem_4_botao.clicked.connect(self.removendo_itens)
        self.ui.e_adicionar_botao.clicked.connect(self.inserindo_pedido)

    def zerando_campos(self):
        zerar = [
            self.ui.b_cliente_campo,
            self.ui.d_obs_obs
        ]

        z1 = [
            self.ui.tab_add_3_campo,
            self.ui.tab_rem_3_campo,
        ]

        resetar = [
            self.ui.a_header_modelo_combo,
            self.ui.tab_add_2_combo,
            self.ui.tab_rem_2_combo,
        ]

        self.relacao_itens = {}
        self.exibindo_produtos()

        for item in zerar:
            item.setText('')

        for item in z1:
            item.setText('1')

        for item in resetar:
            item.setCurrentIndex(0)

    def buscando_cliente(self):
        try:
            PeeweeCliente.get(PeeweeCliente.nome == self.ui.b_cliente_campo.text())
            self.pontos_de_checagem += 1
            self.emitindo_aviso(f'Cliente {self.ui.b_cliente_campo.text()} selecionado.')
            self.buscando_produtos_disponiveis()
        except Exception as erro:
            self.emitindo_aviso(f'Cadastro não encontrado.\nErro: {erro}')
            self.ui.b_cliente_campo.setText('')

    def buscando_produtos_disponiveis(self):
        produto = PeeweeProduto.select()
        self.ui.tab_add_2_combo.clear()

        lista_de_produtos = [item.nome for item in produto]
        lista_de_produtos.sort()
        lista_de_produtos.reverse()

        for item in lista_de_produtos:
            self.ui.tab_add_2_combo.insertItem(-1, item)

    def exibindo_produtos(self):
        self.ui.campo_exibicao.setText('')

        for item in self.relacao_itens.keys():
            busca = PeeweeProduto.get(PeeweeProduto.nome == item)
            preco = int(busca.preco)*self.relacao_itens[item]
            preco = str(preco)[:-2]+','+str(preco)[-2:]
            self.ui.campo_exibicao.insertPlainText(f'{preco} = {self.relacao_itens[item]} x {item}.\n')

        self.atualizando_lista_itens_remover()

        self.autorizando_criacao_pedido()

    def autorizando_criacao_pedido(self):
        qt_itens = 0
        for item in [item for item in self.relacao_itens.keys()]: qt_itens += 1

        if qt_itens > 0: self.ui.e_adicionar_botao.setEnabled(True)
        else: self.ui.e_adicionar_botao.setEnabled(False)

    def atualizando_lista_itens_remover(self):
        self.ui.tab_rem_2_combo.clear()

        lista_de_produtos = [item for item in self.relacao_itens.keys()]
        lista_de_produtos.sort()
        lista_de_produtos.reverse()

        for item in lista_de_produtos:
            self.ui.tab_rem_2_combo.insertItem(-1, item)

    def adicionando_itens(self):
        item = self.ui.tab_add_2_combo.currentText()
        qt = self.ui.tab_add_3_campo.text()
        if item in self.relacao_itens.keys():
            self.relacao_itens[item] = int(qt) + self.relacao_itens[item]
        else: self.relacao_itens[item] = int(qt)
        self.exibindo_produtos()

    def removendo_itens(self):
        item = self.ui.tab_rem_2_combo.currentText()
        qt = self.ui.tab_rem_3_campo.text()
        if int(qt) < int(self.relacao_itens[item]):
            self.relacao_itens[item] = self.relacao_itens[item] - int(qt)
        else: self.relacao_itens.pop(item)
        self.exibindo_produtos()

    def inserindo_pedido(self):
        global login

        pin = token_creator(15)
        insercao = {}

        for nome_item in self.relacao_itens.keys():
            insercao[nome_item] = {
                'login'      : login,
                'modo'       : self.ui.a_header_modelo_combo.currentIndex(),
                'cliente'    : self.ui.b_cliente_campo.text(),
                'quantidade' : self.relacao_itens[nome_item],
                'observacao' : self.ui.d_obs_obs.toPlainText(),
                'token'      : pin
            }

        try:
            for chave in insercao:
                print(f'{chave} : {insercao[chave]}')
                PeeweePedido.create(
                    criado_por = insercao[chave]['login'],
                    criado_em = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),
                    modo = insercao[chave]['modo'],
                    cliente = insercao[chave]['cliente'],
                    produto = chave,
                    quantidade = insercao[chave]['quantidade'],
                    observacao = insercao[chave]['observacao'],
                    codigo = insercao[chave]['token']
                )

            self.zerando_campos()
            self.emitindo_aviso(f'Pedido cadastrado com sucesso.\nToken: {insercao[chave]["token"]}')
        except Exception as erro:
            self.emitindo_aviso(f'Erro ao cadastrar o pedido.\nErro: {erro}')


class WidgetCadastroCliente(SuporteWidget, QWidget):
    def __init__(self, parent=None):
        super(WidgetCadastroCliente, self).__init__(parent)

        self.ui = Ui_cadastro_cliente()
        self.ui.setupUi(self)

        # - Modulos a serem utilizados:
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
            self.ui.add_e_tel_2_campo,
            self.ui.att_a_cliente_campo,
            self.ui.att_c_nome_campo,
            self.ui.att_d_id_campo,
            self.ui.att_e_end_campo,
            self.ui.att_f_tel_1_campo,
            self.ui.att_g_tel_2_campo,
            self.ui.rem_a_cliente_campo
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
            self.emitindo_aviso(f'Cadastro {self.ui.add_a_nome_campo.text()} adicionado com sucesso.')
            self.zerando_cliente()
        except Exception as e:
            self.emitindo_aviso(f'Aconteceu um erro ao cadastrar.\nErro: {e}')

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
            self.emitindo_aviso('Cadastro não encontrado.')

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
            self.emitindo_aviso('Cadastro Atualizado com Sucesso!')

        except Exception as erro:
            self.emitindo_aviso(f'Não foi possivel atualizar.\nErro: {erro}.')

        finally:
            self.zerando_cliente()

    def excluindo_cadastro(self, etapa):
        comparativo = PeeweeCliente.get(PeeweeCliente.nome == self.ui.rem_a_cliente_campo.text())

        if etapa == 1:
            try:
                self.emitindo_aviso(f'Cliente {comparativo.nome} foi escolhido')
                self.ui.rem_c_remover_botao.setEnabled(True)
            except:
                self.emitindo_aviso('Cadastro não encontrado.')
                self.ui.rem_c_remover_botao.setEnabled(False)

        elif etapa == 2:
            try:
                nome = comparativo.nome
                if not self.ui.rem_b_ciente_checkbox.isChecked():
                    raise Exception
                comparativo.delete_instance()

                self.emitindo_aviso(f'Cadastro {nome} excluido com sucesso.')
                self.zerando_cliente()
                self.ui.rem_b_ciente_checkbox.setChecked(False)
                self.ui.rem_c_remover_botao.setEnabled(False)

            except Exception as erro:
                self.emitindo_aviso('Cheque a caixa de ciente para confirmar a exclusão.')


class WidgetCadastroItem(SuporteWidget, QWidget):
    def __init__(self, parent=None):
        super(WidgetCadastroItem, self).__init__(parent)

        self.ui = Ui_cadastro_item()
        self.ui.setupUi(self)

        # - Modulos a serem utilizados:
        self.cliente = PeeweeProduto()
        self.aviso = JanelaAviso()


        # - Comportamento:
        # -- zerando os campos dos formularios:
        self.zerando_campos()
        self.ui.rem_c_remover_botao.setEnabled(False)
        
        # -- iniciando escondido:
        self.hide()

        # -- inserindo opções no combobox:
        self.ui.add_b_tipo_lista.insertItem(0, 'Produto')
        self.ui.add_b_tipo_lista.insertItem(1, 'Serviço')
        self.ui.att_e_tipo_lista.insertItem(0, 'Produto')
        self.ui.att_e_tipo_lista.insertItem(1, 'Serviço')
        

        # - Sinais:
        # -- disparando função de adicionar item:
        self.ui.add_f_cadastrar_botao.clicked.connect(self.criando_cadastro)

        # -- disparando função de atualizar item:
        self.ui.att_a_produto_botao.clicked.connect(lambda: self.buscando_cadastro('att'))
        self.ui.att_h_atualizar_botao.clicked.connect(self.atualizando_cadastro)
        
        # -- disparando função de remover item:
        self.ui.rem_a_produto_botao.clicked.connect(lambda: self.excluindo_cadastro(1))
        self.ui.rem_c_remover_botao.clicked.connect(lambda: self.excluindo_cadastro(2))


    def zerando_campos(self):
        itens = [
            self.ui.add_a_produto_campo,
            self.ui.add_d_preco_campo,
            self.ui.att_a_produto_campo,
            self.ui.att_c_nome_campo,
            self.ui.att_d_id_campo,
            self.ui.att_f_preco_campo,
            self.ui.rem_a_produto_campo
        ]

        for item in itens:
            item.setText('')

    def checando_campos_adicionar(self):
        pass

    def criando_cadastro(self):
        try:
            #self.checando_campos_adicionar()
            self.cliente.create(
                nome = self.ui.add_a_produto_campo.text(),
                tipo = bool(self.ui.add_b_tipo_lista.currentIndex()),
                preco = self.ui.add_d_preco_campo.text().replace(',','')
            )
            self.zerando_campos()
            self.emitindo_aviso('Cadastro de Item bem-sucedido.')
        except Exception as e:
            self.emitindo_aviso(f'Erro ao realizar o cadastro.\nErro: {e}.')
        finally:
            print(self.ui.add_d_preco_campo.text().replace(',',''))

    def buscando_cadastro(self, campo):
        try:
            if campo == 'att':
                busca = self.ui.att_a_produto_campo.text()
            elif campo == 'rem':
                busca = self.ui.rem_a_produto_campo.text()

            try:
                comparativo = PeeweeProduto.get(PeeweeProduto.nome == busca)
            except:
                print('não é nome')
                try:
                    comparativo = PeeweeProduto.get(PeeweeProduto.id == busca)
                except:
                    print('nao é id')

            self.ui.att_c_nome_campo.setText(f'{comparativo.nome}')
            self.ui.att_d_id_campo.setText(f'{comparativo.id}')
            self.ui.att_e_tipo_lista.setCurrentIndex(int(comparativo.tipo))
            self.ui.att_f_preco_campo.setText(f'{str(comparativo.preco)[0:-2]+","+str(comparativo.preco)[-2:]}')
        except Exception as erro:
            self.emitindo_aviso(f'Item não encontrado.\nErro: {erro}')

    def atualizando_cadastro(self):
        try:
            comparativo = PeeweeProduto.get(PeeweeProduto.nome == self.ui.att_a_produto_campo.text())

            comparativo.nome = self.ui.att_c_nome_campo.text()
            comparativo.tipo = bool(self.ui.att_e_tipo_lista.currentIndex())
            comparativo.preco = self.ui.att_f_preco_campo.text()

            print(
                comparativo.nome,
                comparativo.tipo,
                comparativo.preco,
            )

            comparativo.save()
            self.emitindo_aviso('Item Atualizado com Sucesso!')

        except Exception as erro:
            self.emitindo_aviso(f'Não foi possivel atualizar.\nErro: {erro}.')

        finally:
            self.zerando_campos()

    def excluindo_cadastro(self, etapa):
        comparativo = PeeweeProduto.get(PeeweeProduto.nome == self.ui.rem_a_produto_campo.text())

        if etapa == 1:
            try:
                self.emitindo_aviso(f'Item {comparativo.nome} foi escolhido')
                self.ui.rem_c_remover_botao.setEnabled(True)
            except:
                self.emitindo_aviso('Item não encontrado.')
                self.ui.rem_c_remover_botao.setEnabled(False)

        elif etapa == 2:
            try:
                nome = comparativo.nome
                if not self.ui.rem_b_ciente_checkbox.isChecked():
                    raise Exception
                comparativo.delete_instance()

                self.emitindo_aviso(f'Item {nome} excluido com sucesso.')
                self.zerando_campos()
                self.ui.rem_b_ciente_checkbox.setChecked(False)
                self.ui.rem_c_remover_botao.setEnabled(False)

            except:
                self.emitindo_aviso('Cheque a caixa de ciente para confirmar a exclusão.')




class JanelaAviso(Suporte, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # - Comportamento
        self.retirar_frame_padrao()
        self.adicionar_sombra()
        self.adicionar_icone_titulo('Aviso')

        # - Eventos
        # -- função de arrastar a janela ao clicar no titulo.
        self.ui.frame_8.mouseMoveEvent = self.movendo_janela

        # -- gatilho para transitar para o main
        self.ui.botao_voltar.clicked.connect(self.hide)
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = WidgetLogin()
    janela.show()
    sys.exit(app.exec_())