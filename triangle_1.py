import math

while True:
    print("\nНовая проверка")

    try:
        edge1 = float(input("a: "))
        edge2 = float(input("b: "))
        edge3 = float(input("c: "))
    except ValueError:
        print("")
        print([(-2, -2)] * 3)
        continue

    sides = [edge1, edge2, edge3]

    if min(sides) <= 0 or max(sides) >= sum(sides) - max(sides):
        print("не треугольник")
        print([(-1, -1)] * 3)
        continue

    # тип
    unique_sides = len(set(sides))
    if unique_sides == 1:
        print("равносторонний")
    elif unique_sides == 2:
        print("равнобедренный")
    else:
        print("разносторонний")

    # коорды 3 верш
    proj_x = (edge1 ** 2 + edge2 ** 2 - edge3 ** 2) / (2 * edge1)
    proj_y = math.sqrt(edge2 ** 2 - proj_x ** 2)

    x_coords = [0.0, edge1, proj_x]
    y_coords = [0.0, 0.0, proj_y]

    # границы масш
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    width = max_x - min_x
    height = max_y - min_y

    # расчитыв масштаб
    scale = 80.0 / max(width, height)
    offset_x = (100.0 - width * scale) / 2.0
    offset_y = (100.0 - height * scale) / 2.0

    result_points = [
        (
            int((x - min_x) * scale + offset_x),
            int((y - min_y) * scale + offset_y)
        )
        for x, y in zip(x_coords, y_coords)
    ]

    print(result_points)