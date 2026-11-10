# tests/test_my_project.py
import unittest
import sys
import os

# Добавляем папку src в путь, чтобы импортировать модуль
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from my_project import validate_triangle, get_triangle_type, calculate_vertices, scale_and_center_points

class TestTriangleProject(unittest.TestCase):

    # --- Тесты валидации ---
    def test_valid_triangle_returns_true(self):
        self.assertTrue(validate_triangle(3, 4, 5))

    def test_invalid_zero_side_returns_false(self):
        self.assertFalse(validate_triangle(0, 4, 5))

    def test_invalid_negative_side_returns_false(self):
        self.assertFalse(validate_triangle(-3, 4, 5))

    def test_invalid_triangle_inequality_returns_false(self):
        # Сумма двух сторон равна третьей (не треугольник)
        self.assertFalse(validate_triangle(2, 3, 5))

    # --- Тесты типов треугольников ---
    def test_equilateral_triangle_type(self):
        self.assertEqual(get_triangle_type(5, 5, 5), "равносторонний")

    def test_isosceles_triangle_type(self):
        self.assertEqual(get_triangle_type(5, 5, 3), "равнобедренный")

    def test_scalene_triangle_type(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "разносторонний")

    # --- Тесты координат и масштабирования ---
    def test_vertices_calculation_right_triangle(self):
        # Для прямоугольного треугольника 3,4,5 (гипотенуза 5, но мы берем a=3, b=4, c=5)
        # proj_x = (9 + 16 - 25)/6 = 0. proj_y = 4.
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

if __name__ == '__main__':
    unittest.main()