![Logo](/icon.png)

# 30-seconds-of-python-code [![Tweet](https://jpillora.com/github-twitter-button/img/tweet.png)](http://www.twitter.com/share?text=%2330secondsofcode+30-seconds-of-python-code+-+Python+Implementation+of+30+seconds+of+code%0Ahttps://github.com/kriadmin/30-seconds-of-python-code&url=a")
[![License](https://img.shields.io/aur/license/yaourt.svg)](https://github.com/kriadmin/30-seconds-of-python-code/blob/master/LICENSE)
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](http://www.firsttimersonly.com/) [![Gitter chat](https://img.shields.io/badge/chat-on%20gitter-4FB999.svg)](https://gitter.im/30-seconds-of-python-code/Lobby) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com) [![Travis Build](https://travis-ci.org/kriadmin/30-seconds-of-python-code.svg?branch=master)](https://travis-ci.org/kriadmin/30-seconds-of-python-code) [![Insight.io](https://img.shields.io/badge/insight.io-Ready-brightgreen.svg)](https://insight.io/github.com/kriadmin/30-seconds-of-python-code/tree/master/?source=0) [![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/Flet/semistandard)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fkriadmin%2F30-seconds-of-python-code.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fkriadmin%2F30-seconds-of-python-code?ref=badge_shield)

## Welcome to 30-seconds-of-🐍-code!

>A Python implementation of 30-seconds-of-code.

**Note**:- This is in no way affiliated with the original [30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code/).

If you've come here from javascript land then you should be aware that this project uses `python 3`, therefore not all snippets will work as expected in every python interpreter or on system. You'll need to check your python version with the command `python -v`. If you need help installing the latest stable release of python 3 on your system checkout docs.python.org if you run into trouble make sure you research stackoverflow. Eventually it might be worth looking into how to set up a virtual environment for python projects with virtualenv or even a tool like anaconda.

This project contains plenty of useful snippets which can help beginners and newcomers quickly ramp-up on grasping python 3's syntax.

### Table of contents
### :books: List

<details><summary>View contents</summary> <ul><li><a href = "#bubble_sort"><code>bubble_sort</code></a></li>
<li><a href = "#chunk"><code>chunk</code></a></li>
<li><a href = "#compact"><code>compact</code></a></li>
<li><a href = "#count_by"><code>count_by</code></a></li>
<li><a href = "#count_occurences"><code>count_occurences</code></a></li>
<li><a href = "#deep_flatten"><code>deep_flatten</code></a></li>
<li><a href = "#difference"><code>difference</code></a></li>
<li><a href = "#difference_by"><code>difference_by</code></a></li>
<li><a href = "#has_duplicates"><code>has_duplicates</code></a></li>
<li><a href = "#insertion_sort"><code>insertion_sort</code></a></li>
<li><a href = "#shuffle"><code>shuffle</code></a></li>
<li><a href = "#spread"><code>spread</code></a></li>
<li><a href = "#zip"><code>zip</code></a></li>
</ul></details>

### :heavy_division_sign: Math

<details><summary>View contents</summary> <ul><li><a href = "#average"><code>average</code></a></li>
<li><a href = "#factorial"><code>factorial</code></a></li>
<li><a href = "#fibonacci_until_num"><code>fibonacci_until_num</code></a></li>
<li><a href = "#gcd"><code>gcd</code></a></li>
<li><a href = "#lcm"><code>lcm</code></a></li>
<li><a href = "#max_n"><code>max_n</code></a></li>
<li><a href = "#min_n"><code>min_n</code></a></li>
</ul></details>

### :card_file_box: Object

<details><summary>View contents</summary> <ul><li><a href = "#all_unique"><code>all_unique</code></a></li>
<li><a href = "#keys_only"><code>keys_only</code></a></li>
<li><a href = "#values_only"><code>values_only</code></a></li>
</ul></details>

### :scroll: String

<details><summary>View contents</summary> <ul><li><a href = "#byte_size"><code>byte_size</code></a></li>
<li><a href = "#capitalize"><code>capitalize</code></a></li>
<li><a href = "#capitalize_every_word"><code>capitalize_every_word</code></a></li>
<li><a href = "#count_vowels"><code>count_vowels</code></a></li>
<li><a href = "#decapitalize"><code>decapitalize</code></a></li>
<li><a href = "#is_lower_case"><code>is_lower_case</code></a></li>
<li><a href = "#is_upper_case"><code>is_upper_case</code></a></li>
<li><a href = "#palindrome"><code>palindrome</code></a></li>
</ul></details>

<hr></hr> 

## :books: List

### bubble_sort 
<span style="color:grey">Author:-</span> [Shobhit Sachan](https://www.github.com/sachans) 

 <span style="color:grey">Contributors:-</span> [Shobhit Sachan](https://www.github.com/sachans)

Bubble_sort uses the technique of comparing and swapping
```py
def bubble_sort(lst):
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
```
<details><summary>View Examples</summary>

```py
lst = [54,26,93,17,77,31,44,55,20]
bubble_sort(lst)
print("sorted %s" %lst) # [17,20,26,31,44,54,55,77,91]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### chunk 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Chunks an list into smaller lists of a specified size.

Uses `range` to create a list of desired size. Then use `map` on this list and fill it with splices of `lst`.
```py
from math import ceil


def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))
```
<details><summary>View Examples</summary>

```py
chunk([1,2,3,4,5],2) # [[1,2],[3,4],5]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### compact 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Removes falsey values from a list.

Use `filter()` to filter out falsey values (False, None, 0, and "").
```py
def compact(lst):
    return list(filter(bool, lst))
```
<details><summary>View Examples</summary>

```py
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### count_by 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

:information_source: Already implemented via `collections.Counter`

Groups the elements of a list based on the given function and returns the count of elements in each group.

Use `map()` to map the values of the list using the given function. Iterate over the map and increase the the elements count each time it occurs.
```py
def count_by(arr, fn=lambda x: x):
    key = {}
    for el in map(fn, arr):
        key[el] = 0 if el not in key else key[el]
        key[el] += 1
    return key
```
<details><summary>View Examples</summary>

```py
from math import floor
count_by([6.1, 4.2, 6.3], floor) # {4: 1, 6: 2}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### count_occurences 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin),  [Hui Binyuan](https://www.github.com/huybery)

:information_source: Already implemented via `list.count()`.

Counts the occurrences of a value in a list.

Uses the list comprehension to increment a counter each time you encounter the specific value inside the list.
```py
def count_occurrences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])
```
<details><summary>View Examples</summary>

```py
count_occurrences([1, 1, 2, 1, 2, 3], 1) # 3
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### deep_flatten 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin), [Meet Zaveri](https://www.github.com/meetzaveri)

Deep flattens a list.

Use recursion. Use `list.extend()` with an empty list (`result`) and the spread function to flatten a list. Recursively flatten each element that is a list.
```py
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result
```
<details><summary>View Examples</summary>

```py
deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### difference 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Returns the difference between two iterables.

Use list comprehension to only keep values not contained in `b`
```py
def difference(a, b):
    return [item for item in a if item not in b]
```
<details><summary>View Examples</summary>

```py
difference([1, 2, 3], [1, 2, 4]) # [3]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### difference_by 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Returns the difference between two list, after applying the provided function to each list element of both.

Create a `set` by applying `fn` to each element in `b`, then use list comprehension in combination with fn on a to only keep values not contained in the previously created `set`.
```py
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]
```
<details><summary>View Examples</summary>

```py
from math import floor
difference_by([2.1, 1.2], [2.3, 3.4],floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### has_duplicates 
<span style="color:grey">Author:-</span> [Rob-Rychs](@Rob-Rychs) 

 <span style="color:grey">Contributors:-</span> [Rob-Rychs](@Rob-Rychs)

Checks a flat list for duplicate values. Returns True if duplicate values exist and False if values are all unique.

This function compares the length of the list with length of the set() of the list. set() removes duplicate values from the list.
```py
def has_duplicates(lst):
    return len(lst) != len(set(lst))
```
<details><summary>View Examples</summary>

```py
x = [1,2,3,4,5,5]
y = [1,2,3,4,5]
has_duplicates(x) # True
has_duplicates(y) # False
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### insertion_sort 
<span style="color:grey">Author:-</span> [Meet Zaveri](https://www.github.com/meetzaveri) 

 <span style="color:grey">Contributors:-</span>[Meet Zaveri](https://www.github.com/meetzaveri), [Rohit Tanwar](https://www.github.com/kriadmin)

On a very basic level, an insertion sort algorithm contains the logic of shifting around and inserting elements in order to sort an unordered list of any size. The way that it goes about inserting elements, however, is what makes insertion sort so very interesting!
```py
def insertion_sort(lst):

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            lst[j + 1] = key
```
<details><summary>View Examples</summary>

```py
lst = [7,4,9,2,6,3]
insertionsort(lst)
print('Sorted %s'  %lst) # sorted [2, 3, 4, 6, 7, 9]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### shuffle 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

:information_source: The same algorithm is already implemented via `random.shuffle`.

Randomizes the order of the values of an list, returning a new list.

Uses the [Fisher-Yates algorithm](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) to reorder the elements of the list.
```py
from copy import deepcopy
from random import randint


def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst
```
<details><summary>View Examples</summary>

```py
foo = [1,2,3]
shuffle(foo) # [2,3,1] , foo = [1,2,3]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### spread 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Implements javascript's `[].concat(...arr)`. Flattens the list(non-deep) and returns an list.
```py
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret
```
<details><summary>View Examples</summary>

```py
spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### zip 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin), [Leonardo Galdino](https://www.github.com/LeonardoGaldino)

:information_source: Already implemented via `itertools.zip_longest()`

Creates a list of elements, grouped based on the position in the original lists.

Use `max` combined with `list comprehension` to get the length of the longest list in the arguments. Loops for `max_length` times grouping elements. If lengths of `lists` vary `fill_value` is used. By default `fill_value` is `None`.
```py
def zip(*args, fillvalue=None):
    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            args[k][i] if i < len(args[k]) else fillvalue for k in range(len(args))
        ])
    return result
```
<details><summary>View Examples</summary>

```py
zip(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
zip(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
zip(['a'], [1, 2], [True, False], fill_value = '_') # [['a', 1, True], ['_', 2, False]]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

## :heavy_division_sign: Math

### average 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin), [Hui Binyuan](https://www.github.com/huybery)

:information_source: Already implemented via `statistics.mean`. `statistics.mean` takes an array as an argument whereas this function takes variadic arguments.

Returns the average of two or more numbers.

Takes the sum of all the `args` and divides it by `len(args)`. The second argument `0.0` in sum is to handle floating point division in `python3`.
```py
def average(*args):
    return sum(args, 0.0) / len(args)
```
<details><summary>View Examples</summary>

```py
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### factorial 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Calculates the factorial of a number.

Use recursion. If `num` is less than or equal to `1`, return `1`. Otherwise, return the product of `num` and the factorial of `num - 1`. Throws an exception if `num` is a negative or a floating point number.
```py
def factorial(num):
    if not ((num >= 0) & (num % 1 == 0)):
        raise Exception(
            f"Number( {num} ) can't be floating point or negative ")
    return 1 if num == 0 else num * factorial(num - 1)
```
<details><summary>View Examples</summary>

```py
factorial(6) # 720
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### fibonacci_until_num 
<span style="color:grey">Author:-</span> [Nian Lee](https://www.github.com/scraggard) 

 <span style="color:grey">Contributors:-</span> [Nian Lee](https://www.github.com/scraggard)

Returns the n-th term in a Fibonnaci sequence that starts with 1

A term in a Fibonnaci sequence is the sum of the two previous terms.
This function recursively calls the function to find the n-th term.
```py
def fibonacci_until_num(n):
  if n < 3:
    return 1
  return fibonacci_until_num(n - 2) + fibonacci_until_num(n - 1)
```
<details><summary>View Examples</summary>

```py
fibonnaci_until_num(5) # 5
fibonnaci_until_num(15) # 610
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### gcd 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin), [cclauss](https://www.github.com/cclauss), [Sandhya Saravanan](https://www.github.com/sandy9999)

Calculates the greatest common divisor of a list of numbers.

Uses the reduce function from the inbuilt module `functools`. Also uses the `math.gcd` function over a list.
```py
from functools import reduce
import math

def gcd(numbers):
    return reduce(math.gcd, numbers)
```
<details><summary>View Examples</summary>

```py
gcd([8,36,28]) # 4
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### lcm 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Returns the least common multiple of two or more numbers.

Use the `greatest common divisor (GCD)` formula and the fact that `lcm(x,y) = x * y / gcd(x,y)` to determine the least common multiple. The GCD formula uses recursion.

Uses `reduce` function from the inbuilt module `functools`. Also defines a method `spread` for javascript like spreading of lists.
```py
from functools import reduce


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def lcm(*args):
    numbers = []
    numbers.extend(spread(list(args)))

    def _gcd(x, y):
        return x if not y else _gcd(y, x % y)

    def _lcm(x, y):
        return x * y / _gcd(x, y)

    return reduce((lambda x, y: _lcm(x, y)), numbers)
```
<details><summary>View Examples</summary>

```py
lcm(12, 7) # 84
lcm([1, 3, 4], 5) # 60
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### max_n 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Returns the `n` maximum elements from the provided list. If `n` is greater than or equal to the provided list's length, then return the original list(sorted in descending order).

Use `list.sort()` combined with the `deepcopy` function from the inbuilt `copy` module to create a shallow clone of the list and sort it in ascending order and then use `list.reverse()` reverse it to make it descending order. Use `[:n]` to get the specified number of elements. Omit the second argument, `n`, to get a one-element list
```py
def max_n(lst, n=1, reverse=True):
    return sorted(lst, reverse=reverse)[:n]
```
<details><summary>View Examples</summary>

```py
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3,2]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### min_n 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Returns the `n` minimum elements from the provided list. If `n` is greater than or equal to the provided list's length, then return the original list(sorted in ascending order).

Use `list.sort()` combined with the `deepcopy` function from the inbuilt `copy` module to create a shallow clone of the list and sort it in ascending order. Use `[:n]` to get the specified number of elements. Omit the second argument, `n`, to get a one-element list
```py
from copy import deepcopy


def min_n(lst, n=1):
    numbers = deepcopy(lst)
    numbers.sort()
    return numbers[:n]
```
<details><summary>View Examples</summary>

```py
min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1,2]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

## :card_file_box: Object

### all_unique 
<span style="color:grey">Author:-</span> [Rob-Rychs](@Rob-Rychs) 

 <span style="color:grey">Contributors:-</span> [Rob-Rychs](@Rob-Rychs)

Checks a flat list for all unique values. Returns True if list values are all unique and False if list values aren't all unique.

This function compares the length of the list with length of the set() of the list. set() removes duplicate values from the list.
```py
def all_unique(lst):
    return len(lst) == len(set(lst))
```
<details><summary>View Examples</summary>

```py
x = [1,2,3,4,5,6]
y = [1,2,2,3,4,5]
all_unique(x) # True
all_unique(y) # False
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### keys_only 
<span style="color:grey">Author:-</span> [Rob-Rychs](@Rob-Rychs) 

 <span style="color:grey">Contributors:-</span> [Rob-Rychs](@Rob-Rychs)

Function which accepts a dictionary of key value pairs and returns a new flat list of only the keys.

Uses the .items() function with a for loop on the dictionary to track both the key and value and returns a new list by appending the keys to it. Best used on 1 level-deep key:value pair dictionaries (a flat dictionary) and not nested data-structures which are also commonly used with dictionaries. (a flat dictionary resembles a json and a flat list an array for javascript people).
```py
def keys_only(flat_dict):
    lst = []
    for k, v in flat_dict.items():
        lst.append(k)
    return lst
```
<details><summary>View Examples</summary>

```py
ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### values_only 
<span style="color:grey">Author:-</span> [Rob-Rychs](@Rob-Rychs) 

 <span style="color:grey">Contributors:-</span> [Rob-Rychs](@Rob-Rychs)

Function which accepts a dictionary of key value pairs and returns a new flat list of only the values.

Uses the .items() function with a for loop on the dictionary to track both the key and value of the iteration and returns a new list by appending the values to it. Best used on 1 level-deep key:value pair dictionaries and not nested data-structures.
```py
def values_only(dict):
    lst = []
    for k, v in dict.items():
        lst.append(v)
    return lst
```
<details><summary>View Examples</summary>

```py
ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
}
values_only(ages) # [10, 11, 9]
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

## :scroll: String

### byte_size 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Returns the length of a string in bytes.

`utf-8` encodes a given string, then `len` finds the length of the encoded string.
```py
def byte_size(string):
    return(len(string.encode('utf-8')))
```
<details><summary>View Examples</summary>

```py
byte_size('😀') # 4
byte_size('Hello World') # 11
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### capitalize 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Capitalizes the first letter of a string.

Capitalizes the fist letter of the string and then adds it with rest of the string. Omit the `lower_rest` parameter to keep the rest of the string intact, or set it to `true` to convert to lowercase.
```py
def capitalize(string, lower_rest=False):
    return string[:1].upper() + (string[1:].lower() if lower_rest else string[1:])
```
<details><summary>View Examples</summary>

```py
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### capitalize_every_word 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Capitalizes the first letter of every word in a string.

Uses `str.title` to capitalize first letter of evry word in the string.
```py
def capitalize_every_word(string):
    return string.title()
```
<details><summary>View Examples</summary>

```py
capitalize_every_word('hello world!') # 'Hello World!'
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### count_vowels 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Retuns `number` of vowels in provided `string`.

Use a regular expression to count the number of vowels `(A, E, I, O, U)` in a string.
```py
import re


def count_vowels(str):
    return len(len(re.findall(r'[aeiou]', str, re.IGNORECASE)))
```
<details><summary>View Examples</summary>

```py
count_vowels('foobar') # 3
count_vowels('gym') # 0
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### decapitalize 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Decapitalizes the first letter of a string.

Decapitalizes the fist letter of the sring and then adds it with rest of the string. Omit the `upper_rest` parameter to keep the rest of the string intact, or set it to `true` to convert to uppercase.
```py
def decapitalize(string, upper_rest=False):
    return str[:1].lower() + (str[1:].upper() if upper_rest else str[1:])
```
<details><summary>View Examples</summary>

```py
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### is_lower_case 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Checks if a string is lower case.

Convert the given string to lower case, using `str.lower()` method and compare it to the original.
```py
def is_lower_case(string):
    return string == string.lower()
```
<details><summary>View Examples</summary>

```py
is_lower_case('abc') # True
is_lower_case('a3@$') # True
is_lower_case('Ab4') # False
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### is_upper_case 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Checks if a string is upper case.

Convert the given string to upper case, using `str.upper()` method and compare it to the original.
```py
def is_upper_case(string):
    return string == string.upper()
```
<details><summary>View Examples</summary>

```py
is_upper_case('ABC') # True
is_upper_case('a3@$') # False
is_upper_case('aB4') # False
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>

### palindrome 
<span style="color:grey">Author:-</span> [Rohit Tanwar](https://www.github.com/kriadmin) 

 <span style="color:grey">Contributors:-</span>[Rohit Tanwar](https://www.github.com/kriadmin)

Returns `True` if the given string is a palindrome, `False` otherwise.

Convert string `str.lower()` and use `re.sub` to remove non-alphanumeric characters from it. Then compare the new string to the reversed.
```py
def palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]
```
<details><summary>View Examples</summary>

```py
palindrome('taco cat') # True
```
</details>

<br><a href = "#table-of-contents">:arrow_up: Back to top</a>


## Credits

*Icons made by [Smashicons](https://www.flaticon.com/authors/smashicons) from [www.flaticon.com](https://www.flaticon.com/) is licensed by [CC 3.0 BY](http://creativecommons.org/licenses/by/3.0/).*



## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fkriadmin%2F30-seconds-of-python-code.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fkriadmin%2F30-seconds-of-python-code?ref=badge_large)
