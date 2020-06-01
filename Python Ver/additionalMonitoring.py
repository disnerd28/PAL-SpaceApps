# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:26:14 2020

@author: Lan Bui
"""

import csv

#open csv file and go through data 
file_epaNO2 = open('epaNO2.csv')
file_epaPM2_5 = open('epaPM2_5.csv')
data_epaNO2 = csv.reader(file_epaNO2)
data_epaPM2_5 = csv.reader(file_epaPM2_5)

#skip header in csv file
next(data_epaNO2)
next(data_epaPM2_5)

#put csv elements into a list to simplify analysis
list_epaNO2 = list(data_epaNO2)
list_epaPM2_5 = list(data_epaPM2_5)

#read through NO2 data 
for row in list_epaNO2:
    #reading from csv is str so convert to float for if else statements
    no2Conc = float(row[4])
    
    #print concentration value and respective power setting
    if 100 < no2Conc:
       print(str(no2Conc) + " ppb = Please keep the air purfier on at full capacity. The air outdoors has very high levels of NO2.")
       print("   It is recommended that everyone be wary of the time spent outdoors as long exposure may be harmful.\n")
    elif 53 < no2Conc <= 100:
       print(str(no2Conc) + " ppb = Please set the air purifier at 50% capacity. The air outdoors has some moderate levels of NO2.")
       print("   It is recommended that patients with underlying health conditions should not go outside if possible.\n")
    else:
       print(str(no2Conc) + " ppb = You can keep the purifier off. The air outdoors seems pretty great today!\n")

#read through particulate matter data     
for row in list_epaPM2_5:
    #reading from csv is str so convert to float for if else statements
    pmConc = float(row[4])
    
    #print concentration value and respective power setting
    if 35 < pmConc:
       print(str(pmConc) + " ug/m3 = Please keep the air purfier on at full capacity. The air outdoors has very high levels of PM.")
       print("   It is recommended that everyone be wary of the time spent outdoors as long exposure may be harmful.\n")
    elif 12 < pmConc <= 35:
       print(str(pmConc) + " ug/m3 = Please set the air purifier at 50% capacity. The air outdoors has some moderate levels of PM.")
       print("   It is recommended that patients with underlying health conditions should not go outside if possible.\n")
    else:
       print(str(pmConc) + " ug/m3 = You can keep the purifier off. The air outdoors seems pretty great today!\n")
