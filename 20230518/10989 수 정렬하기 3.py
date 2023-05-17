import sys
n=int(input())
nums={}
for _ in range(n):
    num=int(sys.stdin.readline())
    if num in nums: nums[num]+=1
    else: nums[num]=1
for i in range(10001):
    if i in nums:
        for _ in range(nums[i]):print(i)