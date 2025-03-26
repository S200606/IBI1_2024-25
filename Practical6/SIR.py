#import libraries
import numpy as np
import matplotlib.pyplot as plt

#create the variables
N = 10000 #the total number of people in the population
beta = 0.3 #infection probability upon contact beta
gamma = 0.05 #recovery probability
I0 = 1 #the initial number of infected people
R0 = 0 #the initial number of recovered people
S0 = N - I0 - R0 #the initial number of susceptible people

#create the arrays
infected = [I0]
recovered = [R0]
susceptible = [S0]

#begin cygling
times = 1000
for time in range(times):
    new_R0 = np.random.choice(range(2), I0, p=[1-gamma, gamma]).sum() #the number of recovered people in this round
    contact_possiblity = beta*I0/N #the probability of contact
    new_I0 = np.random.choice(range(2), S0, p=[1-contact_possiblity, contact_possiblity]).sum() #the number of infected people in this round
    new_R0 = min(new_R0, I0) #no larger than I0
    new_I0 = min(new_I0, S0) #no larger than S0
    I0 = I0 + new_I0 - new_R0
    R0 += new_R0
    S0 -= new_I0  #the number of susceptible people in this round
    #record the number and append the arrays
    infected.append(I0)
    recovered.append(R0)
    susceptible.append(S0)

#draw the plot
plt.figure(figsize=(10, 6),dpi=80)  
plt.plot(infected, label="Infected", color="red")  
plt.plot(recovered, label="Recovered", color="green")  
plt.plot(susceptible, label="Susceptible", color="blue")  
plt.title("SIR Model Simulation")
plt.xlabel("Time")
plt.ylabel("Number of People")
plt.show()

#save the image
plt.figure(figsize=(6, 4),dpi=150)
plt.savefig("SIR.png", format="png")
