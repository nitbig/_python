"""
Useful String Methods

upper()    Converts to uppercase    "hi".upper 
lower()    Converts to Lowercase     "hi".lower()    
title()    Capitalizes each word     "hello world".title()
capitalize()   capitalise first character   "hello world".title
strip()     Removes spaces(leading&trailing)   " hello ".strip --> "hello"
lstrip/rstrip()  Removes left/right spaces     "hello".lstrip()-->"hello"
replace(a,b)     Replace substring        "hello".replace("l","x")--> "hexxo"
split()        Split into list        "a,b,c".split()
join()        Joins iterable into string  "-".join(['a','b','c'])-->"a-b-c"
find()        Returns index of substring   "hello".find("")-->1
count()       Count occurences              "banana".count("a") --> 3
startswith()   Checks prefix             "hello".startswith("he")-->True
endswith()     Checks suffix             "hello".endswith("lo")-->True
isalpha()       True if all letters       "abc".isalpha()-->True
isdigit()       True if all digits        "123".isdigit()-->True
isalnum()       True if letters & numbers  "abc123".isalnum()-->True
isspace()       True if only spaces        "".isspace() --> True   

"""