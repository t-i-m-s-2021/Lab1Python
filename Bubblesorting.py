import random
nums = list(range(0,10))
random.shuffle(nums)
print("Исходный массив чисел: ", nums)
N = len(nums)
i = 0
while i < N-1:
    j=0
    while j < N - 1 - i:
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
        j += 1
    i += 1

print("Отсортированный массив чисел:", nums)
    
