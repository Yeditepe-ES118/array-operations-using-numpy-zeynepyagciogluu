# assignment2.py

import numpy as np

def stat():
    # Load the populations.txt file
    data = np.loadtxt("populations.txt")
    
    # Extract the Hare column (2nd column)
    hare = data[:, 1]
    
    # Find the year when the Hare population is at its minimum
    min_year_hare = data[np.argmin(hare), 0]
    
    # Compute the average Lynx population over the years (3rd column)
    lynx_avg = np.mean(data[:, 2])
    
    # Compute the sum of all species for each year
    species_sum = np.sum(data[:, 1:], axis=1)
    
    # Create a new array by adding the sum as the last column
    new_data = np.column_stack((data, species_sum))
    
    # Set Carrot population values below 40000 to 0
    # Carrot column index is 3
    new_data[new_data[:, 3] < 40000, 3] = 0
    
    return data, hare, min_year_hare, lynx_avg, new_data
