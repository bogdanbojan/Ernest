import instaloader
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog
import time


""" - add fake login info/ make a new account from which you scrape
    - add more security - rotating ip's when scraping?
    - visualize the data*
    """


from PyQt5 import QtCore, QtGui, QtWidgets





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

        # self.startAnalysisButton.clicked.connect(self.download)
        # self.startAnalysisButton.clicked.connect(self.write)
        self.resetButton.clicked.connect(self.reset)

        self.startAnalysisButton.clicked.connect(self.btnFunc)
        self.startAnalysisButton.clicked.connect(self.write)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def btnFunc(self):
        self.thread = Thread()
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()
        self.startAnalysisButton.setEnabled(False)

    def signal_accept(self, msg):
        self.progressBar.setValue(int(msg))
        if self.progressBar.value() == 99:
            self.progressBar.setValue(0)
            self.progressBar.setEnabled(True)

    def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.progress.setValue(value)

    def reset(self):
        self.accountsForm.setPlainText("")
        self.passwordForm.setText("")
        self.usernameForm.setText("")


    def write(self):

        ig_username = self.usernameForm.text()
        ig_password = self.passwordForm.text()

        accounts_to_compare_gui = self.accountsForm.toPlainText()
        print("Accounts compared: ", accounts_to_compare_gui,)
        accounts_to_compare_gui = accounts_to_compare_gui.replace(',', '  ')
        accounts_to_compare = accounts_to_compare_gui.split()

        following_followers = 'following' if self.setFollowingFollowers.currentIndex() == 0 else 'followers'

        # Get instance
        L = instaloader.Instaloader()

        # Login or load session
        L.login(ig_username, ig_password)  # (login)

        nr_accounts_to_compare = len(accounts_to_compare)
        # !I can write a while loop for the accounts and ditch the first nr_accounts_to_compare variable

        for acc in range(int(nr_accounts_to_compare)):
            account = accounts_to_compare[acc]
            profile = instaloader.Profile.from_username(L.context, account)

            file = open("{acc}_{f}.txt".format(acc=account, f=following_followers), "a+")

            if self.setFollowingFollowers.currentIndex() == 0:
                for followingee in profile.get_followees():
                    username = followingee.username
                    file.write(username + "\n")
                file.close()

            elif self.setFollowingFollowers.currentIndex() == 1:
                for followee in profile.get_followers():
                    username = followee.username
                    file.write(username + "\n")
                file.close()

        # compare
        self.completed = 30
        self.progressBar.setValue(self.completed)


        txt_files = []
        for account in accounts_to_compare:
            txt_files.append("{acc}_{f}.txt".format(acc=account, f=following_followers))

        all_files = []
        for file in txt_files:
            file_nr = open(file, 'r')
            all_files.append(set(file_nr))

        same = set.intersection(*all_files)

        same.discard('\n')

        self.completed = 60
        self.progressBar.setValue(self.completed)

        with open('some_output_file.txt', 'w+') as file_out:
            for line in same:
                file_out.write(line)

        # read the file

        self.completed = 100
        self.progressBar.setValue(self.completed)

        text = open('some_output_file.txt').read()
        self.textEdit.setPlainText(text)

        num_lines = sum(1 for line in open('some_output_file.txt'))
        print('Total number of accounts that intersect: ', num_lines, '\n')

        output_file_content = open('some_output_file.txt', 'r').read()
        print("List of accounts:", "\n", output_file_content)

    def download(self):
        self.completed = 10
        self.progressBar.setValue(self.completed)

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
