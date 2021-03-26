from PyQt5 import QtCore, QtGui, QtWidgets
import instaloader
from ui import Ui_Dialog
from app import InstagramApplication


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
