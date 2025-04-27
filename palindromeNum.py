class palindrome:
    def palindromeNum(num):
        def reverse(x):
            revNum = 0
            while x > 0:
                digit = x % 10
                revNum = ((revNum * 10) + digit)
                x = x // 10
            return revNum
        
        reverseNum = reverse(num)
        if num == reverseNum:
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
    num = int(input("Enter a number:"))
    palindromeNum(num)
