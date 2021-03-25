from PyQt5 import QtCore, QtGui, QtWidgets
import instaloader


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

        self.startAnalysisButton.clicked.connect(self.download)
        self.startAnalysisButton.clicked.connect(self.app)
        self.resetButton.clicked.connect(self.clear_forms)




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def app(self):

        self.instaloader_initial_setup(*self.get_login_information())

        acc_to_compare = self.split_accounts_to_compare()
        nr_of_acc = self.nr_accounts_to_compare(acc_to_compare)
        follower_or_following = self.get_follower_or_following_option()

        self.iterate_over_accounts_to_compare(nr_of_acc, acc_to_compare, follower_or_following)
        self.write_txt_files(acc_to_compare, follower_or_following)
        self.read_txt_files()


    def clear_forms(self):
        self.accountsForm.setPlainText("")
        self.passwordForm.setText("")
        self.usernameForm.setText("")

    def get_login_information(self):
        ig_username = self.usernameForm.text()
        ig_password = self.passwordForm.text()

        return ig_username, ig_password

    def instaloader_initial_setup(self, ig_username, ig_password):
        self.L = instaloader.Instaloader()

        self.L.login(ig_username, ig_password)
        print('Login successful')  # TODO: make it give and error if it is not successful

    def split_accounts_to_compare(self):
        self.accounts_to_compare_gui = self.accountsForm.toPlainText()
        print("Accounts compared: ", self.accounts_to_compare_gui)
        self.accounts_to_compare_gui = self.accounts_to_compare_gui.replace(',', '  ')
        self.accounts_to_compare = self.accounts_to_compare_gui.split()

        return self.accounts_to_compare

    def nr_accounts_to_compare(self, accounts_to_compare):
        self.nr_accounts_compared = len(accounts_to_compare)
        print(self.nr_accounts_compared)

        return self.nr_accounts_compared

    def get_follower_or_following_option(self):
        self.following_or_follower = 'following' if self.setFollowingFollowers.currentIndex() == 0 else 'followers'
        print(self.following_or_follower)

        return self.following_or_follower


    def iterate_over_accounts_to_compare(self, nr_accounts_compared, accounts_to_compare, following_or_follower):
        for acc in range(int(nr_accounts_compared)):
            account = accounts_to_compare[acc]
            print("got here")
            profile = instaloader.Profile.from_username(self.L.context, account)
            print('it passed')

            file = open("{acc}_{f}.txt".format(acc=account, f=following_or_follower), "a+")

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

    def write_txt_files(self, accounts_to_compare, following_or_follower):

        txt_files = []
        for account in accounts_to_compare:
            txt_files.append("{acc}_{f}.txt".format(acc=account, f=following_or_follower))

        all_files = []
        for file in txt_files:
            file_nr = open(file, 'r')
            all_files.append(set(file_nr))

        same = set.intersection(*all_files)

        same.discard('\n')

        with open('some_output_file.txt', 'w+') as file_out:
            for line in same:
                file_out.write(line)

        # need to chang this
        self.completed = 60
        self.progressBar.setValue(self.completed)

    def read_txt_files(self):

        self.completed = 100
        self.progressBar.setValue(self.completed)

        text = open('some_output_file.txt').read()
        self.textEdit.setPlainText(text)

        num_lines = sum(1 for line in open('some_output_file.txt'))
        print('Total number of accounts that intersect: ', num_lines, '\n')

        output_file_content = open('some_output_file.txt', 'r').read()
        print("List of accounts:", "\n", output_file_content)

    def download(self):
        self.completed = 20
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
