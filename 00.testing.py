stR = "Hello, world!"
# strArr = list(stR)

# print(strArr)
# print(len(strArr))
# print(len(stR))
def removeDuplicate(str):
    strArr = list(str)
    for i in range(0, len(strArr)-1):
        if(strArr.count(strArr[i])>1):
            newStrArr = strArr.remove(strArr[i])
            return newStrArr
arr = []
print(removeDuplicate(stR))