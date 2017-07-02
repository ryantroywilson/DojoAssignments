#Basic strngs

name = "Zen"
print "My name is", name

name = "Ryan"
print "My name is " + name

first_name = "Ryan"
last_name = "Wilson"
print "My name is {} {}".format(first_name, last_name)

hw = "hello %s" % 'world'
print hw

#Built-In String Methods

x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"

""""
->string.count(substring): returns number of occurrences of substring in string.

->string.endswith(substring): returns a boolean based upon whether the last
characters of string match substring.

->string.find(substring): returns the index of the start of the first occurrence
of substring within string.

->string.isalnum(): returns boolean depending on whether the
string's length is > 0 and all characters are alphanumeric
(letters and numbers only). Strings that include spaces and punctuation
will return False for this method. Similar methods include .isalpha(),
 .isdigit(), .islower(), .isupper(), and so on. All return booleans.

->string.join(list): returns a string that is all strings within our set
(in this case a list) concatenated.

string.split(): returns a list of values where string is split at the given
character. Without a parameter the default split is at every space.
"""

#list examples !!!!!!!!!!!!!

fruits = ['apple','banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables
salad = 3 * vegetables
print salad


drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens


x = [1,2,3,4,5]
x.append(99)
print x


x = [99,4,2,5,-3];
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];

my_list = [1, 'Zen', 'hi']
print len(my_list)
# output = 3
"""
Some built-in functions for sequences:
-> enumerate(sequence) used in a for loop context to return two-item-tuple for
each item in the list indicating the index followed by the value at that index.

-> map(function, sequence) applies the function to every item in the sequence
you pass in. Returns a list of the results.

-> min(sequence) returns the lowest value in a sequence.
-> sorted(sequence) returns a sorted sequence
"""

my_list = [1,5,2,8,4]
my_list.append(7)
print my_list
# output:
# [1,5,2,8,4,7]
"""
The following are some commonly used list methods:
-> list.extend(list2) adds all values from a second sequence to the end of
the original sequence.
-> list.pop(index) remove a value at given position. if no parameter is passed,
defaults to final value in the list.
-> list.index(value) returns the index position in a list for the given
parameter.
"""
