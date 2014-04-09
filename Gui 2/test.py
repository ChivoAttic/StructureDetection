__author__ = 'teohoch'
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class MyWidget(QWidget):

    # Defining signals below:

    # No arguments, its a simple signal that can
    # be emitted.
    simpleSig = pyqtSignal()

    # A signal that requires two parameters.
    # (One is an integer, other is a Python list type)
    # You can have one or more than two as well.
    argumentSig = pyqtSignal(int, list)

    # A signal that allows two different sets of params.
    # One is if you send an int, the other is for QString.
    # This signal is also optionally named using 'name'
    # for use in more dynamic purposes.
    doubleSig = pyqtSignal((int,), (QString,), name='doubles')

    def __init__(self, parent=None):
        # Construct the parent, never forget this!
        super(MyWidget, self).__init__(parent)

        # Connect our signals to their slots
        self.simpleSig.connect(self.simpleSlot)
        self.argumentSig.connect(self.argumentSlot)
        # We have same slot for the double signals
        # (aka) overloaded signals.
        # Cause we can check the argument from within too!
        self.doubleSig['int'].connect(self.doubleSlot)
        self.doubleSig['QString'].connect(self.doubleSlot)

        # Connect our button to a slot which
        # will call the signals.
        self.button = QPushButton('Press me', self)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self, checked=False):
        # Emit the various signals to use them.
        self.simpleSig.emit()
        self.argumentSig.emit(2, [1,2,3])
        # Overloaded signals have the following format
        # for emitting specifically.
        self.doubleSig['int'].emit(42)
        self.doubleSig['QString'].emit('Hitchhiking a ride.')

    # Defining custom-signal slots below:

    def simpleSlot(self):
        # Takes no arguments
        print "Simple custom signal:",
        print "No arguments in this type of signal."

    def argumentSlot(self, *args):
        # ( Can also be 'argumentSlot(self, intArg, listArg)' )
        # Has two arguments anyway, which is collected into one
        # using '*' (A Python feature)
        print "Multi-argument signal:",
        print "Two arguments were passed: value: '%d' of %s and value: '%s' of %s." % (args[0], type(args[0]), args[1], type(args[1]))

    def doubleSlot(self, someArgument):
        # This slot handles both doubleSig(int)
        # and doubleSig(QString)
        print "Overloaded signal:",
        print "An argument was passed and it was of '%s' and value: '%s'." % (type(someArgument), someArgument)

if __name__=='__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec_()