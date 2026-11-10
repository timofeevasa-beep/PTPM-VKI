def calculate_delivery_cost(weight_kg, distance_km, is_express=False):
    if weight_kg < 0:  # БАГ 1: Отрицательный вес должен выдавать ошибку, а не считаться
        return 0

    base_cost = 100
    cost_per_km = 5
    cost_per_kg = 10

    # Скидка 20% при доставке дальше 100 км
    discount = 0
    if distance_km > 100:
        discount = 0.20

    total = base_cost + (distance_km * cost_per_km) + (weight_kg * cost_per_kg)

    # БАГ 2: Ошибка в применении скидки (вычитаем 20, а не умножаем на 0.8)
    if discount > 0:
        total = total - 20

    if is_express:
        total = total * 1.5

    return total