# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Intro.ui'
#
# Created: Tue Mar 25 15:20:18 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(636, 292)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ButtonBuscar = QtGui.QPushButton(self.centralwidget)
        self.ButtonBuscar.setObjectName(_fromUtf8("ButtonBuscar"))
        self.gridLayout.addWidget(self.ButtonBuscar, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ButtonCargar = QtGui.QPushButton(self.centralwidget)
        self.ButtonCargar.setObjectName(_fromUtf8("ButtonCargar"))
        self.gridLayout.addWidget(self.ButtonCargar, 1, 3, 1, 1)
        self.PathLine = QtGui.QLineEdit(self.centralwidget)
        self.PathLine.setReadOnly(True)
        self.PathLine.setObjectName(_fromUtf8("PathLine"))
        self.gridLayout.addWidget(self.PathLine, 0, 2, 1, 1)
        self.spinBoxLevel = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxLevel.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxLevel.setObjectName(_fromUtf8("spinBoxLevel"))
        self.gridLayout.addWidget(self.spinBoxLevel, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinBoxK = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxK.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxK.setObjectName(_fromUtf8("spinBoxK"))
        self.gridLayout.addWidget(self.spinBoxK, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ButtonBuscar.setText(_translate("MainWindow", "Buscar", None))
        self.label_2.setText(_translate("MainWindow", "N° de Niveles", None))
        self.ButtonCargar.setText(_translate("MainWindow", "Cargar", None))
        self.label.setText(_translate("MainWindow", "Ubicacion Archivo", None))
        self.label_3.setText(_translate("MainWindow", "K", None))

