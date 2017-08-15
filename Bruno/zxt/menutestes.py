import sys
import pymysql # metodo que liga o python no mysql 
from menuprincipal  import *# inportando janela banco1.py


comfig ={'host':'localhost',# criando metodo de entrada do Mysql
         'port':3306,
         'database':'Lojadb',
         'user':'root',
         'password':'34387'}
db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
cursor = db.cursor()


class MeuFormulario (QtGui.QDialog ) :
    def __init__(self, parent=None) :
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_menuprincipal()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnsalvar, QtCore.SIGNAL('clicked()'), self.gravar)# metodo que faz a açao ao clicar no motao
        
    def gravar (self): 
                
                
                comando =("insert into Lojadb.cliente (nome,codigo) " " values (%s,%s)" )  # meto
            
                varnome = (self.ui.linhanome .text())

                   
            
                varcodigo = ( self.ui.linhacodigo.text())
                
                dados = (varnome,varcodigo)
                
                cursor.execute (comando,dados)

                db.commit()
                print('ja foi')

                cursor.close()
                db.close

                
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp =   Ui_menuprincipal()
    myapp.show()
    sys.exit(app.exec_())    