import re
print(re.search(r".com", "welcome").group())
print(re.search(r"\.com", "welcome.com").group())

#string interpolation

indian_greeting = 'Namaste'
print('Indian people greet everyone with', indian_greeting, 'with folded hands!')
print(indian_greeting.count('a'))

