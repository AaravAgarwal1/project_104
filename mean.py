
import csv

with open("project_data.csv", newline='') as f:
    reader=csv.reader(f)
    file_data= list(reader)


file_data.pop(0) #removes the text title from data

new_data=[]
for i in range(len(file_data)): #length of container
    n_num= file_data[i][2] #takes row and coloumns of the data 1 is coloumn number(of height) # one by one we want height of each row 
    new_data.append(float(n_num)) #converts to float (decimal) and adds to new_data list
new_data.sort()
#getting the mean/average
n=len(new_data) #length of new data
total=0
for x in new_data:
    total+=x

mean= total/n #sum of values/number of values get it? noice.

print(f"Average Weight is: {str(mean)}")
