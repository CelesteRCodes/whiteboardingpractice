# STARTED ON 4/19

## Given list of ints, return True if any two nums in list sum to 0.

def sum_zero(numberlist):
    numberlist = set(numberlist)
    for n in numberlist:
        if -n in numberlist: 
            return True
       

# numberlist = [1, 8, -1, 2, 2]

# ---------------------------------

## Given two lists. concatenate them (that is, combine them into a single list)

final_list = []
def concat_lists(list1, list2):
    """Combine lists."""
    new_list = list1 + list2
    for lists in new_list:
        final_list.append(lists)
        print(final_list)

# list1 = []
# list2 = [3, 4]

# -------------------------------

## Given a list of numbers, return the smallest and the largest number.

def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple."""
    # i want to sort the numbers in ascending order and then return numbers at first index and last index (max and main)
    nums = sorted(nums)
    if len(nums) == 0:
        return (None, None)
    else:
        high_low = nums[0], nums[-1]
        print(tuple(high_low))

# nums = []

# ----------------------------

# 4/20


## Given a word in English, return True if that word contains more vowels than non-vowels; otherwise, return False. The word will always be a single word, without any punctuation or spaces. It will contain only uppercase and lowercase letters.

# If the phrase is over half vowels, it should return True

def has_more_vowels(phrase):
    vowels = 'aeiou'
    vowel_count = 0
    const_count = 0
    for char in phrase:
        if char in vowels:
            vowel_count +=1 
        else:
            const_count += 1
    print(vowel_count > const_count)


# ------------------------------
## Write a program that counts from 1 to 20 in fizzbuzz fashion.

# To do so, loop from 1 to 20 (inclusive). Each time through, if the number is evenly divisible by 3, say ‘fizz’. If the number is evenly divisible by 5, say ‘buzz’. If the number is evenly divisible by both 3 and 5, say ‘fizzbuzz’. Otherwise, say the number.

def fizzbuzz(num):
    for x in range(num + 1):
        if x == 0:
            pass
        elif x % 3 == 0 and x % 5 == 0:
            print('fizzbuzz')
        elif x % 5 == 0:
            print('buzz')
        elif x % 3 == 0:
            print('fizz')
        else:
            print(x)
# -------------------------------    

## Given a word, return True if that word contains only unique characters. Return False otherwise

def has_unique_char(word):
    
    new_word = set(word)
    if len(word) == len(new_word):
        print(True)
    else:
        print(False)
        

## Write a function the returns True or False, depending on whether the integer passed into it is a prime number.

# Only numbers >1 can be prime numbers 

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        print(False)
    else: 
        return True


for n in range(2, num):
        if num % n == 0:
            return False

# def is_prime(num):
#     """Is a number a prime number?"""

#     # START SOLUTION

#     if num < 2:
#         return False

# ---------------------------------

# 4/29:
# Sum a list of integers using recursion.

# For example::

#     >>> sum_list([5, 5])
#     10

#     >>> sum_list([-5, 10, 4])
#     9

#     >>> sum_list([20])
#     20

# The sum of an empty list is zero::

#     >>> sum_list([])
#     0


def sum_list(list):
    number_list = 0
    for numbers in list:
        number_list += numbers
    return number_list
    

# ----------------------------------------------

# in which standard letters are often replaced by numerals or special characters.
# Letter Becomes:
# a - @
# o - 0
# e - 3
# l - 1
# s - 5
# t - 7

# In this exercise, you’ll make a function that translate a word to leet-speak:

# >>> translate_leet("Hi Balloonicorn")
# 'Hi B@1100nic0rn'

# >>> translate_leet("Hackbright is the Shizzle")
# 'H@ckbrigh7 i5 7h3 5hizz13'

leets = {'a': '@', 'o': '0', 'e':'3', 'l':'1', 's':'5', 't':'7'}

def translate_leet(word):
    new_word = ""
    for char in word:
        
        if char in leets:
            new_word += leets[char]
        else:
            new_word += char

    return new_word
    
        
# -------------------------------------------

# Find the largest integer in a list of integers.
# For example:
# >>> max_num([5, 3, 6, 2, 1])
# 6

def max_num(list):
    max = []
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            max.append(list[i])
    for i in range(len(max)):
        if max[i] > max[i - 1]:
            return max[i]

# ---------------------------------------------------
# Define a function max_of_three that takes in three numbers as arguments and returns the largest of them.
# For example:
# >>> maxofthree(1, 5, 2)
# 5
# >>> maxofthree(10, 1, 11)
# 11

def maxofthree(list):
    list.sort()
    # print(list)
    return list[-1]

    # ----------------------------------------

# A pangram is a sentence that contains all the letters of the English alphabet at least once, like “The quick brown fox jumps over the lazy dog.”
# Write a function to check a sentence to see if it is a pangram or not.
# For example:
# >>> is_pangram("The quick brown fox jumps over the lazy dog!")
# True
# >>> is_pangram("I like cats, but not mice")
# False

# def is_pangram(phrase):
#     alphabet = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'y', 'Y', 'z', 'Z']

# #  had to hard code the uppercase because .lower() wasn't working 

#     words = phrase.split()
    
   
#     new_phrase = []
#     for char in words:
#         if char[0] in alphabet:
#             new_phrase.append(char)
            
            
#     return len(words) == len(new_phrase)

# want to make sure the phrase has all of the letters of the alphabet?
 