 def isPalindrome(string):
     cleaned_str=string.replace(" ","").lower()
     return cleaned_str==cleaned_str[::-1]
user_input=input("Enter a string: ")
if isPalindrome(user_input):
    print("You got a palindrome!")
else:
    print("It's not a palindrome.")