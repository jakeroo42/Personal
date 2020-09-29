#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:39:48 2020

@author: jakerabinowitz
"""



import pyautogui, tims 

time.sleep(5)

script = "Any words" 

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("Enter")
  
    