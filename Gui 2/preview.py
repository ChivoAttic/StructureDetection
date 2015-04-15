"""
This file is part of ChiVO
Copyright (C) Rodrigo Gregorio

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisorPreview.ui'
#
# Created: Tue Mar 25 15:41:26 2014
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
        Preview.resize(367, 376)
        self.gridLayout = QtGui.QGridLayout(Preview)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(Preview)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 3)
        self.ButtonAceptar = QtGui.QPushButton(Preview)
        self.ButtonAceptar.setObjectName(_fromUtf8("ButtonAceptar"))
        self.gridLayout.addWidget(self.ButtonAceptar, 1, 2, 1, 1)
        self.ButtonCancelar = QtGui.QPushButton(Preview)
        self.ButtonCancelar.setObjectName(_fromUtf8("ButtonCancelar"))
        self.gridLayout.addWidget(self.ButtonCancelar, 4, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Preview)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spinBoxK = QtGui.QSpinBox(self.groupBox_2)
        self.spinBoxK.setObjectName(_fromUtf8("spinBoxK"))
        self.horizontalLayout.addWidget(self.spinBoxK)
        self.ButtonRecalcular = QtGui.QPushButton(self.groupBox_2)
        self.ButtonRecalcular.setObjectName(_fromUtf8("ButtonRecalcular"))
        self.horizontalLayout.addWidget(self.ButtonRecalcular)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Preview)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.spinBoxNiveles = QtGui.QSpinBox(self.groupBox)
        self.spinBoxNiveles.setObjectName(_fromUtf8("spinBoxNiveles"))
        self.verticalLayout.addWidget(self.spinBoxNiveles)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 2, 1)

        self.retranslateUi(Preview)
        QtCore.QMetaObject.connectSlotsByName(Preview)

    def retranslateUi(self, Preview):
        Preview.setWindowTitle(_translate("Preview", "Visualizador", None))
        self.ButtonAceptar.setText(_translate("Preview", "Aceptar", None))
        self.ButtonCancelar.setText(_translate("Preview", "Cancelar", None))
        self.groupBox_2.setTitle(_translate("Preview", "Valor de K", None))
        self.ButtonRecalcular.setText(_translate("Preview", "Recalcular", None))
        self.groupBox.setTitle(_translate("Preview", "Numero de Niveles", None))

