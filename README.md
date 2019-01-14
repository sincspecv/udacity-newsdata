### News Data Project

NOTE: This script uses Python 3.

Run the program in your terminal by typing `$ python newsdata.py`

You will be prompted to make a selection:
```
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

Which query would you like to run?
```
Selection 1 calls the `get_articles()` function and should return something like this:
```
The three most popular articles of all time are: 

"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views
```

Selection 2 calls the `get_authors()` function and should return something like this: 
```
The most popular article authors of all time are: 

Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views
```

Selection 3 calls the `get_404s` function and should return something like this:
```
The days on which more than 1% of requests lead to errors are: 

July 17, 2016 -- 2.26% errors
```

