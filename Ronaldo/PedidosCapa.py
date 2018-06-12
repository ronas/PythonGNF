# -*- coding: iso-8859-15 -*-

#---------------------------------------------------------------------------------------------
#
#   Criação da Base de Testes ....
#
#   CREATE DATABASE lojadb;
#   
#   CREATE TABLE `lojadb`.`pedidocapa` (
#     `Pedido` INT NOT NULL,
#     `Cliente_Cod` VARCHAR(10) NOT NULL,
#     `Cliente_Nome` VARCHAR(50) NULL,
#     `Data` DATETIME NULL,
#     PRIMARY KEY (`Pedido`));
#   
#   CREATE TABLE `lojadb`.`pedidolinha` (
#     `Pedido` INT NOT NULL,
#     `Linha` INT NOT NULL, 
#     `Produto_Cod` VARCHAR(10) NOT NULL,
#     `Quantidade` VARCHAR(50) NULL,
#     PRIMARY KEY (`Pedido`,`Linha`)
#   );
#   
#   CREATE TABLE `lojadb`.`produtos` (
#     `Codigo` VARCHAR(10) NOT NULL,
#     `Descricao`  VARCHAR(50) NOT NULL,
#     PRIMARY KEY (`Codigo`)
#   );
#   
#   CREATE TABLE `lojadb`.`parceiros` (
#     `Codigo` VARCHAR(10) NOT NULL,
#     `Nome`  VARCHAR(50) NOT NULL,
#     PRIMARY KEY (`Codigo`)
#   );
#   
#   INSERT INTO `lojadb`.`parceiros` VALUES('0000000001','ACME MATERIAIS DE ESCRITÓRIO');
#   INSERT INTO `lojadb`.`parceiros` VALUES('0000000002','AJAX PRODUTOS DE LIMPEZA');
#   INSERT INTO `lojadb`.`parceiros` VALUES('0000000003','CONSTRUTORA APOLLO LTDA');
#   
#   INSERT INTO `lojadb`.`produtos`  VALUES('ESC0000001','CARTOLINA');
#   INSERT INTO `lojadb`.`produtos`  VALUES('ESC0000002','CANETA');
#   INSERT INTO `lojadb`.`produtos`  VALUES('ESC0000003','LAPIS');
#   INSERT INTO `lojadb`.`produtos`  VALUES('LIM0000001','SABONETE');
#   INSERT INTO `lojadb`.`produtos`  VALUES('LIM0000002','PAPÉL');
#   INSERT INTO `lojadb`.`produtos`  VALUES('LIM0000003','DESINFETANTE');
#   INSERT INTO `lojadb`.`produtos`  VALUES('SERV000001','PINTURA');
#   INSERT INTO `lojadb`.`produtos`  VALUES('SERV000002','ALVENARIA');
#   INSERT INTO `lojadb`.`produtos`  VALUES('SERV000003','SERRALHERIA');
#
#   INSERT INTO `lojadb`.`pedidocapa`  VALUES(1,'0000000001','ACME MATERIAIS DE ESCRITÓRIO','2018-06-12');
#   INSERT INTO `lojadb`.`pedidolinha`  VALUES(1,1,'ESC0000001',10);
#   INSERT INTO `lojadb`.`pedidolinha`  VALUES(1,2,'ESC0000003',30);
#   INSERT INTO `lojadb`.`pedidolinha`  VALUES(1,3,'ESC0000002',15);
#   
#   INSERT INTO `lojadb`.`pedidocapa`  VALUES(2,'0000000002','AJAX PRODUTOS DE LIMPEZA','2018-06-12');
#   INSERT INTO `lojadb`.`pedidolinha`  VALUES(2,1,'LIM0000001',10);
#   INSERT INTO `lojadb`.`pedidolinha`  VALUES(2,2,'LIM0000002',55);
#   
#   INSERT INTO `lojadb`.`pedidocapa`  VALUES(3,'0000000003','CONSTRUTORA APOLLO LTDA','2018-06-12');
#   INSERT INTO `lojadb`.`pedidolinha`  VALUES(3,1,'SERV000001',10);
#   
#   INSERT INTO `lojadb`.`pedidocapa`  VALUES(4,'0000000001','ACME MATERIAIS DE ESCRITÓRIO','2018-06-12');
#   INSERT INTO `lojadb`.`pedidolinha`  VALUES(4,1,'ESC0000002',2);
#   INSERT INTO `lojadb`.`pedidolinha`  VALUES(4,2,'ESC0000001',5);
#---------------------------------------------------------------------------------------------

import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QToolTip, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt

import pymysql

config = {'host':'localhost',# criando metodo de entrada do Mysql
          'port':3306,
          'database':'lojadb',
          'user':'root',
          'password':'12345'}

db = pymysql.connect(** config)# criando ponteiro que o intermediario
cursor = db.cursor()

class ClasseAPP(QWidget):

    def __init__(self):
        super(ClasseAPP, self).__init__()
        self.initUI()

    def initUI(self):

        super(ClasseAPP, self).__init__()

        self.setGeometry(300, 200, 0, 0)
        self.setFixedSize(850, 400)
        self.setWindowTitle("Pedidos")
        #self.setWindowIcon(QIcon('pythonlogo.png'))

        self.CriarFormulario()

    def CriarFormulario(self):

      # Pedido ...
        self.lblPedido = QLabel("Pedido:",self)
        self.lblPedido.setGeometry(30, 260, 50, 17)
        self.txtPedido = QLineEdit(self)
        self.txtPedido.setGeometry(130, 260, 90, 21)

      # Data ...
        self.lblNome = QLabel("Data:",self)
        self.lblNome.setGeometry(240, 260, 50, 17)
        self.txtNome = QLineEdit(self)
        self.txtNome.setGeometry(300, 260, 90, 21)        

      # Parceiro ...
        self.lblParceiro = QLabel("Parceiro:",self)
        self.lblParceiro.setGeometry(30, 290, 68, 17)
        self.txtParceiro = QLineEdit(self)
        self.txtParceiro.setGeometry(130, 290, 90, 21)

      # Nome ...
        self.lblData = QLabel("Nome:",self)
        self.lblData.setGeometry(240, 290, 68, 17)
        self.txtData = QLineEdit(self)
        self.txtData.setGeometry(300, 290, 421,21)
 
      # Tabela ...
        self.tabela = QTableWidget(3,11,self)
        self.tabela.setGeometry(30, 20, 800, 211)
        self.tabela.setColumnCount(4)
        self.tabela.setRowCount(3)
        self.tabela.setHorizontalHeaderLabels(('Pedido', 'Parceiro', 'Nome','Data'))

      # Criar Botões ...
        btnincluir = QPushButton("&Incluir",self)
        btnincluir.setGeometry(20, 350, 115, 35)

        btnalterar = QPushButton("&Excluir",self)
        btnalterar.setGeometry(140, 350, 115, 35)

        btnsair = QPushButton("&Sair",self)
        btnsair.setGeometry(730, 350, 105, 35)
        btnsair.clicked.connect(self.close_application)

        self.PopularTabela()

        self.show()
   
    def PopularTabela(self):

        pt_cursor = db.cursor()                                                              # Cria cursor para leitura dos registros ...
        pt_cursor.execute("select * from pedidocapa")                                        # Lê os registros do banco de dados ...

        self.tabela.setRowCount(0)                                                           # Remove todas as linhas da tabela ...

        for registro in pt_cursor:                                                           # Loop para ler todos os registros ...
            numeroLinhas = self.tabela.rowCount()                                            # Verifica a quantidade de linhas na tabela ...
            self.tabela.insertRow(numeroLinhas)                                              # Inclui uma nova linha na tabela ...

            item = QTableWidgetItem( str(registro[0])       )                                # Para realizar o alinhamento de uma célula é necessário criar o WidgetItem primeiro ...
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)                           # ... e depois os atributos são definidos.
            item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)                              # Define os indicadores do  campo para não permitir alteração na coluna do código.
            #item.clicked.connect(self.CarregaCampos)
            self.tabela.setItem(numeroLinhas, 0, item)

            self.tabela.setItem(numeroLinhas, 1, QTableWidgetItem( registro[1]            ))
            self.tabela.setItem(numeroLinhas, 2, QTableWidgetItem( registro[2]            ))
            self.tabela.setItem(numeroLinhas, 3, QTableWidgetItem( str(registro[3])[0:10] )) # Converte a data para formato string e seleciona apenas os 10 primeiros caracteres ...

        self.tabela.resizeColumnsToContents()                                                # Do the resize of the columns by content

        pt_cursor.close()

    #def CarregaCampos(self):

        #self.txtNome.setText("XXXX")

    def close_application(self):
        print("Fim!!!")
        sys.exit()



def main():
    app = QApplication(sys.argv)
    ui = ClasseAPP()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
