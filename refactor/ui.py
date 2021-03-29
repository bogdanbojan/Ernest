from PyQt5 import QtCore, QtGui, QtWidgets
import controller

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(573, 492)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(30, 410, 511, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.accountsForm = QtWidgets.QPlainTextEdit(Dialog)
        self.accountsForm.setGeometry(QtCore.QRect(320, 250, 221, 71))
        self.accountsForm.setPlainText("")
        self.accountsForm.setObjectName("accountsForm")
        self.startAnalysisButton = QtWidgets.QPushButton(Dialog)
        self.startAnalysisButton.setGeometry(QtCore.QRect(320, 330, 221, 61))
        self.startAnalysisButton.setObjectName("startAnalysisButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 170, 211, 41))
        self.label_2.setObjectName("label_2")
        self.resetButton = QtWidgets.QPushButton(Dialog)
        self.resetButton.setGeometry(QtCore.QRect(30, 450, 75, 23))
        self.resetButton.setObjectName("resetButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 551, 80))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(290, 30, 61, 20))
        self.label_4.setObjectName("label_4")
        self.passwordForm = QtWidgets.QLineEdit(self.groupBox)
        self.passwordForm.setGeometry(QtCore.QRect(350, 30, 181, 31))
        self.passwordForm.setText("")
        self.passwordForm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordForm.setObjectName("passwordForm")
        self.usernameForm = QtWidgets.QLineEdit(self.groupBox)
        self.usernameForm.setGeometry(QtCore.QRect(90, 30, 181, 31))
        self.usernameForm.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.usernameForm.setObjectName("usernameForm")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 180, 251, 211))
        self.textEdit.setObjectName("textEdit")
        self.setFollowingFollowers = QtWidgets.QComboBox(Dialog)
        self.setFollowingFollowers.setGeometry(QtCore.QRect(320, 220, 221, 22))
        self.setFollowingFollowers.setObjectName("setFollowingFollowers")
        self.setFollowingFollowers.addItem("")
        self.setFollowingFollowers.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 20, 141, 16))
        self.label.setObjectName("label")
        self.setMainFunctionality = QtWidgets.QComboBox(Dialog)
        self.setMainFunctionality.setGeometry(QtCore.QRect(300, 20, 261, 22))
        self.setMainFunctionality.setObjectName("setMainFunctionality")
        self.setMainFunctionality.addItem("")
        self.setMainFunctionality.addItem("")
        self.setMainFunctionality.addItem("")

        instagram_app = controller.InstagramApplication(self.accountsForm, self.passwordForm, self.usernameForm, self.setFollowingFollowers, self.progressBar, self.textEdit)

        self.startAnalysisButton.clicked.connect(lambda: instagram_app.download())
        self.startAnalysisButton.clicked.connect(lambda: instagram_app.app())
        self.resetButton.clicked.connect(lambda: instagram_app.clear_forms())

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ernest"))
        self.startAnalysisButton.setText(_translate("Dialog", "Start the analysis"))
        self.label_2.setText(_translate("Dialog", "Write the account names to be compared:\n"
                                                  "(account1, account2, etc)"))
        self.resetButton.setText(_translate("Dialog", "Reset"))
        self.groupBox.setTitle(_translate("Dialog", "Instagram Login"))
        self.label_3.setText(_translate("Dialog", "Username:"))
        self.label_4.setText(_translate("Dialog", "Password:"))
        self.setFollowingFollowers.setItemText(0, _translate("Dialog", "Compare \'\'Following\'\'"))
        self.setFollowingFollowers.setItemText(1, _translate("Dialog", "Compare \'\'Followers\'\'"))
        self.label.setText(_translate("Dialog", "Select current functionality:"))
        self.setMainFunctionality.setItemText(0, _translate("Dialog", "Similarities between accounts"))
        self.setMainFunctionality.setItemText(1, _translate("Dialog", "Top posts of account"))
        self.setMainFunctionality.setItemText(2, _translate("Dialog", "Ghost followers of account"))


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ernest.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)

