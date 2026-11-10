import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from my_project import validate_triangle, get_triangle_type, calculate_vertices, scale_and_center_points

class TestTriangleProject(unittest.TestCase):

    def test_valid_triangle_returns_true(self):
        self.assertTrue(validate_triangle(3, 4, 5))

    def test_invalid_zero_side_returns_false(self):
        self.assertFalse(validate_triangle(0, 4, 5))

    def test_invalid_negative_side_returns_false(self):
        self.assertFalse(validate_triangle(-3, 4, 5))

    def test_invalid_triangle_inequality_returns_false(self):
        self.assertFalse(validate_triangle(2, 3, 5))

    def test_equilateral_triangle_type(self):
        self.assertEqual(get_triangle_type(5, 5, 5), "равносторонний")

    def test_isosceles_triangle_type(self):
        self.assertEqual(get_triangle_type(5, 5, 3), "равнобедренный")

    def test_scalene_triangle_type(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "разносторонний")

    def test_vertices_calculation_right_triangle(self):
        vertices = calculate_vertices(3, 4, 5)
        self.assertAlmostEqual(vertices[2][0], 0.0)
        self.assertAlmostEqual(vertices[2][1], 4.0)

    def test_scaling_fits_in_canvas(self):
        points = [(0, 0), (10, 0), (5, 8.66)]
        scaled = scale_and_center_points(points)
        for x, y in scaled:
            self.assertGreaterEqual(x, 0)
            self.assertLessEqual(x, 100)
            self.assertGreaterEqual(y, 0)
            self.assertLessEqual(y, 100)

    # НОВЫЙ 10-й ТЕСТ для покрытия требования >= 10 тестов
    def test_scaling_very_small_triangle(self):
        # Проверка, что масштабирование корректно работает для очень маленького треугольника
        points = [(0.0, 0.0), (0.1, 0.0), (0.0, 0.1)]
        scaled = scale_and_center_points(points)
        # Проверяем, что точки не схлопнулись в одну и остались в пределах холста
        self.assertTrue(len(set(scaled)) >= 2)
        for x, y in scaled:
            self.assertGreaterEqual(x, 0)
            self.assertLessEqual(x, 100)

if __name__ == '__main__':
    unittest.main()