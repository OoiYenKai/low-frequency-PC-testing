#!/usr/bin/env python3
import psutil
import os
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

duration_hours = 1
iterations = duration_hours * 3600

def get_cpu_temp():
    """
    Obtains the current value of the CPU temperature.
    :returns: Current value of the CPU temperature if successful, zero value otherwise.
    :rtype: float
    """
    result = 0.0
    # The first line in this file holds the CPU temperature as an integer times 1000.
    # Read the first line and remove the newline character at the end of the string.
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
        if line.isdigit():
            result = float(line) / 1000
    return result

def main():
    with open('cpu_log.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Timestamp', 'CPU Frequency', 'CPU Temperature'])

        for _ in range(iterations):
            cpu_temp = get_cpu_temp()
            cpu_freq = psutil.cpu_freq()[0]
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')  # Timestamp for current time

            # Write the data to the CSV file
            csvwriter.writerow([timestamp, cpu_freq, cpu_temp])
            
            # Print the values if needed
            print(timestamp, cpu_freq, cpu_temp)
            
            time.sleep(1)

    print("Data logging complete.")

    # Read data from the CSV file into a DataFrame
    data = pd.read_csv('cpu_log.csv')

    # Convert the 'Timestamp' column to datetime format
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Plot CPU Frequency over time
    plt.figure(figsize=(10, 6))
    plt.plot(data['Timestamp'], data['CPU Frequency'], color='blue', marker='o', linestyle='-')
    plt.title('CPU Frequency over Time')
    plt.xlabel('Time')
    plt.ylabel('CPU Frequency (MHz)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('cpu_frequency_plot.png')  # Save the plot as an image file
    plt.show()

    # Plot CPU Temperature over time
    plt.figure(figsize=(10, 6))
    plt.plot(data['Timestamp'], data['CPU Temperature'], color='red', marker='o', linestyle='-')
    plt.title('CPU Temperature over Time')
    plt.xlabel('Time')
    plt.ylabel('CPU Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('cpu_temperature_plot.png')  # Save the plot as an image file
    plt.show()

    # Plot CPU frequency over CPU temperature
    plt.figure(figsize=(10, 6))
    plt.plot(data['CPU Temperature'], data['CPU Frequency'], color='yellow', marker='o', linestyle='-')
    plt.title('CPU frequency over CPU temperature')
    plt.xlabel('CPU Temperature (°C)')
    plt.ylabel('CPU Frequency (MHz)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('cpu_frequency_over_cpu_temperature.png')  # Save the plot as an image file
    plt.show()

if __name__ == "__main__":
    main()