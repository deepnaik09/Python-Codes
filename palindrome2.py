class palindrome:
    def isPalindrome(text):
        def reverse(x):
            return x[::-1]
        revText = reverse(text)
        if text == revText:
            print("It is a Palindrome")
        else:
            print("It is not a Palindrome")

    text = input("Enter a text:")
    isPalindrome(text)  