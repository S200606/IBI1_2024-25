#import libraries
import numpy as np
import matplotlib.pyplot as plt

def SIR_vaccination(rate):
    #create the variables
    N = 10000 #the total number of people in the population
    beta = 0.3 #infection probability upon contact beta
    gamma = 0.05 #recovery probability
    I0 = 1 #the initial number of infected people
    R0 = 0 #the initial number of recovered people
    V0 = int(rate * N)
    S0 = N - I0 - R0 - V0 #the initial number of susceptible people

    #create the arrays
    infected = [I0]
    recovered = [R0]
    susceptible = [S0]

    #begin cygling
    times = 1000
    for time in range(times):
        if I0 > 0:
            new_R0 = np.random.choice(range(2), I0, p=[1-gamma, gamma]).sum() #the number of recovered people in this round
        else:
            new_R0 = 0
        contact_possiblity = beta*I0/N #the probability of contact
        if S0 > 0:
            new_I0 = np.random.choice(range(2), S0, p=[1-contact_possiblity, contact_possiblity]).sum() #the number of infected people in this round
        else:
            new_I0 = 0
        new_R0 = min(new_R0, I0) #no larger than I0
        new_I0 = min(new_I0, S0) #no larger than S0
        I0 = max(0,I0 + new_I0 - new_R0) #the number of infected people in this round
        R0 = max(0,R0+new_R0)
        S0 = max(0, S0-new_I0)  #the number of susceptible people in this round
        #record the number and append the arrays
        infected.append(I0)
        recovered.append(R0)
        susceptible.append(S0)
    return infected

N = 10000 #the total number of people in the population
beta = 0.3 #infection probability upon contact beta
gamma = 0.05 #recovery probability
times = 1000
v_rate = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.9,1]
for rate in v_rate:
        infected = SIR_vaccination(rate)
        plt.plot(infected, label=f"{int(rate * 100)}%")

    
#draw the plot 
plt.title("SIR Model with Vaccination")
plt.legend()    
plt.xlabel("Time")
plt.ylabel("Number of People")
plt.show()
