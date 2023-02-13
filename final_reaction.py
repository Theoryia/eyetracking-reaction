#%%            
import pyautogui
import time
import keyboard
import csv

# Define the size of the box in pixels
box_size = 200

# Read the coordinate data from the CSV file
with open("coordinates.csv", "r") as file:
    reader = csv.reader(file)
    coordinates = list(reader)

# Display the prompt
print("Ready...")
time.sleep(2)
print("Go!")

# Record the starting time
start_time = time.time()

# Check if the mouse is inside the box
mouse_reached = False
mouse_reach_time = None
while not mouse_reached:
    mouse_x, mouse_y = pyautogui.position()
    for coord in coordinates:
        x1, y1, x2, y2 = map(int, coord)
        if (x1 < mouse_x < x2) and (y1 < mouse_y < y2):
            mouse_reach_time = time.time()
            mouse_reached = True
            break
    time.sleep(0.1)

if mouse_reach_time is None:
    print("Mouse did not reach any of the boxes.")
else:
    # Calculate the reaction time to reach the center
    reaction_time_to_reach = mouse_reach_time - start_time

# Wait for the space bar to be pressed
space_bar_pressed = False
while not space_bar_pressed:
    if keyboard.is_pressed('b'):
        space_bar_pressed = True
        end_time = time.time()

# Calculate the time to press the space bar
time_to_press_space = end_time - mouse_reach_time

# Calculate the total time
total_time = end_time - start_time

# Write the results to a CSV file
with open('results.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([format(reaction_time_to_reach, '.4f'), format(time_to_press_space, '.4f'), format(total_time, '.4f')])

# Display the results
print("Reaction time to reach the area: {:.2f} seconds".format(reaction_time_to_reach))
print("Time to press the space bar: {:.2f} seconds".format(time_to_press_space))
print("Total time: {:.2f} seconds".format(total_time))