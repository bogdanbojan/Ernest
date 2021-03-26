from PyQt5 import QtCore, QtGui, QtWidgets
import instaloader
from ui import Ui_Dialog

class InstagramApplication(Ui_Dialog):
    def __init__(self, accountsForm, passwordForm, usernameForm, setFollowingFollowers, progressBar, textEdit):
        self.accountsForm = accountsForm
        self.passwordForm = passwordForm
        self.usernameForm  = usernameForm
        self.setFollowingFollowers = setFollowingFollowers
        self.progressBar = progressBar
        self.textEdit = textEdit


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



