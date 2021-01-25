# # try instance of list
# x = list([1,2,3])

# # try instance of integer
# x = 5

# # try instance of float
# x = 1.1

# # try instance of string
# x =''

def liskov_substitution_principle(x):
    x = x % x
    x = x * 2
    print(x)

liskov_substitution_principle(x)    