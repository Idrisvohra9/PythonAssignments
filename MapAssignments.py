import math
import random

numList = [1,2,3,4,5,6,7]
# Triple all the numbers given in list:
print("Number List:", numList)
print()
def MyTripler(elem): return elem*3;

res1 =  list(map(MyTripler,numList))

print("Triple all numbers in the list: ", res1)
print()

# Separate even odd number from given list:
def getOddNums(elem): 
    if(elem%2 != 0): return elem;
    # else: pass

def getEvenNums(elem): 
    if(elem%2 == 0): return elem;
    # else: pass;
    
res2OddNums = list(filter(getOddNums,numList))
res2EvenNums = list(filter(getEvenNums,numList))

print("Separated Odd numbers: ", res2OddNums)
print()
print("Separated Even numbers: ", res2EvenNums)
print()

# Print all string in lower case from given tuple

tupleStr = ("HELLO","HOW", "ARE","YOU?")
print("Tuple of strings: ", tupleStr)
print()

print("ToLower: ", tuple(map(lambda element: element.lower(),tupleStr)))
print()

# Print square root of numbers given in list
sqrtNumList = list(map(lambda e: math.sqrt(e),numList))

print("sqrtNumList: ", sqrtNumList)
print()

# Eliminate duplicate letter from given string
Str = "AABCD112"
print("Str: ", Str)
# Converting the string value to set so that there are no duplicates and then converting it back to list so that it can be converted back to string with indexes.

remDuplicate = list(set(Str))
i =0
s = "";
while i < len(remDuplicate):
    s+=remDuplicate[i]
    i+=1

print("Eliminate duplicate letter from Str: "+s)
print()

# Print table of any number:
getRandomNumber = random.choice(numList)

def PrintTable(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

print("Printing table of random number: ")
PrintTable(getRandomNumber)
print()

# Add two list:
list1 = [9,8,7,6]
list2 = [5,4,3,2]
print("List1: ",list1)
print("List2: ",list2)

list1.extend(list2)
print("Extending List1 with List2",list1)

print()


# Convert all float digits into integer using
# built in function from given list.

floatArr = [1.23,2.34,6.77]
print("floatArr: ", floatArr)

intArr = list(map(int, floatArr))

print("Float list To Integer: ",intArr)

print()

# Reverse given set
#todo: Couldn't be done with map.
set1 = {1,2,3,4,5}
print("set1: ", set1)
listSet1 = list(set1)
listSet1.reverse()

set1 = listSet1
print("Reverse set1: ",set1)
print()

# Add ‘@gmail.com’ to all the values of
# given dictionary and convert it to lower
# case.

dict1 = {
    "name": "Idris",
    "value": "123",
    "type": "integer"
}

Email = dict(map(lambda x:(x[0],x[1].lower()+"@gmail.com"),dict1.items()))

print("Email: ",Email)

print()

