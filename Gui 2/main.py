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
        self.ui.ButtonAceptar.clicked.connect(self.)# TODO seguir aqui!!

    def Iniciar(self, k , Nlevel, CurrentPath, CurrentFile):
        self.CurrentFile = CurrentFile
        self.CurrentPath = CurrentPath
        self.K = k
        self.Nlevel = Nlevel

        self.ui.spinBoxK.setValue(k)
        self.ui.spinBoxNiveles.setValue(Nlevel)

    def PushAceptar(self):
        self.emit(self.Sinal)

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
        self.Visor.destroy()
        self.ui.spinBoxK.setValue(0)
        self.ui.spinBoxLevel.setValue(0)
        print "k"
    def wow(self):
        print("Holop")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    Aperture = AppIntro()
    Aperture.show()


    sys.exit(app.exec_())