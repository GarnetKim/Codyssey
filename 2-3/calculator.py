import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QVBoxLayout, QGridLayout, QLineEdit)
from PyQt5.QtCore import Qt


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone 스타일 계산기")
        self.setFixedSize(300, 400)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("font-size: 24px;")
        main_layout.addWidget(self.display)

        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)

        buttons = [
            ['AC', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '−'],
            ['1', '2', '3', '+'],
            [' ', '0', '.', '=']
        ]

        for row, row_values in enumerate(buttons):
            for col, button_text in enumerate(row_values):
                if button_text == '0':
                    button = QPushButton(button_text)
                    button.setFixedHeight(60)
                    button.setFixedWidth(140)
                    grid_layout.addWidget(button, row + 1, col, 1, 2)  # 2칸 차지
                    button.clicked.connect(self.handle_button_click)
                elif button_text == '=':
                    button = QPushButton(button_text)
                    button.setFixedHeight(60)
                    button.setFixedWidth(70)
                    grid_layout.addWidget(button, row + 1, col + 1)
                    button.clicked.connect(self.handle_button_click)
                else:
                    button = QPushButton(button_text)
                    button.setFixedSize(70, 60)
                    grid_layout.addWidget(button, row + 1, col)
                    button.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        button = self.sender()
        text = button.text()

        # 계산 기능 제외, 입력만 표시
        current = self.display.text()

        if text == 'AC':
            self.display.clear()
        elif text == '±':  # ± = ± = ±: plus/minus
            if current.startswith('-'):
                self.display.setText(current[1:])
            elif current:
                self.display.setText('-' + current)
        else:
            self.display.setText(current + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())