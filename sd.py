set1 ={"a","b","c"}
set2 ={1,2,3}
set3 = set1.union(set2)
print(set3)
{1, 2, 3, 'c', 'b', 'a'}
set1 ={"a","b","C"}
set2 = {1,2,3}
set3 = set1|set2
print(set3)
{1, 2, 3, 'C', 'b', 'a'}
set1 ={"a","b","c"}
set2 = {1,2,3}
set3 = {"John","Elena"}
set4 = {"apple","banana","grape","mango"}
myset =set1|set2|set3|set4
print(myset)
{1, 2, 3, 'c', 'banana', 'apple', 'b', 'mango', 'grape', 'Elena', 'a', 'John'}
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"John","Elena"}
set4 = {"apple","banana","grape","mango"}
myset = set1.union(set2,set3,set4)
print(myset)
{1, 2, 3, 'c', 'banana', 'apple', 'b', 'mango', 'grape', 'Elena', 'a', 'John'}
set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)
{1, 2, 3, 'c', 'b', 'a'}
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1 & set2
print(set3)
{'apple'}
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1.difference(set2)
print(set3)
{'banana', 'cherry'}
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1 - set2
print(set3)
{'banana', 'cherry'}
thisdict = {"brand":"Ford","model":"Mustang","year":1964}
print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
thisdict = {"brand":"Ford","model":"Mustang","year":1964}
print(thisdict["brand"])
thisdict = {"brand":"Ford","model":"Mustang","year":1964,"year":2020}
print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
thisdict = {"brand":"Ford","model":"Mustang","year":1964}
x = thisdict["model"]
