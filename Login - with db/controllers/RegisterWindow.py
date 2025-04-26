from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys

from models.User import User

class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        # self.setGeometry(100, 100, 300, 200)
        uic.loadUi("views/register.ui", self)  # Load the UI file
        self.registerBtn.clicked.connect(self.handle_register)  # Connect button click to handler
        self.setWindowTitle("Register")
        
    def handle_register(self):
        print("✅ Register button clicked")
        username = self.username.text()
        password = self.password.text()
        gender = self.gender.currentText()
        
        if not username or not password:
            print("⚠️ Missing fields")
            QMessageBox.warning(self, "Registration Failed", "Please fill in all fields.")
            return

        try:
            user_model = User()
            is_success = user_model.register_user(username, password, gender)
            print(f"🟢 Register success: {is_success}")

            if is_success:
                QMessageBox.information(self, "Registration Successful", "User registered successfully.")
                self.username.clear()
                self.password.clear()
            else:
                QMessageBox.warning(self, "Registration Failed", "User registration failed. Please try again.")

        except Exception as e:
            print(f"❌ Exception occurred: {e}")
            QMessageBox.critical(self, "Error", "An unexpected error occurred.")


