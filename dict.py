set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)
{'b', 1, 2, 'c', 3, 'a'}
set1 = {"a","b","c"}
set2 = {1,2,3}
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1 | set2
print(set3)
{'b', 1, 2, 'c', 3, 'a'}
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"john","Elen"}
set1 {"a","b","c"}
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"John","Elen"}
set4 = {"apple","banana","cherry"}
myset = set1.union(set2,set3,set4)
print(myset)
{1, 2, 'c', 3, 'apple', 'Elen', 'banana', 'b', 'John', 'cherry', 'a'}
set1 {"a","b","c"}
set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print (set1)
{'b', 1, 2, 'c', 3, 'a'}
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1.intersection(set2)
print(set3)
{'apple'}
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 =set1 & set2
print(set3)
{'apple'}
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1 -set2
print(set3)
{'cherry', 'banana'}
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1.difference(set2)
print(set3)
{'cherry', 'banana'}
thisdict = {
	"brand":"Ford",
	"model":"Mustang",
	"year":1964
	}
print (thisdict["brand"])
Ford
print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
thisdict = {
	"brand":"Ford"
	"model" "Mustang"
}