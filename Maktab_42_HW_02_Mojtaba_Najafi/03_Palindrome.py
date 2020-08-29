def reversString(n):
    #reversring a string using list
     n = n[::-1]
     return n

def IsPalindrome(n):
    #if arg is equal with reversred arg it is a palindrome
    if reversString(n)==n:return True
    else: return False


Entery = input("Please input any Phrase : ")
if IsPalindrome(Entery):lambda:print(f"{Entery} is not a palindrome"),print(f"{Entery} is a palindrome")


