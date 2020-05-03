#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:37:57 2020

@author: sohan
"""
'''
def person(*attr):
    print(type(attr))
    print('Person details', attr[1])


person('John', 25, 'Male', 'Avenue 1, Dallas, TX')

person('Smith', 22, 'Male');'''


def student(**args):
    print(args.get('name'))

student(name='Lori', age=30, gender='Female', address='Street1 abc, India')
    