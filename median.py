
import csv

with open("project_data.csv", newline='') as f:
    reader=csv.reader(f)
    file_data= list(reader)


file_data.pop(0) #removes the text title from data

new_data=[]
for i in range(len(file_data)): #length of container
    n_num= file_data[i][1] #takes row and coloumns of the data 1 is coloumn number(of height) # one by one we want height of each row 
    new_data.append(float(n_num)) #converts to float (decimal) and adds to new_data list

#getting the mean/average
n=len(new_data) #length of new data
new_data.sort() #sorts the data by ascending and desecdeing

if n%2==0: #if length of n is even then 2 number othewise one
    median1= float(new_data[n//2]) #get the nearest whole number.

    #getting the second number
    median2= float(new_data[n//2-1]) #if n=8 then first numbher is 4th number and second number is 4-1 = 3 rd number
    median=(median1+median2)/2 #add and divide by 2 to get the median of n even number 
else:
    median= new_data[n//2] #gets the middle value on n odd numbers

    
print("Median is: "+ str(median))