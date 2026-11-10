# tests/test_delivery.py
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from delivery_service import calculate_delivery_cost

class TestDeliveryService(unittest.TestCase):

    def test_base_cost_short_distance(self):
        # 100 (база) + 10*5 (км) + 2*10 (кг) = 170
        self.assertEqual(calculate_delivery_cost(2, 10), 170)

    def test_negative_weight_handling(self):
        # Ожидаем, что отрицательный вес либо вызывает ошибку, либо возвращает None/ошибку.
        # Но код возвращает 0, что является багом.
        self.assertNotEqual(calculate_delivery_cost(-5, 10), 0)

    def test_discount_applied_correctly_long_distance(self):
        # 100 + 200*5 + 5*10 = 1150. Скидка 20% -> 1150 * 0.8 = 920.
        # Код делает 1150 - 20 = 1130 (БАГ)
        self.assertEqual(calculate_delivery_cost(5, 200), 920)

    def test_express_multiplier(self):
        # 170 * 1.5 = 255
        self.assertEqual(calculate_delivery_cost(2, 10, is_express=True), 255)

    def test_express_with_discount(self):
        # 1150 * 0.8 = 920. Экспресс: 920 * 1.5 = 1380.
        self.assertEqual(calculate_delivery_cost(5, 200, is_express=True), 1380)

    def test_zero_weight(self):
        # 100 + 10*5 + 0 = 150
        self.assertEqual(calculate_delivery_cost(0, 10), 150)

    def test_zero_distance(self):
        # 100 + 0 + 2*10 = 120
        self.assertEqual(calculate_delivery_cost(2, 0), 120)

    def test_boundary_distance_exactly_100(self):
        # Ровно 100 км, скидки нет. 100 + 500 + 50 = 650
        self.assertEqual(calculate_delivery_cost(5, 100), 650)

    def test_boundary_distance_101(self):
        # 101 км, скидка есть. 100 + 505 + 50 = 655. 655 * 0.8 = 524.
        self.assertEqual(calculate_delivery_cost(5, 101), 524)

    def test_large_weight(self):
        # Проверка на отсутствие переполнения или скрытых багов
        self.assertEqual(calculate_delivery_cost(100, 10), 1600)

if __name__ == '__main__':
    unittest.main()