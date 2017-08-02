import sys
from PyQt4.QtGui import *
 
# Crie um objeto de aplicação PyQT4
a = QApplication(sys.argv)       
 
# O widget QWidget é a classe base de todos os objetos da interface do usuário no PyQt4.
w = QMainWindow()
 
# Defina o tamanho da janela. 
w.resize(320, 240)
 
# Defina o título da janela 
w.setWindowTitle("Hello World!") 
 
 # Criar menu principal
mainMenu = w.menuBar()
mainMenu.setNativeMenuBar(False)
fileMenu = mainMenu.addMenu('&amp;File')
 
# Adicionar botão de saída
exitButton = QAction(QIcon('exit24.png'), 'Exit', w)
exitButton.setShortcut('Ctrl+Q')
exitButton.setStatusTip('Exit application')
exitButton.triggered.connect(w.close)
fileMenu.addAction(exitButton)
 
# Mostrar janela
w.show() 
 
sys.exit(a.exec_())