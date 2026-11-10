import unittest
from unittest.mock import Mock
import sys
import os

# Добавляем путь к src, чтобы импорты работали
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import TriangleCalculator
from database import TriangleDB
from controller import TriangleController


class TestTriangleIntegration(unittest.TestCase):

    def setUp(self):
        # Для тестов используем БД в памяти (быстро и изолированно)
        self.db = TriangleDB(":memory:")
        self.calculator = TriangleCalculator()

        # Создаем заглушки (Mock) для ввода и внешнего сервиса
        self.mock_input = Mock()
        self.mock_ext_service = Mock()

        self.controller = TriangleController(
            self.calculator, self.db, self.mock_input, self.mock_ext_service
        )

    def tearDown(self):
        self.db.close()

    # --- ИНТЕГРАЦИОННЫЕ ТЕСТЫ (3 штуки) ---

    def test_integration_new_calculation(self):
        """Интеграционный тест 1: Полная цепочка, данных в БД нет."""
        # Настраиваем заглушку ввода
        self.mock_input.get_sides.return_value = (3.0, 4.0, 5.0)

        # Запускаем контроллер
        result = self.controller.process()

        # Проверяем результат
        self.assertEqual(result, "Разносторонний")

        # Проверяем, что данные реально сохранились в БД
        db_record = self.db.get(3.0, 4.0, 5.0)
        self.assertIsNotNone(db_record)
        self.assertEqual(db_record[0], "Разносторонний")

        # Проверяем, что внешний сервис был вызван
        self.mock_ext_service.send_result.assert_called_once()

    def test_integration_cache_hit(self):
        """Интеграционный тест 2: Данные уже есть в БД, калькулятор не должен вызываться."""
        # Предварительно кладем данные в реальную БД
        self.db.add(5.0, 5.0, 5.0, "Равносторонний", None)

        self.mock_input.get_sides.return_value = (5.0, 5.0, 5.0)

        # Подменяем реальный калькулятор на Mock, чтобы проверить, что он НЕ вызывался
        self.controller.calculator = Mock()

        result = self.controller.process()

        self.assertEqual(result, "Равносторонний")
        # Калькулятор не должен был вызываться, так как данные взяты из БД
        self.controller.calculator.calculate.assert_not_called()
        self.mock_ext_service.send_result.assert_called_once()

    def test_integration_invalid_input(self):
        """Интеграционный тест 3: Ошибка ввода (отрицательные стороны)."""
        self.mock_input.get_sides.return_value = (-1.0, 2.0, 3.0)

        result = self.controller.process()

        self.assertIn("Ошибка", result)
        # Проверяем, что ошибка сохранилась в БД
        db_record = self.db.get(-1.0, 2.0, 3.0)
        self.assertIsNotNone(db_record)
        self.assertEqual(db_record[0], "Ошибка ввода")

        # Проверяем, что внешний сервис получил сообщение об ошибке
        call_args = self.mock_ext_service.send_result.call_args[0][0]
        self.assertIn("Ошибка", call_args)

    # --- ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ (для покрытия и проверки БД) ---

    def test_db_add_and_get(self):
        """Проверка методов добавления и получения в БД."""
        self.db.add(1.0, 1.0, 1.0, "Равносторонний", None)
        record = self.db.get(1.0, 1.0, 1.0)
        self.assertEqual(record, ("Равносторонний", None))

    def test_db_delete(self):
        """Проверка метода удаления из БД."""
        self.db.add(2.0, 2.0, 3.0, "Равнобедренный", None)
        self.db.delete(2.0, 2.0, 3.0)
        record = self.db.get(2.0, 2.0, 3.0)
        self.assertIsNone(record)


if __name__ == '__main__':
    unittest.main()