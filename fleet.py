#Class:Fleet
#Author: Samuel LP McKnight
#Created : August 11th, 2021

from robots import Robots


class Fleet: 
    def __init__(self,name,):
        self.name  = name
        self.robots = []

    # ===== Methods =====
    def add_robots(self):
        first_robot   = Robots("infantrybotI", 60, 40 )
        second_robot  = Robots("GladitorI",   100, 60)
        third_robot   = Robots("infantrybotII", 60, 40)
        fourth_robot  = Robots("infantrybotIII", 60, 40 )
        fifth_robot   = Robots("GladitorII", 100, 60) 
        self.robots.append(first_robot)
        self.robots.append(second_robot)
        self.robots.append(third_robot)
        self.robots.append(fourth_robot)
        self.robots.append(fifth_robot)