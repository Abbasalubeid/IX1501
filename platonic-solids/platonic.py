import numpy as np
import random as rnd
import matplotlib.pyplot as plt

# Task 1

# Each die is represented as a probability distribution over its faces.
tetrahedron = np.array([1/4]*4)
cube = np.array([1/6]*6)
octahedron = np.array([1/8]*8)
dodecahedron = np.array([1/12]*12)
icosahedron = np.array([1/20]*20)

# Convolve the distributions sequentially
result_distribution = np.convolve(tetrahedron, cube)
result_distribution = np.convolve(result_distribution, octahedron)
result_distribution = np.convolve(result_distribution, dodecahedron)
result_distribution = np.convolve(result_distribution, icosahedron)

# Create table data
columns = ["Sum (S)", "Probability P(S = s)"]
rows = list(range(5, 51))
data = [[s, "{:.1e}".format(result_distribution[s-5])] for s in rows] 

# Create table
fig, ax = plt.subplots(figsize=(6, 8))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=columns, cellLoc='center', loc='center')

table.auto_set_column_width(col=list(range(len(columns))))

fig.tight_layout()
plt.savefig('task1_probability_functon.png', dpi=300)

# Plotting the bar chart for the probability distribution
plt.figure(figsize=(15, 7))
bars = plt.bar(rows, result_distribution, color='red', edgecolor='black')
plt.xlabel('Sum (S)')
plt.ylabel('Probability P(S = s)')
plt.title('Probability distribution of sum (S) for five Platonic solid dices')
plt.xticks(rows)
plt.tight_layout()
plt.grid(axis='y')

# Labeling bars with very small probabilities
for bar in bars:
    height = bar.get_height()
    if height < 0.001:  
        plt.text(bar.get_x() + bar.get_width() / 2., height,
                 '{:.1e}'.format(height), 
                 ha='center', va='bottom', rotation=90, fontsize=8)


plt.savefig('task1_probability_distribution.png', dpi=300)


# Task 2

# Extract the probabilities corresponding to the winning conditions
# result_distribution[0] =  the probability of S = 5
# result_distribution[46] = the probability of S = 50
winning_prob_lower = sum(result_distribution[0:6])   # Indices for sums 5-10 
winning_prob_upper = sum(result_distribution[40:46]) # Indices for sums 45-50

# Sum the two probabilities to get the total probability of winning
total_winning_prob = winning_prob_lower + winning_prob_upper

print(f"The probability of winning the game is: {total_winning_prob:.6f}")

# Task 3

def dice_simulation(trials, dice_faces):
    # Simulate the dice game for a given number of trials and return the winning probability
    winning_games = 0
    for _ in range(trials):
        total_sum = sum(rnd.randint(1, faces) for faces in dice_faces)
        
        if total_sum <= 10 or total_sum >= 45:
            winning_games += 1

    return winning_games / trials

# Number of faces for each dice (Platonic solids)
dice_faces = [4, 6, 8, 12, 20]

n_trials_task3 = 1000
winning_prob_simulation_task3 = dice_simulation(n_trials_task3, dice_faces)

print(f"Probability of winning the game based on {n_trials_task3} trials (Monte Carlo): {winning_prob_simulation_task3:.4f}")

# Task 4

# Define the exact probability from Task 2
exact_probability = total_winning_prob

# Define a range of trial numbers from small to large
trial_numbers = [10, 100, 1000, 10000, 100000, 1000000]

# Calculate simulated probabilities for each trial number
simulated_probabilities = [dice_simulation(trials, dice_faces) for trials in trial_numbers]

# Plotting the results
plt.figure(figsize=(10, 7))
plt.plot(trial_numbers, simulated_probabilities, marker='o', linestyle='-', color='b', label='Simulated probability')
plt.axhline(exact_probability, color='r', linestyle='--', label='Exact probability')

plt.xscale('log')
plt.xlabel('Number of trials (Log scale)')
plt.ylabel('Probability')
plt.title('Change in Probability with varying numbers of trials')
plt.legend()
plt.grid(True)

plt.savefig('task4.png', dpi=300)

# Task 5

# The desired relative error threshold (10%)
relative_error_threshold = 0.10

trials = 10

relative_error = 1.0 

while True:
    simulated_prob = dice_simulation(trials, dice_faces)
    
    # Calculate the relative error
    relative_error = abs((simulated_prob - exact_probability) / exact_probability)

    print(f"Trials: {trials}, Simulated probability: {simulated_prob:.4f}, Relative Error: {relative_error:.4f}")

    # Check if the relative error is within the desired threshold
    if relative_error <= relative_error_threshold:
        break

    # Double the number of trials for the next iteration
    trials *= 2

print(f"Number of trials needed to achieve <10% relative error: {trials}")