from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
import sys

from models.User import User

class UpdateForm(QMainWindow):
    def __init__(self, user=None):
        super().__init__()
        self.user = user
        self.setWindowTitle("Update User")
        uic.loadUi("views/update_form.ui", self)  # Load the UI file
        self.updateBtn.clicked.connect(self.handle_update)  # Connect button click to handler
        self.populate_fields()
        
    def populate_fields(self):
        if self.user:
            self.username.setText(self.user.get('username'))
            self.password.setText(self.user.get('password'))
            self.gender.setCurrentText(self.user.get('gender'))
        else:
            print("⚠️ No user data provided to populate fields.")
            QMessageBox.warning(self, "Error", "No user data provided to populate fields.")
    
    def handle_update(self):
        print("✅ Register button clicked")
        username = self.username.text(self.user.get('username'))
        password = self.password.text(self.user.get('password'))
        gender = self.gender.currentText(self.user.get('gender'))
        
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


