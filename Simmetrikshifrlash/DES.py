from PyQt5 import QtCore, QtGui, QtWidgets
import pyaes,  binascii, os, secrets
from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes
class Ui_DES(object):
    def setupUi(self, DES):
        DES.setObjectName("DES")
        DES.resize(840, 604)
        font = QtGui.QFont()
        font.setPointSize(16)
        DES.setFont(font)
        self.SHIFRLASH = QtWidgets.QPushButton(DES)
        self.SHIFRLASH.setGeometry(QtCore.QRect(540, 70, 211, 101))
        self.SHIFRLASH.setObjectName("SHIFRLASH")
        self.SHIFRLASH.clicked.connect(self.shifrla)
        self.ochiqmatn = QtWidgets.QLineEdit(DES)
        self.ochiqmatn.setGeometry(QtCore.QRect(70, 70, 411, 91))
        self.ochiqmatn.setObjectName("ochiqmatn")
        self.SHIFRMATN = QtWidgets.QLineEdit(DES)
        self.SHIFRMATN.setGeometry(QtCore.QRect(70, 270, 401, 91))
        self.SHIFRMATN.setObjectName("SHIFRMATN")
        self.label = QtWidgets.QLabel(DES)
        self.label.setGeometry(QtCore.QRect(100, 30, 361, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DES)
        self.label_2.setGeometry(QtCore.QRect(120, 210, 361, 31))
        self.label_2.setObjectName("label_2")
        self.retranslateUi(DES)
        QtCore.QMetaObject.connectSlotsByName(DES)
    def shifrla(self):
        key2 = get_random_bytes(16)
        #print(binascii.hexlify(key2))
        cipher2 = AES.new(key2, AES.MODE_OFB, IV=get_random_bytes(16))
        mal=self.ochiqmatn.text()
        print(mal)
        SHIFRMAL = cipher2.encrypt(bytes(mal,'utf-8'))
        print(SHIFRMAL)
        self.SHIFRMATN.setText(str(binascii.hexlify(SHIFRMAL)))
        print(binascii.hexlify(SHIFRMAL))
        deshifr=cipher2.decrypt(SHIFRMAL)
        print(binascii.hexlify(deshifr))
    def retranslateUi(self, DES):
        _translate = QtCore.QCoreApplication.translate
        DES.setWindowTitle(_translate("DES", "Form"))
        self.SHIFRLASH.setText(_translate("DES", "SHifrla"))
        self.label.setText(_translate("DES", "Ma\'lumotni kiriting"))
        self.label_2.setText(_translate("DES", "Shifrma\'lumot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DES = QtWidgets.QWidget()
    ui = Ui_DES()
    ui.setupUi(DES)
    DES.show()
    sys.exit(app.exec_())
