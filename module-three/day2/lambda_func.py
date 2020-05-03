# -*- coding: utf-8 -*-


'''
def addition(a, b):
    return a + b

addition(10, 5)'''


# lambda arguments : expression
'''
sum = lambda a, b : a + b

print(sum(5,10))


cube = lambda x : x * x * x

print('Cube value is: %s' %cube(5)) '''
'''
str1 = 'EDUREKA'
print(str1.lower())

names = ['PYTHON', 'JAVA', 'AI/ML', 'DATASCIENCE']

#map(function, sequence)

lower_names = map(lambda x: x.lower(), names)
print(list(lower_names))'''

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

odd = filter(lambda x : x % 2 != 0, numbers)

print(list(odd))

