from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys


class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)  # Load the UI file
        self.loginBtn.clicked.connect(self.handle_login) # Connect button click to handler
        self.registerBtn.clicked.connect(self.open_register_window) # Connect register button to handler

    def handle_login(self):
        username = self.username.text()
        password = self.password.text()
        if username == "admin" and password == "password":
            QMessageBox.information(self, "Login Successful", "Welcome!")
        else:
            # Show error message if login fails
            self.username.clear()
            self.password.clear()
            self.username.setFocus()
            # Display a warning message box
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
            
    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()
            
            
class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("register.ui", self)  # Load the UI file
        self.registerBtn.clicked.connect(self.handle_register) # Connect button click to handler

    def handle_register(self):
        username = self.username.text()
        password = self.password.text()
        if username and password:
            QMessageBox.information(self, "Registration Successful", "You are now registered!")
        else:
            QMessageBox.warning(self, "Registration Failed", "Please fill in all fields.")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())