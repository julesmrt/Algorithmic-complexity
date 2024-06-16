import numpy as np

# Configuration des maisons où le simple tri ou la méthode gourmande ne sont pas optimaux vous pouvez changer l'ordre si vous le
houses = [-10.0, -5.0, 10.0, 8.0, 2.0, -2.0]

def compute_waiting_times(order, houses):
    waiting_times = []
    current_position = 0
    current_time = 0
    for house in order:
        travel_time = abs(house - current_position)
        current_time += travel_time
        waiting_times.append(current_time)
        current_position = house
    return np.mean(waiting_times)

# Tri des maisons par position
sorted_order = sorted(houses)
sorted_waiting_time = compute_waiting_times(sorted_order, houses)

# Méthode gourmande (aller à la maison la plus proche à chaque étape)
def greedy_order(houses):
    remaining_houses = houses[:]
    current_position = 0
    order = []
    while remaining_houses:
        next_house = min(remaining_houses, key=lambda x: abs(x - current_position))
        order.append(next_house)
        current_position = next_house
        remaining_houses.remove(next_house)
    return order

def main():
    # Ordre trié
    sorted_order = sorted(houses)
    sorted_waiting_time = compute_waiting_times(sorted_order, houses)

    # Ordre gourmande
    greedy_order_result = greedy_order(houses)
    greedy_waiting_time = compute_waiting_times(greedy_order_result, houses)

    print("Sorted order:", sorted_order)
    print("Greedy order:", greedy_order_result)
    print("Sorted waiting time:", sorted_waiting_time)
    print("Greedy waiting time:", greedy_waiting_time)

if __name__ == "__main__":
    main()
