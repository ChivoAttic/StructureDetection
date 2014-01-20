# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created: Mon Jan 20 13:08:23 2014
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

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName(_fromUtf8("mainwindow"))
        mainwindow.resize(808, 726)
        self.centralwidget = QtGui.QWidget(mainwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 801, 241))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(110, 30, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 70, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser_3.setGeometry(QtCore.QRect(110, 110, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 71, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser_4.setGeometry(QtCore.QRect(110, 150, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(420, 20, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tableView = QtGui.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(420, 40, 256, 192))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 280, 400, 400))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.graphicsView = QtGui.QGraphicsView(self.groupBox_2)
        self.graphicsView.setGeometry(QtCore.QRect(20, 40, 300, 300))
        self.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform)
        self.graphicsView.setResizeAnchor(QtGui.QGraphicsView.AnchorViewCenter)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(400, 320, 361, 341))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.groupBox_4)
        self.graphicsView_3.setGeometry(QtCore.QRect(20, 50, 291, 261))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainwindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(mainwindow)
        self.actionOpen.setMenuRole(QtGui.QAction.ApplicationSpecificRole)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(mainwindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainwindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("activated()")), mainwindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(_translate("mainwindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("mainwindow", "Data", None))
        self.label.setText(_translate("mainwindow", "Name", None))
        self.label_2.setText(_translate("mainwindow", "Simple", None))
        self.label_3.setText(_translate("mainwindow", "BitPix", None))
        self.label_4.setText(_translate("mainwindow", "N° Axis", None))
        self.label_5.setText(_translate("mainwindow", "Axis", None))
        self.groupBox_2.setTitle(_translate("mainwindow", "Original Image", None))
        self.groupBox_4.setTitle(_translate("mainwindow", "Clusters", None))
        self.menuFile.setTitle(_translate("mainwindow", "File", None))
        self.actionOpen.setText(_translate("mainwindow", "Open FIT", None))
        self.actionClose.setText(_translate("mainwindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainwindow = QtGui.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())

