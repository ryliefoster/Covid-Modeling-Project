import pickle
import pandas as pd
import numpy as np
import csv

day = np.array([0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 19])

number = np.array([0, 10, 20, 61, 64, 70, 135, 174, 218, 285, 355, 454, 542, 621, 634, 691])

data = [
    ['day', 'count'],
    [0, 0],
    [1, 10],
    [2, 20],
    [3, 61],
    [4, 64],
    [5, 70],
    [6, 135],
    #[7, np.inf],
    [8, 174],
    [9, 218],
    #[10, np.inf],
    [11, 285],
    [12, 355],
    [13, 454],
    [14, 542],
    [15, 621],
    [16, 634],
    #[17, np.inf],
    #[18, np.inf],
    [19, 691]
]


filename = 'diamondprincess.csv'

with open(filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(data[0])
    csv_writer.writerows(data[1:])

print(f'data successfully written to {filename}')



