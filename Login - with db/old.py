from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys

# Main class for the application
class User:
    def __init__(self, username, password, gender):
        self.username = username
        self.password = password
        self.gender = gender

    def display_info(self):
        print("Username: ", self.username)
        print("Password: ", self.password)
        print("Gender: ", self.gender)

    def validate_login(self, username, password):
        return self.username == username and self.password == password


# Global list to store registered users
registered_users = []

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("views/login.ui", self)  # Load the UI file
        self.loginBtn.clicked.connect(self.handle_login)  # Connect button click to handler
        self.registerBtn.clicked.connect(self.open_register_window)  # Connect register button to handler

    def handle_login(self):
        username = self.username.text()
        password = self.password.text()

        # Validate login using the User class
        for user in registered_users:
            if user.validate_login(username, password):
                QMessageBox.information(self, "Login Successful", f"Welcome, {username}!")
                self.dashboard_window = DashboardWindow(user)
                self.dashboard_window.show()
                self.close()  # Close the current window
                return

        # Show error message if login fails
        self.username.clear()
        self.password.clear()
        self.username.setFocus()
        QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        # self.setGeometry(100, 100, 300, 200)
        uic.loadUi("views/register.ui", self)  # Load the UI file
        self.registerBtn.clicked.connect(self.handle_register)  # Connect button click to handler

    def handle_register(self):
        username = self.username.text()
        password = self.password.text()
        gender = self.gender.currentText()

        # Check if username already exists
        for user in registered_users:
            if user.username == username:
                QMessageBox.warning(self, "Registration Failed", "Username already exists.")
                return

        if username and password:
            # Create a new user and add to the registered_users list
            new_user = User(username, password, gender)
            registered_users.append(new_user)
            QMessageBox.information(self, "Registration Successful", "You are now registered!")
            self.close()
            self.login_window = LoginApp()
            self.login_window.show()
        else:
            QMessageBox.warning(self, "Registration Failed", "Please fill in all fields.")

class DashboardWindow(QMainWindow):
    def __init__(self, user: User):
        super().__init__()
        self.user = user
        uic.loadUi("views/dashboard.ui", self)

        self.setWindowTitle("Dashboard")
        print("Dashboard initialized")
        self.user.display_info()

        self.populate_table()  # Fill the table using a model

        self.show()

    def populate_table(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Username", "Password", "Gender"])

        for user in registered_users:
            model.appendRow([
                QStandardItem(user.username),
                QStandardItem(user.password),
                QStandardItem(user.gender)
            ])

        self.usersTbl.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())