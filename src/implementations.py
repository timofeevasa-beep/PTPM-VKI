from src.interfaces import IUserInput, IExternalService

class ConsoleInput(IUserInput):
    def get_sides(self):
        a = float(input("Введите сторону a: "))
        b = float(input("Введите сторону b: "))
        c = float(input("Введите сторону c: "))
        return a, b, c

class EmailService(IExternalService):
    def send_result(self, data: str):
        # Имитация отправки на сервер
        print(f"[EMAIL SERVER] Отправлено сообщение: {data}")