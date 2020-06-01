# -*- coding: utf-8 -*-
"""
Created on Sun May 31 05:48:39 2020

@author: Lan Bui
"""

import csv

#open csv file and go through data 
file_CSV = open('csaNO2.csv')
data_CSV = csv.reader(file_CSV)

#put csv elements into a list to simplify analysis
list_CSV = list(data_CSV)
 
for row in list_CSV:
    #reading from csv is str so convert to float for if else statements
    no2Conc = float(row[0])
    
    #print concentration value and respective power setting
    if no2Conc == -999.0: #no reading, based on comments from the CSA txt file
       print(str(no2Conc) + " = A reading was not performed")
    elif no2Conc == -888.0: #reading error, based on comments from the CSA txt file
       print(str(no2Conc) + " = There is an error in data collection")
    elif 3.61e-09 < no2Conc:
       print(str(no2Conc) + " = Please keep the air purfier on at full capacity. The air outdoors has very high levels of NO2.")
       print("   It is recommended that everyone be wary of the time spent outdoors as long exposure may be harmful.\n")
    elif 4.10e-10 < no2Conc <= 3.61e-09:
       print(str(no2Conc) + " = Please set the air purifier at 75% capacity. The air outdoors has some high levels of NO2.")
       print("   It is recommended that patients with underlying health conditions should not leave their room if possible.\n")
    elif 1.76e-11 < no2Conc <= 4.10e-10:
       print(str(no2Conc) + " = Please set the air purifier at 50% capacity. The air outdoors has some moderate levels of NO2.")
       print("   It is recommended that patients with underlying health conditions should not go outside if possible.\n")
    elif 1.2e-12 < no2Conc <= 1.76e-11:
       print(str(no2Conc) + " = Please set the air purifier at 25% capacity. The air outdoors has some low concentrations of NO2.")
       print("   Going outside would not be harmful, but may be uncomfortable to breathe if you are sensitive.\n")    
    else:
       print(str(no2Conc) + " = You can keep the purifier off. The air outdoors seems pretty great today!\n")