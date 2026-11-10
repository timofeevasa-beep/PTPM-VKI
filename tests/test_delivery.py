import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from delivery_service import calculate_delivery_cost

class TestDeliveryService(unittest.TestCase):

    def test_base_calculation_normal_package(self):
        cost, date = calculate_delivery_cost(2.0, 100, "обычный")
        self.assertEqual(cost, 700)
        self.assertEqual(date, "2026-09-04")

    def test_invalid_weight_too_low(self):
        cost, date = calculate_delivery_cost(0.05, 100, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_weight_too_high(self):
        cost, date = calculate_delivery_cost(55.0, 100, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_distance_out_of_bounds(self):
        cost, date = calculate_delivery_cost(5.0, 5001, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_package_type(self):
        cost, date = calculate_delivery_cost(2.0, 100, "секретный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_weight_boundary_exactly_5kg(self):
        cost, date = calculate_delivery_cost(5.0, 100, "обычный")
        self.assertEqual(cost, 840)

    def test_weight_heavy_multiplier(self):
        cost, date = calculate_delivery_cost(25.0, 100, "обычный")
        self.assertEqual(cost, 1050)

    def test_fragile_package_surcharge(self):
        cost, date = calculate_delivery_cost(2.0, 100, "хрупкий")
        self.assertEqual(cost, 1000)

    def test_dangerous_package_surcharge(self):
        cost, date = calculate_delivery_cost(2.0, 100, "опасный")
        self.assertEqual(cost, 1700)

    def test_express_delivery_logic(self):
        cost, date = calculate_delivery_cost(2.0, 100, "обычный", is_express=True)
        self.assertEqual(cost, 1050)
        self.assertEqual(date, "2026-09-04")

if __name__ == '__main__':
    unittest.main()