import time
import numpy as np
import matplotlib.pyplot as plt

def function_1(n):
    total = 0
    for i in range(n):
        for j in range(i):
            for k in range(j):
                total += 1
    return total

def function_2(n):
    total = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                for k in range(j - i):
                    total += 1
    return total

def measure_execution_time(func, n):
    start_time = time.time()
    func(n)
    return time.time() - start_time

def plot_complexity(func, max_n):
    n_values = list(range(1, max_n + 1))
    times = []
    for n in n_values:
        times.append(measure_execution_time(func, n))

    # Fit a polynomial of degree 3 to the measured times
    coeffs = np.polyfit(n_values, times, 3)
    fitted_polynomial = np.poly1d(coeffs)

    # Plotting
    plt.figure()
    plt.scatter(n_values, times, label='Measured Time')
    plt.plot(n_values, fitted_polynomial(n_values), color='red', label='Fitted Polynomial')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title(f'Execution Time and Fitted Polynomial for {func.__name__}')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    max_n = 20

    print("Testing function_1:")
    plot_complexity(function_1, max_n)

    print("\nTesting function_2:")
    plot_complexity(function_2, max_n)

if __name__ == "__main__":
    main()
