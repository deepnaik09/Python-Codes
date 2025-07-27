class Solution:
# Solution 1:
    def validAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False
            count[char] -=1
            if count[char] < 0:
                return False
        return True





# Solution 2
#     def validAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
        
#         count = {}

#         for char in s:
#             count[char] = count.get(char, 0) + 1
        
#         for char in t:
#             if char not in count:
#                 return False
            
#             count[char] -= 1
#             if count[char] < 0:
#                 return False
#         return True





# Solution 3
#     def validAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
        
#         count = [0] * 26

#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1
#             count[ord(t[i]) - ord('a')] -= 1

#         for val in count:
#             if val != 0:
#                 return False
#         return True


s = "cat"
t = "tac"
sol = Solution()
print(sol.validAnagram(s, t))