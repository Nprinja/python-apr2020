# -*- coding: utf-8 -*-


import sys


print('Number of Arguments: ', len(sys.argv), 'arguments.')

print('Arguments List: ', str(sys.argv))


'''
a = int(sys.argv[1])
b = int(sys.argv[2])

print(a + b)
'''

#Connect to a database url
'''
if(len(sys.argv) > 0):
    environment =sys.argv[1]
    
    if(environment == 'UAT'):
        print('UAT')
    elif(environment == 'QA'):
        print('QA')
    else: 
        print('Dev')'''