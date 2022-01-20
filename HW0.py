# Create variables of String , Integer , Float , Bytes , List , Tuple , Set , Frozen set , Dict
# Output all the above variables to the console with the data type added.
#string
a = "Hello"
print(type(a), a)
#Integer
b = 2
print(type(b), b)
#Float
c = 3.14
print(type(c), c)
#Bytes
d = b"Hello"
print(type(d), d)
#List
e = ['Hello', 'Hi', 'Ola']
print(type(e), e)
#Tuple
f = ('Hello', 'Hi', 'Ola')
print(type(f), f)
#Set
g = {'H', 'e', 'l', 'l', 'o'}
print(type(g), g)
#Frozenset
h = frozenset(('H', 'e', 'l', 'l', 'o'))
print(type(h), h)
#Dict
i = {'name': 'Dan', 'age':36}
print(type(i), i)

#Create 2 String variables, create a variable in which you merge these variables. Output to the console
g = str("Mer")
k = str("ge")
l = g+k
print(l)

#Output String and Integer variables in one line using "," (comma)
print(a, b)
print(a, b, sep=',') #outputs the value of the variables in the console, separated by commas

#Output String and Integer variables in one line using "+" (plus)
print(a + str(b))
print(a, b, sep="+") #outputs the value of the variables in the console with a plus






