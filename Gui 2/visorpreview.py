# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisorPreview.ui'
#
# Created: Fri Mar 21 11:50:31 2014
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

class Ui_Preview(object):
    def setupUi(self, Preview):
        Preview.setObjectName(_fromUtf8("Preview"))
        Preview.resize(504, 399)
        self.gridLayout_3 = QtGui.QGridLayout(Preview)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        self.ButtonAceptar = QtGui.QPushButton(Preview)
        self.ButtonAceptar.setObjectName(_fromUtf8("ButtonAceptar"))
        self.gridLayout_3.addWidget(self.ButtonAceptar, 2, 2, 1, 1)
        self.ButtonCancelar = QtGui.QPushButton(Preview)
        self.ButtonCancelar.setObjectName(_fromUtf8("ButtonCancelar"))
        self.gridLayout_3.addWidget(self.ButtonCancelar, 3, 2, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(Preview)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 3)
        self.groupBox_2 = QtGui.QGroupBox(Preview)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.spinBoxK = QtGui.QSpinBox(self.groupBox_2)
        self.spinBoxK.setObjectName(_fromUtf8("spinBoxK"))
        self.gridLayout_2.addWidget(self.spinBoxK, 0, 0, 1, 1)
        self.ButtonRecalcular = QtGui.QPushButton(self.groupBox_2)
        self.ButtonRecalcular.setObjectName(_fromUtf8("ButtonRecalcular"))
        self.gridLayout_2.addWidget(self.ButtonRecalcular, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Preview)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.spinBoxNiveles = QtGui.QSpinBox(self.groupBox)
        self.spinBoxNiveles.setObjectName(_fromUtf8("spinBoxNiveles"))
        self.gridLayout.addWidget(self.spinBoxNiveles, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)

        self.retranslateUi(Preview)
        QtCore.QMetaObject.connectSlotsByName(Preview)

    def retranslateUi(self, Preview):
        Preview.setWindowTitle(_translate("Preview", "Form", None))
        self.ButtonAceptar.setText(_translate("Preview", "Aceptar", None))
        self.ButtonCancelar.setText(_translate("Preview", "Cancelar", None))
        self.groupBox_2.setTitle(_translate("Preview", "Valor de K", None))
        self.ButtonRecalcular.setText(_translate("Preview", "Recalcular", None))
        self.groupBox.setTitle(_translate("Preview", "Numero de Niveles", None))

