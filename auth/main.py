from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
import sys

registered_users = []

class User:
    name: str 
    age: int
    username: str
    password: str
    crush: str
    gender: str
    
    def __init__(self, name: str, age: int, username: str, password: str, crush: str, gender: str):
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        self.crush = crush
        self.gender = gender
        
    def login_validation(self, username: str, password: str):
        return self.username == username and self.password == password
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Username: {self.username}, Crush: {self.crush} <3 \n"
    

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login_ui.ui', self)
        self.loginBtn.clicked.connect(self.handle_login)
        self.registerBtn.clicked.connect(self.handle_register)
        
    def handle_login(self):
        username = self.username.text()
        password = self.password.text()
        
        for user in registered_users:
            
            if user.login_validation(username, password):
                self.close()
                self.home_page = HomePageWindow(user)
                self.home_page.show()
                return
            else:
                QMessageBox.warning(self, "Error", "Invalid username or password!")
                break
                    
            
    def handle_register(self):
        self.register_page = registerPageWindow()
        self.register_page.show()
        self.close()
            
class registerPageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('register.ui', self)
        self.registerBtn.clicked.connect(self.handle_create_account)
        
    def handle_create_account(self):
        name = self.name.text()
        age = self.age.text()
        username = self.username.text()
        password = self.password.text()
        crush = self.crush.text()
        gender = self.gender.currentText()
        
        if name and age and username and password and crush and gender:
            new_user = User(name, int(age), username, password, crush, gender)
            registered_users.append(new_user)
            QMessageBox.information(self, "Success", "Account created successfully!")
            self.close()
            self.login_page = LoginWindow()
            self.login_page.show()
        else:
            QMessageBox.warning(self, "Error", "Please fill all fields!")
        
        
    def handle_register(self):
        print("Registering...")
        

class HomePageWindow(QMainWindow):
    def __init__(self, user: User):
        super().__init__()
        user.display_info()
        uic.loadUi('homepage.ui', self)
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
        