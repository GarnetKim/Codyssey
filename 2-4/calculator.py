import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton,QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt

class CalculatorEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current = ""
        self.operator = ""
        self.previous = ""
        self.result_shown = False

    def input(self, value):
        if self.result_shown:
            self.current = ""
            self.result_shown = False
        self.current += value
        return self.current

    def set_operator(self, op):
        if self.current:
            self.previous = self.current
            self.operator = op
            self.current = ""
        return op

    def calculate(self):
        try:
            a = float(self.previous)
            b = float(self.current)
            result = 0
            if self.operator == "+":
                result = a + b
            elif self.operator == "−":
                result = a - b
            elif self.operator == "×":
                result = a * b
            elif self.operator == "÷":
                if b == 0:
                    return "Error"
                result = a / b
            else:
                return self.current
            self.reset()
            self.result_shown = True
            self.current = str(result)
            return self.current
        except:
            return "Error"

    def toggle_sign(self):
        if self.current:
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
        return self.current

    def percent(self):
        try:
            self.current = str(float(self.current) / 100)
        except:
            self.current = "Error"
        return self.current


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone 스타일 계산기")
        self.setFixedSize(360, 450)
        self.engine = CalculatorEngine()
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("font-size: 24px; padding: 10px; border-radius: 10px;")

        layout.addWidget(self.display)

        grid = QGridLayout()

        buttons = [
            ["⌫", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["🙂", "0", ".", "="]
        ]

        row = 0
        for row_values in buttons:
            col = 0
            for btn_text in row_values:
                btn = QPushButton(btn_text)
                btn.setFixedHeight(60)
                btn.setFixedSize(70, 60)
                btn.setStyleSheet(self.style_for_button(btn_text))
                grid.addWidget(btn, row, col)
                btn.clicked.connect(self.on_button_click)
                col += 1
            row += 1

        layout.addLayout(grid)
        self.setLayout(layout)
        
    def style_for_button(self, text):
        base_style = "font-size: 18px; border-radius: 30px;"
        if text in {"⌫", "±", "%"}:
            return f"{base_style} background-color: lightgray;"
        elif text in {"÷", "×", "−", "+", "="}:
            return f"{base_style} background-color: orange; color: white;"
        elif text == "🙂":
            return f"{base_style} background-color: #555; color: white;"
        else:
            return f"{base_style} background-color: #333; color: white;"
        
    def on_button_click(self):
        btn = self.sender()
        text = btn.text()

        if text in "0123456789":
            updated = self.engine.input(text)
            self.display.setText(updated)
        elif text == ".":
            if "." not in self.engine.current:
                updated = self.engine.input(".")
                self.display.setText(updated)
        elif text in {"+", "−", "×", "÷"}:
            self.engine.set_operator(text)
        elif text == "=":
            result = self.engine.calculate()
            self.display.setText(result)
        elif text == "⌫":
            self.engine.reset()
            self.display.setText("")
        elif text == "±":
            updated = self.engine.toggle_sign()
            self.display.setText(updated)
        elif text == "%":
            updated = self.engine.percent()
            self.display.setText(updated)
        elif text == "🙂":
            self.display.setText("🙂 Hello!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())