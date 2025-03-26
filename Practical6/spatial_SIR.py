#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#make array of all susceptible population
population = np.zeros((100,100))
#randomly select one person to be infected
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
beta = 0.3 #infection probability upon contact beta
gamma = 0.05 #recovery probability
times = 100

def SIR(population, beta, gamma, times):
    for t in range(times):
        new_population = population.copy()  # Copy the current state of the population
        for i in range(100):
            for j in range(100): #locate one person
                if population[i, j] == 1:  # If the individual is infected
                    # Try to infect 8 neighbors
                    for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        i1, j1 = i + x, j + y #new infected
                        if 0 <= i1 < 100 and 0 <= j1 < 100 and population[i1, j1] == 0: #ensure they are in the population and are not infected before
                            if np.random.rand() < beta:  # randomly create a number between 0 and 1, if it is less than beta, then the person is infected
                                new_population[i1, j1] = 1  # Newly infected individuals are marked as 1
                    # Recovery occurs with probability gamma
                    if np.random.rand() < gamma:
                        new_population[i, j] = 2  # Recovered individuals are marked as 2
        population = new_population  # Update the population state

        # Plot the heatmap at specific time points
        if t in [9, 49, 99]:
            plt.figure(figsize=(6, 4), dpi=150)
            plt.title(f"Time step: {t+1}")
            plt.imshow(population, cmap='viridis', interpolation='nearest')
            plt.colorbar(label="State (0: Susceptible, 1: Infected, 2: Recovered)")
            plt.show()

# Run the simulation
SIR(population, beta, gamma, times)