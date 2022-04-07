nums = [2,4,6,5,6] #just for checking
target = 10 #just for checking
index1 = 0
index2 = 0
arr1 = []
flag = False
for index1 in range(0,len(nums)):
    for index2 in range(index1+1,len(nums)):
        if nums[index1]+nums[index2] == target:
            arr1.append(index1)
            arr1.append(index2)
            flag = True
            break
    if(flag == True):
        break
print(arr1)
