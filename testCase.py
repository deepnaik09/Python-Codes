class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        revNum = 0
        while num > 0:
            digit = num % 10
            revNum = ((revNum*10)+digit)
            num = num // 10
        if x == revNum:
            return True
        else:
            return False
                                            