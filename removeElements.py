class Solutions:
    def removeElements(nums, val):
        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != val:
                i=+1
                nums[i] = nums[j]
    nums = [3,2,2,3]
    val = 3
    
    removeElements(nums, val)