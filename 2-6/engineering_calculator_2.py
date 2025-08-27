import sys
import math
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt

class EngineeringCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Engineering Calculator")
        self.setFixedSize(620, 500)
        self.memory = 0.0
        self.rad_mode = True
        self.func_stack = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(80)
        self.display.setStyleSheet("font-size: 28px; padding: 10px; border-radius: 10px;")
        self.display.textChanged.connect(self.update_clear_label)
        layout.addWidget(self.display)

        self.grid = QGridLayout()
        self.clear_btn = QPushButton("AC")
        self.clear_btn.setFixedSize(50, 50)
        self.clear_btn.setStyleSheet(self.button_style("AC"))
        self.clear_btn.clicked.connect(self.handle_clear_or_back)
        self.grid.addWidget(self.clear_btn, 0, 6)

        self.buttons = [
            ["(", ")", "mc", "m+", "m−", "mr", None, "±", "%", "÷"],
            ["2ⁿ", "x²", "x³", "xʸ", "eˣ", "10ˣ", "7", "8", "9", "×"],
            ["1/x", "²√x", "³√x", "ʸ√x", "ln", "log", "4", "5", "6", "−"],
            ["x!", "sin", "cos", "tan", "e", "EE", "1", "2", "3", "+"],
            ["🙂", "sinh", "cosh", "tanh", "π", "Rad", "Rand", "0", ".", "="]
        ]
        self.add_buttons()
        layout.addLayout(self.grid)
        self.setLayout(layout)

    def button_style(self, text):
        base = "font-size: 16px; border-radius: 20px; margin: 2px;"
        if text in {"mc", "m+", "m−", "mr"}:
            return f"{base} background-color: #333; color: white;"
        elif text in {"AC", "⌫", "±", "%"}:
            return f"{base} background-color: gray; color: white;"
        elif text in {"÷", "×", "−", "+", "="}:
            return f"{base} background-color: orange; color: white;"
        elif text == "Rad":
            return f"{base} background-color: black; color: white;"
        else:
            return f"{base} background-color: #333; color: white;"

    def update_clear_label(self):
        self.clear_btn.setText("⌫" if self.display.text() else "AC")

    def handle_clear_or_back(self):
        if self.display.text():
            self.display.setText(self.display.text()[:-1])
        else:
            self.display.clear()
            self.func_stack.clear()

    def add_buttons(self):
        for row_idx, row in enumerate(self.buttons):
            for col_idx, text in enumerate(row):
                if text is None:
                    continue
                btn = QPushButton(text)
                btn.setFixedSize(50, 50)
                btn.setStyleSheet(self.button_style(text))
                btn.clicked.connect(self.handle_button)
                self.grid.addWidget(btn, row_idx, col_idx)

    def handle_button(self):
        sender = self.sender()
        text = sender.text()
        current = self.display.text()

        try:
            if text in {"sin", "cos", "tan", "sinh", "cosh", "tanh", "ln", "log"}:
                self.func_stack.append(text)
                self.display.clear()
            elif text == "=":
                self.compute_result()
            elif text == "π":
                self.display.setText(str(math.pi))
            elif text == "e":
                self.display.setText(str(math.e))
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
            elif text == "x²":
                self.display.setText(str(float(current) ** 2))
            elif text == "x³":
                self.display.setText(str(float(current) ** 3))
            elif text == "xʸ":
                self.func_stack.append(("pow", float(current)))
                self.display.clear()
            elif text == "ʸ√x":
                self.func_stack.append(("root", float(current)))
                self.display.clear()
            elif text == "2ⁿ":
                self.display.setText(str(2 ** float(current)))
            elif text == "eˣ":
                self.display.setText(str(math.exp(float(current))))
            elif text == "10ˣ":
                self.display.setText(str(10 ** float(current)))
            elif text == "1/x":
                self.display.setText(str(1 / float(current)))
            elif text == "²√x":
                self.display.setText(str(math.sqrt(float(current))))
            elif text == "³√x":
                self.display.setText(str(float(current) ** (1 / 3)))
            elif text == "x!":
                self.display.setText(str(math.factorial(int(float(current)))))
            elif text == "±":
                self.display.setText(current[1:] if current.startswith("-") else "-" + current)
            elif text == "%":
                self.display.setText(str(float(current) / 100))
            elif text == "EE":
                self.display.setText(current + "e")
            elif text == "🙂":
                self.display.setText("🙂 Hello!")
            else:
                self.display.setText(current + text)
        except:
            self.display.setText("Error")
            self.func_stack.clear()

    def compute_result(self):
        expr = self.display.text()
        try:
            if self.func_stack:
                func = self.func_stack.pop()
                if isinstance(func, tuple):
                    if func[0] == "pow":
                        result = math.pow(func[1], float(expr))
                    elif func[0] == "root":
                        result = float(expr) ** (1 / func[1])
                else:
                    angle = float(expr)
                    if func in {"sin", "cos", "tan"} and not self.rad_mode:
                        angle = math.radians(angle)
                    if func == "log":
                        result = math.log10(angle)
                    elif func == "ln":
                        result = math.log(angle)
                    else:
                        result = getattr(math, func)(angle)
                self.display.setText(str(result))
            else:
                self.display.setText(str(eval(expr.replace("÷", "/").replace("×", "*").replace("−", "-"))))
        except:
            self.display.setText("Error")
            self.func_stack.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EngineeringCalculator()
    window.show()
    sys.exit(app.exec())