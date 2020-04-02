### is_anagram

Determine if 2 strings are anagrams.

Returns true if 2 strings are anagrams of each other, false otherwise.
Capital letters and whitespaces are ignored.

``` python
def is_anagram(str1, str2):
    str1, str2 = str1.replace(" ", ""), str2.replace(" ", "")

    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1.lower()) == sorted(str2.lower())
```

``` python
is_anagram("anagram", "Nag a ram")  # True
```
