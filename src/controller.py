from src.interfaces import IUserInput, IExternalService


class TriangleController:
    def __init__(self, calculator, db, user_input: IUserInput, ext_service: IExternalService):
        self.calculator = calculator
        self.db = db
        self.user_input = user_input
        self.ext_service = ext_service

    def process(self) -> str:
        # 1. Запрос данных
        a, b, c = self.user_input.get_sides()

        # 2. Проверка БД
        db_record = self.db.get(a, b, c)

        if db_record:
            t_type, error = db_record
            result = t_type if not error else f"Ошибка: {error}"
        else:
            # 3. Вычисление и сохранение
            try:
                t_type, error = self.calculator.calculate(a, b, c)
                self.db.add(a, b, c, t_type, error)
                result = t_type if not error else f"Ошибка: {error}"
            except Exception as e:
                self.db.add(a, b, c, "Ошибка ввода", str(e))
                result = f"Ошибка: {e}"

        # 4. Отправка сторонней зависимости
        payload = f"Стороны: {a}, {b}, {c} | Результат: {result}"
        self.ext_service.send_result(payload)

        # 5. Возврат результата
        return result