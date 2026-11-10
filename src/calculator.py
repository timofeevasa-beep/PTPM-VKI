class TriangleCalculator:
    def calculate(self, a: float, b: float, c: float) -> tuple[str, str | None]:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны должны быть строго положительными")

        if a + b <= c or a + c <= b or b + c <= a:
            return "Не существует", "Нарушено неравенство треугольника"

        if a == b == c:
            return "Равносторонний", None
        if a == b or b == c or a == c:
            return "Равнобедренный", None

        return "Разносторонний", None