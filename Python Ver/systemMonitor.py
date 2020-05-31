# -*- coding: utf-8 -*-
"""
Created on Sun May 31 05:48:39 2020

@author: Lan Bui
"""

import csv

#open csv file and go through data 
file_CSV = open('epaPM2016.csv')
data_CSV = csv.reader(file_CSV)

#skip header in csv file
next(data_CSV)

#put csv elements into a list to simplify analysis
list_CSV = list(data_CSV)
 
count = 0
for row in list_CSV:
    #reading from csv is str so convert to float for if else statements
    rawConc = float(row[5])
    
    #print concentration value and respective power setting
    if rawConc > 18.0:
       print (str(rawConc) + " = 100%")
    elif 14.0 < rawConc <= 18.0:
       print (str(rawConc) + " = 75%")
    elif 10.0 < rawConc <= 14.0:
       print (str(rawConc) + " = 50%")
    elif 4.0 < rawConc <= 10.0:
       print (str(rawConc) + " = 25%")
    else:
       print (str(rawConc) + " = 0%")
    
    #counter to stop getting values after a certain date
    count += 1
    if count == 121:
        break