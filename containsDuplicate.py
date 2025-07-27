class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
nums = [1, 2, 3, 4]
s = Solution()
print(s.containsDuplicate(nums))


# Most optimal and fastest soltion
   # def containsDuplicate(self, nums):
    #     seen = set()
    #     for num in nums:
    #         if num in seen:
    #             return True
    #         seen.add(num)
    #     return False



# Ran the following code, worked but it exceed the time limit at the 65th Testcase out of 77 in LeetCode
# class Solution:
#     def containsDuplicate(self, nums):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] == nums[j]:
#                     return True
            
#         return False
