import re

# Raw string:
# s = r"\n"
s = "Hello123" # <- Alpha numeric

s2 = "Missisipi@123,*# "# <- Alpha numeric & symbols
# print(type(s))
# print(s)
print(s2)
print(re.findall("[a-z]",s2))# all lower cased alphabets
print(re.findall("[A-Z]",s2))# all large alphabets
print(re.findall("[0-9]",s2))# all numeric charcters
print(re.findall("\W",s2))# All the non Alphanumeric characters a-z, A-Z, 0-9 (Pattern)
print(re.findall("[s]",s2))# Single charcter
print(re.findall("[aeiou]",s2))# All the vowels
print(re.findall(" ",s2))# Find space
print(re.findall("\s",s2))# Find space
print(re.findall("\S",s2))# Find non white space
print(re.findall("M|@",s2))# Find alternate characters

print()

from re import match
strings = ["Welcome to TutorialsTeacher", "weather forecast",
           "Winston Churchill",
           "W.G.Grace",
           "Wonders of India",
           "Water park"]

for string in strings:
    obj = match("W[a-z]", string)
    
    if (obj != None):
        print(obj.group())

# Split when found numbers and from its left
str2 = "Six Nine:69 Twelve:12 Zero:0 Sixty:60"

pattern = '\d'# +: Gives all the characters on the left side of the given pattern
result = re.split(pattern, str2)
print(result)