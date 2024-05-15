dict ={1:'Shoaib',2:'Noor',3:'Arhaan'}
for key in dict :
    print(key,dict[key])
    
for key in dict.items():
    print(key[0],key[1])

# Add element
dict[4]='Shoaib'
print(dict)

# second way to add element using update method
dict.update({5:'Asif'})
print(dict)

# update value using update method 
dict.update({5:'gufran'})
print(dict)

# Delete key value pair element using pop method
#dict.pop(5)
print(dict.pop(5))
print(dict)

# Remove last dictionary item and return key value pair item 
print(dict.popitem())
print(dict)

# clear method remove all dict item and returns none
print(dict.clear())