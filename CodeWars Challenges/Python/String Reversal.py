'''
                        CHALLENGE
Complete the function that accepts a string parameter,
and reverses each word in the string.
All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

# MY SOLUTION
def reverse_words(string):
# This converts the string into a list of substrings using space as the indicator
    words = string.split(" ")
    
# This reverses each word in the list of substrings
    for i in range(len(words)):
        words[i] = words[i][::-1]
        
# This converts the list back into a string separating reversed words with a space
    return " ".join(words) 

# Test cases
print(reverse_words("This is an example!"))  # Output: "sihT si na !elpmaxe"
print(reverse_words("double  spaces"))       # Output: "elbuod  secaps"


# BEST SOLUTION ON CODEWARS
'''
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
'''
