## Question 1

### 1 `help(t)`

Help on BlankClass in module __main__ object:

class BlankClass(builtins.object)
 |  This is a Blank class for CS162.
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

### 2 `type(t)`

This prints the type. The type is a class with name of the class

<class '__main__.BlankClass'>


### 3 `dir(t)`

This prints all the methods of t (including built in methods)

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


### 4 `hash(t)`

This returns the hash value of the object __t__. 

279396916


### 5 `id(t)`

This returns a unique id of the object and it never changes during its lifetime. In Cpython it is the memory address of the object.


### 6 `hasattr(my_attr,'x3')`

The hasattr() function is used to determine if the object contains the corresponding property.

This will return true in this case.


### 7 `getattr(my_attr,'x3')`

Python getattr() function is used to get the value of an object's attribute and if no attribute of that object is found, default value is returned.


### 8 `delattr(my_attr,'x3')`

Python delattr() is a built-in function that deletes the named attribute of an object. delattr() does not return any value and deletes the attribute if object allows it.


### 9 `vars(t)`

The vars() function returns the `__dic__` attribute of an object. The `__dict__` attribute is a dictionary containing the object's changeable attributes. Note: calling the vars() function without parameters will return a dictionary containing the local symbol table.


### 10 `bool(t)`

Returns true