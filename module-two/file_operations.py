#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


newfile = open('patients.txt', 'r+')
for i in range(1, 10):
   newfile.write('\n Hello, Welcome to Python:')

for i in range(1, 10):
    print(newfile.readline())
    
#newfile.seek(0)
print(newfile.tell())
    



"""
Created on Sun Apr 26 22:41:24 2020

@author: sohan
"""
''''

empFile = open('employee.txt')

for record in empFile:
    print(record)

empFile.close()'''
'''
wf = open('employee.txt', 'a')
wf.write('\nSmith,26,SE,8000,Male')


wf.close()
'''

