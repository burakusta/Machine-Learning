# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:26:51 2024

@author: burak
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
path=r"C:\Users\burak\OneDrive\Masaüstü\datas\TopSellingAlbums.csv"
df1=pd.read_csv(path, header=0)
class Circle(object):
    
    # Constructor
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
        
        
class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h
    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0
    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed
    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed
    
    
    
file1=open(r"C:\Users\burak\OneDrive\Masaüstü\u.txt","a")
file1.write("ilk line mı")
file1.close()
file1=open(r"C:\Users\burak\OneDrive\Masaüstü\u.txt","r")
file_stuff=file1.read()
file1.close()
#file1=open(r"C:\Users\burak\OneDrive\Masaüstü\u.txt","r")
#file_lines = file1.readlines()
#file_lines = [int(line.strip()) for line in file_lines]    

fruits = ["apple", "banana", "orange"] 
fruits.append("mango") 
my_list = [1, 2, 2, 3, 4, 2, 5, 2] 
count = my_list.count(2)
#print(count) 




x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df


print(df1.iloc[3, 0])