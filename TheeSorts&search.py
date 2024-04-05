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
        