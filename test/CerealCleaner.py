import os
import csv

csvpath = os.path.join('.', 'cereal.csv')

def find(cerealdata)):

   fiber = int(cerealdata[5])
   
   if(fiber > 5):
       print(cerealdata[1] + " has " + cerealdata[5] " grams of fiber.")



