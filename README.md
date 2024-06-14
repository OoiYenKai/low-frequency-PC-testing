# Low frequency PC testing
### About:
- __log_CPU.py__: to log CPU temperature and frequency over 1 hour, plot the data onto 3 different graphs; __CPU temperature over time__, __CPU frequency over time__ and __CPU frequency over temperature__.
- __CPU_min_max_mean.py__: To calculate the data logged in the CSV files and print out the __minimum__, __maximum__ and __mean__ values of the data.
### Instructions:
Before running the scripts there are a few steps that you have do:
1. ``sudo apt-get install stress``
2. ``pip3 install psutils``
3. ``pip3 install pandas``
4. ``pip3 install matplotlib``
5. command to stress CPU at 100%: ``stress --cpu `nproc` --vm `nproc` --vm-bytes 1GB --io `nproc` --hdd `nproc` --hdd-bytes 1GB --timeout 3600s``
