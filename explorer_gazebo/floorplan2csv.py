#!/usr/bin/env python3

import numpy as np
from PIL import Image
import csv

def image_to_csv(image_path, csv_path):
    # Open the image and convert to grayscale
    with Image.open(image_path) as img:
        bw = img.convert('1')  # Convert image to black and white

    # Convert image data to a numpy array
    data = np.array(bw)

    # Convert boolean to integers (True becomes 1, False becomes 0)
    data = 1 - data.astype(int)

    # Write data to CSV
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    # Specify the path to your image and the output CSV file
    image_path = 'ahsr.png'  # Update with the path to your black and white image
    csv_path = 'ahsr.csv'  # The path where the CSV will be saved
    image_to_csv(image_path, csv_path)

