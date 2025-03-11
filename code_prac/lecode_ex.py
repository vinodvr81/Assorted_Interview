# 8.
# String
# to
# Integer(atoi)
# Medium
# Topics
# Companies
# Implement
# the
# myAtoi(string
# s) function, which
# converts
# a
# string
# to
# a
# 32 - bit
# signed
# integer.
#
# The
# algorithm
# for myAtoi(string s) is as follows:
#
# Whitespace: Ignore
# any
# leading
# whitespace(" ").
# Signedness: Determine
# the
# sign
# by
# checking if the
# next
# character is '-' or '+', assuming
# positivity if neither
# present.
# Conversion: Read
# the
# integer
# by
# skipping
# leading
# zeros
# until
# a
# non - digit
# character is encountered or the
# end
# of
# the
# string is reached.If
# no
# digits
# were
# read, then
# the
# result is 0.
# Rounding: If
# the
# integer is out
# of
# the
# 32 - bit
# signed
# integer
# range[-231, 231 - 1], then
# round
# the
# integer
# to
# remain in the
# range.Specifically, integers
# less
# than - 231
# should
# be
# rounded
# to - 231, and integers
# greater
# than
# 231 - 1
# should
# be
# rounded
# to
# 231 - 1.
# Return
# the
# integer as the
# final
# result.
#
# Example
# 1:
#
# Input: s = "42"
#
# Output: 42
#
# Explanation:
#
# The
# underlined
# characters
# are
# what is read in and the
# caret is the
# current
# reader
# position.
# Step
# 1: "42"(no
# characters
# read
# because
# there is no
# leading
# whitespace)
# ^
# Step
# 2: "42"(no
# characters
# read
# because
# there is neither
# a
# '-'
# nor
# '+')
# ^
# Step
# 3: "42"("42" is read in)
# ^
# Example
# 2:
#
# Input: s = " -042"
#
# Output: -42
#
# Explanation:
#
# Step
# 1: "   -042"(leading
# whitespace is read and ignored)
# ^
# Step
# 2: "   -042"('-' is read, so
# the
# result
# should
# be
# negative)
# ^
# Step
# 3: "   -042"("042" is read in, leading
# zeros
# ignored in the
# result)
# ^
# Example
# 3:
#
# Input: s = "1337c0d3"
#
# Output: 1337
#
# Explanation:
#
# Step
# 1: "1337c0d3"(no
# characters
# read
# because
# there is no
# leading
# whitespace)
# ^
# Step
# 2: "1337c0d3"(no
# characters
# read
# because
# there is neither
# a
# '-'
# nor
# '+')
# ^
# Step
# 3: "1337c0d3"("1337" is read in;
# reading
# stops
# because
# the
# next
# character is a
# non - digit)
# ^
# Example
# 4:
#
# Input: s = "0-1"
#
# Output: 0
#
# Explanation:
#
# Step
# 1: "0-1"(no
# characters
# read
# because
# there is no
# leading
# whitespace)
# ^
# Step
# 2: "0-1"(no
# characters
# read
# because
# there is neither
# a
# '-'
# nor
# '+')
# ^
# Step
# 3: "0-1"("0" is read in;
# reading
# stops
# because
# the
# next
# character is a
# non - digit)
# ^
# Example
# 5:
#
# Input: s = "words and 987"
#
# Output: 0
#
# Explanation:
#
# Reading
# stops
# at
# the
# first
# non - digit
# character
# 'w'.
#
# Constraints:
#
# 0 <= s.length <= 200
# s
# consists
# of
# English
# letters(lower - case and upper - case), digits(0 - 9), ' ', '+', '-', and '.'.

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# def user_add(x:tuple, y:tuple, z:tuple) -> int:
#     for i,v,f in zip(x,y,z):
#         if i and v and f:
#             yield i+v+f

# for (i,v,f) in zip(tuple([i for i in range(5)]), tuple([i for i in range(5)]),tuple([i for i in range(5)])):
#     for i in user_add((i,), (v,), (f,) ):
#         print(i)

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# def check_anagram(s1:str, s2: str) -> bool:
#     if set(list(s1)) == set(list(s2)):
#         return True
#     else:
#         return False

# print(check_anagram("anagram", "nagaram"))
# print(check_anagram("rat", "car"))

import re


# pattern_constraint1 = r"[A-Z]+"
# pattern_constraint2 = r"[a-z]+"
# pattern_constraint3 = r"[0-9]+"
# pattern_constraint4 = r"[' ']"+[-]+[.]+
class Solution:
    def myAtoi(self, s: str) -> int:
        pattern_list: int = 0
        if len(s) > 0 and len(s) <= 200:
            s = s.lstrip()  # Whitespace: Ignore any leading whitespace (" ").
            if s[0].isdigit() and s[0].startswith("0"):
                return 0
            if not s[0].isdigit() and not s[0].startswith("-") and s[0].startswith("+"):
                return 0
            else:
                pattern_list = [i.group() for i in re.finditer(r'^[-,+]*\d+', s)]
                if pattern_list:
                    return int("".join(pattern_list))
                else:
                    return 0


        else:
            raise ("OutOfBound Exception")


input_list = ["42", " -042", "1337c0d3", "words and 987", "0-1"]

for i in input_list:
    print(Solution().myAtoi(i))










