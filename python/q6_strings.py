# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    
        
    if count > 9:
    
        return ("Number of donuts: many")
    
    else:
        
        return ("Number of donuts: " + str(count))
    
    

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    
    if len(s) < 2:
        return ''
    
    else:
        
        return s[0:2] + s[len(s)-2:len(s)+1]



def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    return s[0] + s[1:len(s)].replace(s[0], '*')


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    return (b[0:2]+a[2:len(a)] + " " + a[0:2] + b[2:len(b)])


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) > 2:
        
        if s[len(s)-3:len(s)] == "ing":
        
            return s+"ly"
    
        else:
            
            return s+"ing"
    else:
        
        return s
    

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    not_index = s.find('not')
    bad_index = s.find('bad')
    
    if bad_index > not_index:
        s = s.replace(s[not_index:bad_index+3], 'good')
    
    return s


def front_back(a, b):
    

    if len(a) % 2 == 0:
        a_halfpoint = int(len(a)/2)
    
    else:
        
        a_halfpoint = int(len(a)/2) + 1
    
    if len(b) % 2 == 0:
        b_halfpoint = int(len(b)/2)
    
    else:
        
        b_halfpoint = int(len(b)/2) + 1
    
    a_half_1 = a[0:a_halfpoint]
    a_half_2 = a[a_halfpoint:len(a)]
    
    b_half_1 = b[0:b_halfpoint]
    b_half_2 = b[b_halfpoint: len(b)]
    
    '''
    
    print("a_half_1: " + a_half_1)
    
    print("b_half_1: " + b_half_1)
    
    print("a_half_2: " + a_half_2)
          
    print("b_half_2: " + b_half_2)
    
    '''
    
    return a_half_1 + b_half_1 + a_half_2 + b_half_2
