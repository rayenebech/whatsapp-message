

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:22:39 2020

@author: Rayene Bech
This codes sends message to numbers stored in xlsx file
based on their responses stored in  DECISION column
"""

#preparing the message


#Filtering the data
import pandas as pd

members_list = pd.read_excel('responses.xlsx')
# reading the spreadsheet
# getting the names and the emails
names = members_list['NAME']
numbers = members_list['NUMBER']
decisions= members_list['DECISION']

#sending the message
import pywhatkit
for i in range(30,97):
    if numbers[i]!= None and decisions[i] != 'NO':
        if names[i] != None:
            greetings= "Hello " + names[i]
        else:
            greetings= "Hello "
        message = """
    This is a  message that will be send
            """
        message = greetings +" " + message
        pywhatkit.sendwhatmsg("+90"+ str(numbers[i]), message, 21,i-30)
