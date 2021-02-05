# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:21:44 2021

@author: DELL
"""

dict1={'R1':'10.0.0.1',
     1:'AP',
     2:2.5,3:True,
     'R1':'172.17.0.1'}
print(dict1)
print(len(dict1))
print(type(dict1))
print(dict1['R1'])
dict1['R3']='10.0.0.3'
print ('R3' in dict1)