import collections

#1
print("enter elements to be stored in the list")
a = [int(x) for x in input().split()]
ce=0
co=0

for i in range(len(a)):
    if(a[i]%2==0):
        ce=ce+1
    else:
        co=co+1
print(" total even numbers =",ce)
print(' total odd numbers =',co)

#2
techGiants = ["google","Apple","facebook","microsoft","tesla"]
a.extend(techGiants)
print(a)

#3
count = collections.Counter(a)
print(count)

#4
num = [12,5452,24,454,644,3,32,5]
num.sort()

#5
array1=[[1,2,3],[15,18,19],[7,8,9]]
array2=[[0,1,2],[4,5,6],[45,67,89],[100,109,182,564]]
array = array1 + array2
array.sort()
print(array)

#6

#STACK IMPLEMETATION

def POP(a):
    a.pop()
def PUSH(a,x):
    a.append(x)

#QUEUE IMPLEMENTATION

def ENQUEUE(a,x):
    a.insert(0,x)
def DEQUEUE(a):
    a.pop(0)

#Calling functions defined
b = [1,2,3,4,5,6,7,8,9,10]
POP(b)
print(b)

PUSH(b,10)
print(b)

ENQUEUE(b,0)
print(b)

DEQUEUE(b)
print(b)