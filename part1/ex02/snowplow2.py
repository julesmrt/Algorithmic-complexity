import numpy as np

def parcours(houses):
    # Tri des maisons par leur distance à 0 (position initiale de la déneigeuse)
    optimal_order = sorted(houses, key=lambda x: abs(x))
    return optimal_order

def compute_waiting_times(order):
    waiting_times = []
    current_position = 0
    current_time = 0
    for house in order:
        travel_time = abs(house - current_position)
        current_time += travel_time
        waiting_times.append(current_time)
        current_position = house
    return np.mean(waiting_times)

def main():
    # Test avec des données générées (1000 maisons)
    houses = np.random.normal(0, 1000, 1000).tolist() #change the third value to chnage the size of the list
    cleaning_order = parcours(houses)

    print("Cleaning order for 20 random houses:", cleaning_order)

    # Calcul du temps d'attente moyen pour la méthode parcours
    parcours_waiting_time = compute_waiting_times(cleaning_order)

    # Implémentation de l'ordre greedy pour comparaison
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

    greedy_order_result = greedy_order(houses)
    greedy_waiting_time = compute_waiting_times(greedy_order_result)

    print("Greedy order:", greedy_order_result)
    print("Parcours waiting time:", parcours_waiting_time)
    print("Greedy waiting time:", greedy_waiting_time)

if __name__ == "__main__":
    main()
