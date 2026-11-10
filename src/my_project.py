# src/my_project.py
import math


def validate_triangle(a, b, c):
    """существует ли треугольник с такими сторонами"""
    sides = [a, b, c]
    if min(sides) <= 0 or max(sides) >= sum(sides) - max(sides):
        return False
    return True


def get_triangle_type(a, b, c):
    """Возвращает тип треугольника."""
    unique_sides = len(set([a, b, c]))
    if unique_sides == 1:
        return "равносторонний"
    elif unique_sides == 2:
        return "равнобедренный"
    return "разносторонний"


def calculate_vertices(a, b, c):
    """рассчет координаты вершин треугольника"""
    proj_x = (a ** 2 + b ** 2 - c ** 2) / (2 * a)
    # Защита от отрицательного подкоренного выражения из-за float погрешностей
    val = b ** 2 - proj_x ** 2
    proj_y = math.sqrt(val) if val > 0 else 0.0

    return [(0.0, 0.0), (a, 0.0), (proj_x, proj_y)]


def scale_and_center_points(points):
    """масш и центрирует точки в холсте 100x100"""
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    width = max_x - min_x
    height = max_y - min_y

    if width == 0 and height == 0:
        return [(50, 50), (50, 50), (50, 50)]

    scale = 80.0 / max(width, height)
    offset_x = (100.0 - width * scale) / 2.0
    offset_y = (100.0 - height * scale) / 2.0

    return [
        (
            int((x - min_x) * scale + offset_x),
            int((y - min_y) * scale + offset_y)
        )
        for x, y in points
    ]