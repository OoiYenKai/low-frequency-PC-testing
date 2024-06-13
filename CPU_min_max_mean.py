#!/usr/bin/env python3
import pandas as pd

def main():
    # Read data from the CSV file into a DataFrame
    data_ok = pd.read_csv('cpu_log_ok.csv')

    # Calculate statistics for CPU Frequency
    cpu_freq_mean_ok = data_ok['CPU Frequency'].mean()
    cpu_freq_max_ok = data_ok['CPU Frequency'].max()
    cpu_freq_min_ok = data_ok['CPU Frequency'].min()

    # Calculate statistics for CPU Temperature
    cpu_temp_mean_ok = data_ok['CPU Temperature'].mean()
    cpu_temp_max_ok = data_ok['CPU Temperature'].max()
    cpu_temp_min_ok = data_ok['CPU Temperature'].min()

    # Read data from the CSV file into a DataFrame
    data_faulty = pd.read_csv('cpu_log.csv')

    # Calculate statistics for CPU Frequency
    cpu_freq_mean_faulty = data_faulty['CPU Frequency'].mean()
    cpu_freq_max_faulty = data_faulty['CPU Frequency'].max()
    cpu_freq_min_faulty = data_faulty['CPU Frequency'].min()

    # Calculate statistics for CPU Temperature
    cpu_temp_mean_faulty = data_faulty['CPU Temperature'].mean()
    cpu_temp_max_faulty = data_faulty['CPU Temperature'].max()
    cpu_temp_min_faulty = data_faulty['CPU Temperature'].min()

    # Print the results
    print("Normal PC CPU Frequency (MHz):")
    print(f"Mean: {cpu_freq_mean_ok:.2f}")
    print(f"Max: {cpu_freq_max_ok:.2f}")
    print(f"Min: {cpu_freq_min_ok:.2f}")
    print()
    
    print("Normal PC CPU Temperature (°C):")
    print(f"Mean: {cpu_temp_mean_ok:.2f}")
    print(f"Max: {cpu_temp_max_ok:.2f}")
    print(f"Min: {cpu_temp_min_ok:.2f}")
    print()

    # Print the results
    print("Faulty PC CPU Frequency (MHz):")
    print(f"Mean: {cpu_freq_mean_faulty:.2f}")
    print(f"Max: {cpu_freq_max_faulty:.2f}")
    print(f"Min: {cpu_freq_min_faulty:.2f}")
    print()
    
    print("Faulty PC CPU Temperature (°C):")
    print(f"Mean: {cpu_temp_mean_faulty:.2f}")
    print(f"Max: {cpu_temp_max_faulty:.2f}")
    print(f"Min: {cpu_temp_min_faulty:.2f}")

if __name__ == "__main__":
    main()