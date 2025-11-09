def find(s, n):
# write your implementation here
# s is the array
# n is the target number

    # for i in range(len(s)):
    #     temp = n - s[i]
    #     for j in range(len(s)):
    #         if s[j] == temp and i != j:
    #             return [i,j]
    # return None

    dict = {}       #dictionary
    
    for i in range(len(s)):
        temp = n - s[i]

        if temp in dict:
            return [dict[temp], i]
        
        dict[s[i]] = i

    return None

array1 = [2,7,11,15]
n1 = 9
array2 = [3,2,4]
n2 = 6
array3 = [3,3]
n3 = 6

print(find(array1,n1))
print(find(array2,n2))
print(find(array3,n3))