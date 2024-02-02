import numpy as np

def simulated_annealing(objective_function, initial_solution, temperature, cooling_rate, iterations):
    current_solution = initial_solution
    current_energy = objective_function(current_solution)

    best_solution = current_solution
    best_energy = current_energy

    for iteration in range(iterations):
        # Generate a neighboring solution
        neighbor_solution = current_solution + np.random.normal(0, 1, size=len(current_solution))

        # Calculate energy for the neighbor
        neighbor_energy = objective_function(neighbor_solution)

        # Decide whether to accept the neighbor as the current solution
        if neighbor_energy < current_energy or np.random.rand() < np.exp((current_energy - neighbor_energy) / temperature):
            current_solution = neighbor_solution
            current_energy = neighbor_energy

        # Update the best solution if needed
        if current_energy < best_energy:
            best_solution = current_solution
            best_energy = current_energy

        # Cool the temperature
        temperature *= cooling_rate

    return best_solution, best_energy

# Example usage:
def quadratic_function(x):
    return np.sum(x**2)

initial_solution = np.array([1.0, 2.0, -3.0])
initial_temperature = 100.0
cooling_rate = 0.95
num_iterations = 1000

result_solution, result_energy = simulated_annealing(quadratic_function, initial_solution, initial_temperature, cooling_rate, num_iterations)

print("Best Solution:", result_solution)
print("Best Energy:", result_energy)
