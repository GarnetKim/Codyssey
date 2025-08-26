import sys
import math
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone 스타일 공학용 계산기")
        self.setFixedSize(620, 500)
        self.memory = 0.0
        self.rad_mode = True
        self.expecting_second_value = None
        self.temp_value = None
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(80)
        self.display.setStyleSheet("font-size: 28px; padding: 10px; border-radius: 10px;")
        self.display.textChanged.connect(self.update_clear_or_back_label)
        layout.addWidget(self.display)

        grid = QGridLayout()

        self.clear_or_back_btn = QPushButton("AC")
        self.clear_or_back_btn.setFixedSize(50, 50)
        self.clear_or_back_btn.setStyleSheet(self.style_for_button("AC"))
        self.clear_or_back_btn.clicked.connect(self.on_clear_or_back_click)
        grid.addWidget(self.clear_or_back_btn, 0, 6)

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
                    continue
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
        elif text == "Rad":
            return f"{base_style} background-color: black; color: white;"
        else:
            return f"{base_style} background-color: #333; color: white;"

    def update_clear_or_back_label(self):
        self.clear_or_back_btn.setText("⌫" if self.display.text() else "AC")

    def on_clear_or_back_click(self):
        self.display.setText(self.display.text()[:-1] if self.display.text() else "")

    def on_button_click(self):
        btn = self.sender()
        text = btn.text()
        current = self.display.text()

        try:
            if text in {"sin", "cos", "tan", "sinh", "cosh", "tanh"}:
                angle = float(current)
                if not self.rad_mode:
                    angle = math.radians(angle)
                func = getattr(math, text)
                self.display.setText(str(func(angle)))
            elif text in {"x²", "x³"}:
                power = 2 if text == "x²" else 3
                self.display.setText(str(float(current) ** power))
            elif text in {"π", "e"}:
                self.display.setText(str(getattr(math, "pi" if text == "π" else "e")))
            elif text == "xʸ":
                self.temp_value = float(current)
                self.expecting_second_value = ("pow",)
                self.display.setText("")
            elif text == "ʸ√x":
                self.temp_value = float(current)
                self.expecting_second_value = ("root",)
                self.display.setText("")
            elif text == "EE":
                self.display.setText(current + "e")
            elif text == "Rand":
                self.display.setText(str(round(math.random(), 5)))
            elif text == "Rad":
                self.rad_mode = not self.rad_mode
            elif text == "mc":
                self.memory = 0.0
            elif text == "m+":
                self.memory += float(current)
            elif text == "m−":
                self.memory -= float(current)
            elif text == "mr":
                self.display.setText(str(self.memory))
            elif self.expecting_second_value:
                mode = self.expecting_second_value[0]
                if mode == "pow":
                    self.display.setText(str(math.pow(self.temp_value, float(current))))
                elif mode == "root":
                    self.display.setText(str(float(current) ** (1 / self.temp_value)))
                self.expecting_second_value = None
                self.temp_value = None
            elif text == "=":
                result = eval(current.replace("÷", "/").replace("×", "*").replace("−", "-"))
                self.display.setText(str(result))
            elif text == "±":
                self.display.setText(current[1:] if current.startswith("-") else "-" + current)
            elif text == "%":
                self.display.setText(str(float(current) / 100))
            elif text == "🙂":
                self.display.setText("🙂 Hello!")
            else:
                self.display.setText(current + text)
        except:
            self.display.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
