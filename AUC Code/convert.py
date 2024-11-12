import os
import re
import numpy as np
import pickle

# Regular expression to parse the lines in the .txt files, ignoring everything after "Day x"
pattern = r"District (\d+), Truck (\d+), (Morning|Evening), Day (\d+)"

def process_txt_file(filepath):
    # Initialize a (12, 7, 2) array filled with zeros
    convert = np.zeros((12, 7, 2), dtype=int)
    
    # Open and read the .txt file
    with open(filepath, 'r') as file:
        for line in file:
            # Use regular expression to extract details
            match = re.match(pattern, line.strip())
            if match:
                district = int(match.group(1))  # District is already zero-indexed (0-11)
                truck = int(match.group(2))     # We don’t use truck directly in this task
                period = match.group(3)         # "Morning" or "Evening"
                day = int(match.group(4)) - 1   # Convert Day to zero-based index
                
                # Determine the index for Morning/Evening
                time_index = 0 if period == "Morning" else 1
                
                # Increment the count in the convert array
                convert[district, day, time_index] += 1
    
    return convert

# Process each .txt file in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        # Get the file path
        filepath = os.path.join('.', filename)
        
        # Process the .txt file to get the (12, 7, 2) array
        convert = process_txt_file(filepath)
        
        # Define the output .pkl file name (same as .txt but with .pkl extension)
        pkl_filename = filename.replace('.txt', '.pkl')
        
        # Save the array as a .pkl file
        with open(pkl_filename, 'wb') as pkl_file:
            pickle.dump(convert, pkl_file)
        
        print(f"Processed and saved {pkl_filename}")

