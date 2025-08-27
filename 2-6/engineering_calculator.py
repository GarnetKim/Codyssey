import sys
import math
import random
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt


# -----------------------------
# Base Calculator (UI scaffolding)
# -----------------------------
class Calculator(QWidget):
    def __init__(self, *, width=620, height=500, title="iPhone 스타일 공학용 계산기"):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)
        self._buttons = []  # subclass가 채움
        self._grid = None
        self._layout = None
        self._button_refs = {}  # label -> list[QPushButton]
        self._build_base_ui()

    # 공통 UI 뼈대 구성 (디스플레이 + 그리드 + 동적 AC/⌫ 버튼)
    def _build_base_ui(self):
        layout = QVBoxLayout()
        self._layout = layout

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(80)
        self.display.setStyleSheet("font-size: 28px; padding: 10px; border-radius: 10px;")
        self.display.textChanged.connect(self._update_clear_or_back_label)
        layout.addWidget(self.display)

        # Grid
        grid = QGridLayout()
        self._grid = grid

        # 동적 버튼(AC/⌫)을 (0,6)에 배치
        self.clear_or_back_btn = QPushButton("AC")
        self.clear_or_back_btn.setFixedSize(50, 50)
        self.clear_or_back_btn.setStyleSheet(self.style_for_button("AC"))
        self.clear_or_back_btn.clicked.connect(self._on_clear_or_back_click)
        grid.addWidget(self.clear_or_back_btn, 0, 6)
        self._remember_button("AC", self.clear_or_back_btn)

        layout.addLayout(grid)
        self.setLayout(layout)

    # 스타일 공통
    def style_for_button(self, text: str) -> str:
        base_style = "font-size: 16px; border-radius: 20px; margin: 2px;"
        if text in {"mc", "m+", "m−", "mr"}:
            return f"{base_style} background-color: #333; color: white;"
        elif text in {"AC", "⌫", "±", "%"}:
            return f"{base_style} background-color: gray; color: white;"
        elif text in {"÷", "×", "−", "+", "="}:
            return f"{base_style} background-color: orange; color: white;"
        elif text in {"Rad", "Deg"}:  # 라벨 토글 대응
            return f"{base_style} background-color: black; color: white;"
        else:
            return f"{base_style} background-color: #333; color: white;"

    # 버튼 매트릭스 추가 (None은 비워두기; (0,6)는 이미 동적 버튼)
    def _add_buttons(self, buttons_matrix):
        for row, row_vals in enumerate(buttons_matrix):
            for col, label in enumerate(row_vals):
                if label is None:
                    continue
                if row == 0 and col == 6:
                    # 동적 버튼 자리이므로 skip
                    continue
                btn = QPushButton(label)
                btn.setFixedSize(50, 50)
                btn.setStyleSheet(self.style_for_button(label))
                btn.clicked.connect(self.on_button_click)  # subclass에서 구현
                self._grid.addWidget(btn, row, col)
                self._remember_button(label, btn)

    # label -> 버튼 참조 저장 (동일 라벨 여러 개 대비)
    def _remember_button(self, label: str, btn: QPushButton):
        self._button_refs.setdefault(label, []).append(btn)

    # 표시 내용에 따라 AC/⌫ 라벨 갱신
    def _update_clear_or_back_label(self):
        self.clear_or_back_btn.setText("⌫" if self.display.text() else "AC")
        # 스타일도 라벨에 맞춰 갱신
        self.clear_or_back_btn.setStyleSheet(self.style_for_button(self.clear_or_back_btn.text()))

    # AC/⌫ 클릭 처리 (공통)
    def _on_clear_or_back_click(self):
        if self.clear_or_back_btn.text() == "⌫":
            self.display.setText(self.display.text()[:-1])
        else:
            self.display.setText("")

    # 안전한 eval (사칙연산/괄호만)
    def safe_eval(self, expr: str) -> float:
        expr = (
            expr.replace("÷", "/")
                .replace("×", "*")
                .replace("−", "-")
        )
        # 과학 표기용 'e'는 숫자 뒤에 올 수 있으므로 그대로 허용
        allowed = {"__builtins__": None, "math": math, "pi": math.pi, "e": math.e}
        return eval(expr, allowed, {})

    # 하위 클래스에서 버튼 클릭 로직 구현
    def on_button_click(self):
        raise NotImplementedError("Subclass must implement on_button_click")


# -------------------------------------
# EngineeringCalculator (공학 기능 확장)
# -------------------------------------
class EngineeringCalculator(Calculator):
    def __init__(self):
        # 상태들 먼저 준비
        self.memory = 0.0
        self.rad_mode = True  # True: 라디안, False: 도
        self.expecting = None  # ("pow", base) / ("root", degree)
        super().__init__(title="iPhone 스타일 공학용 계산기")

        # 버튼 매트릭스 정의 (동적 자리 (0,6)는 None)
        self._buttons = [
            ["(", ")", "mc", "m+", "m−", "mr", None, "±", "%", "÷"],
            ["2ⁿ", "x²", "x³", "xʸ", "eˣ", "10ˣ", "7", "8", "9", "×"],
            ["1/x", "²√x", "³√x", "ʸ√x", "ln", "log₁₀", "4", "5", "6", "−"],
            ["x!", "sin", "cos", "tan", "e", "EE", "1", "2", "3", "+"],
            ["🙂", "sinh", "cosh", "tanh", "π", "Rad", "Rand", "0", ".", "="],
        ]
        self._add_buttons(self._buttons)

    # --------- 공학 연산 메서드 분리 ---------
    def _angle_in_radians(self, x: float) -> float:
        return x if self.rad_mode else math.radians(x)

    def calc_sin(self, x):  return math.sin(self._angle_in_radians(x))
    def calc_cos(self, x):  return math.cos(self._angle_in_radians(x))
    def calc_tan(self, x):  return math.tan(self._angle_in_radians(x))
    def calc_sinh(self, x): return math.sinh(x)
    def calc_cosh(self, x): return math.cosh(x)
    def calc_tanh(self, x): return math.tanh(x)

    def calc_square(self, x): return x ** 2
    def calc_cube(self, x):   return x ** 3
    def pow_2_n(self, n):     return 2 ** n
    def exp_e_x(self, x):     return math.exp(x)
    def exp_10_x(self, x):    return 10 ** x

    def recip(self, x):       return 1 / x
    def sqrt2(self, x):       return math.sqrt(x)
    def sqrt3(self, x):       return x ** (1/3)
    def ln(self, x):          return math.log(x)
    def log10(self, x):       return math.log10(x)
    def fact(self, x):        return math.factorial(int(x))

    def const_pi(self):       return math.pi
    def const_e(self):        return math.e

    # -----------------------------------------
    # 버튼 클릭 핸들러
    # -----------------------------------------
    def on_button_click(self):
        btn = self.sender()
        label = btn.text()
        cur = self.display.text()

        try:
            # 숫자/점/괄호/연산자(사칙) → 그대로 누적
            if label.isdigit() or label in {".", "(", ")"} or label in {"+", "−", "×", "÷"}:
                self.display.setText(cur + label)
                return

            # 부호 토글
            if label == "±":
                if cur:
                    self.display.setText(cur[1:] if cur.startswith("-") else "-" + cur)
                return

            # 백분율
            if label == "%":
                if cur:
                    self.display.setText(str(float(cur) / 100.0))
                return

            # EE (과학 표기)
            if label == "EE":
                # 숫자 없으면 1e 형태로 시작
                if not cur or not (cur[-1].isdigit() or cur[-1] == "."):
                    self.display.setText((cur if cur else "") + "1e")
                else:
                    # 이미 e/E 가 있다면 추가하지 않음
                    if "e" not in cur and "E" not in cur:
                        self.display.setText(cur + "e")
                return

            # 메모리 기능
            if label == "mc":
                self.memory = 0.0
                return
            if label == "m+":
                if cur: self.memory += float(cur)
                return
            if label == "m−":
                if cur: self.memory -= float(cur)
                return
            if label == "mr":
                self.display.setText(str(self.memory))
                return

            # 모드 토글 (Rad/Deg)
            if label in {"Rad", "Deg"}:
                self.rad_mode = not self.rad_mode
                # 버튼 라벨/스타일도 토글
                new_label = "Rad" if self.rad_mode else "Deg"
                btn.setText(new_label)
                btn.setStyleSheet(self.style_for_button(new_label))
                return

            # 난수
            if label == "Rand":
                self.display.setText(str(round(random.random(), 8)))
                return

            # 상수
            if label == "π":
                self.display.setText(str(self.const_pi()))
                return
            if label == "e":
                self.display.setText(str(self.const_e()))
                return

            # 2ⁿ, x², x³, eˣ, 10ˣ
            if label == "2ⁿ":
                if cur: self.display.setText(str(self.pow_2_n(float(cur))))
                return
            if label == "x²":
                if cur: self.display.setText(str(self.calc_square(float(cur))))
                return
            if label == "x³":
                if cur: self.display.setText(str(self.calc_cube(float(cur))))
                return
            if label == "eˣ":
                if cur: self.display.setText(str(self.exp_e_x(float(cur))))
                return
            if label == "10ˣ":
                if cur: self.display.setText(str(self.exp_10_x(float(cur))))
                return

            # 역수/루트/로그/팩토리얼
            if label == "1/x":
                if cur: self.display.setText(str(self.recip(float(cur))))
                return
            if label == "²√x":
                if cur: self.display.setText(str(self.sqrt2(float(cur))))
                return
            if label == "³√x":
                if cur: self.display.setText(str(self.sqrt3(float(cur))))
                return
            if label == "ln":
                if cur: self.display.setText(str(self.ln(float(cur))))
                return
            if label == "log₁₀":
                if cur: self.display.setText(str(self.log10(float(cur))))
                return
            if label == "x!":
                if cur: self.display.setText(str(self.fact(float(cur))))
                return

            # 삼각/쌍곡 함수
            if label in {"sin", "cos", "tan", "sinh", "cosh", "tanh"}:
                if not cur:
                    return
                x = float(cur)
                func_map = {
                    "sin": self.calc_sin, "cos": self.calc_cos, "tan": self.calc_tan,
                    "sinh": self.calc_sinh, "cosh": self.calc_cosh, "tanh": self.calc_tanh
                }
                self.display.setText(str(func_map[label](x)))
                return

            # 이항 연산(두 값 필요): xʸ, ʸ√x
            if label == "xʸ":
                if cur:
                    self.expecting = ("pow", float(cur))
                    self.display.setText("")  # 두 번째 값 입력 대기
                return
            if label == "ʸ√x":
                if cur:
                    self.expecting = ("root", float(cur))  # 저장: y (root degree)
                    self.display.setText("")               # 이후 x 입력 대기
                return

            # 이스터에그
            if label == "🙂":
                self.display.setText("🙂 Hello!")
                return

            # = 처리 (일반 수식 or 이항 연산 확정)
            if label == "=":
                if self.expecting:
                    mode, first = self.expecting
                    if not cur:
                        return
                    second = float(cur)
                    if mode == "pow":
                        self.display.setText(str(math.pow(first, second)))
                    elif mode == "root":
                        # y√x = x ** (1/y)  (first = y, second = x)
                        self.display.setText(str(second ** (1.0 / first)))
                    self.expecting = None
                else:
                    # 일반식 평가
                    res = self.safe_eval(self.display.text())
                    self.display.setText(str(res))
                return

            # 그 외 텍스트는 그대로 붙임(혹시 남은 기호가 있을 경우)
            self.display.setText(cur + label)

        except Exception:
            self.display.setText("Error")


# -----------------------------
# main
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EngineeringCalculator()
    window.show()
    sys.exit(app.exec())