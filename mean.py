import math


import csv

with open('case.csv',newline='') as f:

    reader=csv.reader(f)
    file_data=list(reader)

    data=file_data[0]

    #getting the mean
# data = [20,69,56,90,40,99,86,100,70,69,80,65,57,82,90,70,79,39,90,80,86,53,97,95,88,47,100,56,97,100] #list of x or y
# data=[60,61,65,63,98,99,90,95,91,96]

#finding the mean
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
        mean=total/n

        return mean


        sqaured_list=[]
        for number in data:
            a=int (number)- mean(data)
            a=a**2
            sqaured_list.append(a)


            sum=0

            for i in sqaured_list:
                sum=+ i

            result = sum/ (len(data)-1)
            mean=math.sqrt(result)
            print(mean)
        
