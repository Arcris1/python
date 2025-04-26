from PyQt6.QtWidgets import QApplication
import sys

from controllers.LoginApp import LoginApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())