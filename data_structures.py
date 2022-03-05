"""
>>> l=[3,2,4,"python",5.6]
>>> print(l)
[3, 2, 4, 'python', 5.6]
>>> print(l[0])
3
>>> print(l[-1])
5.6
>>> print(l[3])
python
>>>  print(l[3])
  File "<stdin>", line 1
    print(l[3])
    ^
IndentationError: unexpected indent
>>> print(l[3][0])
p
>>> print(l[:])
[3, 2, 4, 'python', 5.6]
>>> print(l[1:4])
[2, 4, 'python']
>>> dir(l)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l.count(3)
1
>>> l.append(56)
>>> print(l)
"""

"""
>>> print(l.index(2))
1
>>> print(l.count(4))
1
>>> print(l.clear())
None
>>> print(l)
[]
>>> l=[3, 2, 4, 'python', 5.6]
>>> a = l.copy()
>>> print(id(a), id(l))
140548280810544 140548279983472
>>> l.append(10)
>>> print(1)
1
>>> l.insert(1,55)
>>> print(l)
[3, 55, 2, 4, 'python', 5.6, 10]
>>> c=[5,6]
>>> print(l.append(c))
None
>>> print(l)
[3, 55, 2, 4, 'python', 5.6, 10, [5, 6]]
>>> print(l.extend(c))
None
>>> print(l)
[3, 55, 2, 4, 'python', 5.6, 10, [5, 6], 5, 6]
>>> print(l.remove(c))
None
>>> print(l)
[3, 55, 2, 4, 'python', 5.6, 10, 5, 6]
>>> l.pop()
6
>>> l.pop()
5
>>> l.pop(2)
2
>>> l.pop(4)
5.6
>>> l.reverse()
>>> print(l)
[10, 'python', 4, 55, 3]
"""

#TUPLE
"""
>>> a=(3,4,5)
>>> print(a, type(a))
(3, 4, 5) <class 'tuple'>
>>> print(bool(a))
True
>>> x=(3,4,[5,6],7,8)
>>> print(x[0])
3
>>> print(x[2])
[5, 6]
>>> print(x[2][0])
5
>>> print(x[:])
(3, 4, [5, 6], 7, 8)
>>> print(x.count(4))
1
>>> print(x.index(7))
3
>>> print(len(x))
5
"""

#DICTIONARY
"""
>>> d = {'fruit':'apple', 'animal':'fox', 1:'one', 'two':2}
>>> print(d, type(d))
{'fruit': 'apple', 'animal': 'fox', 1: 'one', 'two': 2} <class 'dict'>
>>> print(d['fruit'])
apple
>>> print(d[1])
one
>>> print(d.get('animal'))
fox
>>> print(d['three'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'three'
>>> print(d.get('three'))
None
>>> d['three']=56
>>> print(d.get('three'))
56
>>> print(d)
{'fruit': 'apple', 'animal': 'fox', 1: 'one', 'two': 2, 'three': 56}
>>> print(d.keys())
dict_keys(['fruit', 'animal', 1, 'two', 'three'])
>>> print(d.values())
dict_values(['apple', 'fox', 'one', 2, 56])
>>> print(d.item())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'item'
>>> print(d.items())
dict_items([('fruit', 'apple'), ('animal', 'fox'), (1, 'one'), ('two', 2), ('three', 56)])
>>> y = {'four': '4'}
>>> d.update(y)
>>> print(d)
{'fruit': 'apple', 'animal': 'fox', 1: 'one', 'two': 2, 'three': 56, 'four': '4'}
>>> d.pop('four')
'4'
>>> d.popitem()
('three', 56)
>>> print(d)
{'fruit': 'apple', 'animal': 'fox', 1: 'one', 'two': 2}
>>> keys = ['a', 'e', 'i', 'o', 'u']
>>> dicti = dict.fromkeys(keys)
>>> print(dicti)
{'a': None, 'e': None, 'i': None, 'o': None, 'u': None}
"""

#SET
"""
>>> a={3, 4, 5, 3, 6, 6}
>>> print(a)
{3, 4, 5, 6}
>>> b={3, 2, 6, 7, 5}
>>> print(a.union(b))
{2, 3, 4, 5, 6, 7}
>>> print(a.intersection(b))
{3, 5, 6}
"""
