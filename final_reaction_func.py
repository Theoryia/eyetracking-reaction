#%%
import pyautogui
import time
import keyboard
import csv
import random

def get_mouse_reach_time(coordinates, box_size):
    """Returns the time when the mouse reaches one of the boxes defined by the coordinates"""
    while True:
        mouse_x, mouse_y = pyautogui.position()
        for coord in coordinates:
            if (coord[0] - box_size/2 < mouse_x < coord[0] + box_size/2) and (coord[1] - box_size/2 < mouse_y < coord[1] + box_size/2):
                return time.time()
        time.sleep(0.1)

def get_space_bar_press_time():
    """Returns the time when the space bar is pressed"""
    while True:
        if keyboard.is_pressed('b'):
            return time.time()

def run_test(coordinates, box_size, start_time):
    """Runs a single test and returnbbs the reaction time to reach the box, time to press the b key, and total time"""
    mouse_reach_time = get_mouse_reach_time(coordinates, box_size)
    space_bar_press_time = get_space_bar_press_time()
    reaction_time_to_reach = mouse_reach_time - start_time
    time_to_press_space = space_bar_press_time - mouse_reach_time
    total_time = space_bar_press_time - start_time
    return reaction_time_to_reach, time_to_press_space, total_time

def main():
    candidate_no = input("Input the users candidate number: ")
    csvfile = f"results_test{candidate_no}.csv"
    # Define the size of the box in pixels
    box_size = 200
    
    # Read the coordinate data from the CSV file
    with open("coordinates.csv", "r") as file:
        reader = csv.reader(file)
        coordinates = [list(map(int, coord)) for coord in reader]

    # Display the prompt
    input()

    # Run the tests
    results = []
    for i, coord in enumerate(coordinates):
        # Record the starting time for the current test
        print("Test Starting")
        print("-------------")
        print("Please ensure the test is open")
        time.sleep(5)
        print("Ready")
        time.sleep(random.uniform(4, 6))
        print("Go!")
        pyautogui.press('right')
        start_time = time.time()
        print("Test {}/{}".format(i + 1, len(coordinates)))
        reaction_time_to_reach, time_to_press_space, total_time = run_test([coord], box_size, start_time)
        results.append([reaction_time_to_reach, time_to_press_space, total_time])

        # Prompt the user to continue to the next test
        if i < len(coordinates) - 1:
            print("Press 'Enter' to continue to the next test. Please return to the test immediately")
            input()
            time.sleep(2)
            pyautogui.press('right')
            

    # Show results
    print("\nResults:")
    for i, result in enumerate(results):
        print("Test {} - Reaction time to reach box: {:.4f} seconds - Time to press space bar: {:.4f} seconds - Total time: {:.2f} seconds".format(i + 1, result[0], result[1], result[2]))
        input()
    # Write the results to a CSV file
    with open(csvfile, 'a', newline='') as file:
        fieldnames = ['Test Number', 'Reaction Time to Reach Box', 'Time to Press Space Bar', 'Total Time']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i, result in enumerate(results):
            writer.writerow({'Test Number': i + 1, 'Reaction Time to Reach Box': format(result[0], '.4f'), 'Time to Press Space Bar': format(result[1], '.4f'), 'Total Time': format(result[2], '.2f')})

    # for i, result in enumerate(results):
    #     print("Test {} results:".format(i + 1))
    #     print("Reaction time to reach box: {:.4f} seconds".format(result[0]))
    #     print("Time to press space bar: {:.4f} seconds".format(result[1]))
    #     print("Total time: {:.2f} seconds".format(result[2]))
        
        
main()