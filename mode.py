import csv
import collections
from collections import Counter

with open("project_data.csv", newline='') as f:
    reader=csv.reader(f)
    file_data= list(reader)


file_data.pop(0) #removes the text title from data

new_data=[]
for i in range(len(file_data)): #length of container
    n_num= file_data[i][1] #takes row and coloumns of the data 1 is coloumn number(of height) # one by one we want height of each row 
    new_data.append(float(n_num)) #converts to float (decimal) and adds to new_data list

data= Counter(new_data)

mode_data_for_range= {
    "50-60":0,
    "60-70":0,
    "70-80":0
} #dictionary

#check if height lies between these values they key will get increased by 1

for height, occurence in data.items():
    if 50< float(height) <60:
        mode_data_for_range["50-60"]+=occurence
    elif 60< float(height) <70:
        mode_data_for_range["60-70"]+=occurence
    elif 70< float(height) <80:
        mode_data_for_range["70-80"]+=occurence

mode_range=0
mode_occurence=0

for range, occurence in mode_data_for_range.items(): #convert to list (the occurences of child falling in height brackets)
    if occurence> mode_occurence:
        mode_range, mode_occurence=[int(range.split("-")[0]), int(range.split("-")[1])], occurence #removes the dash between 50-60 and now 0 index is 50 and 1 is 60
        mode= float(mode_range[0] + mode_range[1])/2 #adds 50 as index 0 and 60 as index 1 and then divides by 2

print(f"Mode is: {mode}")