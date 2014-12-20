#!/usr/bin/env python

'''

    Routine to extract data from sensor file and plot graphs between date
    and temperature for each sensor or node id. Mean value of temerature
    can also be determined for a given time period.
    
'''

import sys
import numpy as np
import scipy as sci
import matplotlib.pylab as plt
import datetime as dt
import matplotlib.dates as md

#Generates an array with names of each column ad type auto determined 
#my_data=np.genfromtxt('/Users/marcogeron/Documents/Experiment_LG04/R_0_D_1_W_1/20120319/Data.csv',delimiter=",",names=True,dtype=None)
my_data=np.genfromtxt('Data.csv',delimiter=",",names=True,dtype=None)


# Get unique sensor or node ids
sensor_names = np.unique( my_data['Node_ID'] )
print '\n Total number of unique sensors in the data file = ', len(sensor_names)


# For the unique sensor or node id, create an entry in the
# date_temp dictionary with sensor name as  the key and
# python list of (date, temperature) tuple as the value 
date_temp = {}
for sensor in sensor_names:
    date_temp_lst = []
    for i in range ( my_data.shape[0] ):
        if my_data['Node_ID'][i] == sensor:
            date_temp_lst.append( ( my_data['Timestamp'][i], float(my_data['Temperature'][i]) ) )
            
    date_temp[ sensor ] = np.array( date_temp_lst )


# Iterate through sensor name and plot graph between timestamp and
# temperature. String timestamp has to be first converted to python
# datetime before plotting.
for sensor in date_temp:
    print '\n Plotting graph for sensor ', sensor
    
    # Create two python lists; one for timestamp and another for temperature
    timestamp, temperature = [], []
    for data in date_temp[ sensor ]:
        # Split the timestamp in datetime and microsecond time
        parts = data[0].split('+')[0].split('.')
        
        # Convert the string timestamp from the input file into python 
        # datetime. Taking care to microsecond part of the time. Append
        # the timestamp to timestamp list
        temp_date = dt.datetime.strptime(parts[0], '%Y-%m-%d %H:%M:%S')
        if len(parts) > 1:
            timestamp.append( temp_date.replace(microsecond=int(parts[1])) )
        else:
            timestamp.append( temp_date )
        
        # Append temperature to temperature list    
        temperature.append( data[1] )
        
 
    # Set matplotlib parameters
    fig_size =  [8, 6]
    params = {  'backend': 'ps',
                'axes.labelsize': 11,
                'text.fontsize': 11,
                'font.size': 11,
                'font.weight': 'bold',
                'legend.fontsize': 8,
                'font.family': 'serif',
                'lines.markersize': 4,
                'axes.labelweight': 'bold',
                'xtick.labelsize': 8,
                'ytick.labelsize': 8,
                'figure.figsize': fig_size,
                'dpi': 600,
                'ps.papersize': 'auto'
          }
    plt.rcParams.update(params)
 
 
    # Plot the graph using matplotlib    
    ax=plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M')
    ax.xaxis.set_major_formatter(xfmt)
    plt.xticks(rotation=10)
    
    plt.title( 'Temperature Plot for sensor ' + sensor )
    plt.xlabel( 'Timestamp' )
    plt.ylabel( 'Temperature' )
    plt.plot( timestamp, temperature, 'g-' )
    plt.show()

        
