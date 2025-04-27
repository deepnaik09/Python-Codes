class palindrome:
    def palindromeText(text):
        isPalindrome = True
        mid = (len(text)//2)

        for i in range(0 , mid):
            if text[i] != text[(len(text) - 1 - i)]:
                isPalindrome = False

        if isPalindrome == True:
            print("It is a Palindrome")
        else:
            print("It is not a Palindrome") 

    text = int(input("Enter a text: "))
    palindromeText(text)
