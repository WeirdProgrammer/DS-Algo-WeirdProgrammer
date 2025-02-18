# arr = [1,3,5,7,9] 
# print(arr)
# for i in range(len(arr)):
#     arr[i] = -arr[i]
    
    
# print(arr)

# arr = [[0,1],[1,2],[2,0]]
# n = 3
# source = 0

# for u, v in arr:
#     print(u, v)



# def romanToInt(s):
#     hashmap = {
#         'I':1,'V':5,'X':10,'L':50,'C':100,
#         'D':500,'M':1000, 'IV':4, 'IX':9,
#         'XL':40,'XC':90, 'CD':400,'CM':900
#     }
#     val , res = 0,0
#     i = 0
    
#     while i < len(s):
#         res = s[i] + s[i+1]
#         if res in hashmap.keys():
#             print(i)
#             val += hashmap[res]
#             print(res)
#             i += 2
#         elif res not in hashmap.keys():
#             val += hashmap[s[i]]
#             i += 1
#         else:
#             i += 1
            
#     return val

# print(romanToInt("MCMXCIV")) #1994




# strs = ["flower","flow","flight"]
# def longestCommonPrefix(strs):
#     if not strs:  # If the list is empty, return an empty string
#         return ""

#     prefix = strs[0]  # Assume the first string as the prefix

#     for string in strs[1:]:
#         while not string.startswith(prefix):  # Trim the prefix until it matches
#             prefix = prefix[:-1]
#             if not prefix:  # If the prefix becomes empty, return empty
#                 return ""
    
#     return prefix

# print(longestCommonPrefix(strs))


def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    n1 = len(nums)
    nums = set(nums)
    nums = list(nums)
    nums1 = []
    # for i in range(n1):
    #     if nums[i] is not None:
    #         nums1.append(nums[i])
    #     else:
    #         nums1.append('_')
    i = 0 
    while i < n1:
        nums1.append(nums[i] if not None else '_')
        i+= 1
            
            
    print(nums1)
            
    
    
arr = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(arr)


