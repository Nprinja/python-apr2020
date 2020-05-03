#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:52:13 2020

@author: sohan

"""


#for i in range(10):
#    i = i + i
#    
#    print(i)
#    
'''
for i in [1,2,3,4,5,'cat','fish']:
    if(i == 2):
        i = i + i
    print(i)'''
'''
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)

subject_marks.sort(key = lambda x: x[1])

print("\nSorting the List of Tuples:")
print(subject_marks)'''


courses = ['PYTHON', 'JAVA', 'AI/ML', 'DATA SCIENCE']

course_list = map(lambda item: item.lower(), courses)

print(list(course_list))