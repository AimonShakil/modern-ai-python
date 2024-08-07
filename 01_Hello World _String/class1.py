print("pakistan")

# if put str type should show error
name : int = 700 
print(name) # print
print (type(name)) #type
print(id(name)) # physical address
print([i for i in dir(name) if "__" not in i]) # methods and attributes

name3 : str = 900  # this error will not be shown in jupyter notebook
print(name3)

