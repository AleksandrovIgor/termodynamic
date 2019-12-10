

from PyQt4 import QtCore, QtGui


class AlarmDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AlarmDialog, self).__init__(parent)

        self.setWindowTitle(self.tr("Alarm"))
        self.setWindowIcon(QtGui.QIcon('icons/old_clock.png'))
        self.resize(100, 100)
        self.setSizeGripEnabled(False)
        self.setModal(True)
     
        self.verticalLayout = QtGui.QVBoxLayout()

        self.message = QtGui.QLabel(self.tr('Wake Up!!!'))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.message.setFont(font)
        
        self.verticalLayout.addWidget(self.message)

        self.buttonBox = QtGui.QDialogButtonBox()
        #self.buttonBox.setOrientation(QtCore.Qt.Horisontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)
        QtCore.QObject.connect(self.buttonBox,
                                   QtCore.SIGNAL("accepted()"),
                               self.accept)
        self.setLayout(self.verticalLayout)

        

    def play(self):
        self.a = QtGui.QSound('Alarm.wav')
        self.a.play()
        print 'sss'

       
        

if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = AlarmDialog()
    sys.exit(dialog.exec_())



    
