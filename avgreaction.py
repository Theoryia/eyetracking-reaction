#%%
import csv

with open('results_test78.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

num_rows = len(data)

# Get the sum of each column
reaction_time_sum = 0
time_to_press_space_sum = 0
total_time_sum = 0
for row in data:
    reaction_time_sum += float(row[0])
    time_to_press_space_sum += float(row[1])
    total_time_sum += float(row[2])

# Calculate the average of each column
reaction_time_avg = reaction_time_sum / num_rows
time_to_press_space_avg = time_to_press_space_sum / num_rows
total_time_avg = total_time_sum / num_rows

# Round the averages to 2 decimal places
reaction_time_avg = round(reaction_time_avg, 2)
time_to_press_space_avg = round(time_to_press_space_avg, 2)
total_time_avg = round(total_time_avg, 2)

# Print the averages
print("Average reaction time to reach the center: {} seconds".format(reaction_time_avg))
print("Average time to press the space bar: {} seconds".format(time_to_press_space_avg))
print("Average total time: {} seconds".format(total_time_avg))