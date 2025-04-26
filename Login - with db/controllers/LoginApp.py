from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys

from models.User import User

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("views/login.ui", self)  # Load the UI file
        self.loginBtn.clicked.connect(self.handle_login)  # Connect button click to handler
        self.registerBtn.clicked.connect(self.open_register_window)  # Connect register button to handler
        self.setWindowTitle("Login")
        
    def handle_login(self):
        username = self.username.text()
        password = self.password.text()

        # Check if username and password are provided
        if not username or not password:
            QMessageBox.warning(self, "Login Failed", "Please enter both username and password.")
            return
        
        # Attempt to validate user credentials
        user_model = User()
        is_valid = user_model.validate_user(username, password)
        
        if is_valid:
            # Show success message and proceed to the next window
            QMessageBox.information(self, "Login Successful", "Welcome!")
            self.username.clear()
            self.password.clear()
            from controllers.Dashboard import DashboardWindow
            self.main_window = DashboardWindow()
            self.main_window.show()
            self.close()
        else:
            # Show error message if login fails
            self.username.setFocus()
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def open_register_window(self):
        from controllers.RegisterWindow import RegisterWindow
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()
