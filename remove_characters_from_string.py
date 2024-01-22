#Exercise 4: Remove first n characters from a string
#Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_chars(word, n):
    print('Original string:', word)
    if n < len(word):
        result = word[n:]
        return result
    
print("Remove characters from the string")

#Print: output should be tive
print(remove_chars("pynative", 4)) 

#Print: output should be native
print(remove_chars("pynative", 2)) 
