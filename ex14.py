d={1001:'Dharun anna kumar',1002:'kavin kumar',1003:'pasupathi raj kumar',1004:'sudarsan',1005:'kavin  sanker'}
print('The length of the dictionary is:',len(d))
print('The copied dictionary is:' ,d.copy())
print('The removed element is :' ,d.pop(1005))
print('The dictionary d after removing 1005 is :' ,d)
print('The element in 1001 key is:' ,d.get(1001))
print('The key-value pair  as  a tuple in a list is:' ,d.items())
print('The dictionary values as a list is:' ,d.values())
print('The removed last item  from dicionary is:' ,d.popitem())
d.clear()
print('The dictionary after removing  all element is :' ,d)
