#bubble sort
def bubble_sort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

nums=[4,6,7,9,10,24,13,2,3,4,]
bubble_sort(nums)
print("Sorted array",nums)
        

def buble_sort(digits):
    n=len(digits)
    for i in range(n):
        for j in range(n-i-1):   #even(n-2)worked. this is because after the two loops, 
                              #the last 2 i elements are already in place. 
            if digits[j]>digits[j+1]:
                digits[j],digits[j+1]=digits[j+1],digits[j]

digits=[5,3,8,1,2]
buble_sort(digits)
print("This is the sorted array",digits)
