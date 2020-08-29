def reversString(n):
     n = n[::-1]
     return n

def IsPalindrome(n):
    if reversString(n)==n:return True
    else: return False


Entery = input("Please input any Phrase : ")
if IsPalindrome(Entery):lambda:print(f"{Entery} is not a palindrome"),print(f"{Entery} is a palindrome")


