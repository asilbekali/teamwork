from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt

class Oyna(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Instagram")
        self.setFixedSize(600, 600)
        self.setWindowIcon(QIcon('in.jpg'))

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("side.jpg"))
        self.background.setGeometry(0, 0, 600, 600)

        self.title_label = QLabel("Instagram", self)
        self.title_label.setFont(QFont("Brush Script MT", 25, QFont.Bold))
        self.title_label.setGeometry(200, 15, 300, 100)
        self.title_label.setStyleSheet("color: white;")

        self.subtitle_label = QLabel(
            "---------------------- Instagram Login ----------------------", self
        )
        self.subtitle_label.setGeometry(50, 440, 500, 40)
        self.subtitle_label.setStyleSheet("color: white; font-size: 20px;")

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Phone number, Username, or Email")
        self.username_input.setGeometry(130, 150, 350, 40)
        self.username_input.setStyleSheet(
            "border-radius: 7px; border: 3px solid #aaa; font-size: 16px;"
        )

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setGeometry(130, 220, 350, 40)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(
            "border-radius: 7px; border: 3px solid #aaa; font-size: 16px;"
        )

        self.signup_button = QPushButton("Sign Up", self)
        self.signup_button.setGeometry(130, 380, 350, 40)
        self.signup_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 10px;
                border: 2px solid #2980b9;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
                border: 2px solid #16a085;
            }
        """)
        self.signup_button.clicked.connect(self.button_clicked)

        self.goit = QLabel("", self)
        self.goit.setGeometry(120, 500, 350, 40)
        self.goit.setFont(QFont("Brush Script MT", 25, QFont.Bold))
        self.goit.setStyleSheet("color: white;")
        self.goit.setAlignment(Qt.AlignCenter)

    def button_clicked(self):
        with open("data.txt", "w+") as file:
            if self.username_input.text().endswith("@gmail.com"):
                file.write(f"User name: {self.username_input.text()}\n")
                file.write(f"Password: {self.password_input.text()}\n")
            else:
                self.goit.setText("Error")
                return

        self.username_input.clear()
        self.password_input.clear()


        self.goit.setText("Data saved")

if __name__ == "__main__":
    app = QApplication([])

    window = Oyna()
    window.show()

    app.exec_()
