from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys

from models.User import User

class DashboardWindow(QMainWindow):
    
    selected_user = None
    
    def __init__(self):
        super().__init__()
        uic.loadUi("views/dashboard.ui", self)

        self.setWindowTitle("Dashboard")
        print("Dashboard initialized")

        self.populate_table()  # Populate the table with user data
        
        # Connect click signal
        self.usersTbl.clicked.connect(self.on_row_clicked)
        self.deleteUserBtn.clicked.connect(self.delete_user)
        self.updateUserBtn.clicked.connect(self.update_user)

        self.show()

    def update_user(self):
        if self.selected_user is None:
            QMessageBox.warning(self, "Update Failed", "No user selected.")
            return
        
        from controllers.UpdateForm import UpdateForm
        self.update_form = UpdateForm(self.selected_user)
        self.update_form.show()
        self.hide()
    
    def delete_user(self):
        proceed = QMessageBox.question(self, 
                    "Confirmation", "Are you sure you want to delete this?",
                    QMessageBox.StandardButton.Yes,
                    QMessageBox.StandardButton.No
                )

        if proceed == QMessageBox.StandardButton.Yes:
            user_id = self.selected_user.get('id')
            user_model = User()
            result = user_model.delete_user(user_id)
            if result:
                QMessageBox.information(self, "Success", "User deleted successfully.")
                self.populate_table()
            else:
                QMessageBox.warning(self, "Error", "Failed to delete user.")
        else:
            print("No")
        
    def populate_table(self):
        # Create model with headers
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["ID", "Username", "Password", "Gender"])
        
        # Get data from users model
        user_model = User()
        users = user_model.get_all_users()
        
        # Populate model with data
        for user in users:
            print(f"User data: {user}")
            row = [
                QStandardItem(str(user.get('id', ''))),
                QStandardItem(user.get('username', '')),
                QStandardItem(user.get('password', '')),  # Note: Consider hashing passwords in display
                QStandardItem(user.get('gender', ''))
            ]
            model.appendRow(row)
            
        self.usersTbl.setModel(model)
        
        # Optional: Adjust column widths
        self.usersTbl.setColumnWidth(0, 50)   # ID column
        self.usersTbl.setColumnWidth(1, 150)  # Username
        self.usersTbl.setColumnWidth(2, 150)  # Password
        self.usersTbl.setColumnWidth(3, 100)  # Gender

    def on_row_clicked(self, index):
        model = self.usersTbl.model()
        self.selected_user = {
            'id': model.index(index.row(), 0).data(),
            'username': model.index(index.row(), 1).data(),
            'password': model.index(index.row(), 2).data(),  # Mask password
            'gender': model.index(index.row(), 3).data()
        }
        
        print(self.selected_user)
        # details = "\n".join([f"{key}: {value}" for key, value in row_data.items()])
        # QMessageBox.information(self, "User Details", details)