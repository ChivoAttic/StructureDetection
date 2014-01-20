import sys
from PyQt4 import QtGui, QtCore
import pyfits
import os

from gui import Ui_mainwindow as MW
from analysis import *


class ModeloTablaEjes(QtCore.QAbstractListModel):

    def __init__(self, ejes = [], parent = None):
        QtCore.QAbstractListModel.__init__(self,parent)
        self._ejes = ejes

    def rowCount(self, parent):
        return len(self._ejes)

    def data(self, index, role):

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self._ejes[row]
            return value






class MainWindow(QtGui.QMainWindow):
    CurrentPath = ""
    CurrentFile = ""
    Simple = False
    NAxis = 0
    BitPix = 0
    Axis = []


    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = MW()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.test)


    def test(self):
        filename = str(QtGui.QFileDialog.getOpenFileName(self, "Open Fits"))
        self.CurrentPath = filename
        self.CurrentFile = os.path.basename(filename)
        print(filename)
        self.lectura()

    def lectura(self):
        hdu = pyfits.open(str(self.CurrentPath))
        header = hdu[0].header
        self.Simple = str(header["SIMPLE"])
        self.BitPix = str(header["BITPIX"])
        self.NAxis = str(header["NAXIS"])
        for i in range(1, (int(self.NAxis)+1)):
            eje = "NAXIS" + str(i)
            self.Axis.append(header[eje])
        hdu.close()
        #self.Cluster()
        self.Mostrar()


    def Mostrar(self):
        """
        Muestra los datos del Fit en la pantalla principal.
        :return Null
        """
        self.ui.textBrowser.setText(self.CurrentFile)
        self.ui.textBrowser_2.setText(self.Simple)
        self.ui.textBrowser_3.setText(self.BitPix)
        self.ui.textBrowser_4.setText(self.NAxis)
        model = ModeloTablaEjes(self.Axis)
        self.ui.tableView.setModel(model)






        scene = QtGui.QGraphicsScene()
        scene.setSceneRect(-600,-600, 600,600)
        pic = QtGui.QPixmap("1-Orig.png")
        scene.addItem(QtGui.QGraphicsPixmapItem(pic))
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.ui.graphicsView.show()



    def Cluster(self):
        ana = analicis()
        ana.Clusterisar(self.CurrentPath, self.CurrentFile)





if __name__ == "__main__":

    dirs()
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()


    sys.exit(app.exec_())

