import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone 스타일 공학용 계산기")
        self.setFixedSize(620, 500)
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(80)
        self.display.setStyleSheet("font-size: 28px; padding: 10px; border-radius: 10px;")
        layout.addWidget(self.display)

        grid = QGridLayout()

        self.clear_or_back_btn = QPushButton("AC")
        self.clear_or_back_btn.setFixedSize(50, 50)
        self.clear_or_back_btn.setStyleSheet(self.style_for_button("AC"))
        self.clear_or_back_btn.clicked.connect(self.on_clear_or_back_click)
        grid.addWidget(self.clear_or_back_btn, 0, 6)    # (0, 6) 위치

        buttons = [
            ["(", ")", "mc", "m+", "m−", "mr", None, "±", "%", "÷"],
            ["2ⁿ", "x²", "x³", "xʸ", "eˣ", "10ˣ", "7", "8", "9", "×"],
            ["1/x", "²√x", "³√x", "ʸ√x", "ln", "log₁₀", "4", "5", "6", "−"],
            ["x!", "sin", "cos", "tan", "e", "EE", "1", "2", "3", "+"],
            ["🙂", "sinh", "cosh", "tanh", "π", "Rad", "Rand", "0", ".", "="]
        ]

        for row, row_values in enumerate(buttons):
            for col, btn_text in enumerate(row_values):
                if btn_text is None:
                    continue     # 동적 버튼 위치는 건너뜀
                btn = QPushButton(btn_text)
                btn.setFixedSize(50, 50)
                btn.setStyleSheet(self.style_for_button(btn_text))
                btn.clicked.connect(self.on_button_click)
                grid.addWidget(btn, row, col)

        layout.addLayout(grid)
        self.setLayout(layout)

    def style_for_button(self, text):
        base_style = "font-size: 16px; border-radius: 20px; margin: 2px;"
        if text in {"mc", "m+", "m−", "mr"}:
            return f"{base_style} background-color: #333; color: white;"
        elif text in {"AC", "⌫", "±", "%"}:
            return f"{base_style} background-color: gray; color: white;"
        elif text in {"÷", "×", "−", "+", "="}:
            return f"{base_style} background-color: orange; color: white;"
        else:
            return f"{base_style} background-color: #333; color: white;"

    def update_clear_or_back_label(self):
        if self.display.text():
            self.clear_or_back_btn.setText("⌫")
        else:
            self.clear_or_back_btn.setText("AC")

    def on_clear_or_back_click(self):
        if self.clear_or_back_btn.text() == "⌫":
            self.display.setText(self.display.text()[:-1])
        else:
            self.display.setText("")
            
    def on_button_click(self):
        btn = self.sender()
        text = btn.text()
        # 입력만 표시 (기능은 구현하지 않음)
        current = self.display.text()
        self.display.setText(current + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())