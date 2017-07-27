# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Similarities:
*Both are iterable and you can loop through both of their elements
*You can access specific elements by their index numbers
*You can search for the index of a specific element in both

Differences:
*You cannot use lists as keys in dictionaries
*Lists are mutable, but tuples are immutable
*tuples are declared with "()", but lists are declared with "[]"
---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Similarities:
* Lists and sets are iterable
* Lists and sets are searchable

Differences:
* Lists are mutable and sets are immutable
* Lists can contain duplicates of entries

Sets perform faster when searching for a specific element because when a set is created,
a hash table is populated through a hash function. This means that when searching for
a specific element, the set can pin point where in the hash table the piece of data is
stored rather than looping through the entire set, which a list does.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

A lambda is an anonymized/unnamed function. It is used for applying a single function all members of a collection.

```python
#This lambda will sort the list according to whether each digit is even or odd.

list1 = [3,14,7,10,11,6,15]

sorted(list1, key = lambda x: x%2 == 0)

Out[15]: [3, 7, 11, 15, 14, 10, 6]
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

___

List comprehensions is a way to populate a list using a function on the elements of another iterable. There is also the ability to select the elements with a condition.

___

```python
#This list comprehensions will populate a list of the squares of even numbers between 0 - 19.

list_10_sq = [i*i for i in range(10) if i % 2 == 0]

>>> list_10_sq
[0, 4, 16, 36, 64]

```

Maps and filters can achieve the same application of a function and conditional selection, but can be a bit less readable.

```python
list_10_sq = list(map(lambda x: x*x), filter(lambda x : x % 2 == 0, range(10)))

>>list_10_sq
[0, 4, 16, 36, 64]


```

___
Set comprehensions are implemented quite similarly to list comprehensions.
___

```python

#This creates a set of squares of all odd numbers in the list nums

nums = [1,1,1,2,3,4,4,4,5,6,7,9,10]

set10 = {i*i for i in nums if i % 2 > 0}

>>>set10
{1, 9, 25, 49, 81}

```
___
Dictionary comprehensions can also be used to populate a dictionary from two iterables.

___

```python

characters = ['Ash', 'Goku', 'Inuyasha', 'Holmes']

nemeses = ['Gary', 'Frieza', 'Naraku', 'Moriarti']

dict_heros_nem_anime = {character: enemy for character, enemy in zip (characters, nemeses) if character != 'Holmes'}

>>> dict_heros_nem_anime
{'Ash': 'Gary', 'Goku': 'Frieza', 'Inuyasha': 'Naraku'}

```


### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)
