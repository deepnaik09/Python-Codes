def Solutions(nums):
    temp = 0
    for i in range(0, (len(nums))):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
            else:
                continue
    print("Sorted Array:", nums)

nums = [5, 4, 3, 2, 1]
Solutions(nums)