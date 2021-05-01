import csv 
import math

with open('c105sd.csv', newline='') as f:
    reader = csv.reader(f)
    fileData=list(reader)
    data=fileData[0]
    
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total += int(x)
        
    mean=total/n
    return mean 

#squaring and getting the values

squaredList=[]
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squaredList.append(a)

#getting sum

sum=0
for i in squaredList:
    sum=sum+i

#dividing the sum by the total values
result=sum/(len(data)-1)

#getting the deviation by taking sq root of the result
std_deviation=math.sqrt(result)
print(std_deviation)