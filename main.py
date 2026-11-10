from src.calculator import TriangleCalculator
from src.database import TriangleDB
from src.implementations import ConsoleInput, EmailService
from src.controller import TriangleController


def main():
    db = TriangleDB("triangle.db")
    calc = TriangleCalculator()
    user_input = ConsoleInput()
    ext_service = EmailService()

    controller = TriangleController(calc, db, user_input, ext_service)

    print("--- Запуск программы ---")
    result = controller.process()
    print(f"Итоговый результат: {result}")

    db.close()


if __name__ == "__main__":
    main()