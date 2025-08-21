import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone 스타일 계산기")
        self.setFixedSize(300, 400)

        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")

        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            ["AC", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        row = 0
        for row_values in buttons:
            col = 0
            for btn_text in row_values:
                btn = QPushButton(btn_text)
                btn.setFixedSize(60, 60)
                btn.setStyleSheet(self.style_for_button(btn_text))
                btn.clicked.connect(self.on_button_click)

                if btn_text == "0":
                    grid.addWidget(btn, row, col, 1, 2)  # 0은 가로로 2칸
                    col += 2
                    continue

                grid.addWidget(btn, row, col)
                col += 1
            row += 1

        layout.addLayout(grid)
        self.setLayout(layout)

    def style_for_button(self, text):
        if text in {"AC", "±", "%"}:
            return "background-color: lightgray; font-size: 18px;"
        elif text in {"÷", "×", "−", "+", "="}:
            return "background-color: orange; color: white; font-size: 18px;"
        else:
            return "background-color: #333; color: white; font-size: 18px;"

    def on_button_click(self):
        btn = self.sender()
        current = self.display.text()
        new_text = btn.text()
        self.display.setText(current + new_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())