import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

def plot_truck_schedule(schedule, filename=None):
    """
    Visualizes the truck schedule over a week with two subplots for morning and evening shifts,
    displaying the number of trucks in each cell centered and adding color to indicate quantities.
    
    Parameters:
    - schedule: 3D numpy array with shape (12, 7, 2) where schedule[i][j][k] represents
                the number of trucks sent to district i on day j in shift k (0 for morning, 1 for evening).
    - filename: Optional; if provided, the plot will be saved to this file.
    """
    days, districts = schedule.shape[1], schedule.shape[0]
    day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Extract morning and evening schedules
    morning_schedule = schedule[:, :, 0].T  # Transpose for 7x12 display
    evening_schedule = schedule[:, :, 1].T  # Transpose for 7x12 display

    # Set up the figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(20, 8), sharey=True)
    fig.suptitle("Trash Truck Schedule: Morning and Evening Shifts", fontsize=20)

    # Morning shift schedule with color
    im1 = axs[0].imshow(morning_schedule, cmap='Blues', aspect='auto', vmin=0, vmax=np.max(schedule))
    axs[0].set_title("Morning Shift", fontsize=15)
    axs[0].set_xlabel("Districts", fontsize=15)
    axs[0].set_ylabel("Days", fontsize=15)
    axs[0].set_xticks(range(districts))
    axs[0].set_xticklabels([f'{i+1}' for i in range(districts)])
    axs[0].set_yticks(range(days))
    axs[0].set_yticklabels(day_names, fontsize=12)  # Set day names as y-tick labels

    # Add integer labels to morning shift cells
    for i in range(days):
        for j in range(districts):
            axs[0].text(j, i, f"{int(morning_schedule[i, j])}", ha='center', va='center', color='black', fontsize=15)

    # Evening shift schedule with color
    im2 = axs[1].imshow(evening_schedule, cmap='Oranges', aspect='auto', vmin=0, vmax=np.max(schedule))
    axs[1].set_title("Evening Shift", fontsize=15)
    axs[1].set_xlabel("Districts", fontsize=15)
    axs[1].set_xticks(range(districts))
    axs[1].set_xticklabels([f'{i+1}' for i in range(districts)])
    axs[1].set_yticks(range(days))
    axs[1].set_yticklabels(day_names, fontsize=12)  # Set day names as y-tick labels

    # Add integer labels to evening shift cells
    for i in range(days):
        for j in range(districts):
            axs[1].text(j, i, f"{int(evening_schedule[i, j])}", ha='center', va='center', color='black', fontsize=15)

    # Save the plot if a filename is provided
    if filename:
        plt.savefig(filename)

    plt.tight_layout(rect=[0, 0, 1, 0.98])
    plt.show()

# Process each .pkl file in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.pkl'):
        # Load the .pkl file
        with open(filename, 'rb') as pkl_file:
            schedule = pickle.load(pkl_file)

        # Check if the array has the correct shape (12, 7, 2)
        if schedule.shape != (12, 7, 2):
            print(f"Skipping {filename}: Incorrect shape {schedule.shape}")
            continue  # Skip this file if shape does not match

        # Set the output filename to the same name as the .pkl file but with a .png extension
        output_filename = filename.replace('.pkl', '.png')

        # Plot the truck schedule and save it
        plot_truck_schedule(schedule, filename=output_filename)
        
        print(f"Processed and saved {output_filename}")