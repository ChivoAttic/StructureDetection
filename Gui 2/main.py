__author__ = 'teohoch'

import sys
from PyQt4 import QtGui, QtCore
import pyfits
import os

from intro import Ui_MainWindow as intro
from preview import *
from visorpreview import Ui_Preview as visp

class VisorPreview(QtGui.QWidget):

    CurrentPath = ""
    CurrentFile = ""
    K = 0
    Nlevel = 0

    def __init__(self, k , Nlevel, CurrentPath, CurrentFile, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = visp()
        self.ui.setupUi(self)

        self.CurrentFile = CurrentFile
        self.CurrentPath = CurrentPath
        self.K = k
        self.Nlevel = Nlevel

        self.ui.spinBoxK.setValue(k)
        self.ui.spinBoxNiveles.setValue(Nlevel)

    def Cancelar(self):
        self.hide()


class AppIntro(QtGui.QMainWindow):


    Visor = VisorPreview

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = intro()
        self.ui.setupUi(self)
        self.ui.ButtonBuscar.clicked.connect(self.Buscar)
        self.ui.ButtonCargar.clicked.connect(self.loadFit)

    def Buscar(self):
        path = str(QtGui.QFileDialog.getOpenFileName(self, "Open Fits"))
        self.ui.PathLine.setText(path)

    def loadFit(self):
        K = self.ui.spinBoxK.value()
        N = self.ui.spinBoxLevel.value()
        Path = str(self.ui.PathLine.text())
        File = os.path.basename(Path)
        self.Visor = VisorPreview(K,N,Path,File)
        self.Visor.show()
        self.hide()




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Aperture = AppIntro()
    Aperture.show()


    sys.exit(app.exec_())