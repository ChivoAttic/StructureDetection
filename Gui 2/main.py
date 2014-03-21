__author__ = 'teohoch'

import sys
from PyQt4 import QtGui, QtCore
import pyfits
import os

from intro import Ui_MainWindow as intro
from preview import *
from visorpreview import Ui_Preview as visp

class VisorPreview(QtGui.QMainWindow):

    CurrentPath = ""
    CurrentFile = ""
    K = 0
    Nlevel = 0

    def __init__(self, k , Nlevel, CurrentPath, CurrentFile, parent = None):
        QtGui.QWidget.__init__(self, parent)


        self.ui = visp
        self.ui.setupUi(self)

class AppIntro(QtGui.QMainWindow):

    Visor = VisorPreview


    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = intro()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.loadFit)

    def loadFit(self):
        self.CurrentPath = filename
        self.CurrentFile = os.path.basename(filename)
        self.Visor = VisorPreview(self.ui.spinBoxK.value(),self.ui.spinBoxLevel.value(), self.ui.PathLine.)





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Aperture = AppIntro()
    Aperture.show()
    #visor = VisorPreview(Aperture.K, Aperture.Nlevel, Aperture.CurrentPath, Aperture.CurrentFile)

    sys.exit(app.exec_())