__author__ = 'teohoch'

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#import pyfits
import os

from intro import Ui_MainWindow as intro
from visorpreview import Ui_Preview as visp

class VisorPreview(QWidget):

    CurrentPath = ""
    CurrentFile = ""
    K = 0
    Nlevel = 0
    Sinal = pyqtSignal()



    def __init__(self,parent = None):
        QWidget.__init__(self, parent)

        self.ui = visp()
        self.ui.setupUi(self)
        self.ui.ButtonAceptar.clicked.connect(self.PushAceptar)

    def Iniciar(self, k , Nlevel, CurrentPath, CurrentFile):
        self.CurrentFile = CurrentFile
        self.CurrentPath = CurrentPath
        self.K = k
        self.Nlevel = Nlevel

        self.ui.spinBoxK.setValue(k)
        self.ui.spinBoxNiveles.setValue(Nlevel)

        #TODO Incluir rutina generadora de imagenes preview, se mas facil si creo una funcion que lo haga asi puedo llamarla para el recalculo

    def PushAceptar(self):
        self.Sinal.emit()
        #TODO abrir ventana "analicis"

class AppIntro(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = intro()
        self.ui.setupUi(self)
        self.ui.ButtonBuscar.clicked.connect(self.Buscar)
        self.ui.ButtonCargar.clicked.connect(self.LoadFit)

        self.Visor = VisorPreview()

        self.Visor.Sinal.connect(self.wow)


    def Buscar(self):
        path = str(QFileDialog.getOpenFileName(self, "Open Fits"))
        self.ui.PathLine.setText(path)

    def LoadFit(self):

        K = self.ui.spinBoxK.value()
        N = self.ui.spinBoxLevel.value()
        Path = str(self.ui.PathLine.text())
        File = os.path.basename(Path)
        self.Visor.Iniciar(K,N,Path,File)
        self.Visor.show()
        self.Visor.ui.ButtonCancelar.clicked.connect(self.CancelarPreview)
        self.hide()

    def CancelarPreview(self):
        self.Visor.hide()
        self.ui.spinBoxK.setValue(0)
        self.ui.spinBoxLevel.setValue(0)
        self.show()
    def wow(self):
        print("Holop")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    Aperture = AppIntro()
    Aperture.show()


    sys.exit(app.exec_())

#TODO Generar ventana analicis, incluyendo la clase contenedora y conectarla con el wrapper!