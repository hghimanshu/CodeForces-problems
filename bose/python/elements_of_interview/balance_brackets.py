#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 00:21:55 2019

@author: abhishek
"""

open_bracket_list = ['(']
close_bracket_list = [')']

x = '((()))'

count=0
for i in x:
    if i in close_bracket_list:
        print('Found close bracket')
    
for i in range(0,len(x)):
    