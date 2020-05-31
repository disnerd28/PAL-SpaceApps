# -*- coding: utf-8 -*-
"""
Created on Sun May 31 05:48:39 2020

@author: Lan Bui
"""

import csv

#open csv file and go through data 
file_CSV = open('csaNO2.csv')
data_CSV = csv.reader(file_CSV)

#skip header in csv file
#next(data_CSV)

#put csv elements into a list to simplify analysis
list_CSV = list(data_CSV)
 
count = 0
for row in list_CSV:
    #reading from csv is str so convert to float for if else statements
    no2Conc = float(row[0])
    
    #print concentration value and respective power setting
    if no2Conc == -999.0: #no reading
       print (str(no2Conc) + " = A reading was not performed")
    elif no2Conc == -888.0: #reading error
       print (str(no2Conc) + " = There is an error in data collection")
    elif 3.61e-09 < no2Conc:
       print (str(no2Conc) + " = 100%")
    elif 4.10e-10 < no2Conc <= 3.61e-09:
       print (str(no2Conc) + " = 75%")
    elif 1.76e-11 < no2Conc <= 4.10e-10:
       print (str(no2Conc) + " = 50%")
    elif 1.2e-12 < no2Conc <= 1.76e-11:
       print (str(no2Conc) + " = 25%")
    else:
       print (str(no2Conc) + " = 0%")