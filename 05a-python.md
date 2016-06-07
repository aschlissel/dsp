# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are both sequences of values that are indexed by integers and can be any type. The main difference between Python lists and tuples are that lists are mutable and tuples are immutable.  
  
>> Tuples will work as keys in a dictionary. Tuples and dictionaries work well together, for example, you can use a tuple assignment to traverse a dictionary cleanly.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets contain objects. However, a set is an unordered collection of unique and immutable objects,
while a list is ordered, allows duplicates, and is mutable.

>> One example of using a set is to keep track of a guest list when planning a party.
```python
RSVP_Yes = {"John", "Mary", "Sue M.", "Jean", "Billy", "Sue Q."}
```

>> One example of using a list is to store Tony Musical winners in order.
```python
Tony_Winners = ["Contact", "The Producers", "Hairspray", "Avenue Q", "Monty Python's Spamalot"]
```

>> It is much faster to find an element in a set than a list because sets use the hash function to map to a bucket (O(1)). 
Lists take time proportional to the list's length in average and worst cases (O(n)).

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's lambda is a tool for building functions. Although lambda isn't necessary, there are situations where it makes writing code a bit easier and cleaner.  
  
>> Example:  
```python
t = ['Lambda', 'can', 'be', 'cool', 'sometimes']  
sorted(t, key=lambda word: word.upper())
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>>  List comprehension is an elegant way to define and create a list in Python. It is a substitute for the functions lambda, map(), filter(), and reduce().

>> Map is a cleaner way to write a for loop to perform operations on a list and it usually performs faster than a for loop. Filter prints values in a list that return the boolean True. The same task can also be accomplished using a for loop, but this is cleaner.

>> For my example I will convert miles to kilometers.

>> List Comprehension
```python
miles = [3.1, 6.2, 13.1, 26.2]
kilometers = [(1.6 * x) for x in miles]
print kilometers
```
>> Map
```python
miles = [3.1, 6.2, 13.1, 26.2]
kilometers = map(lambda x: (1.6 * x), miles)
print kilometers
```
>> Filter  
>> Print just the half marathon and marathon values
```python
miles = [3.1, 6.2, 13.1, 26.2]
pro_runners = filter(lambda x: x > 10, miles)
print pro_runners
```
>> Set Comprehension  
>> Set comprehension performs a similar in function to a list comprehension, but it returns a set instead of a list, denoted by curly brackets.
```python
miles = {3.1, 6.2, 13.1, 26.2}
kilometers = {(1.6 * x) for x in miles}
print kilometers
```
>> Dictionary Comprehension
```python
miles = [3.1, 6.2, 13.1, 26.2]
miles2km = {x: (1.6 * x) for x in miles}
print miles2km
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```python
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```python
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```python
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





